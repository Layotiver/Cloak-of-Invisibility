# 创建一个新的张量，默认是不求导的
# 如果需要求导，可以指定参数tensor.requires_grad = True
# 在张量的计算过程中，如果在所有输入中，有一个输入需要求导，那么输出一定需要求导；
# 相反，只有当所有输入都不需要求导的时候，输出才会不需要

import torch
import torch.nn as nn

input = torch.randn(8, 3, 50, 100)
print(input.requires_grad)
# False

net = nn.Sequential(nn.Conv2d(3, 16, 3, 1),
                    nn.Conv2d(16, 32, 3, 1))
for param in net.named_parameters():
    print(param[0], param[1].requires_grad)
# 0.weight True
# 0.bias True
# 1.weight True
# 1.bias True

output = net(input)
print(output.requires_grad)
# True