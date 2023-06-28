import uuid

def generate_incremental_uuid():
    # Load the last generated UUID from a file or database
    # Here, we'll assume the last UUID is stored in a file called "last_uuid.txt"
    try:
        with open("last_uuid.txt", "r") as file:
            last_uuid = uuid.UUID(file.read().strip())
    except FileNotFoundError:
        last_uuid = uuid.uuid4()  # Generate a random UUID if the file doesn't exist
    
    # Generate the next UUID by incrementing the last UUID
    next_uuid = last_uuid.int + 1
    next_uuid = uuid.UUID(int=next_uuid)
    
    # Store the next UUID for future use
    with open("last_uuid.txt", "w") as file:
        file.write(str(next_uuid))

    return str(next_uuid)

# Generate the next incremental UUID
next_uuid = generate_incremental_uuid()
print("Next UUID:", next_uuid)
