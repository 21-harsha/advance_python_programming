import gc
import tracemalloc

# Function to create objects
def create_objects():
    objects = []
    for i in range(1000):
        objects.append([i] * 100)
    return objects

# Function to display memory usage
def display_memory():
    current, peak = tracemalloc.get_traced_memory()
    print("Current Memory Usage:", current, "bytes")
    print("Peak Memory Usage:", peak, "bytes")

# Start memory tracking
tracemalloc.start()

# Display initial memory usage
print("Initial Memory Usage:")
display_memory()

# Create objects
data = create_objects()

# Display memory after creating objects
print("\nMemory After Creating Objects:")
display_memory()

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_STATS)

# Delete objects
del data

# Collect garbage
print("\nGarbage Collection:")
collected = gc.collect()
print("Objects Collected:", collected)

# Display memory after garbage collection
print("\nMemory After Garbage Collection:")
display_memory()

# Disable garbage collection debugging
gc.set_debug(0)

# Stop memory tracking
tracemalloc.stop()

print("\nMemory Management Completed.")
