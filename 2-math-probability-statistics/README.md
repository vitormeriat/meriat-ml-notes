# MATH

> ... the objective of statistical methods is the reduction of data. A quantity of data... is to be replaced by relatively few quantities which shall adequately represent ... the relevant information contained in the original data. Since the number of independent facts supplied in the data is usually far greater than the number of facts sought, much of the information supplied by an actual sample is irrelevant. It is the object of
the statistical process employed in the reduction of data to exclude this irrelevant information, and to isolate the whole of the relevant
information contained in the data...  **R. A. Fisher**

In general, data representation can be vectors, matrices (esp. graphs, networks), tensors, and possibly unstructured such as images, videos, languages, sequences, etc. We start from a basic data representation as Euclidean vectors. Principal Component Analysis (PCA) and Multidimensional
Scaling (MDS) are dual one to the other. In PCA, one starts from high dimensional Euclidean representation and looks for a best affine (linear) approximation of data variations; while in MDS, one is exposed with a pairwise distance metric, and pursues an Euclidean representation preserving such a metric. They are actually dual problems, in the sense that given data indeed lying in an Euclidean space, PCA and MDS give different sides of singular vectors of the same data matrix, respectively. Such a geometric picture can be extended to Hilbert spaces of infinite dimension
via reproducing kernels as positive definite functions.

Principal component analysis (PCA), invented by Pearson (1901) and Hotelling (1933), is perhaps the most ubiquitous method for dimensionality reduction with high dimensional Euclidean data, under various names in science and engineering such as Karhunen-Lo`eve Transform, Empirical Orthogonal Functions, and Principal Orthogonal Decomposition, etc. Previously we have seen the geometric interpretation of PCA.

---

## Table of Contents

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


# Ref

1. A Mathematical Introduction to Data Science - by Yuan Yao

2. MOOCs on Mathematics & Statistics for Data Science & Machine Learning:
    1. ### Beginners Mathematics & Statistics
    * [1. Data Science Maths Skills](https://www.coursera.org/learn/datasciencemathskills)
    * [2. Intro to Descriptive Statistics](https://www.udacity.com/course/intro-to-descriptive-statistics--ud827)
    * [3. Intro to Inferential Statistics](https://www.udacity.com/course/intro-to-inferential-statistics--ud201)
    * [4. Introduction to Probability and Data](https://www.coursera.org/learn/probability-intro)
    * [5. Math is Everywhere: Applications of Finite Math](https://www.udemy.com/math-is-everywhere-applications-of-finite-math/)
    * [6. Probability: Basic Concepts & Discrete Random Variables](https://www.edx.org/course/probability-basic-concepts-discrete-purduex-416-1x)
    * [7. Mathematical Biostatistics Boot Camp 1](https://www.coursera.org/learn/biostatistics)
    * [8. Applications of Linear Algebra Part 1](https://www.edx.org/course/applications-linear-algebra-part-1-davidsonx-d003x-1)
    * [9. Introduction to Mathematical Thinking](https://www.coursera.org/learn/mathematical-thinking)

    2. ### Intermediate Mathematics & Statistics
    * [1. Bayesian Statistics: From Concept to Data Analysis](https://www.coursera.org/learn/bayesian-statistics)
    * [2. Game Theory 1](https://www.coursera.org/learn/game-theory-1)
    * [3. Game Theory II: Advanced Applications](https://www.coursera.org/learn/game-theory-2)
    * [4. Introduction to Linear Models and Matrix Algebra](https://www.edx.org/course/introduction-linear-models-matrix-harvardx-ph525-2x-0)
    * [5. Advanced Linear Models for Data Science 1: Least Squares](https://www.coursera.org/learn/linear-models)
    * [6. Advanced Linear Models for Data Science 2: Statistical Linear Models](https://www.coursera.org/learn/linear-models-2)
    * [7. Maths in Sports](https://www.edx.org/course/math-sports-notredamex-mat150x#!)

    3. ### Advanced Mathematics & Statistics
    * [1.Discrete Optimization](https://www.coursera.org/learn/discrete-optimization)
    * [2. Statistics for Genomic Data Science](https://www.coursera.org/learn/statistical-genomics)
    * [3. Biostatistics for Big Data Applications](https://www.edx.org/course/biostatistics-big-data-applications-utmbx-stat101x#!)

