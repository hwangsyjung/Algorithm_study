def case(array):
    if len(set(array))==1:
        return 50000+array[0]*5000
    elif len(set(array))==2 and array[1]==array[2]:
        return 10000+array[1]*1000
    elif len(set(array))==2 and array[1]!=array[2]:
        return 2000+array[1]*500+array[2]*500
    elif len(set(array))==3:
        return 1000+(array)



lst = []
money = 0
for _ in range(int(input())):
    a = sorted(list(map(int,input().split())))
    lst.append(a)
