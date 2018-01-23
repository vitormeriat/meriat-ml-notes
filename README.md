<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.1/css/font-awesome.min.css">

![version](https://img.shields.io/badge/version-v1.0-yellowgreen.svg) [![GitHub issues](https://img.shields.io/github/issues/vitormeriat/meriat-ml-notes.svg)](https://github.com/vitormeriat/meriat-ml-notes/issues) [![Twitter](https://img.shields.io/twitter/url/https/github.com/vitormeriat/meriat-ml-notes.svg?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D)

# Meriat Machine Learning Notes

Documentação contendo as anotações, observações e aprendizados durante minha árdua tarefa de estudar **Machine Learning**...

Minha intenção aqui é agrupar de forma lógica todo o conteúdo produzido neste repositório. Muito aqui é resultado de exercícios de livros e cursos realizados ao longo dos meus estudos.

Todo o material é referenciado para sua fonte, e como exercício será traduzido para o `inglês` e em tempo oportuno para a linguagem `R`.

#### Author

[Vitor Meriat](http://www.vitormeriat.com.br/) is a computer scientist who is passionate about creating software that will positively change the world we live in.

<img alt="Vitor Meriat" src="http://www.vitormeriat.com.br/assets/images/profile.jpg" height="50" width="50">

:alien: <a class="fa fa-twitter" aria-hidden="true" href="https://twitter.com/vitormeriat" target="_blank"> twitter</a> | <a class="fa fa-facebook" aria-hidden="true" href="https://www.facebook.com/vitormeriat/" target="_blank"> facebook</a> | <a class="fa fa-instagram" aria-hidden="true" href="https://www.instagram.com/vitormeriat/" target="_blank"> instagram</a> | <a class="fa fa-linkedin" aria-hidden="true" href="https://www.linkedin.com/in/vitormeriat" target="_blank"> linkedin</a> | <a class="fa fa-youtube" aria-hidden="true" href="https://www.youtube.com/user/vitormeriat/" target="_blank"> youtube</a>

Como **Cloud specialist** não posso deixar de indicar com uma certa importância, que todos leiam sobre a utilização de **cloud computing**. Pode não parecer o foco deste material mas a importância desta tecnologia para o universo da inteligência artificial é algo que deve ser notado...

> Depending on your company, mission, and budget, the biggest limitation is usually cost: powerful hardware and smart people don’t come cheap. But it seems a few companies are moving to eliminate the infrastructure part of the equation. Cloud computing has already permeated every facet of online activity. However, recent developments in AI and the increasing sophistication of programmers, presages a new age of cloud computing.

<p align="center">
  <img src="https://i0.wp.com/metakermit.com/files/2017/09/compiling.png" alt="mkcd" />
  <br/>
  by XKCD
</p>



## Foundations
1. [What is Machine Learning](/01-concepts/0-what-is-machine-learning.ipynb)
2. Programming
    * Syntax and basic concepts
    * Practice: Coderbyte, Codewars, HackerRank
3. Math
    1. Calculus
        * [Basic math notions](/02-math-probability-statistics/Basic-Math.ipynb)        
        * [NaN and Numeric Limits](/02-math-probability-statistics/NaN-and-Numeric-Limits.ipynb)
    2. Linear algebra
        * [Linear Algebra](/02-math-probability-statistics/Linear-Algebra.ipynb)
    3. Probability 
        * [Basic Probability](/02-math-probability-statistics/Basic-Probability.ipynb)
        * Common Ground
        * Limit Theorems
        * Derived Distributions
            * Covariance
            * Correlation
    4. Statistics
        * [Basic Statistic](/02-math-probability-statistics/Basic-Statistic.ipynb)
        * [More Statistics](/02-math-probability-statistics/Statistics.ipynb)
4. Packages for scientific computing
    1. Numpy
        * [Numpy arrays](/data-assimilation-and-visualization/numpy-arrays.ipynb)
        * [Numpy indexing and selection](/data-assimilation-and-visualization/numpy-indexing-and-selection.ipynb)
        * [Numpy operations](/data-assimilation-and-visualization/numpy-operations.ipynb)
        * [Numpy tests](/data-assimilation-and-visualization/numpy-tests.ipynb)
    2. Pandas
 

## Exploratory Data Analysis

1. Visualization
    * [Criação de gráficos interativos com Bokeh](/data-assimilation-and-visualization/criação-de-gráficos-interativos-com-bokeh.ipynb)  
    * [Maps with the Basemap Library](/data-assimilation-and-visualization/maps-with-the-basemap-library.ipynb)
    * [Plotando mapas com folium](/data-assimilation-and-visualization/plotando-mapas-com-folium.ipynb)
    * [Simple Plotting](/data-assimilation-and-visualization/simple-plotting.ipynb) 
2. Assimilation
    * [Song Recommender](/data-assimilation-and-visualization/song-recommender.ipynb)
    * [Web scraping](/data-assimilation-and-visualization/web-scraping-with-python.ipynb)
    * [Data Cleaning](/data-assimilation-and-visualization/data-cleaning.ipynb)
    * [File Handling](/data-assimilation-and-visualization/file-handling.ipynb)
    * [Handling Missing Data Values](/data-assimilation-and-visualization/handling-missing-data-values.ipynb)
    * [Introducing-Scikit-Learn](/data-assimilation-and-visualization/introducing-scikit-learn.ipynb)



## Artificial intelligence

1. Machine learning
    1. [Algorithms](/05-algorithms-and-complexity/)
        * Análise do componente principal (PCA)
        * Árvores de decisão e Florestas Aleatórias
        * K-Means-Clustering
        * K-Nearest-Neighbors
        * Processamento de Linguagem Natural
        * Regressão Logística
        * Regressões Lineares
        * Sistemas de recomendação
        * Support-Vector-Machines
        * Map and Reduce
        * Regular Expression
    2. [Natural Language Processing](/05-algorithms-and-complexity/natural-language-processing/)
        * [Basic Natural Language Processing](/05-algorithms-and-complexity/natural-language-processing/Basic-Natural-Language-Processing.ipynb)
        * [Tokenizing Words](/05-algorithms-and-complexity/natural-language-processing/Tokenizing-Words.ipynb)
        * [Tokenizing Sentences](/05-algorithms-and-complexity/natural-language-processing/Tokenizing-Sentences.ipynb)
        * [Stopword Removal](/05-algorithms-and-complexity/natural-language-processing/Stopword-Removal.ipynb)
        * N-Grams
        * WordSense Disambiguation
        * Parts-of-Speech
        * [Autosummarize](/05-algorithms-and-complexity/natural-language-processing/Autosummarize.ipynb)
        * [Frequency Analysis](/05-algorithms-and-complexity/natural-language-processing/Frequency-Analysis.ipynb)
2. [Deep learning](/08-deep-learning/)
    * **MeriatFlow**: Deep neural network building library
    * CNTK
        * [Introduction](/08-deep-learning/CNTK-Introduction.ipynb)
        * [Intro to NN with Iris dataset](/08-deep-learning/CNTK-Intro-to-NN-with-Iris-dataset.ipynb)
        * [SMS Spam Filtering](/08-deep-learning/CNTK-SMS-Spam-Filtering.ipynb)
    * TensorFlow
        * [Basic syntax and constructs](/08-deep-learning/Tensorflow-Basic-syntax-and-constructs.ipynb)
        * [Compare GPU vs CPU perfomance](/08-deep-learning/Tensorflow-Compare-GPU-vs-CPU-perfomance .ipynb)
        * [DNN classifier IRIS data](/08-deep-learning/Tensorflow-DNN-classifier-IRIS-data.ipynb)
        * [Estimator API Regression](/08-deep-learning/Tensorflow-Estimator-API-Regression-Example.ipynb)
        * [Function approximation by linear model and deep network](/08-deep-learning/Tensorflow-Function-approximation-by-linear-model-and-deep-network.ipynb)
        * [Intro with Iris dataset](/08-deep-learning/Tensorflow-Iris.ipynb)
        * [Iris with Sklearn](/08-deep-learning/Tensorflow-Iris-with-Sklearn.ipynb)
        * [Manually building NN by defining Class Graph Operation](/08-deep-learning/Tensorflow-Manually-building-NN-by-defining-Class-Graph-Operation.ipynb)
        * [Regression hyperparameters](/08-deep-learning/Tensorflow-Regression-hyperparameters.ipynb)
        * [RNN time series prediction intro](/08-deep-learning/Tensorflow-RNN-time-series-prediction-intro.ipynb)
        * [Train API with Linear Regression](/08-deep-learning/Tensorflow-Train-API-with-Linear-Regression.ipynb)
    * Reinforcement learning (TBA)
3. Reinforcement learning
    * TBA



## [Data](/data/)

> Folders and datasets or files used in projects.

* Data Cleaning
* File Handling
* Forest Cover Type
* Indian Diabetes
* Map Plotting
* SMS Spam
* Titanic



## Ref

As referências vão estar documentadas nos arquivos de cada módulo, tópico ou nos próprios cadernos em área reservada ao mesmo.

Parte do conteúdo é baseado em livros e cursos, sobre os quais apenas posso indicar os meios de obtenção do material.

O que for oriundo de **papers** e **blogs** vai contar com o link para as fontes originais :D