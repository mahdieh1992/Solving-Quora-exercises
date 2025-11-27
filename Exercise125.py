# Greedy Algoritm
class Cake:
    def max_count_cake(self,price: list[int],money: int) -> dict:
        cake_buy = {}
        ln = len(price)
        # order by prices with selection sort algoritm
        for i in range(ln):
            min = i 
            for j in range(i + 1,ln):
                if price[min] > price[j]:
                    min = j
            price[i], price[min] = price[min], price[i]
        # find more count cake with greedy Algoritm
        for i in range(ln):
            if money >= price[i]:
                money = money - price[i]
                cake_buy[price[i]] = cake_buy.get(price[i],0) + 1
            else:
                break
        cake_buy['money'] = money
        return cake_buy        
