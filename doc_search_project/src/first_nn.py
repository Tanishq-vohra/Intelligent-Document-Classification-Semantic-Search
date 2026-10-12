import torch
import torch.nn as nn
import torch.optim as optim

# 1. Dummy Data: We want the model to learn the pattern y = 2x + 1
# X is the input, y is the true answer
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[3.0], [5.0], [7.0], [9.0]])

# 2. The Model: A single neuron. Takes 1 input, gives 1 output.
model = nn.Linear(in_features=1, out_features=1)

# 3. The Loss Function: Mean Squared Error
criterion = nn.MSELoss()

# 4. The Optimizer: Stochastic Gradient Descent.
# lr is learning rate (how big of a step to take).
optimizer = optim.SGD(model.parameters(), lr=1.00)

# --- YOUR TURN STARTS HERE ---

epochs = 100

for epoch in range(epochs):

    optimizer.zero_grad()

    output = model(X)

    loss = criterion(output,y)

    loss.backward()

    optimizer.step()
    
    # Print the loss every 20 epochs so we can watch it learn!
    if (epoch + 1) % 20 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")