# 它总会在代码块开始之前调用 thefile.__enter__ 函数
# 并且总会在代码块执行完毕之后调用 thefile.__exit__
with open("poem.txt") as f:
    for line in f:
        print(line, end="")

