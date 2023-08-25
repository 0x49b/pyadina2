import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#make this example reproducible
np.random.seed(0)

#create dataset
period = np.arange(1, 101, 1)
leads = np.random.uniform(1, 50, 100)
prospects = np.random.uniform(40, 80, 100)
sales = 60 + 2*period + np.random.normal(loc=0, scale=.5*period, size=100)
df = pd.DataFrame({'period': period,
                   'leads': leads,
                   'prospects': prospects,
                   'sales': sales})


#plot individual lines
plt.plot(df['leads'])
plt.plot(df['prospects'])
plt.plot(df['sales'])

#display plot
plt.show()