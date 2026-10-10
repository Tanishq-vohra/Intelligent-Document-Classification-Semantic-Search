import torch

x= torch.tensor([10, 20, 30, 40, 50])
y= torch.zeros(2, 3, 4)
z=torch.tensor([1, 2, 3])

print("the 1-d tensor is called a vector",x,"the shape is",x.shape,"and the dimension is",x.dim())
print("the 3-d tensor is called a cube of numbers",y,"the shape is",y.shape,"and the dimension is",y.dim())
print(x+z)