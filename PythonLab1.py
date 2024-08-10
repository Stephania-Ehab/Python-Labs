# Question (1)

billAmount = 47.28
billTips = billAmount * 0.15
billTotal = billAmount + billTips
friendShare = billAmount / 2

print(f"Each person needs to pay: ${friendShare:}")


# Question (2)

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

if num2 != 0:
    result = num1 / num2
    print(f"The result is: {result}")
else:
    print("Cannot divide by zero.")


# Question (3)

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "{}"
word6 = "so"
word7 = "far ?"

sentence = f"{word1} {word2} {word3} {word4} {word5} {word6} {word7}"
print(sentence)


# Question (4)

word7 = word7.replace('?', '!')
sentence = f"{word1} {word2} {word3} {word4} {word5} {word6} {word7}"

word5 = word5.format("python")

sentence = f"{word1} {word2} {word3} {word4} {word5} {word6} {word7}"
print(sentence)


# Question (5)

sentence = input("Please enter your sentence : ")
length = len(sentence)

print(f"Length of sentence is: {length} characters")


# Question (6)

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
operator = input("Please enter an oprator (+,-,*,/) : ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero."
else:
        result = "Invalid operator."
        

print(f"The result is: {result}")

