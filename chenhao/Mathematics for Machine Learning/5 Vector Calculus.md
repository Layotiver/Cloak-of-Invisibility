# 5 Vector Calculus
## 5.1 Differentiation of Univariate Functions
### 5.1.1 Taylor Series
### 5.1.2 Differentiation Rules
## 5.2 Partial Differentiation and Gradients
- definiton of gradient
- Gradient as a Row Vector
1. we can consistently generalize the gradient to vector-valued functions.
2. we can immediately apply the multi-variate chain rule without paying attention to the dimension of the gradient.

### 5.2.1 Basic Rules of Partial Differentiation
### 5.2.2 Chain Rule
- 链式法则的矩阵形式

## 5.3 Gradients of Vector-Valued Functions
- 向量值函数$\mathbf {f(x)}$
把一个向量映射为另一个向量，f 对 x 的一个分量求偏导得到一个列向量

- Jacobian
$f$对$x$求导得到的一个矩阵

## 5.4 Gradients of Matrices
- tensor Jacobian
一个m\*n 的矩阵对p\*q的矩阵求梯度，将得到(m\*n)\*(p\*q)的Jacobian

## 5.5 Useful Identities for Computing Gradients
列了几条与矩阵求导有关的公式

- trace and transpose of tensor
D x D x E x F 的tensor，trace为 E x F 的矩阵，transposse为调换最开始的两个维度

## 5.6 Backpropagation and Automatic Differentiation
### 5.6.1 Gradients in a Deep Network
梯度反向传播
### 5.6.2 Automatic Differentiation
- The automatic differentiation approach above works whenever we have a function that can be expressed as a computation graph, where the elementary functions are differentiable.
感觉还是在讲反向传播

## 5.7 Higher-Order Derivatives
- Hessian Matrix
If $f$ : $R_n$ → $R_m$ is a vector field, the Hessian is an (m × n × n)-tensor

## 5.8 Linearization and Multivariate Taylor Series
- $(\mathbf x-\mathbf x_0)^k$ 是一个k维的tensor，每次乘积是一次outer product