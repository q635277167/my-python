# 这是一个字符串对象
name = "Swaroop"

if name.startswith("Swa"):
    print('Yes, the string starts with "Swa"')

if "a" in name:
    print('Yes, it contains the string "a"')

if name.find("war") != -1:  # 如果找不到相应的子字符串,find会返回 -1
    print('Yes, it contains the string "war"')

delimiter = "_*_"
mylist = ["Brazil", "Russia", "India", "China"]
print(delimiter.join(mylist))
