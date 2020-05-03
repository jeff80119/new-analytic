data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		#if count % 1000 == 0:
		#	print(len(data))
print(len(data))
#   print(data[0:5])

sum_len = 0
for d in data:
	sum_len += len(d)
print(sum_len/len(data))

new = []
good = []
for d in data:
	if len(d) < 100:
		new.append(d)
	if 'good' in d:
		good.append(d)
print('一共有', len(new), '長度小於100')
print(new[0])