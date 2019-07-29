# This is my shopping list
shoplist = ["apple", "mango", "carrot", "banana"]

print("I have", len(shoplist), "items to purchase.")

print("These items are:", end=" ")
for item in shoplist:
    print(item, end=" ")

print("\n", shoplist)  # 上面与直接输出的区别

print("\nI also have to buy rice.")
shoplist.append("rice")
print("My shopping list is now", shoplist)

print("I will sort my list now")
shoplist.sort()
print("Sorted shopping list is", shoplist)

print("The first item I will buy is", shoplist[0])
olditem = shoplist[0]
del shoplist[0]  # 删除掉第0个元素
print("I bought the", olditem)
print("My shopping list is now", shoplist)
