# -*- coding: utf-8 -*-
"""GB840-class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17dR_aX69oxo6vb1OX241zN3okhLpcjhZ

# My name is Kanchan Tenginakai
This is my Jupyter notebook
"""

import pandas as pd

url = 'http://bit.ly/ad_spend'
df_ads = pd.read_csv(url)

df_ads.shape

df_ads.head()

df_ads['sales'].plot.hist(bins=12);