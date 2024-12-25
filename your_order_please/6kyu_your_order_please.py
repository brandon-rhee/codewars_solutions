def order(sentence):
    import re
    if sentence == "":
        res = ""
        return res
    a = sentence.split(' ')
    b = re.findall(r'\d+', sentence)
    b_int = [int(x) for x in b]
    parsed = list(zip(b_int,a))
    sorted_list = sorted(parsed, key=lambda x:x[0])
    final_list = []
    for i in range(len(sorted_list)):
        final_list.append(sorted_list[i][1])
        res=" ".join(final_list)
    return res

print(order(""))