a = "кошка, котейка, корабль, корова, котик, комендант"

words_list = a.split(", ")
words_num = 0
for word in words_list:
    if "кот" in word:
        words_num += 1
print(words_num)
