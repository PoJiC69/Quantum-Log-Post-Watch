import hashlib

class TerraHash:
    def __init__(self, data):
        self.data = data

    def digest_sha512(self):
        sha512_hasher = hashlib.sha512()
        sha512_hasher.update(self.data)
        return sha512_hasher.digest()

    def digest_sha3_512(self):
        sha3_512_hasher = hashlib.sha3_512()
        sha3_512_hasher.update(self.data)
        return sha3_512_hasher.digest()

    def digest_blake2b(self):
        blake2b_hasher = hashlib.blake2b(self.data, digest_size=64)  # 64 bytes = 512 bits
        return blake2b_hasher.digest()

    def terra_hash(self):
        sha512_digest = self.digest_sha512()
        sha3_512_digest = self.digest_sha3_512()
        blake2b_digest = self.digest_blake2b()

        # Concatenate all digests
        combined_digest = sha512_digest + sha3_512_digest + blake2b_digest

        # Create the final hash
        final_hash = hashlib.sha512(combined_digest).digest()  # Final hash of concatenated digests

        return final_hash.hex()  # Return as hex string

# Example usage
if __name__ == '__main__':
    data = b'This is some data to hash.'
    th = TerraHash(data)
    print('TerraHash-8192:', th.terra_hash())