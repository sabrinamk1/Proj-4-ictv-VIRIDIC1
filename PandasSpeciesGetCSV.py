
#this code automates getting the 3rd sheet from the ICTV master species excel file 

import pandas as pd

#read sheet directly into data frame
df= pd.read_excel('ICTV Master Species List 2020.v1', 'ICTV2020 Master Species List#36')

#use pandas to go to column names, can use method columns()


data = df['Species'].tolist()


#write to Species.csv file to be used in our for loop 
with open ('Species.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
