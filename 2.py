# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.
import os

def count_letter(file_name, letter):
    j = 0
    if os.path.isfile(file_name):
        f = open(file_name)
        text = f.read()
        for i in text:
            if i == letter:
                j += 1
        f.close()
        return j
    else:
        return 0

print(count_letter('test.txt', 'a'))
print(count_letter('x.txt', 'a'))
