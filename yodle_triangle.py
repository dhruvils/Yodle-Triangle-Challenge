#! python
# yodle triangle challenge
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='Yodle triangle challenge')
parser.add_argument('-i', '--input', default='triangle.txt', help='input file (default triangle.txt)')
opts = parser.parse_args()

triangle = []
for line in open(opts.input):
	triangle.append([int(x) for x in line.split()])

# total = 0
# j = 0
# for row in triangle:
# 	if j + 1 < len(row):
# 		if row[j] > row[j + 1]:
# 			total += row[j]
# 		else:
# 			total += row[j + 1]
# 			j = j + 1
# 	else:
# 		total += row[j]
total = defaultdict(int)
i = len(triangle) - 1
while i >= 0:
	j = 0
	while j < len(triangle[i]):
		if i + 1 < len(triangle):
			total[(i, j)] = max(triangle[i][j] + total[(i + 1, j)], triangle[i][j] + total[(i + 1, j + 1)])
		else:
			total[(i, j)] = triangle[i][j]
		j += 1
	i -= 1

print("%s " %(total[(0, 0)]))