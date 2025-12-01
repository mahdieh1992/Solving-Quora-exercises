# greedy algoritm
# buying max cake with weight
price = [18,23,53,38,13,40,25]
weight = [2,1,4,3,2,4,3]
ln = len(price)
pw = [price[i] / weight[i] for i in range(ln)]
money = 95
total_w = 0
for i in range(ln):
    min = i 
    for j in range(i + 1,ln):
        if pw[j] < pw[min]:
            min = j
    pw[i],pw[min] = pw[min],pw[i]
    price[i],price[min] = price[min] ,price[i]
    weight[i],weight[min] = weight[min] ,weight[i]
    
for i in range(ln):
    if price[i] < money:
        money -= price[i]
        total_w += weight[i]
    else:
        if money > 0:
            total_w = total_w + money / price[i] * weight[i]
            money = 0
        break

print(money,total_w)
