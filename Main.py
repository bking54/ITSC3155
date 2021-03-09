from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    inv = Invoice()
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber('Please enter unit price : ')
    qnt = Invoice().inputNumber('Please enter quantity of product : ')
    discount = Invoice().inputNumber(input_value = 'Discount percent (%) : ')
    repeat = Invoice().inputAnswer(input_value = 'Another product (y,n) : ')
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == 'n':
        break

total_amount = Invoice().totalPurePrice(products)
num_products = Invoice().countTotalProducts(products)

print('Your total pure price is: ', total_amount)
print('Total number of selected products: ', num_products)