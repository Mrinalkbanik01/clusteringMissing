import pandas as pd
import numpy as np
from getClusters import getClusters
from dummyData import data
from typing import Literal
from basicImputer import mice , sice , em
from clustering import encode , decode
def impute(df , basic_imputation : Literal["mice" , "sice" , "em"] , num_imputation : Literal["mean" , "median"] , 
           corr_threshold : 0.6 , max_iter : 10):
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    encode(df , cat_cols)
    clusters = getClusters(df , num_imputation , corr_threshold  , num_cols , cat_cols)
    dataFrames = []
    for cluster in clusters:
        df_cl = df[cluster]
        if basic_imputation == "mice":
            df_cl = mice(df_cl ,max_iter)
        elif basic_imputation == "sice":
            df_cl = sice(df_cl , max_iter)
        else:
            df_cl = em(df_cl)
        dataFrames.append(df_cl)

    ans = dataFrames[0]
    for i in range(1 , len(dataFrames)):
        ans = pd.concat([ans , dataFrames[i]] , axis = 1)
    decode(ans  , cat_cols)
    df = ans

    
# testing