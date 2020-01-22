operators = []

def constrain(a):
    ix = 0
    for i in range(5):
        for i in range(4):
            if(operators[i] == '>'):
                if a[i] > a[i+1]:
                    return True


def func(a):
    while(a != )