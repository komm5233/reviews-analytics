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
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new) , '筆留言長度小於100')
print(new[0])


#有GOOD的字篩選出來
good = []
for d in data:
	if 'good' in d:    #'a' in 'abc' -> True
		good.append(d)
print('一共有',len(good), '筆留言提到GOOD')
print(good[0])


# 文字計數
wc = {} # word_count
for d in data:	
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的KEY進WC字典 


for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])


print(wc['Matt'])


while True:
	word = input('請輸入你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word , '出現的次數為:', wc[word])
	else:
		print('沒出現過這字喔!')

print('感謝使用本次查詢功能')




