LABELS =['word', 'count']
MAX_LEN = 500
LEN_LABELS = 2
ip1 = "count_eng_word.txt"
ip2 = "count_viet_word.txt"
op1 = "engWordList.json"
op2 = "vietWordList.json"


import json
def write_to_json(outputfile, mainlist):
    with open(outputfile, encoding='utf-8', mode='w') as outfile:
        json.dump(mainlist, outfile, ensure_ascii=False)

def txt_json(inputfile, outputfile):
    mainlist = []
    k = 0
    with open(inputfile, encoding='utf-8', mode='r') as f1:
        for line in f1:
            if k == MAX_LEN:
                break
            description = list(line.strip().split())
                
            tempdict = dict()
            for i in range(LEN_LABELS):
                tempdict[LABELS[i]] = description[i]

            mainlist.append(tempdict)
            k += 1

    write_to_json(outputfile, mainlist)

txt_json(ip1, op1)
# txt_json(ip2, op2)