# 4 Matrix Decomposition
- In this chapter, we present three aspects of matrices:
1. how to summarize matrices
2. how matrices can be decomposed
3. how these decompositions can be used for matrix approximations

## 4.1 Determinant and Trace
- trace
1. tr(AB) = tr(BA)
2. while matrix representations of linear mappings are basis dependent the trace of a linear mapping Φ is independent of the basis.
3. the trace is invariant under cyclic permutations: tr(AKL) = tr(KLA)

- Characteristic Polynomial
$$p_\mathbf A(λ)= det(\mathbf A − λ\mathbf I)$$
$$c_0=det(\mathbf A)$$
$$c_{n-1}=(-1)^{n-1}tr(A)$$
## 4.2 Eigenvalues and Eigenvectors
- algrbraic multiplicity
The algebraic multiplicity of λ is the number of times the root appears in the characteristic polynomial.

- geometric multiplicity
the geometric multiplicity of λ is the number of linearly independent vectors associated with λ

- eigenspace

- The set of all eigenvalues of A is called the eigenspectrum of A.

- Theorem 4.12
The eigenvectors a matrix with n distinct eigenvalues are linearly independent.

- definition of defect

- we can always obtain a symmetric, positive semidefinite matrix S
$$\mathbf S=\mathbf{A^\top A}$$
- Theorem 4.15 (Spectral Theorem)
If A is symmetric, there exists an orthonormal basis of the corresponding vector space V consisting of eigenvectors of A, and each eigenvalue is real.

- The determinant of a matrix is the product of its eigenvalues.
- The trace of a matrix is the sum of its eigenvalues.

## 4.3 Cholesky Decomposition
- Theorem 4.18 (Cholesky Decomposition)
A symmetric, positive definite matrix A can be factorized into a product
$$ \mathbf {A=LL^\top} $$
L is a lowertriangular matrix with positive diagonal elements
L is called the Cholesky factor of A, and L is unique.

## 4.4 Eigendecomposition and Diagonalization
- definition of diagonalizable

- Theorem 4.20 (Eigendecomposition)
满秩方阵可以被特征值分解。

- Theorem 4.21
A symmetric matrix can always be diagonalized.

## 4.5 Singular Value Decomposition
- definition of SVD, singular values, left-singular vectors, right-singular vectors
- The SVD exists for any matrix.

### 4.5.1 Geometric Intuitions for the SVD
- 类似特征值分解
基变换，拉伸基向量，再变换回去

### 4.5.2 Construction of the SVD
- 将矩阵乘上它的转置得到一个对称阵，根据Spectral Theorem得到一个正交分解，然后可求singular values，left-singular vectors

### 4.5.3 Eigenvalue Decomposition vs. Singular Value Decomposition
- In the SVD, the left- and right-singular vector matrices U and V are generally not inverse of each other
- In the SVD, the entries in the diagonal matrix Σ are all real and nonnegative
- For symmetric matrices the eigenvalue decomposition and the SVD are one and the same

- other types of SVD
reduced SVD

## 4.6 Matrix Approximation
- rank-k approximatoin
$$ \mathbf{\hat A}(k)=\sum_{i=1}^k\sigma_i\mathbf{u_i v_i^\top} $$
- spectral norm
$$||A||_2=max\frac{||AX||_2}{||x||_2} $$
- Theorem 4.24. 
The spectral norm of A is its largest singular value $\sigma_1$.

- Theorem 4.25 (Eckart-Young Theorem )
原矩阵与k近似矩阵之差的范数为$\sigma_{k+1}$
原矩阵与其他rank-k矩阵的差的范数都比这大

## 4.7 Matrix Phylogeny
回顾了本书到此为止介绍的各种矩阵及其性质
