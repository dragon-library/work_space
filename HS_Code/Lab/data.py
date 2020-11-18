import pandas as pd
import numpy as np
def get_data(urls,sheets,types):
    a = []
    i = 0
    for s in sheets:
        s = pd.read_excel(urls,sheet_name= s)
        s = s[[types,'description']]
        s['description'] = s['description'].str.lower()
        if i == 0:
            data = s.copy()            
        else:            
            data = pd.concat([data,s], ignore_index=True)            
        i += 1         
    data.columns =  ['target', 'data']    
    data['target'] = data['target'].apply(str)
        
    return data