#  pip install pandas

import pandas as pd

dataframe = pd.read_excel('testFiles/data1.xlsx', sheet_name='Лист1')
print(dataframe.head())
print(dataframe.info())  # Общая информация о данных
print(dataframe.describe())  # Статистическое резюме данных
print(dataframe['A'])  # Выбор одного столбца
print(dataframe[['B', 'C']])  # Выбор нескольких столбцов
print("Фильтрация данных")
print(dataframe[dataframe['Age'] > 30])  # Фильтрация данных


# Serie
print("Serie!!!!!!!!!!!!!!!Serie!!!!!!!!!!!!!!!!!!!")
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)  #  0 1   1 7   2 2   dtype: int64
print(myvar[0])  # 1

# назначить свои метки (индексы)
a = [1, 7, 2]
myvar2 = pd.Series(a, index=["x", "y", "z"])
print(myvar2)  # x 1   y 7   z 2   dtype: int64
print(myvar2["y"])  # 7

# словарь как серия
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar3 = pd.Series(calories)
print(myvar3)  # day1 420   day2 380   day3 390   dtype: int64

# DataFrame из двух серий
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)  # load data into a DataFrame object
print(df)  # calories duration    0 420 0    1 380 40    2 390 45
print(df.loc[0])  # локальный ряд: calories 420    duration 50    Name: 0, dtype: int64
print(df.loc[[0]])  # calories  duration    0 420 50
print(df.loc[[0, 1]])  # calories duration    0 420 50    1 380 40


# назначить свои метки (индексы)
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)  # calories duration    day1 420 50    day2 380 40    day3 390 45
print(df.loc["day2"])  # calories 380    duration 40    Name: day2, dtype: int64
print(df.iloc[1])  # calories 380    duration 40    Name: day2, dtype: int64
print(df.loc[["day2"]])  # calories duration    day2 380 40
print(df.iloc[[1]])  # calories duration    day2 380 40
print(df.loc[["day1", "day2"]])  # calories duration    day1 420 50    day2 380 40
print(df.loc[["day2"], ["duration"]])  # duration    day2 40
print(df.iloc[[1], [1]])  # duration    day2 40
print(df.iloc[1, 1])  # 40
print(df.loc["day2", "duration"])  # 40


print("+++++++++++++++++++++++++")
# from CSV into a DataFrame
df = pd.read_csv('testFiles/data.csv')
print(df)  # напечатает по 5 первых и последних рядков
print(df.to_string())  # напечатает всю таблицу
print(pd.options.display.max_rows)   # 60
pd.options.display.max_rows = 9999  # увеличить макс возможное кол-во отображаемых строк (по дефолту=60)

# from JSON into DataFrame
df2 = pd.read_json('testFiles/data3.json')
print(df2.to_string())  # весь документ
print(df2)  # первые и последние 5 рядков
print(df2.head(2))  # верхние 2 рядка
print(df2.head())  # первые 5 рядков
print(df2.tail())  # последние 5 рядков
print(df2.tail(2))  # последние 2 рядка
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# dict to dataframe
dic = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  }
}
df3 = pd.DataFrame(dic)
print(df3)


