data = []
count = 0                               #計數功能
with open('reviews.txt', 'r') as f:     #讀取檔案的coding
	for line in f:
		data.append(line)
		count += 1                      #count = count + 1
		if count % 1000 == 0:           #如果count的1000筆餘數是0，才印出來,意思就是1000筆印一次
			print(len(data))            #印出清單裡面的筆數
print('檔案讀取完了，總共有', len(data), '筆資料')

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')








#算留言的平均長度↓
sum_len = 0  
for d in data:                    #data丟到變數d裡面(每一個d是一個字串)
	sum_len += len(d)             #每一個留言算出長度後(len(d))加回去sun_len(總共留言加總長度)
print('留言的平均長度為',sum_len/len(data))  #sun_len總長度/len(data)總共留言筆數1000000筆

#留言篩選(小於100字的)
new = []                          #建立一個空白清單
for d in data:                    #for loop(把清單中的東西一個一個拿出來)
	if len(d) < 100:              #清單篩選功能
		new.append(d)             #把d <100留言長度的data append到new清單裡
print('一共有', len(new), '筆留言長度小於100')
print(new[0])                     #印出第一筆的留言


#留言篩選(有good的留言)
good = []
for g in data:
	if 'good' in g:
		good.append(g)
print('一共有', len(g), '筆留言提到good')