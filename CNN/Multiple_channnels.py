import torch
from d2l import torch as d2l

def corr2d_multi_in(X, K):
    # 先遍历“X”和“K”的第0个维度（通道维度），再把它们加在一起
    return sum(d2l.corr2d(x, k) for x, k in zip(X, K))

def corr2d_multi_in_out(X, K):
    return torch.stack([corr2d_multi_in(X, k) for k in K], 0)

# def corr2d_multi_in_out_1x1(X, K):
#     c_i, h, w = X.shape
#     c_o = K.shape[0]
#     X = X.reshape((c_i, h * w))
#     K = K.reshape((c_o, c_i))
#     # 全连接层中的矩阵乘法
#     Y = torch.matmul(K, X)
#     return Y.reshape((c_o, h, w))

def corr2d_multi_in_out_1x1(X, K):
    c_i, h, w = X.shape
    c_o = K.shape[0]
    X = X.reshape((c_i, h * w))
    K = K.reshape((c_o, c_i))
    Y = torch.matmul(K, X)
    return Y.reshape((c_o, h, w))

if __name__ == '__main__':
    # X = torch.tensor([[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]],
    #                   [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]])
    # print(X)
    # K = torch.tensor([[[0.0, 1.0], [2.0, 3.0]], [[1.0, 2.0], [3.0, 4.0]]])
    # print(K)
    #
    # print(corr2d_multi_in(X, K))
    #
    # K = torch.stack((K, K + 1, K + 2), 0)
    # print(K.shape)
    # print(corr2d_multi_in_out(X, K))

    X = torch.normal(0, 1, (3, 3, 3))
    K = torch.normal(0, 1, (2, 3, 1, 1))

    Y1 = corr2d_multi_in_out_1x1(X, K)
    Y2 = corr2d_multi_in_out(X, K)
    assert float(torch.abs(Y1 - Y2).sum()) < 1e-6