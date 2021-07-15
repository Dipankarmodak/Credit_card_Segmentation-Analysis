from sklearn.base import TransformerMixin, BaseEstimator
\
import pandas as pd



class CreateCategory(TransformerMixin, BaseEstimator):
    
        def __init__(self):
            print('n>>>>>>init() called.\n')
           
            
        
    
        def fit(self, X, y= None):
            return self
        
        def transform(self, X: pd.DataFrame) -> pd.DataFrame:
            X.loc[(X['ONEOFF_PURCHASES']==0) & (X['INSTALLMENTS_PURCHASES']==0),'Type_of_Purchase']='No_purchase'
            X.loc[(X['ONEOFF_PURCHASES']>0) & (X['INSTALLMENTS_PURCHASES']==0),'Type_of_Purchase']='One_of_purchase'
            X.loc[(X['ONEOFF_PURCHASES']==0) & (X['INSTALLMENTS_PURCHASES']>0),'Type_of_Purchase']='Installment_purchase'
            X.loc[(X['ONEOFF_PURCHASES']>0) & (X['INSTALLMENTS_PURCHASES']>0),'Type_of_Purchase']='Both_purchase'
            return X