from quick_merge import quick_merge

"""[summary]
temp = []
for i in range(int(input())):
    temp.append([int(i) for i in input().split()])
"""

n = int(input())
st = [] #пустой
temp = [] #заполненный
for i in range(n):
    temp.append([int(i) for i in input().split()])
    st = quick_merge(st, temp[i])
    st.sort()
print(*st)