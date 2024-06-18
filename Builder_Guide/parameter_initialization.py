import torch
from torch import nn
from d2l import torch as d2l

def block1():
    return nn.Sequential(nn.Linear(4, 8), nn.ReLU(),
                         nn.Linear(8, 4), nn.ReLU())

def block2():
    net = nn.Sequential()
    for i in range(4):
        net.add_module(f"block{i}", block1())
    return net

def init_normal(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, mean=0, std=0.01)
        nn.init.zeros_(m.bias)

def my_init(m):
    if type(m) == nn.Linear:
        print("Init", *[(name, param.shape) for name, param in m.named_parameters()][0])
        nn.init.uniform_(m.weight, -10, 10)
        m.weight.data *= m.weight.data.abs() >= 5


if __name__ == '__main__':
    # net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 1))
    # X = torch.rand(size=(2, 4))
    # Y = net(X)

    # print(Y)
    # print(net[2].state_dict())
    # print(type(net[2].bias))
    # print(net[2].bias)
    # print(net[2].bias.data)
    # print(*[(name, param.shape) for name, param in net[0].named_parameters()])
    # print(*[(name, param.shape) for name, param in net.named_parameters()])
    # print(net.state_dict()['2.bias'].data

    # rgnet = nn.Sequential(block2(), nn.Linear(4, 1))
    # print(rgnet(X))
    # print(rgnet)
    # print(rgnet[0][1][0].bias.data)

    # net.apply(init_normal)
    # print(net[0].weight.data[0])
    # print(net[0].bias.data[0])

    # net.apply(my_init)
    # print(net[0].weight[:2])

    # net[0].weight.data[:] += 1
    # net[0].weight.data[0, 0] = 42
    # print(net[0].weight.data[0])

    # # 我们需要给共享层一个名称，以便可以引用它的参数
    # shared = nn.Linear(8, 8)
    # net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(),
    #                     shared, nn.ReLU(),
    #                     shared, nn.ReLU(),
    #                     nn.Linear(8, 1))
    # net(X)
    # # 检查参数是否相同
    # print(net[2].weight.data[0] == net[4].weight.data[0])
    # net[2].weight.data[0, 0] = 100
    # # 确保它们实际上是同一个对象，而不只是有相同的值
    # print(net[2].weight.data[0] == net[4].weight.data[0])

    net = nn.Sequential(nn.LazyLinear(256), nn.ReLU(), nn.LazyLinear(10))
    print(net[0].weight)

    X = torch.rand(2, 20)
    net(X)

    print(net[0].weight.shape)