
    #  list
nums = [6, None, True, 6.7, "Hello", [5, 7, 0]]
print(type(nums))  # <class 'list'>
print(type(nums) is list)  # True
print(isinstance(nums, list))  # True

nums[0] = 50
print(nums[1])  # None
print(nums)  # [50, None, True, 6.7, 'Hello', [5, 7, 0]]
print(nums[-1])  # [5, 7, 0]
print(nums[-1][1])  # 7

numbers = [5, 2, 7]
# numbers[3] = 100  # IndexError:
numbers.append(100)
print(numbers)  # [5, 2, 7, 100]
numbers.insert(1, True)
print(numbers)  # [5, True, 2, 7, 100]
numbers.extend([5, 6, 8])
print(numbers)  # [5, True, 2, 7, 100, 5, 6, 8]
numbers.sort()
print(numbers)  # [True, 2, 5, 5, 6, 7, 8, 100]
numbers.reverse()
print(numbers)  # [100, 8, 7, 6, 5, 5, 2, True]
numbers.pop()  # удалили последний элемент
print(numbers)  # [100, 8, 7, 6, 5, 5, 2]
numbers.remove(100)
print(numbers)  # [8, 7, 6, 5, 5, 2]
numbers.pop(-2)  # удалили по индексу
print(numbers)  # [8, 7, 6, 5, 2]
# numbers.clear()  # удалит все
# print(numbers)  # []
print(numbers.count(6))  # количество совпадений
print(len(numbers))  # кол-во елементов

nums2 = [5, 2, 7, "50", False]
for el in nums2:
    el *= 2
    print(el)
