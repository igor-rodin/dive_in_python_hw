KNAPSACK_CAPACITY = 10

goods = {'item_1': 9, 'item_2': 1, 'item_3': 5,
         'item_4': 3, 'item_5': 10, 'item_6': 7, 'item_7': 2, 'item_8': 15}
goods = dict(filter(lambda item: item[1] <= KNAPSACK_CAPACITY, goods.items()))

knapsack_weight = 0
goods_in_knapsack = []

goods_list = list(goods.items())

# Brute force (полным перебором)

for i in range(1, 2 ** len(goods_list)):
    powerTwo = 1
    can_get = []
    for item, weight in goods_list:
        if powerTwo & i != 0:
            knapsack_weight += weight
            can_get.append((item, weight))
        powerTwo *= 2
    if knapsack_weight <= KNAPSACK_CAPACITY:
        goods_in_knapsack.append(can_get)
    knapsack_weight = 0

for i, val in enumerate(goods_in_knapsack, start=1):
    total_weight = sum(map(lambda item: item[1], val))
    print(f"Вариант {i}: {val} Общий вес: {total_weight}")
