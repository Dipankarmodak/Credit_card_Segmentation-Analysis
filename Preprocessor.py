
import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator




class Droprow(TransformerMixin, BaseEstimator):
    
        def __init__(self,variables):
            self.variables=variables
        
    
        def fit(self, X, y= None):
            return self
        
        def transform(self,X):
            X=pd.DataFrame(X)
            X.dropna(axis=0,how='any',subset=self.variables,inplace=True)
            X.reset_index(drop=True,inplace=True)
            return X
    
 
  
           
    
        