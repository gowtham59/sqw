ans1=int(input())
word=list(map(str,input().split()[:ans1]))
word.sort()
word.sort(key=len)
for i in word:
    print(i,end=" ")
