import hashlib

def hashFunction(password):
    # Encode the password as bytes
    password_bytes = password.encode('utf-8')
    
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the encoded password
    sha256.update(password_bytes)
    
    # Get the hexadecimal digest of the hash
    hashed_password = sha256.hexdigest()
    
    return hashed_password


print(hashlib.sha256(('hi'.encode())).hexdigest())
