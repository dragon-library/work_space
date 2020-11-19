import pandas as pd
import numpy as np
import joblib
from time import time


def get_data(urls, sheets, types):
    data = ""
    t0 = time()
    a = []
    i = 0
    for s in sheets:
        s = pd.read_excel(urls, sheet_name=s)
        s = s[[types, 'description']]
        s['description'] = s['description'].str.lower()
        if i == 0:
            data = s.copy()
        else:
            data = pd.concat([data, s], ignore_index=True)
        i += 1
    data.columns = ['target', 'data']
    data['target'] = data['target'].apply(str)
    load_time = time() - t0
    print("Load dataset time:  %0.3fs" % load_time)

    return data


def Load_dataset(paths):
    data = ""
    t0 = time()
    data = joblib.load(paths)
    load_time = time() - t0
    print("Load data time:  %0.3fs" % load_time)

    return data
