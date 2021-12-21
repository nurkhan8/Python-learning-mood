
quantity = int(input('quantity'))

if quantity > 1000:
    print('cost', ((quantity * 100) - (.1 * quantity * 100)))
else:
    print('cost', (quantity * 100))