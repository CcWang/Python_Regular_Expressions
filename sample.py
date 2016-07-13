import re
sample = open('regex_sum_42.txt')
for line in sample:
    line = line.restrip()
    print line
