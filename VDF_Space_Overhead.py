import sys
from VDF_code import n,h_prime,x,proof_phi,y,p,q,t
def get_size(obj):
    """Calculate the size of an object in bytes."""
    if isinstance(obj, bytes):
        return len(obj)
    return sys.getsizeof(obj)

def calculate_overhead(n,h_prime,h_proof,x,y,p,q):
    # Storage overhead
    size_n = get_size(n) 
    size_h_prime = get_size(h_prime)
    size_proof_phi = get_size(proof_phi)
    size_x = get_size(x)
    size_y = get_size(y)
    size_p = get_size(p)
    size_q = get_size(q)
    size_t = get_size(t)
    params_size = size_n + size_p + size_q
    storage_overhead =params_size + size_h_prime + size_proof_phi + size_y + size_x + size_t
    # Communication overhead
    communication_overhead = size_h_prime + size_proof_phi
    return params_size, storage_overhead, communication_overhead
 
params_size, storage_overhead, communication_overhead = calculate_overhead(n,h_prime,proof_phi, x,y,p,q)

print("Params size:", params_size, "bytes")
print("Storage Overhead:", storage_overhead, "bytes")
print("Communication Overhead:", communication_overhead, "bytes")

