

numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])

print ('Sum of rows: ', end=' ')
for i in range(rnum):
	rsum = sum(numbers[i])
	print (rsum, end=' ')
print()

print ('Sum of columns: ', end=' ')
for i in range(cnum):
	csum = 0
	for j in range(rnum):	
		csum += numbers[j][i]
	print (csum, end=' ')
print ()


for i in range(rnum):
	rsum = sum(numbers[i])
	if i == 0 or tmax < rsum:
		tmax = rsum
		idx = i
print ('The row that has greatest sum: ', idx)

maxnum = [ max(numbers[i]) for i in range(rnum) ]
print ('The greatest number: ', max(maxnum))
