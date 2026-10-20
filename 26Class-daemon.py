"""
A daemon thread in Python is a background thread that automatically dies when the main program finishes.

Normally, Python waits for all running threads to finish before exiting. 
But if a thread is marked as a daemon, Python will ignore it and exit immediately when the main thread is done.
"""
import threading
import time

def background_task():
    while True:
        print("Deamon is running in background .....")
        time.sleep(1)
# Set daemon=True when creating the thread
t = threading.Thread(target=background_task, daemon=True)
t.start()
# Main program does some quick work
print("Main Thread Working for 3 secs ....")
time.sleep(3)

print("Main thread: Done! Exiting program.")
# The daemon thread will be killed instantly here

"""
output
Deamon is running in background .....
Main Thread Working for 3 secs ....
Deamon is running in background .....
Deamon is running in background .....
Main thread: Done! Exiting program.
"""

'''
What happens if daemon=False (Standard Thread)?
If you remove daemon=True or set it to False, 
the script will never exit on its own because the while True loop inside background_task will keep Python alive forever.
'''
"""
Common Use Cases:
Periodic background autosaving/caching

Heartbeat pings to a server

Background system monitoring/logging
"""