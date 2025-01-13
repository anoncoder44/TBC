import sys
from TLP_code import n, Cm,Ck,a,k,t,p,q
def get_size(obj):
    """Calculate the size of an object in bytes."""
    if isinstance(obj, bytes):
        return len(obj)
    return sys.getsizeof(obj)

def calculate_overhead(n, Cm, Ck, a, k, t,p,q):
    # Storage overhead
    size_n = get_size(n)
    size_Cm = sum(get_size(part) for part in Cm) 
    size_Ck = get_size(Ck)
    size_a = get_size(a)
    size_k = get_size(k)
    size_t = get_size(t)
    size_p = get_size(p)
    size_q = get_size(q)
    params_size = size_n + size_p + size_q 
    storage_overhead = params_size + size_Cm + size_Ck + size_a + size_k + size_t
    # Communication overhead
    communication_overhead = size_Cm + size_Ck + size_a + size_t
    return params_size, storage_overhead, communication_overhead
 
params_size, storage_overhead, communication_overhead = calculate_overhead(n, Cm, Ck, a, k ,t,p,q)

print("Params Size:", params_size, "bytes")
print("Storage Overhead:", storage_overhead, "bytes")
print("Communication Overhead:", communication_overhead, "bytes")

