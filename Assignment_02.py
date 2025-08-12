
# Problem _01
Num1=float(input("Enter your First Number  :"))
Num2=float(input("Enter your Second Number  :"))
Average=(Num1+Num2)/2
print("The Average of Two Numbers is :",Average)


# Problem_O2

def sort_fruit_Name (Fruit_List):
  return sorted (Fruit_List)

Fruits=["apple", "banana", "cherry", "kiwi", "grape"]
sorted_Fruit_list=sort_fruit_Name(Fruits)

print(sorted_Fruit_list)

# Problem_03

# Given list
numbers = [1, 5, 6, 5, 1, 2, 3]

# Find duplicates


duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)
