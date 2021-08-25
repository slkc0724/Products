products = []
while True:
	name = input('The product u buy: ')
	if name == 'finish':
		break
	price = input('The price of the product: ')
	products.append([name, price])
print(products)	
for p in products:
	print('The price of', p[0], 'is', p[1])