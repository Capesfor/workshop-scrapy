
def isnnumber(i):
    try:
        int(i)
        return int(i)
    except ValueError:
        return 0

def check_if_int(i):
    if type(i) == str:
        return isnnumber(i)
    else:
        return 0

def calculate(a):
    if type(a) == list:
        b = sum(check_if_int(i) for i in a)
        return b
    elif type(int(a)) == int:
        return False

def main():
    print(calculate(['4', '3', '-2']))
    print(calculate(453))
    print(calculate(['nothing', 3, '8', 2,'1']))
    print(calculate('54'))


main()
