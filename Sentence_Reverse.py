
name = 'Matru Ki Bijli Ka Man Dola'
current_word = ""
new_list = []
for i in name:
    if i == ' ':
        new_list.append(current_word)
        current_word = ""
    else:
        current_word += i
new_list.append(current_word)
new_list = new_list[::-1]
new_string = " ".join(new_list)
str1 = ""
for i in new_list:
    str1 = str1 + ' ' + i

print(str1)

