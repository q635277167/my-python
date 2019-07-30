# coding=UTF-8
import pickle


class Address:
    """代表地址簿里的任何成员"""

    def __init__(self, tag=set(["空白"]), mail=set(["空白"]), tel=set(["空白"])):
        self.tag = tag
        self.mail = mail
        self.tel = tel
        self.message = True

    def check(self):
        """检查联系人信息是否全部空白"""
        if len(self.tag) == 0:
            self.tag.add("空白")
        if len(self.mail) == 0:
            self.mail.add("空白")
        if len(self.tel) == 0:
            self.tel.add("空白")
        if ("空白" in self.mail) & ("空白" in self.tag) & ("空白" in self.tel):
            self.message = False
            print("此联系人信息为空，是否删除？Y/N")
            while True:
                i = input(">> ")
                if i == "y":
                    print("代码重构中，暂时不能运行")  # 需要更改
                    break
                elif i == "n":
                    print("重新输入联系人信息")
                    self.add()
                    break
                else:
                    print("输入错误，请重新输入！")
        else:
            self.message = True

    def add(self):
        """添加信息"""
        while True:
            print("1.邮箱 2.分组 3.电话 4.保存")
            c = input(">> ")
            if c == "1":
                if "空白" in self.mail:
                    self.mail.remove("空白")
                self.mail.add(input("邮箱 >> "))
                self.message = True
            elif c == "2":
                if "空白" in self.tag:
                    self.tag.remove("空白")
                self.tag.add(input("分组 >> "))
                self.message = True
            elif c == "3":
                if "空白" in self.tel:
                    self.tel.remove("空白")
                self.tel.add(input("电话 >> "))
                self.message = True
            elif c == "4":
                self.check()
                if self.message:
                    break
            else:
                print("输入错误，请重新输入！")

    def delete(self):
        """删除信息"""
        mail = list(self.mail)
        tag = list(self.tag)
        tel = list(self.tel)
        while True:
            print("选择想要删除的项目：")
            print("1.邮箱 2.分组 3.电话 4.保存")
            c = input(">> ")
            if c == "1":
                print("选择要删除项目的序号：")
                p = int(input(">> "))
                del mail[p - 1]
            elif c == "2":
                print("选择要删除项目的序号：")
                p = int(input(">> "))
                del tag[p - 1]
            elif c == "3":
                print("选择要删除项目的序号：")
                p = int(input(">> "))
                del tel[p - 1]
            elif c == "4":
                break
            else:
                print("输入错误，请重新输入！")
        self.mail = set(mail)
        self.tag = set(tag)
        self.tel = set(tel)
        self.check()

    def output(self, start, information_type, end="\n"):
        """按照格式输出"""
        for t in information_type:
            print(start, t, end=end)

    def tell(self):
        """告诉我关于我的细节"""
        print("\nTag:", end=" ")
        self.output("", self.tag, " ")
        print("\nMail:")
        self.output("\t", self.mail)
        print("Tel:")
        self.output("\t", self.tel)


# 初始化添加
ab = {
    "张聪": Address(
        ["本机"], ["635277167@qq.com", "q635277167@outlook.com"], ["15063743227"]
    )
}


def creation_tips(name):
    """创建新成员"""
    if name in ab:
        print("已经有此人信息，是否查看或更改 S/M")
        while True:
            i = input(">> ")
            if i == "s":
                print(name, "的详细信息是", end=" ")
                ab[name].tell()
                break
            elif i == "m":
                modify(name)
                break
            else:
                print("输入错误，请重新输入！")
    else:
        ab[name] = Address()
        print("选择输入联系人的其他信息")
        ab[name].add()
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
                creation_tips(name)
                break
            elif i == "n":
                break
            else:
                print("输入错误，请重新输入！")


def modify(name):
    """修改成员信息"""
    seek(name)
    print("选择进行的操作：")
    print("\t1.添加 2.删除")
    while True:
        c = input(">> ")
        if c == "1":
            print("选择要添加的信息")
            ab[name].add()
            break
        elif c == "2":
            ab[name].delete()
            break
        else:
            print("输入错误，请重新输入")


def remove(name):
    while True:
        print("确认要删除联系人 {} 吗？Y/N".format(name))
        i = input(">>")
        if i == "y":
            del ab[name]
        elif i == "n":
            break
        else:
            print("输入错误，请重新输入")


while True:
    print("选择你要进行的操作：")
    print("\t1.新建 2.查找 3.修改 4.删除 5.退出")
    c = input(">> ")
    if c == "1":
        print("输入联系人的姓名")
        creation_tips(input(">> "))
        print("保存成功")
    elif c == "2":
        print("输入想要查找的联系人姓名")
        seek(input(">> "))
    elif c == "3":
        print("输入将要修改的联系人姓名")
        modify(input(">> "))
        print("保存成功")
    elif c == "4":
        print("输入将要删除的联系人姓名")
        remove(input(">> "))
        print("保存成功")
    elif c == "5":
        break
    else:
        print("输入错误，请重新输入")
