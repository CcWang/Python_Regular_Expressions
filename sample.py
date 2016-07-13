import re
sample = open('regex_sum_42.txt')
num_sum=0
for line in sample:
    line = line.rstrip()
    num =re.findall('[0-9]+',line)
    if num:
        for value in num:
            num_sum = num_sum+int(value)
print num_sum
