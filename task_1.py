values = [1, 2, 3, 3, 2, 1, 3, 8, 9, 6, 8]

res = {val for val in values if values.count(val) > 1}

print(res)
