from collections import defaultdict 
def solution(genres, plays):
    answer = []
    g_dic = defaultdict(int)
    p_dic = defaultdict(list)
    for idx, (g,p) in enumerate(zip(genres,plays)):
        p_dic[g].append((idx,p))
        g_dic[g]+=p
    for (k,v) in sorted(g_dic.items(), key = lambda x: x[1], reverse = True):
        for (pk,pv) in sorted(p_dic[k], key = lambda x: x[1], reverse = True)[:2]:
            answer.append(pk)
    return answer