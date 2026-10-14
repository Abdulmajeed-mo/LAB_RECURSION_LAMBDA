# Part 1: Recursion

def count_vowels(phrase):
    if phrase == "":
        return 0

    vowels = "aeiouAEIOU"

    if phrase[0] in vowels:
        return 1 + count_vowels(phrase[1:])

    return count_vowels(phrase[1:])


print(count_vowels("I love python"))
print(count_vowels("I love Django"))
print(count_vowels("Abdulmajeed"))







print("---"*15)
# Part 2: Lambda and map

numbers = [40, 35, 10, 15, 20]

squared_numbers = list(map(lambda number: number * number, numbers))

print(squared_numbers)
