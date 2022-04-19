def count_to_100():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        if i % 5 == 0:
            print("Five")
        elif i % 3 == 0:
            print("Three")
        else:
            print(i)

count_to_100()