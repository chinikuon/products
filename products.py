products = []

while True:
	name = input('type product name: ')
	if name == 'q':
		break
	price = input('type price: ')
	products.append([name, price])


print(products)
