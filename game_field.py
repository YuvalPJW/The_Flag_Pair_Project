import random



def create_field():
 (rows, cols) = (25, 50)
 arr = [[0]*cols]*rows

 for row in arr:
    print(row)


def give_random_mines(field):
    for i in range(field):
        for j in range(3):
            if [i]!=0:
                i=random.randint(0, 1)
    print(field)





