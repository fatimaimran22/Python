#For testing and configuration management:
#save the old value
#change it
#restore it afterwards

DEBUG=False

from contextlib import contextmanager

@contextmanager
def Debug():
    global DEBUG
    DEBUG=True
    yield
    DEBUG=False


def process_data():
    if DEBUG:
        print("Processing data.")

with Debug():
    process_data()

print(f"After Debugging: {DEBUG}")