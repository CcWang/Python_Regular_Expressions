import re
text = open('regex_sum_295590.txt')
output = 0
for line in text:
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    if num:
        for value in num:
            output += int(value)
print output
