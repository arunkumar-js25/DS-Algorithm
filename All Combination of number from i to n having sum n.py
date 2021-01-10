def recur(i,n,out,index):
    if n == 0:
        print(out[:index])

    for j in range(i,n+1):
        out[index] = j
        recur(j,n-j,out,index+1)

n = 10
out = [None]*n
recur(1,n,out,0)

output:
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 2]
[1, 1, 1, 1, 1, 1, 1, 3]
[1, 1, 1, 1, 1, 1, 2, 2]
[1, 1, 1, 1, 1, 1, 4]
[1, 1, 1, 1, 1, 2, 3]
[1, 1, 1, 1, 1, 5]
[1, 1, 1, 1, 2, 2, 2]
[1, 1, 1, 1, 2, 4]
[1, 1, 1, 1, 3, 3]
[1, 1, 1, 1, 6]
[1, 1, 1, 2, 2, 3]
[1, 1, 1, 2, 5]
[1, 1, 1, 3, 4]
[1, 1, 1, 7]
[1, 1, 2, 2, 2, 2]
[1, 1, 2, 2, 4]
[1, 1, 2, 3, 3]
[1, 1, 2, 6]
[1, 1, 3, 5]
[1, 1, 4, 4]
[1, 1, 8]
[1, 2, 2, 2, 3]
[1, 2, 2, 5]
[1, 2, 3, 4]
[1, 2, 7]
[1, 3, 3, 3]
[1, 3, 6]
[1, 4, 5]
[1, 9]
[2, 2, 2, 2, 2]
[2, 2, 2, 4]
[2, 2, 3, 3]
[2, 2, 6]
[2, 3, 5]
[2, 4, 4]
[2, 8]
[3, 3, 4]
[3, 7]
[4, 6]
[5, 5]
[10]
