KNAPSACK_CAPACITY = 13

goods = {'item_1': 9, 'item_2': 1, 'item_3': 5,
         'item_4': 3, 'item_5': 10, 'item_6': 7, 'item_7': 2, 'item_8': 15}
goods = filter(lambda item: item[1] <= KNAPSACK_CAPACITY, goods.items())
goods = dict(sorted(goods, key=lambda item: item[1]))

knapsack_weight = 0
goods_in_knapsack = []

goods_list = list(goods.items())
for i in range(len(goods)):
    can_take = []
    for (item, weight) in goods_list[i:]:
        if knapsack_weight + weight <= KNAPSACK_CAPACITY:
            knapsack_weight += weight
            can_take.append((item, weight))
    goods_in_knapsack.append(can_take)
    knapsack_weight = 0

for i, val in enumerate(goods_in_knapsack, start=1):
    total_weight = sum(map(lambda item: item[1], val))
    print(f"Вариант {i}: {val} Общий вес: {total_weight}")
