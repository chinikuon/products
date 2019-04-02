products = []

while True:
	name = input('type product name: ')
	if name == 'q':
		break
	price = input('type price: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是：', p[1])

