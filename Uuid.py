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


def generate_incremental_id():
    # Load the last generated ID from a file or database
    # Here, we'll assume the last ID is stored in a file called "last_id.txt"
    try:
        with open("last_id.txt", "r") as file:
            last_id = int(file.read().strip())
    except FileNotFoundError:
        last_id = 0  # Start from 0 if the file doesn't exist
    
    # Generate the next ID by incrementing the last ID
    next_id = last_id + 1
    
    # Store the next ID for future use
    with open("last_id.txt", "w") as file:
        file.write(str(next_id))
    
    return str(next_id).zfill(8)  # Return the ID as a string with leading zeros

# Generate the next incremental ID
next_id = generate_incremental_id()
print("Next ID:", next_id)


