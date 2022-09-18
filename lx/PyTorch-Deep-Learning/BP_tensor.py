import torch

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.Tensor([1.0])
w.requires_grad = True
# 默认w不需要计算梯度，这里需要手动设置为True

def forward(x):
    return x * w

def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

print("predict (before training)", 4, forward(4).item())

for epoch in range(100):
    for x, y in zip(x_data,y_data):
        l = loss(x, y)  # Forward,compute the loss, also a tensor
        l.backward()    # Backward,compute grad for Tensor whose requires_grad set to True
        print('\tgrad:',x, y, w.grad.item())
        w.data = w.data - 0.01 * w.grad.data    # The grad is utilized to update weight, grad is a tensor

        w.grad.data.zero_()
        # The grad computed by .backward() will be accumulated
        # So after update, remenber to set the grad to ZERO.
    print("progress:",epoch, l.item())

print("predict (after training)", 4, forward(4).item())