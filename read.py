data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1    # count = count + 1
		if count % 1000 == 0 :
			print(len(data))
print('檔案讀取完畢，共有', len(data), '筆資料')


#求留言平均長度
sum_len = 0
for d in data: 
	sum_len += len(d)    #sum_len = sum_len + Len(D)
print('每筆平均長度是', sum_len/len(data))


#篩選概念
new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new) , '筆留言長度小於100')
