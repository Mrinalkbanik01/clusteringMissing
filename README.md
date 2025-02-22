# Clustering Imputation
## Installation
To install the package, run:
```bash
pip install clustering-imputation
```
## Usage

```python
from clustered_imputation import clusterImputer
df = ...  # Load your dataset
x = clusterImputer(data , basic_imputation , num_imputation , corr_threshold , max_iter)
x.impute()
```
# About the Package
## Features to be passed to the class clusterImputer
* data --> Pass your dataframe
* basic_imputation : Literal["mice" , "sice" , "em"] --> What imputation you want to perform on your clusters
* num_imputation : Literal["mean" , "median"] --> How do you want to handle your initial numeric column imputation for creating correlation matrix
* corr_threshold : 0.6 -->Threshold value to be used with respect to correlation matrix to create clusters
* max_iter : 10 -->Maximum iteration for MICE and SICE
## Problem Statement

* Traditional imputation techniques face several challenges:

* High-Dimensional and Sparse Data: Existing methods struggle with large, sparse datasets; efficient techniques for such cases are needed.

* Temporal Dependencies: Current methods often overlook temporal correlations in data.
## Need to develop a new algo
* Non-Random Missingness: Few methods address non-random missing patterns; improvements here could boost real-world application accuracy. We aim to develop an imputation method that considers "Missing Not at Random" (MNAR).

* Computational Complexity: MICE and EM methods are computationally expensive for high-dimensional data. Our approach aims to reduce time complexity.

## Philosophy of Our Solution: Clustered MICE/EM

We propose a clustering-based approach:

* Identify correlations between features.

* Apply MICE/EM within clusters rather than on the entire dataset.

* Combine results to reconstruct the dataset.

* This method effectively handles MNAR data by leveraging feature correlations.

For further details refer this [ppt](https://docs.google.com/presentation/d/1UZ2uDkleSgB2ZttjG1D6nmQhqk7uz5FQRW5UmSkB0Sg/edit?usp=sharing)
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
