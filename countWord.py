stw = ['*','+', '!', '.', '"', ',', '?', "'", "/", "\ufeff*", "’", '-', '(', ')', ':', ';']
count_eng_dict = dict()
count_viet_dict = dict()
i = 0
with open("./data/wseg.txt", encoding='utf-8', mode='r') as fread:
    with open("./data/cword.txt", encoding='utf-8', mode='w') as fwrite:
        while True:
            # if i == 10:
            #     break
            eng_line = fread.readline()
            if eng_line == '':
                break
            for word in eng_line.split():
                if word not in stw:
                    if word.lower() in count_eng_dict:
                        count_eng_dict[word.lower()] += 1
                    else:
                        count_eng_dict[word.lower()] = 1
            viet_line = fread.readline()
            for word in viet_line.split():
                if word not in stw:
                    if word.lower() in count_viet_dict:
                        count_viet_dict[word.lower()] += 1
                    else:
                        count_viet_dict[word.lower()] = 1
            fread.readline()
            fwrite.write("\n\n")
            # i += 1

sorted_count_end_dict = dict(sorted(count_eng_dict.items(), key=lambda item: item[1],reverse=True))
sorted_count_viet_dict = dict(sorted(count_viet_dict.items(), key=lambda item: item[1],reverse=True))

with open("count_eng_word.txt", encoding='utf-8', mode='w') as f:
    for w, c in sorted_count_end_dict.items():
        f.write(w + " " + str(c))
        f.write("\n")

with open("count_viet_word.txt",  encoding='utf-8', mode='w') as f:
    for w, c in sorted_count_viet_dict.items():
        f.write(w + " " + str(c))
        f.write("\n")