products = []
while True:
	name = input('The product u buy: ')
	if name == 'finish':
		break
	price = input('The price of the product: ')
	price = float(price)
	products.append([name, price])
print(products)	
for p in products:
	print('The price of', p[0], 'is', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
