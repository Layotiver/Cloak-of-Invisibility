import torch

x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[2.0], [4.0], [6.0]])

# Our model class should be inherit from nn.Module, which is Base class for all neural network modules.
class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = torch.nn.Linear(1,1)  
# Class nn.Linear contain two member Tensors: weight and bias

    def forward(self, x):
        y_pred = self.linear(x) 
        return y_pred
# Class nn.Linear has implemented the magic method __call__(), which enable the instance of the class can be called just like a function.
# Normally the forward() will be called.
# Module实现了魔法函数__call__()，call()里面有一条语句是要调用forward()。因此新写的类中需要重写forward()覆盖掉父类中的forward()
        
model = LinearModel()
# Create a instance of class LinearModel.

criterion = torch.nn.MSELoss(size_average=False)

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print('w = ',model.linear.weight.item())
print('b = ',model.linear.bias.item())

x_test = torch.Tensor([4.0])
y_test = model(x_test)
print('y_pred = ', y_test.data)