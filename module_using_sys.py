import sys
import os

print(os.getcwd())  # 查看你的程序目前所处在的目录
print("The command line arguments are:")
for i in sys.argv:
    print(i)

print("\n\nThe PYTHONPATH is", sys.path, "\n")

