import pandas as pd

user_list = pd.read_excel('sample.xlsx',  engine='openpyxl')
print(user_list)
