N,M = map(int,input().split(' '))
team_mem, mem_team = {}, {}
for _ in range(N):
    team_name = input()
    number = int(input())
    member_name = []
    for _ in range(number):
        member = input()
        member_name.append(member)
        mem_team[member] = team_name
    team_mem[team_name] = member_name
for _ in range(M):
    quiz = input()
    number = int(input())
    if number == 1:
