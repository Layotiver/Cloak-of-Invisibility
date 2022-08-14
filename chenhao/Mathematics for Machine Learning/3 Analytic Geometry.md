# 3 Analytic Geometry
In this chapter, we will add some geometric interpretation and intuition to vectors, vector spaces, and linear mappings.

## 3.1 Norms
- 范数，不用多说，3个性质：
1. Absolutely homogeneous
2. Triangle inequality
3. Positive definite

- Manhattan Norm and Euclidean Norm

## 3.2 Inner Product
### 3.2.1 Dot Product
### 3.2.2 General Inner Products
- bilinear mapping, symmetric, positive definite

- A positive definite, symmetric bilinear mapping is called an inner product on V

- If we use the dot product, we call (V,<·, ·>) a Euclidean vector space

### 3.2.3 Symmetric, Positive Definite Matrices
- symmetric, positive definite and symmetric, positive semidefinite

- inner product 对应一个 symmetric, positive definite matrix

- properties of symmetric positive definite matrix A
1. The null space (kernel) of A consists only of 0
2. The diagonal elements of A are positive

## 3.3 Lengths and Distances
- the distance between vectors does not require an inner product: a norm is sufficient.

- distance and metric
<x, y> and d(x, y) behave in opposite directions. Very similar x and y will result in a large value for the inner product and a small value for the metric.

## 3.4 Angles and Orthogonality
- inner products also capture the geometry of a vector space by defining the angle ω between two vectors.

- Orthogonal Matrix
正交矩阵，转置为逆的矩阵
1. the length of a vector is not changed when transforming it using an orthogonal matrix
2. the angle between any two vectors is also unchanged when transforming both of them using an orthogonal matrix

## 3.5 Orthonormal Basis
## 3.6 Orthogonal Complement
- Consider a D-dimensional vector space V and an M-dimensional subspace U ⊆ V . Then its orthogonal complement is a (D−M)-dimensional subspace of V and contains all vectors in V that are orthogonal to every vector in U.

- orthogonal complements can be used to describe hyperplanes in n-dimensional vector and affine spaces.
## 3.7 Inner Product of Functions
卷积，介绍的不多
## 3.8 Orthogonal Projections
- definition of projection and projection matrices

### 3.8.1 Projection onto One-Dimensional Subspaces (Lines)
- 求投影后的向量和投影矩阵 p89

### 3.8.2 Projection onto General Subspaces
- 推导类似上一小节
$$ \mathbf\lambda=(\mathbf B^\top \mathbf B)^{-1}\mathbf B^\top\mathbf x $$
$$ \pi_U(\mathbf x)=\mathbf {B\lambda} $$
$$ {\mathbf P}_\pi=\mathbf{B(B^\top B)^{-1}B^\top} $$
- peudo-inverse
$$(\mathbf B^\top \mathbf B)^{-1}\mathbf B^\top$$
can be computed for non-square matrices B.
only requires that $B^\top B$ is positive definite, which is the case if B is full rank

- 考虑Ax=b无解的情况
可以求近似解，也就是把b投影到A的span上

### 3.8.3 Gram-Schmidt Orthogonalization
- 从一组基获得标准正交基的方法
每个基向量都删去在之前向量span上的投影，再将模变为1

### 3.8.4 Projection onto Affine Subspaces
- given an affine space $L = \mathbf x_0 + U$
$$ \pi_L(\mathbf x)=\mathbf x_0+\pi_U(\mathbf{x-x_0})  $$
## 3.9 Rotations
we will have a closer look at specific orthogonal transformation matrices, which describe rotations.

### 3.9.1 Rotatons in $R^2$
- 考虑$\mathbf e_1$和$\mathbf e_2$的旋转，得出rotation matrix

### 3.9.2 Rotations in $R^3$
- 考虑3个方向的旋转

### 3.9.3 Rotatons in n Dimensions
- Givens Rotation
identity matrix $I_n$ with rii = cos θ , rij = − sin θ , rji = sin θ , rjj = cos θ .

### 3.9.4 Properties of Rotations
- preserve distances and angles
- not commutable
the order in which rotations are applied is important