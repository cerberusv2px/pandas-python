import pandas as pd

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(data[['a', 'b']])

dates = pd.date_range('2019-02-01', '2019-02-06')

temps1 = pd.Series([80, 82, 85, 90, 83, 87], index=dates)
temps2 = pd.Series([70, 75, 69, 83, 79, 77], index=dates)

# print(temps1.mean())
temp_diffs = temps1 - temps2
# print(temp_diffs)

temp_df = pd.DataFrame({
    'Ktm': temps1,
    'Pkh': temps2
})

# print(temp_df)
# print(temp_df[['Ktm', 'Pkh']])
# print(temp_df.Ktm)
# print(temp_df.Ktm - temp_df.Pkh)

temp_df['Difference'] = temp_diffs
print(temp_df)
print('-----------------------------------------------')
# slice the temp differences column for the rows at location 1 through 4

# print(temp_df.Difference[1:4])

# get row at array pos1.
# iloc
# iloc retrieves data object by zero-based position of the row.
# It converts the row into series with column names of DataFrame pivoted into index labels

# print(temp_df.iloc[1])

# loc
# retrieves data object by index label

# print(temp_df.loc['2019-02-03'])

# print(temp_df.Ktm > 82)
print(temp_df[temp_df.Ktm > 82])
