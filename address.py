# coding=UTF-8
import pickle


class Address:
    """代表地址簿里的任何成员"""

    def __init__(self, tag, mailbox, tel):
        self.tag = tag
        self.mailbox = mailbox
        self.tel = tel
        print("成功添加一个", end=" ")
        self.output("", tag, " ")
        print("分组的成员")

    def output(self, start, information_type, end="\n"):
        """按照格式输出"""
        for t in information_type:
            print(start, t, end=end)

    def tell(self):
        """告诉我关于我的细节"""
        print("\nTag:", end=" ")
        self.output("", self.tag, " ")
        print("\nMail:")
        self.output("\t", self.mailbox)
        print("\nTel:")
        self.output("\t", self.tel)


# 初始化
ab = {
    "张聪": Address(
        ["本机"], ["q635277167@outlook.com", "qf-cong@163.com"], ["15063743227"]
    )
}


def creation(name):
    """创建新成员"""
    if name in ab:
        print("已经有此人信息，是否查看或更改 S/M")
        c = input(">> ")
        if c == "s":
            print(name, "的详细信息是", end=" ")
            ab[name].tell()
        elif c == "m":
            modify(name)
        else:
            print("输入错误，请重新输入！")
    else:
        print("选择输入他的其他信息")
        mail = set(["空白"])
        tag = set(["空白"])
        tel = set(["空白"])
        message = set()
        while True:
            print("1.邮箱 2.分组 3.电话 4.保存")
            c = input(">> ")
            if c == "1":
                mail.add(input("邮箱 >> "))
                message.add("mail")
            elif c == "2":
                tag.add(input("分组 >> "))
                message.add("tag")
            elif c == "3":
                tel.add(input("电话 >> "))
                message.add("tel")
            elif c == "4":
                if len(message) != 0:
                    break
                else:
                    print("你还没有输入信息")
            else:
                print("输入错误，请重新输入！")
        ab[name] = Address(tag, mail, tel)
        print("(添加了新成员：{})".format(name))


def seek(name):
    """查看成员信息"""
    if name in ab:
        print(name, "的详细信息是", end=" ")
        ab[name].tell()
    else:
        print("没有找到这个人，是否添加？Y/N")
        while True:
            i = input()
            if i == "y":
                creation(name)
            elif i == "n":
                break
            else:
                print("输入错误，请重新输入！")


def modify(name):
    """修改成员信息"""
    print("他的信息是")
    ab[name].tell()
    print("选择进行的操作：")
    print("\t1.添加 2.删除")
    


while True:
    print("选择你要进行的操作：")
    print("\t1.新建 2.查找 3.修改 4.删除 5.退出")
    c = input(">> ")
    if c == "1":
        print("输入他的姓名")
        creation(input(">> "))
    elif c == "2":
        print("输入想要查找的姓名")
        seek(input(">> "))
    elif c == "3":
        print("输入他的姓名")
        modify(input(">> "))
        print("3运行了")
    elif c == "4":
        print("4运行了")
    elif c == "5":
        break
    else:
        print("输入错误，请重新输入")
