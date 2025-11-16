import sys
import os
import hashlib

if len(sys.argv) != 3:
    print("Usage: python3 file_integrity_checker.py [generate/verify] <file_path>")
    sys.exit(1)

mode = sys.argv[1]
file_path = sys.argv[2]

print(f"[*] Mode selected: {mode}")
print(f"[*] File path provided: {file_path}")

if mode == "generate":
    print("\n--- Generate Mode Activated ---")
    try:
        with open(file_path, "rb") as f:
            file_bytes = f.read()
            sha256_hash = hashlib.sha256(file_bytes).hexdigest()
            hash_file_path = f"{file_path}.sha256"

            with open(hash_file_path, "w") as f_hash:
                f_hash.write(sha256_hash)
                print(f"[+] SHA256 hash of '{hash_file_path}' is:")

    except FileNotFoundError:
        print(f"[!] File '{file_path}' not found.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")

elif mode == "verify":
    print("\n--- Verify Mode Activated ---")
    hash_file_path = f"{file_path}.sha256"

    if not os.path.exists(file_path) or not os.path.exists(hash_file_path):
        print(f"[!] Error: Cannot find '{file_path}' or its required hash file '{hash_file_path}'")
        sys.exit(1)

    try:
        with open(file_path, "rb") as f:
            file_bytes = f.read()
            calculated_hash = hashlib.sha256(file_bytes).hexdigest()
        with open(hash_file_path, "r") as f_hash:
            original_hash = f_hash.read().strip()
        print(f"[*] Calculated Hash: {calculated_hash}")
        print(f"[*] Original Hash  : {original_hash}")

        if calculated_hash == original_hash:
            print("\n[+] INTEGRITY VERIFIED: The file is authentic and has not been modified.")
        else:
            print("\n[!] SECURITY ALERT: The file has been tampered with! The hash does not match.")

    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")

else:
    print(f"[!] Error: Invalid mode '{mode}'. Please use 'generate' or 'verify'.")
    sys.exit(1)