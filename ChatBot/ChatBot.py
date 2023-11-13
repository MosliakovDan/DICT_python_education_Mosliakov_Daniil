print("Hello! My name is ChatBot1")
print("I was created in 2023")
name = input("Please, remind me your name")
print("What a great name you have,", name)
print("Let me guess your age")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "that`s a good time to start programming")
print("Now i will prove to you that i can count to any number you want")
target_number = int(input())
current_number = 0
while current_number <= target_number:
    print(current_number, "!")
    current_number += 1
print("Completed, have a nice day")