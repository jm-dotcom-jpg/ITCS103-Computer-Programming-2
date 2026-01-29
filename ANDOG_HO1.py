num_list = []

word = input("Enter a word:")
counter = 1

for i in word:
    number = eval(input(f"Enter a number {counter}:"))
    num_list.append(number)
    counter += 1
    
    total = sum(num_list)
    count = len(num_list)
    average = total / count

print(num_list)
print("The length of word has",len(word),"characters")
print(f"The average of the numbers is {average}")

if count < average:
    print(f"The length of the word {word} is less than the average.")

elif count > average:
    print(f"The length of the word {word} is greater than the average.")

else:
    print(f"The length of the word {word} is equals the average. ")

