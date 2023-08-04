n,m = list(map(int,input().split()))
a_name, b_name = input().split()
mapping = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,
           'P':2,'Q':2,'R':2,'S':1,'T':2,
           'U':1,'V':1,'W':1,'X':2,'Y':2,"Z":1}
name = ''
min_len = min(n,m)
for i in range(min_len):
    name += a_name[i] + b_name[i]
name += a_name[min_len:] + b_name[min_len:]
lst = [mapping[ord(i)] for ]
name_num = []
for i in name:
    name_num.append(mapping[i])
result = []
while True:
    for i in range(1,len(name_num)):
        result[i-1] = name_num[i]+name[i-1]