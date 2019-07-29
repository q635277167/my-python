import string


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    text = text.lower()
    # 转换 string 中所有大写字符为小写
    text = text.replace(" ", "")
    # replace 把 string 中的 str1 替换成 str2
    for char in string.punctuation:  # string.punctuation 里面保存了所有的标点（只有英文）
        text = text.replace(char, "")
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
