def find_change(amount, coins):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while amount >= coin and coin_count[coin] > 0:
            amount -= coin
            change.append(coin)
            coin_count[coin] -= 1
    return change

def update_cash_register(coins_count, received_coins):
    for coin in received_coins:
        if coin in coins_count:
            coins_count[coin] += received_coins.count(coin)

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

coin_count = {
    15: 3,
    10: 2,
    7: 1,
    5: 4,
    1: 5
}

print('Список продуктов:')
for product, price in products.items():
    print(f'{product}: {price}р')

product_choice = input('Выберите продукт из списка выше: ')
if product_choice in products:
    payment = int(input(f'Введите сумму, которую вы даете за {product_choice}: '))
    change_due = payment - products[product_choice]
    coins = list(coin_count.keys())
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
