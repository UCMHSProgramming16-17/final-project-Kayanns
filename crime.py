# import the modules you need 
import csv 
import pandas as pd
import bokeh 

# To read the CSV file and create a dataframe
df = pd.read_csv('crimedata.csv')

#import needed plotting imports
from bokeh.charts import Bar, output_file, save


# To set up the bar graph 
p = Bar(df, label='County Names', values='ROBBERY', title='# of Robberies in different areas', color='green')

# create an output file
output_file('bargraph.html')

# save the bar graph to the file
save(p)





