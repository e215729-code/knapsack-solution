n = 18
capacity = 45
size  = [ 4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
price = [ 6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]

max_size = 0
max_price = 0
combi= []

for e in range(1 << n):

    total_size = 0
    total_price = 0
    total_combi = []

    for i in range(n):
        if e & (1 << i):
            total_size += size[i]
            total_price += price[i]
            total_combi.append(i + 1)   

    if total_size <= capacity:
        if total_price > max_price:
            max_price = total_price
            max_size = total_size
            combi = total_combi


print("選択した品物:", combi)
print("容量:", max_size)
print("合計価格:", max_price)