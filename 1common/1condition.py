import random

        #  if conditions
# isHappy = (random.randint(True, False))
isHappy = True
print(isHappy)
if not isHappy:
    print("I am fine")
else:
    print("Sad")


if 5 == 5:
    print("Yes")
    print("!!!")

isHappy = True
a = 5
if isHappy:  # аналог:if isHappy == True:
    print("User is happy")
elif a == 5:
    print("5 == 5")
else:
    print("User is unhappy")

x = random.randint(0, 1)
print("x=" + str(x))
if x == 0:
    print("x is zero!")
elif x != 0:
    print("x is not zero!")

if not x:
    print("x is None!")
elif x:
    print("x is not None!")

isHappy = False
if not isHappy:
    print("User is happy")  # User is happy

# age = int(input("Enter your age: "))
# if age <= 18:
#     status = "child"
# elif age > 60:
#     status = "pensioner"
# else:
#     status = "adult"
# print(status)

# status = "adult" if age >= 18 else "child"
# print(status)

# message = input()
# if "Hello" in message or "Hi" in message:
#     print("It is greetings, we know")

        # ternar operator
fruit = "apple"
is_apple = "Yes" if fruit == "apple" else "No"
print(is_apple)  # Yes


        # match case condition
my_operation = "read"
match my_operation:
    case "read":
        print("perform read operation…")
    case "update":
        print("perform update operation …")
    case "insert":
        print("perform insert operation …")
    case "delete":
        print("perform delete operation …")
    case _:
        print("wrong variant if operation !!!")

x = 5
match x:
    case 0:
        print("Ноль")
    case 1:
        print("Один")
    case 2:
        print("Два")
    case _:
        print("Неизвестное число")


def describe_value(value):
    match value:
        case int():
            return "Это целое число"
        case float():
            return "Это число с плавающей точкой"
        case str():
            return "Это строка"
        case _:
            return "Это нечто другое"
print(describe_value(42))  # Вывод: Это целое число

#  match-case: status
print("MATCH-CASE")
status = 403
match status:
    case 400:
        print("Bad request")
    case 401 | 403 as error:
        print(f'{error} is authentication error')  # 403 is authentication error
    case 404:
        print("Not found")
    case _:
        print("Other error")



