import pandas as pd
from random import randrange


# Generate the random hour and append in dataframe
data = pd.read_excel("df2.xlsx")

# Create a dictionary and assign values to column 
d1 = {'Time' : pd.date_range(start = '10-10-2022', end = '11-10-2022', freq = f'{randrange(0,9)}H')}
d2 = data.assign(DateAndTimeRecent = pd.DataFrame(d1))
print(d2)