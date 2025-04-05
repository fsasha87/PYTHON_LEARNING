# exception
# x = int(input("Введите число: "))
# x += 5
# print(x)  # ValueError (если не число)

# x = 0
# while x == 0:
#     try:
#         x = int(input("Введите число: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print("Введите лучше число")
#
#
# try:
#     x = int(input())
#     x = 5 / x
# except ZeroDivisionError:
#     print("Деление на ноль")
# except ValueError:
#     print("Вы ввели что-то не так")
# else:
#     print("try is done")
# finally:
#     print("Finally")
#
#         # Raising Exception
# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:
#         raise ValueError("That is not a positive number!")
# except ValueError as ve:
#     print(ve)


a = [5, 6, 7, 8]
try:
    print("Second element = {}".format(a[1]))
    # Throws error since there are only 4 elements in array
    print("Fifth element = {}".format(a[4]))
except IndexError as e:
    print(e)

try:
    a = int(input("Enter your number: "))
    if a < 4:
        b = a / (a - 3)  # throws ZeroDivisionError for a = 3
    if a >= 4:
        print("Value of b = ", b)  # throws NameError
# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError, ValueError):
    print("Error Occurred and Handled")

# Program to handle multiple errors with one except statement
try:
    a = int(input("Enter your number: "))
    if a < 4:
        b = a / (a - 3)  # throws ZeroDivisionError for a = 3
    if a >= 4:
        print("Value of b = ", b)  # throws NameError
# note that braces () are necessary here for multiple exceptions
except ValueError:
    print("Value Error!")
except NameError:
    print("NameError!")
except ZeroDivisionError:
    print("ZeroDivisionError!")
except:
    print("Error!")


try:
    f = open("newfile.txt")
    f.write("Second element: ")
except:
    print("Something went wrong when writing to the file")
else:
    print("Nothing went wrong")
finally:
    # f.close()
    print("The 'try except' is finished")


# class_CustomError(Exception):init(data)=>try:n=int(input(""))=>if n<0:raise CustomError("")=> except_CE_as_e:print(e)
class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    number = int(input("Enter number"))
    if number < 0:
        raise CustomError("Negative value")
except CustomError as e:
    print(e.data)
    print(e)