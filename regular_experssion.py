import re

s = input("Enter string consisting of numbers, characters and whitespaces")

print('string starting and ending with a digit',re.findall("^\d.*\d$",s))


print('string only with whitespaces and characters',re.findall("[a-zA-Z]+|\s",s))


print('string containing no white spaces',re.findall(r"\S+",s))