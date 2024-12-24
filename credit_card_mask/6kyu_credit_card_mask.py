

def maskify(cc):
    last = cc[-4:]
    exes = "#" * len(cc[:-4])
    final = exes + last
    return final
print(maskify('Skippy'))
