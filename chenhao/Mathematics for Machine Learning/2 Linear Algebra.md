# 2 Linear Algebra
## 2.1 Systems of Linear Equations
## 2.2 Matrices
### 2.2.1 Matrices Additon and Multiplication
### 2.2.2 Inverse and Transpose
- inverse of 2x2 matrices p30

### 2.2.3 Multiplication by a Scalar
### 2.2.4 Compact Representations of Systems of Linear Equations
## 2.3 Solving Systems of Linear Equations
### 2.3.1 Particular and General Solution
- The approach to get general solution:
1. Find a particular solution to Ax = b. 
2. Find all solutions to Ax = 0. 
3. Combine the solutions from steps 1. and 2. to the general solution.

### 2.3.2 Elementary Transformations
- elementary transformations
keep the solution set the same, but that transform the equation system into a simpler form.
1. Exchange of two equations
2. Multiplication of an equation (row) with a constant
3. Addition of two equations

- Row-Echelon Form
其实就是上三角矩阵
然后可以区别basic variables and free variables

- reduced row-echelon form
1. It is in row-echelon form.
2. Every pivot is 1. 
3. The pivot is the only nonzero entry in its column.
allowing us to determine the general solution of a system of linear equations in a straightforward way.

### 2.3.3 The Minus-1 Trick
introducing a practical trick for reading out the solutions $\mathbf x$ of a homogeneous system of linear equations Ax = 0

- 过程 p39
先把A（k x n），k<n，化成 row-echelon form，再在没有pivot的列处加上一个对应位置为-1的行，得到n x n矩阵，然后加入-1的那些列的线性组合就是Ax=0的通解

### 2.3.4 Algorithms for Solving a System of Linear Equations
In practice, systems of many linear equations are solved indirectly, by either stationary iterative methods and the successive over-relaxation method.

## 2.4 Vector Spaces

### 2.4.1 Groups
好家伙，群论都出来了

- definiton of group:
1. Closure
2. Associativity
3. Neutral element
4. Inverse element

- General Linear Group
可逆矩阵在矩阵乘法下构成群，即General Linear Group，GL(n, R)

### 2.4.2 Vector Spaces
- definiton p43

### 2.4.3 Vector Subspaces
与 dimensionality reduction 有关

- definition p45
感觉就是在原向量空间里取个子集，然后“继承”向量空间有的那些性质

## 2.5 Linear Independence
- linear combination

- Linear Independence

## 2.6 Basis and Rank
### 2.6.1 Generating Set and Basis
- generating set
- span
The set of all linear combinations of vectors in A is called the span of A.
If A spans the vector space V , we write V = span\[A]

- minimal generating set = basis

- The dimension of a vector space is not necessarily the number of elements in a vector.

- A basis of a subspace U = span\[x1, . . . , xm] ⊆ Rn can be found by executing the following steps:
1. Write the spanning vectors as columns of a matrix A
2. Determine the row-echelon form of A.
3. The spanning vectors associated with the pivot columns are a basis of U

### 2.6.2 Rank
- some properties
1. The columns of A ∈ Rm×n span a subspace U ⊆ Rm with dim(U) = rk(A). So as rows.
2. A is regular (invertible) if and only if rk(A) = n.
3. the linear equation system Ax = b can be solved if and only if rk(A) = rk(A|b).
4. the subspace of solutions for Ax = 0 possesses dimension n − rk(A).
5. the rank of a full-rank matrix is the lesser of the number of rows and columns, i.e., rk(A) = min(m, n).

## 2.7 Linear Mappings
- Theorem 2.17
Finite-dimensional vector spaces V and W are isomorphic if and only if dim(V) = dim(W).

### 2.7.1 Matrix Representation of Linear Mappings
- definiton of the coordinates, coordinate vector

- definiton of transformation matrix
The coordinates of Φ(bj ) with respect to the ordered basis C of W are the j-th column of AΦ.
The transformation matrix can be used to map coordinates with respect to an ordered basis in V to coordinates with respect to an ordered basis in W.

### 2.7.2 Basis Change
- Theorem 2.20 (Basis Change)
$$ \mathbf{\tilde A_\Phi=T^{-1}A_\Phi S} $$
- definition of Equivalance, Similarity

### 2.7.3 Image and Kernel
- definition of kernel/null, image/range
Im(Φ) ⊆ W is a subspace of W, and ker(Φ) ⊆ V is a subspace of V.

- Theorem 2.24 (Rank-Nullity Theorem)
dim(ker(Φ)) + dim(Im(Φ)) = dim(V ).
also referred to as the fundamental theorem of linear mappings

## 2.8 Affine Spaces
look at spaces that are no longer vector subspaces.

### 2.8.1 Affine Subspaces
- definitoin
linear subspace + support point = affine subspace

In $R^n$ , every k-dimensional affine subspace is the solution of a linear inhomogeneous equation system Ax = b, and rk(A) = n − k.

### 2.8.2 Affine Mappings
- definition:
linear mapping + translation vector = affine mapping

- The composition of affine mappings is affine.