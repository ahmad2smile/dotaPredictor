import json
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from pandas.plotting import andrews_curves

names = ['preg', 'plas', 'pres', 'skin',
         'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv("data.csv")

head = data.head()

# print(head)

# data.hist()
# plt.figure()
andrews_curves(data, 6)
# parallel_coordinates(data, 'Name')

# matches = json.load(open("matches.json"))

# totallMatches = len(matches)

# print(totallMatches)
