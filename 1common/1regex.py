
import re
# regex: re.match/search/findall(r'it',str) => re.compile('IT').findall(str) => re.split('e',str) => re.sub('e','E',str) => re.findall("^Hel.0$",str)

res1 = re.match(r'IT', "IT academy softserve")
print(res1)  # <re.Match object; span=(0, 2), match='IT'>
print(res1.group(0))  # IT
res2 = re.match(r'academy', "IT academy softserve")
print(res2)  # None
res3 = re.search(r'academy', "IT academy softserve")
print(res3)  # <re.Match object; span=(3, 10), match='academy'>
print(res3.group(0))  # academy
res4 = re.findall(r'IT', "IT academy softserve IT IT")
print(res4)  # ['IT', 'IT', 'IT']

pattern = re.compile('IT')
res5 = pattern.findall("IT academy softserve IT IT")
print("-----------")
print(re.compile('IT').findall("IT academy softserve IT IT"))
print(res5)  # ['IT', 'IT', 'IT']

res5 = re.split(r'e', 'IT academy softserve IT')
print(res5)  # ['IT acad', 'my softs', 'rv', ' IT']

res6 = re.sub('e', '9', 'IT academy softserve IT')
print(res6)  # 'IT academy softserve IT'

str1 = "IT academy softserve"
res7 = re.findall("[a-m]", str1)  # ['a', 'c', 'a', 'd', 'e', 'm', 'f', 'e', 'e']
print(res7)
str2 = "Softserve celebrates 27 years"
res8 = re.findall('\d', str2)
print(res8)  # ['2', '7']

str3 = "Hello Softserve IT academy"
res9 = re.findall("So......e", str3)
print(res9)  # ['Softserve']
res10 = re.findall("^Hello", str3)
print(res10)  # ['Hello']
res11 = re.findall("academy$", str3)
print(res11)  # ['academy']




