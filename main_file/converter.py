import pandas as pd

df = pd.read_csv('scraped_stock_data.csv')
print(df)
writer_to_excel = pd.ExcelWriter('scraped_stock_data.xlsx')
df.to_excel(writer_to_excel,index=False)
writer_to_excel.save()