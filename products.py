products = []
while True:
	name = input('The product u buy: ')
	if name == 'finish':
		break
	price = input('The price of the product: ')
	products.append([name, price])
print(products)	