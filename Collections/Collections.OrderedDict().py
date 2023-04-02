from collections import OrderedDict
n = int(input())
ordered_dictionary = OrderedDict()
for i in range(n):
    item_name, net_price = input().rsplit(" ", 1)
    ordered_dictionary[item_name] = ordered_dictionary.get(item_name,0) + int(net_price)
for key, value in ordered_dictionary.items():
    print(key, value)
