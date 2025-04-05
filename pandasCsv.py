import pandas as pd

# df = pd.read_csv('testFiles/data.csv')
#
# # # Вывод первых 5 строк данных
# # print(df.head())
# #
# # # Выбор одного столбца
# # names = df['name']
# # print(names)
#
# # # Выбор нескольких столбцов
# # selected_columns = df[['name', 'age', 'height']]
# # print(selected_columns)
#
# # Фильтрация данных
# filtered_data = df[df['age'] > 30]
# print(filtered_data)

            # очистка данных

df = pd.read_csv('testFiles/data2.csv')
print(df['Duration'])  # выведет столбец (серию)
print(df.Duration)  # тоже самое
print(df['Duration'].unique())  # все уникальные значения столбца
print(df.to_string())  # напечатает все
new_df = df.dropna()  # удалить строки, содержащие пустые ячейки
df.dropna(inplace = True)  # удалить строки, содержащие пустые ячейки, меняя исходный документ
df.fillna(130, inplace=True)  # заменить пустую ячейку значением
# df['Calories'].fillna(130, inplace=True)  # заменить пустую ячейку значением в столбце
# x = df["Calories"].mean()  # заменить пустую средним значением
# df["Calories"].fillna(x, inplace=True)
# x = df["DCalories"].median()  # заменить пустую средним значением
# df["Calories"].fillna(x, inplace=True)
# x = df["Calories"].mode()[0]  # заменит пустые на самое частое значение
# df["Calories"].fillna(x, inplace=True)
# df['Date'] = pd.to_datetime(df['Date']) # преобразовать в дату
# df.dropna(subset=['Date'], inplace=True)  # Удалите строки со значением NULL в столбце «Дата»
df.loc[7, 'Duration'] = 45  # заменить значение
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120  # заменить группу перебором по правилу
    df.drop(x, inplace=True)  # удалить группу перебором по правилу
df.drop_duplicates(inplace = True)  # удалит дубликаты
print(df.duplicated())  # перечень дубликатов

print(df.to_string())
