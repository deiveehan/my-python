import pandas

df = pandas.read_csv('04-test-csv.csv')
print(df)

for index, row in df.iterrows():
    print(index)
    print(row['Name'])