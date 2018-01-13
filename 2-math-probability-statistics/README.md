# Meriat Machine Learning Note

> ... the objective of statistical methods is the reduction of data. A quantity of data... is to be replaced by relatively few quantities which shall adequately represent ... the relevant information contained in the original data. Since the number of independent facts supplied in the data is usually far greater than the number of facts sought, much of the information supplied by an actual sample is irrelevant. It is the object of
the statistical process employed in the reduction of data to exclude this irrelevant information, and to isolate the whole of the relevant
information contained in the data...  **R. A. Fisher**

In general, data representation can be vectors, matrices (esp. graphs, networks), tensors, and possibly unstructured such as images, videos, languages, sequences, etc. We start from a basic data representation as Euclidean vectors. Principal Component Analysis (PCA) and Multidimensional
Scaling (MDS) are dual one to the other. In PCA, one starts from high dimensional Euclidean representation and looks for a best affine (linear) approximation of data variations; while in MDS, one is exposed with a pairwise distance metric, and pursues an Euclidean representation preserving such a metric. They are actually dual problems, in the sense that given data indeed lying in an Euclidean space, PCA and MDS give different sides of singular vectors of the same data matrix, respectively. Such a geometric picture can be extended to Hilbert spaces of infinite dimension
via reproducing kernels as positive definite functions.

Principal component analysis (PCA), invented by Pearson (1901) and Hotelling (1933), is perhaps the most ubiquitous method for dimensionality reduction with high dimensional Euclidean data, under various names in science and engineering such as Karhunen-Lo`eve Transform, Empirical Orthogonal Functions, and Principal Orthogonal Decomposition, etc. Previously we have seen the geometric interpretation of PCA.

---

## MATH

* [Basic math notions](/Basic-Math.ipynb)
* [Linear Algebra](/Linear-Algebra.ipynb)
* [NaN and Numeric Limits](/NaN-and-Numeric-Limits.ipynb)

#### Probability
* [Basic Probability](/Basic-Probability.ipynb)
* Common Ground
* Limit Theorems
* Derived Distributions
    * Covariance
    * Correlation
#### Statistics
* [Basic Statistic](/Basic-Statistic.ipynb)
* [More Statistics](/Statistics.ipynb)


## Ref
* A Mathematical Introduction to Data Science - by Yuan Yao