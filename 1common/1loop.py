        #  for cycles
for i in range(5):
    print(i)  # 0  1  2  3  4

for i in range(1, 5):
    print(i)  # 1  2  3  4

for i in range(1, 6, 2):
    print(i)  # 1  3  5

for i in range(1, 11):
    if i == 5:
        break
    print(i)  # 1  2  3  4

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)  # 1  3  5  7  9

word = "asana"
for i in word:
    print(i, end=" ")

counter = 0
for i in word:
    if i == "a":
        counter +=1
print("\nCounter:" + str(counter))

found = None
for k in word:
    if k == "h":
        found = True
        break
    else:
        found = False
print(f"{k} is in word: {found}")


        # while
x = 1
while x < 5:
    print(x)
    x += 1

i = 5
while i < 15:
    print(i)  # 5  8  11  14
    i += 3

y = 0
sum = 0
while y <= 10:
    y += 1
    if y % 2 == 1:
        continue
    sum += y
    print(sum)
print("Sum: ", sum)

# isHasCar = True
# while isHasCar:
#     if input("Enter data: ") == "Stop":
#         isHasCar = False


# x = int(input("Please input 0 to stop iteration: "))
# sum_result = 0
# while x:
#     sum_result += x
#     x = int(input("Please input 0 to stop iteration: "))
# print(sum_result)

# n = int(input("Input integer number: "))
# sum_result = 0
# x = 1
# while x < n:
#     x += 1
#     if x % 2:
#         continue
#     sum_result += x
# print(f"Sum of even numbers: {sum_result}")

# x = int(input("Imput integer number: "))
# is_prime = True
# div = 2
# while div < x:
#     if not x % div:
#         is_prime = False
#         break
#     div += 1
# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")

