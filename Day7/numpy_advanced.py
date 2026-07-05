import numpy as np

arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25

print("Mask:")
print(arr[mask])

scaled = arr + 5

print("\nBroadcasting:")
print(scaled)

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (
        np.linalg.norm(v1) *
        np.linalg.norm(v2)
    )

a = np.array([1, 2, 3])
b = np.array([2, 4, 6])

c = np.array([1, 0, 0])
d = np.array([0, 1, 0])

print("\nSimilarity 1:", cosine_similarity(a, b))
print("Similarity 2:", cosine_similarity(c, d))