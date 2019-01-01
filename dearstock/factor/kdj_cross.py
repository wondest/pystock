'''

kdj 交叉选股因子

Created on Jan 1, 2019

@author: Tender
@group: DearBao
@contact: 396934200@qq.com
@public: weixin public "笛尔宝"
'''

import pandas as pd

def kdj_cross(df):
    """
    Description:
      kdj交叉
    Parameter:
      df : DataFrame : 交易数据,kdj_k,kdj_d
    Return:
      DataFrame :交易数据,kdj_gold,kdj_dead
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')

    if df is None:
        raise ValueError('Argument df is None')
    
    kdj_position = df['kdj_k'] > df['kdj_d']
    # k向上突破d
    df['kdj_gold'] = (kdj_position == True) & (kdj_position.shift(1) == False)
    
    # d向下突破k
    df['kdj_dead'] = (kdj_position == False) & (kdj_position.shift(1) == True)
    
    return df
    