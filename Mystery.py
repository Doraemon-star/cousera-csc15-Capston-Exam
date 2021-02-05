'''
Algorithm 1: Mystery.

Input: undirected graph g = (V, E).
Output: Subset V'⊆ V thst satisfies some property.

1 n ← |V|;
2 for i ← 0 to n do
3    foreach subset V'⊆ V of size i do
4         flag ← True;
5         foreach e ∈ E do
6            if e ∩ V' = ∅ then
7                flag ← False;
8         if flag = True then
9            return V';
'''

def b(outcomes, length):
    ans = set([()])
   
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                if len(seq) == 0 or item > seq[-1]:
                    new_seq = list(seq)
                    new_seq.append(item)                    
                    temp.add(tuple(new_seq))                    
                                                        
        ans = temp                
    return ans


def mystery(g):
    n = len(g)
    vertex = g.keys()
    edges = []
    for v1 in vertex:
        for v2 in g[v1]:
            e = (v1,v2)
            edges.append(e)
    #for item in g.items():
        
     #   for value in item[1]:
       #     e = [item[0], value]
      #      edges.append(e)
            
    for i in range(n+1): 
        subsets = b(vertex, i)
        
        for s in subsets:
            flag = True
            for e in edges:
                if e[0] not in s and e[1] not in s:
                    flag = False
            if flag == True:
                return s
            
