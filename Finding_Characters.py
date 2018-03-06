word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
new_list = []
char = 'n'
for idx in range(0, len(word_list)):
    for iii in word_list[idx]:
        if iii == char:
            new_list.append(word_list[idx])
            break
print word_list
print new_list