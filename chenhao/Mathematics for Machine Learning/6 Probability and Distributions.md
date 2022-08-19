# 6 Probability and Distributions
## 6.1 Construction of a Probability Space
### 6.1.1 Philosophical Issues
### 6.1.2 Probability and Random Variables
### 6.1.3 Statistics
## 6.2 Discrete and Continuous Probabilities
## 6.3 Sum Rule, Product Rule, and Bayes’ Theorem
## 6.4 Summary Statistics and Independence
### 6.4.1 Means and Covariances
### 6.4.2 Empirical Means and Covariances
### 6.4.3 Three Expressions for the Variance
### 6.4.4 Sums and Transformations of Random Variables
- affine transformation 后的均值和协方差矩阵
- affine transformation 后两随机向量的协方差的矩阵表示

### 6.4.5 Statistical Independence
- Conditional Independence
p(x, y | z) = p(x | z)p(y | z) 或者 p(x | y, z) = p(x | z).
given that we know z, knowledge about y does not change our knowledge of x

### 6.4.6 Inner Products of Random Variables
- 内积：两随机变量的协方差
进而范数为方差，夹角为 arccos相关系数

## 6.5 Gaussian Distribution
### 6.5.1 Marginals and Conditionals of Gaussians are Gaussians
- 转换公式 p205

### 6.5.2 Product of Gaussian Densities
- 转换公式 p207

### 6.5.3 Sums and Linear Transformations
- 正态分布的和仍然是正态分布

- mixture density
转换公式 p208

- linear/affine transformation
转换公式 p209
求逆变换的时候用到了伪逆矩阵$(A^\top A)^{-1}$

### 6.5.4 Sampling from Multivariate Gaussian Distributions
- 获取$N\mathbf (0, I)$
先获得（0,1）区间内的（伪）随机数
再通过非线性映射获得N(0,I)的样本
最后取一个vector作为多维标准正态分布的样本

- 获取$N \mathbf (\mu, \Sigma)$
通过$\mathbf{y=Ax+\mu}$获得
A为$\Sigma$的Cholesky decomposition

## 6.6 Conjugacy and the Exponential Family
