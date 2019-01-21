
import re


n = int(input("enter the number of words in your input"))
print('Now enter ',n,'words in each new line')
words = [input() for i in range(n)]
print('following are the words having two adjacent vowels :')
for l in words:
    t = re.findall('.*[aeiou]{2}.*',l)
    if t:
        print(t)