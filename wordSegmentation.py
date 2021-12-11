from underthesea import word_tokenize

with open("./data/evc.txt", encoding='utf-8', mode='r') as fread:
    with open("./data/wseg.txt", encoding='utf-8', mode='w') as fwrite:
        while True:
            eng_line = fread.readline()
            fwrite.write(eng_line)
            if eng_line == '':
                break
            viet_line = fread.readline()
            fwrite.write(word_tokenize(viet_line, format="text"))
            fread.readline()
            fwrite.write("\n\n")