import hashlib
from Crypto.Util import number
import sympy
import time

# Function to generate a large prime
def generate_large_prime(bits=1024):
    return number.getPrime(bits)

# Cryptographic hash function
def cryptographic_hash_function(m, k):
    """ Hash the message m and return an integer of size 2k bits """
    # Hash the message using SHA-256 (which gives a 256-bit hash)
    hash_value = hashlib.sha256(m.encode('utf-8')).hexdigest()
    # Convert hex to integer
    return int(hash_value, 16)

# Function to find the next prime greater than or equal to a given number
def next_prime_of_hashed(hashed_value):
    """ Return the next prime number greater than or equal to hashed_value """
    return sympy.nextprime(hashed_value)

# Setup phase for Wesolowski's VDF
def setup(k):
    # Generate two large primes p and q for RSA
    p = generate_large_prime(1536)  # Generate a 1536-bit prime
    q = generate_large_prime(1536)  # Generate a 1536-bit prime
    n = p * q  # RSA modulus n
    return n

# Evaluation phase for Wesolowski's VDF
def eval_vdf(m, n, t, k):
    """ Evaluate the VDF by performing squaring modulo n for t iterations """
    start_time = time.time()
    
    # Hash the message m to get the starting value
    x = cryptographic_hash_function(m, k)
    
    # Perform t squaring operations modulo n
    y = x
    for _ in range(t+1):
        y = pow(y, 2, n)  # y = y^2 mod n
    
    # Compute the prime related to the hashed value
    h_prime = next_prime_of_hashed(x + y)
    
    # Proof generation: In Wesolowski's VDF, the proof is a pair (y, h_prime)
    proof = (y, h_prime)
    eval_time = time.time() - start_time
    return y, h_prime, proof, eval_time

# Verification phase for Wesolowski's VDF
def verify_vdf(n, proof, m, t, k):
    """ Verify the VDF proof (y, h_prime) """
    y, h_prime = proof
    start_time = time.time()
    
    # Hash the message m to get the starting value
    x = cryptographic_hash_function(m, k)
    
    # Check the verification condition
    r = pow(2, t, h_prime)
    y1 = pow(y, h_prime, n)
    y2 = pow(x, r, n)
    y_res = (y1 * y2) % n
    
    # Verify if the computed result matches the expected prime
    verified = (h_prime == next_prime_of_hashed(x + y_res))
    verify_time = time.time() - start_time
    return verified, verify_time


# Example usage of the VDF
k = 128  # Security parameter (128-bit security)
t = 1000  # Number of squaring operations
message = "hello world"  # Example message

# Setup the VDF (RSA modulus generation)
n = setup(k)

# Evaluate the VDF
y, h_prime, proof, eval_time = eval_vdf(message, n, t, k)

# Print evaluation results
print(f"VDF Evaluation Results:")
print(f"Modulus n: {n}")
print(f"Number of squaring operations (t): {t}")
print(f"Proof (y, h_prime): {proof}")
print(f"Evaluation time: {eval_time:.4f} seconds")

# Verify the VDF
verified, verify_time = verify_vdf(n, proof, message, t, k)

# Print verification results
print(f"Verification result: {verified}")
print(f"Verification time: {verify_time:.4f} seconds")

