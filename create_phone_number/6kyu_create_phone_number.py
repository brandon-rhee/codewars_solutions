
n =[0, 2, 3, 0, 5, 6, 0, 8, 9, 0]

def create_phone_number(n):
    nstring = "".join(map(str, n))
    area = nstring[:3]
    area_parenth = "(" + area + ")"
    combined = area_parenth + " " + nstring[3:6] + "-" + nstring[-4:]
    return combined
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))