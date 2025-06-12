import pandas as pd
import numpy as np
df = pd.read_csv('Data1.csv')
df

#pd.DataFrame(df['Current']-df['Previous'], columns=['results'])

task1 = pd.DataFrame({'Month': df['Month'],
                       'Flat': df['Flaat'],
                       'Results': df['Current']-df['Previous']})

task11=task1.sort_values('Month')
task1
  
#task11.to_csv('Data.csv')
for i in range(1,13):
    
    for line in task11:
        sum=0
        
        if line[1]==i:
            sum+=line[3]
        
        print('{} {} '.format(i,sum))
    