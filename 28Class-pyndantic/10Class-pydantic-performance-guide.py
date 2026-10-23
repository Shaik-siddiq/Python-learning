"""
Deep nesting, large item collections, and circular references can cause high validation overhead, memory spikes, and RecursionError.

The following implementation demonstrates how to mitigate each issue using lazy loading, shallow container validation, and safe serialization.
"""
from __future__ import annotations
from functools import cached_property
from typing import Annotated
from pydantic import BaseModel, Field, model_validator

# ---------------------------------------------------------------------------
# 1. Leaf Model: Circular Reference Protection
# ---------------------------------------------------------------------------
class FileNode(BaseModel):
    name: str
    size_bytes: int
    parent: DirectoryNode | None = Field(default=None, exclude=True)
    # ^ exclude=True prevents infinite loops during .model_dump() / JSON serialization


# ---------------------------------------------------------------------------
# 2. Large Lists & Deep Nesting Optimization: Shallow Validation + Lazy Parsing
# ---------------------------------------------------------------------------
class DirectoryNode(BaseModel):
    path: str
    
    # Large List Optimization:
    # Validate raw dicts at ingestion time instead of eagerly instantiating
    # 50,000+ FileNode Pydantic instances upfront.
    raw_files: list[dict] = Field(default_factory=list, alias="files")
    
    # Recursive branch
    subdirectories: list[DirectoryNode] = Field(default_factory=list)

    # Lazy Loading:
    # Instantiate child FileNode objects on-demand, caching the result.
    @cached_property
    def files(self) -> list[FileNode]:
        return [FileNode(**f, parent=self) for f in self.raw_files]

    # Guard against uncontrolled deep nesting (Recursion / Stack Overflow)
    @model_validator(mode="after")
    def guard_recursion_depth(self) -> DirectoryNode:
        depth = self.path.strip("/").count("/") + 1
        if depth > 15:
            raise ValueError(f"Max directory depth (15) exceeded: {self.path}")
        return self


# Resolve self-referencing and mutual annotations in V2
FileNode.model_rebuild()
DirectoryNode.model_rebuild()

"""
Peermonce issues
[
  {
    "Issue": "Deep Nesting",
    "Bottleneck": "Deep recursion causes stack overflows and exponential schema validation times.",
    "Mitigation Strategy": "Use a @model_validator depth guard to reject payloads exceeding safe nesting limits."
  },
  {
    "Issue": "Large Lists",
    "Bottleneck": "list[LeafModel] forces Pydantic to run validation loops across thousands of objects upfront.",
    "Mitigation Strategy": "Store as list[dict] (shallow validation) and use @cached_property to materialize models on demand."
  },
  {
    "Issue": "Circular References",
    "Bottleneck": "Bidirectional pointers cause infinite loops during .model_dump() or JSON serialization.",
    "Mitigation Strategy": "Mark inverse references (e.g., parent) with Field(exclude=True)."
  },
  {
    "Issue": "Memory Footprint",
    "Bottleneck": "Instantiating deep object graphs holds all intermediate models in memory simultaneously.",
    "Mitigation Strategy": "Defer model instantiation to access time so unused branches consume no extra memory."
  }
]
"""

# Payload with deep directories, circular references, and large payload lists
payload = {
    "path": "/var/log",
    "files": [
        {"name": f"app_{i}.log", "size_bytes": 1024 * i} for i in range(10_000)
    ],
    "subdirectories": [
        {
            "path": "/var/log/audit",
            "files": [{"name": "audit.log", "size_bytes": 4096}],
            "subdirectories": [],
        }
    ],
}

# 1. Ingestion: Fast because 10,000 raw dicts bypass individual class validation
root = DirectoryNode.model_validate(payload)

# 2. Lazy Access: Instantiates and binds FileNode instances on demand
print(f"Loaded: {root.files[0].name}")  # app_0.log
print(f"Circular parent link: {root.files[0].parent.path}")  # /var/log

# 3. Safe Dump: exclude=True prevents infinite recursion loops
clean_dict = root.model_dump(exclude={"raw_files"})
print(f"Serialized keys: {list(clean_dict.keys())}")  # ['path', 'subdirectories']