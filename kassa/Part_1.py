def find_change(amount, coins):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change

products = {
    'молоко': 20,
    'хлеб': 15,
    'яйца': 25,
    'масло': 30,
    'сыр': 40,
    'колбаса': 50,
    'вафли': 12,
    'сок': 18,
    'вода': 10,
    'конфеты': 17
}

print('Список продуктов:')
for product, price in products.items():
    print(f'{product}: {price}р')

product_choice = input('Выберите продукт из списка выше: ')
if product_choice in products:
    payment = int(input(f'Введите сумму, которую вы даете за {product_choice}: '))
    change_due = payment - products[product_choice]
    coins = [15, 10, 7, 5, 1]
    change_coins = find_change(change_due, coins)
    print(f'Выбранный продукт: {product_choice}')
    print(f'Цена продукта: {products[product_choice]} р')
    print(f'Полученная сумма: {payment} р')
    print(f'Сдача: {change_due} р')
    print('Монеты для сдачи:')
    for coin in change_coins:
        print(coin, 'р', end=' ')
else:
    print('Такого продукта нет в списке. Пожалуйста, выберите продукт из представленного списка.')
