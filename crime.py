# import the modules you need 
import csv 
import pandas as pd
import bokeh 

# To read the CSV file and create a dataframe
df = pd.read_csv('crimedata.csv')

#import needed plotting imports
from bokeh.charts import Bar, output_file, save

states = []
for n in range(len(df)):
    name = df.iloc[n]['county_name']
    state = name[-2:]
    states.append(state)

# To set up the bar graph 
p = Bar(df, label='county_name', values='ROBBERY', title='# of Robberies in different areas', color='green')

# create an output file
output_file('bargraph.html')

# save the bar graph to the file
save(p)





