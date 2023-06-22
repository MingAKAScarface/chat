#Thanks for Bonnie, Butter, and Labi
data = []
filename = 'input.txt'
filename_o = 'output.txt'
tx2 = []
#讀檔案
def readfile(filemname): 
	with open(filemname, 'r', encoding='utf-8') as f:
		for line in f:
			data.append(line.strip()) 
			#strip()這功能只能apply to string喔!!! 用在索引data後面他不會理你
	return data

#處理分行
def process(data):
	for d in data:			
		if d == 'Dragon':
			tx1 = []
			tx1.append(d + ':')
			#print(tx1)
		elif d == "Mike":
			tx1 = []
			tx1.append(d + ':')
			#print(tx1)
		#print(tx1)	 #檢查有沒有丟到tx1! 有
		else: 
			tx2.append(tx1[0] + ' ' + d + '\n') 
	return tx2

#寫入檔案
def write_file(filename_o,tx2):
	with open(filename_o, 'w', encoding='utf-8') as f: #, encoding='utf-8'這樣才能有中文
		for d in tx2:
			f.write(d)

readfile(filename)
process(data)
write_file(filename_o, tx2)

