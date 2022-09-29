a_nora = -10  # координата на оси х крота А
b_nora = 5  # координата на оси х крота B
def perebor(cord):
    for i in range(-cord, cord + cord + 1, 1):
        if i == a_nora:
            return True
    return False

def crot(cord):
    if perebor(cord) == False:
        crot(cord + 1)
    else:
        print("крот достиг кротовой норы другого крота")

crot(b_nora)