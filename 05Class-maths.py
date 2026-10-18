import math
'''
1. Division, Numerator, Denominator & ModuloIn mathematics, a fraction represents a part of a whole:
q = quetient, r = reminder, mod = %
a/b = numerator/denominator
Numerator (a): The dividend (the quantity being divided).
Denominator (b): The divisor (the quantity dividing). b != 0, because division by zero is undefined.
In Python Coding:
 Floating Division (/): 
 Returns an exact decimal float (7 / 2 = 3.5).
 Floor Division (//): Returns the largest integer less than or equal to the quotient (7 // 2 = 3). Used in pagination, array indexing, and chunking 
 
 data.Modulo (%): Calculates the remainder after division: a = b * q + r (r = a (mod b))
'''
# Guarding against ZeroDivisionError
numerator = 100
denominator = 0

if denominator != 0:
    ratio = numerator / denominator
else:
    ratio = 0.0  # Common in dashboards/graphs when no data exists (e.g. 0 clicks)

# Modulo in loops (e.g., run code every 5th iteration)
for i in range(1, 16):
    if i % 5 == 0:
        print(f"Checkpoint at {i}")

'''
2. Power and ExponentialA. Power (x^n)In mathematics, x^n means multiplying the base x by itself n times:
y^n = y * y * y ..... * y
In Python: use the ** operator or pow(base, exp).
'''
power_val = 2 ** 3    # 8
compound = 1000 * (1 + 0.05) ** 5  # Financial metric

'''
B. Exponential Function (e^x or exp(x))
Mathematically, the exponential function raises Euler's constant (e approx 2.71828) to the power of x:
f(X) = e^x
Why it matters: Exponential curves model viral growth, compound interest, population expansion, radioactive decay, and activation functions in AI/ML (like Softmax and Sigmoid).

In Python: use math.exp(x).
'''

x = 2
e_x = math.exp(x)  # e^2 ≈ 7.389

# Sigmoid function for probability scoring (0.0 to 1.0)
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

'''
3. Square Root (sqrt{x})The square root of a number x is a number y such that y^2 = x.
In exponent rules:
sqrt{x} = x^{1/2} = x^{0.5}
In Python Coding:
Used for calculating Euclidean distance between points on a graph, standard deviation in statistics, or graphics/geometry calculations:
d = sqrt{(x2 - x1)^2 + (y2 - y1)^2}
'''

# Method 1: math.isqrt (for exact integer roots) or math.sqrt
dist = math.sqrt((5 - 2)**2 + (7 - 3)**2)  # Euclidean distance

# Method 2: fractional power operator
root = 25 ** 0.5  # 5.0

'''
4. Complex Numbers and Complex FunctionsIn mathematics, 
the real number line cannot solve equations like 
x^2 + 1 = 0(x = sqrt{-1}).
Mathematics introduces the imaginary unit i = sqrt{-1}. In engineering and Python, 
it is written with j:
z = a + bj
a is Real part (z.real)
b is Imaginary part (z.imag)
In Coding and Signal Processing: 
Complex numbers are the foundation of Fourier Transforms (FFT), audio processing, 
AC circuit analysis, computer graphics rotation, and quantum computing simulations.
'''
z1 = 3 + 4j
z2 = 1 - 2j

# Basic arithmetic
result = z1 + z2       # (4 + 2j)

# Magnitude / Modulus: |z| = sqrt(a^2 + b^2)
magnitude = abs(z1)    # abs(3 + 4j) -> 5.0 (Distance from origin in complex plane)


'''
5. Sets in Mathematics vs. Python (set & frozenset)
Mathematical Definition of a Set 
A set is an unordered collection of distinct (unique) objects. 
In mathematics:S = {1, 2, 3}
{1, 1, 2, 3} = {1, 2, 3} (Duplicates are collapsed).
A. Python set (Mutable)Unordered, unindexed collection of unique elements.
Elements must be hashable (immutable objects like numbers, strings, tuples; cannot contain lists or dicts).
'''
# set in simple
essential_spices = {"ginger", "cardamom", "cloves"}
optional_spices = {"cloves", "cumim", "cardamom", "black pepper"}
#remove duplicates
all_spices = essential_spices | optional_spices
print(f"{all_spices}") # {'cumim', 'cloves', 'black pepper', 'cardamom', 'ginger'}
# intersection only which are common in both
common_spices = essential_spices & optional_spices
print(common_spices) # {'cloves', 'cardamom'}
# Difference only in essential present but not in optional
only_essential = essential_spices - optional_spices
print(only_essential) # {'ginger'}
# Differences only in optional but not in essential
only_optional = optional_spices - essential_spices
print(only_optional) # {'cumim', 'black pepper'}
# Symmetric Difference elements either in essential or optional but not in both  as {cloves, cardamom} present in both thats why it won't show
only_unique_present = essential_spices ^ optional_spices
print(only_unique_present) #{'cumim', 'ginger', 'black pepper'}
# Subset
admin_roles = {"create", "read", "update", "delete"}
editor_roles = {"read", "update"}
# Check if editor is a subset of admin
is_sub = editor_roles.issubset(admin_roles)  # True

# Find what editor is missing (Set difference)
missing_perms = admin_roles - editor_roles  # {'create', 'delete'}

'''
B. Python frozenset (Immutable)
A frozenset is identical to a set, but it is immutable (cannot be modified after creation with .add() or .remove()).

Why frozenset matters:
Because regular set objects are mutable, they are unhashable—meaning they cannot be used as dictionary keys or stored inside other sets. A frozenset is hashable, so it can:
'''
# 1. Storing sets inside another set
grouped_categories = {
    frozenset(["tea", "coffee"]),
    frozenset(["milk", "water"])
}

# 2. Using sets as Dictionary Keys (e.g., routing graph nodes, graph caches)
edge_weights = {
    frozenset({"Bangalore", "Chennai"}): 350,
    frozenset({"Bangalore", "Hyderabad"}): 570
}

# Looking up distance regardless of direction:
dist = edge_weights[frozenset({"Chennai", "Bangalore"})]  # 350


# 1. Sets for quick deduplication & membership testing (O(1) speed)
active_user_ids = {101, 102, 103, 104, 105}
churned_user_ids = {103, 105}

retained_users = active_user_ids - churned_user_ids  # {101, 102, 104}

# 2. Fractions & Denominator Guarding for Metrics
total_users = len(active_user_ids)
churn_count = len(churned_user_ids)

churn_rate = (churn_count / total_users) * 100 if total_users > 0 else 0.0

# 3. Powers and Square Roots for Standard Deviation
values = [10, 12, 23, 23, 16, 23, 21, 16]
mean = sum(values) / len(values)

variance = sum((x - mean) ** 2 for x in values) / len(values)
std_dev = math.sqrt(variance)

print(f"Retained Users: {retained_users}")
print(f"Churn Rate: {churn_rate:.1f}%")
print(f"Mean: {mean:.2f} | Standard Deviation: {std_dev:.2f}")
