import torch

A = torch.tensor([1, 2, 3],[1, 2, 3])
B = torch.tensor([10, 20, 30],[10, 20, 30])

print("multiplying two tensors using *",A*B)

# X = torch.rand(32,100)
# W = torch.rand(100,10)

M = A@B
N = torch.matmul(A,B)

print("result of multiplying using @",M,"result of multiplying using matmul",N, "Shape of N", N.shape)