import pandas as pd
from tabulate import tabulate

student_data = [
    [1 ,15] ,
    [2 , 11] ,
    [3 , 11] ,
    [4 , 20]
]

# Step 3: Create a DataFrame using the 2D list and assign column names
df = pd.DataFrame(student_data , columns=['student id' , 'age'])
print(tabulate(df , headers='keys' , tablefmt='grid'))