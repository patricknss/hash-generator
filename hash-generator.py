import hashlib

def generate_hash(text, algorithm='sha256'):
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(text.encode('utf-8'))
    return hash_obj.hexdigest()

def compare_hashes(hash1, hash2):
    return hash1 == hash2

def main():
    print("=== Hash Generator ===")
    
    text = input("Enter the text to generate the hash: ")
    algorithm = input("Choose the hash algorithm (md5, sha1, sha256, sha512): ").lower()
    
    valid_algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    if algorithm not in valid_algorithms:
        print("Invalid algorithm! Using SHA-256 as default.")
        algorithm = 'sha256'
    
    generated_hash = generate_hash(text, algorithm)
    print(f"\nGenerated hash ({algorithm.upper()}): {generated_hash}")
    
    print("\n=== Hash Comparison ===")
    text2 = input("Enter another text to compare the hash (or press Enter to skip): ")
    if text2:
        hash2 = generate_hash(text2, algorithm)
        print(f"Hash of the second text ({algorithm.upper()}): {hash2}")
        
        if compare_hashes(generated_hash, hash2):
            print("The hashes are equal!")
        else:
            print("The hashes are different!")
    else:
        print("Hash comparison skipped.")

if __name__ == "__main__":
    main()
