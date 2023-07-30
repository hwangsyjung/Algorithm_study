# https://www.acmicpc.net/problem/1302
N = int(input())
books ={}
for _ in range(N):
    book_name = input()
    if book_name in books.keys():
        books[book_name]+=1
    else:
        books[book_name]=1
target = max(books.values())
array = []

for book, number in books.items():
    if number == target:
        array.append(book)
print(sorted(array)[0])