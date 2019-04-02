import os #operating system

products = []

if os.path.isfile('products.csv')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price =line.strip().split(',')#去\n,分割
			products.append([name, price])
	print(products)

while True:
	name = input('type product name: ')
	if name == 'q':
		break
	price = input('type price: ')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是：', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
