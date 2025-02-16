import pandas as pd
import numpy as np

# Creating a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, np.nan, 30, 35, np.nan],  # Missing values in 'Age'
    "Salary": [50000, 60000, np.nan, 80000, 90000],  # Missing value in 'Salary'
    "Department": ["HR", "IT", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

from clustering_imputation import clusterImputer
x = clusterImputer(df , "mice" ,"mean" , 0.4 ,10)
x.impute()
print(df)