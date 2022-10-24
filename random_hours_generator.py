import pandas as pd
from random import randrange


# Generate the random hour and append in dataframe
data = pd.read_excel("file_name.xlsx")

# Create a dictionary and assign values to column 
d1 = {'Time' : pd.date_range(start = '10-10-2022', end = '11-10-2022', freq = f'{randrange(0,9)}H')}
d2 = data.assign(DateAndTimeRecent = pd.DataFrame(d1))
print(d2)

# Write data in excel file
with pd.ExcelWriter("filename.xlsx") as writer:
    d2.to_excel(writer)
