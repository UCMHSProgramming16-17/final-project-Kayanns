# import necessary modules

import pandas as pd
import bokeh

# create a data frame and read the csv file

data2 = pd.read_csv('crimedata.csv')

#import needed plotting imports
from bokeh.charts import Bar, output_file, save

# To set up the bar graph 
k = Bar(df, label='county_name', values='MURDER', title='Amount of Murders in the US', color='red')

# create an output file to save

output_file('murderbar.html')

# save the changes you made to the file

save(k)