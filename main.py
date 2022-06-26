import MeCab
import random

t = MeCab.Tagger("-Owakati")
model = {}
model[0] = {}
with open("./sample.txt") as f:
    for line in f:
        words = t.parse(line).split()
        if len(words) == 0:
            continue
        words.append(1)
        pre_word = 0
        for word in words:
            if word in model[pre_word]:
                model[pre_word][word] += 1
            else:
                model[pre_word][word] = 1
            pre_word = word
            if pre_word not in model:
                model[pre_word] = {}
pre_word = 0
loop = 1000
random.seed()
for i in range(loop):
    current_dic = model[pre_word]
    rand_max = sum(current_dic.values())
    if rand_max == 0:
        pre_word = 0
        continue
    next_index = random.randrange(0, rand_max)
    count = 0
    for key, val in current_dic.items():
        next_index -= val
        if next_index < 0:
            pre_word = list(current_dic.keys())[count]
            break
        count += 1
    if pre_word == 1:
        break
    else:
        print(pre_word, end="")
print("")
    
