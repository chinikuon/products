import os #operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue
				name, price =line.strip().split(',')#去\n,分割
				products.append([name, price])
	return products				
def user_input(products):
	while True:
		name = input('type product name: ')
		if name == 'q':
			break
		price = input('type price: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products
def print_products(products):
	for p in products:
		print(p[0], '的價格是：', p[1])
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#('products.csv')
		products = read_file(filename)
		print(products)

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
main()