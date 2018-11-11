##############################################################
def dfs_check(dict1, list1, n):
    board = [[0 for i in range(n)] for j in range(n)]
    (a, b) = dict1[0]
    for x in range(n):
        board[x][b] = 1
    for y in range(n):
        board[a][y] = 1
    while a != n - 1 and b != n - 1:
        board[a][b] = 1
        a += 1
        b += 1
    (a, b) = dict1[0]
    while a >= 0 and b <= n - 1:
        board[a][b] = 1
        a -= 1
        b += 1
    (a, b) = dict1[0]
    while a <= n - 1 and b >= 0:
        board[a][b] = 1
        a += 1
        b -= 1
    (a, b) = dict1[0]
    while a >= 0 and b >= 0:
        board[a][b] = 1
        a -= 1
        b -= 1
    (a, b) = dict1[0]
    while a <= n - 1 and b <= n - 1:
        board[a][b] = 1
        a += 1
        b += 1
    for i in list1:
        (x, y) = i[0]
        if board[x][y] == 1:
            return False
    return True
#############################################################

def dfs(dict1, n, p, track, check_ans):
    stack = []
    maxi = check_ans
    stack.append(dict1[track])
    cur_total = dict1[track][1]
    index = dict1.index(stack[len(stack) - 1])

    while stack:
        is_pushed = False
        for i in range(index + 1, len(dict1)):
            est_total = 0
            if stack:   est_index = dict1.index(stack[len(stack) - 1])
            else: break
            if len(dict1) - index > p - len(stack) and est_index < len(dict1) - 1 - p + len(stack):
                for j in range(p - len(stack)):
                    est_total += dict1[est_index + 1][1]
                    est_index += 1
            else:   break
            if maxi - cur_total >= est_total:
                is_pushed = True
                cur_total -= stack[len(stack) - 1][1]
                if len(stack) > 1:   stack.pop()
                index = dict1.index(stack[len(stack) - 1])
                cur_total -= stack[len(stack) - 1][1]
                if stack:   stack.pop()
                break
            total = 0
            if len(stack) == p:
                for i in stack:
                    total += i[1]
                    if total > maxi:
                        maxi = total
                cur_total -= stack[len(stack) - 1][1]
                stack.pop()
                index = dict1.index(stack[len(stack) - 1])
                cur_total -= stack[len(stack) - 1][1]
                stack.pop()
            elif dfs_check(dict1[i], stack, n) and len(stack) < p:
                stack.append(dict1[i])
                cur_total += dict1[i][1]
                is_pushed = True

        if not is_pushed:
            index = dict1.index(stack[len(stack) - 1])
            cur_total -= dict1[index][1]
            stack.pop()
    return maxi

##############################################################

def isPossible(dict1, p, track, n, check_ans):
    maxi = dfs(dict1, n, p, track, check_ans)
    if not maxi:    return False
    return maxi

#############################################################
f = open('input15.txt')
n = int((f.readline()).strip('\n'))
p = int((f.readline()).strip('\n'))
s = int((f.readline()).strip('\n'))
fw = open('output.txt', 'w+')
Matrix = [[0 for i in range(n)] for j in range(n)]
dict1 = {}
for i in range(s * 12):
    x = (f.readline()).strip('\n')
    a, b = x.split(',')
    a = int(a)
    b = int(b)
    if (a, b) not in dict1:
        dict1[(a, b)] = 1
    else:
        dict1[(a, b)] += 1
    for j in range(n):
        for k in range(n):
            if (j, k) not in dict1:
                dict1[(j, k)] = 0
dict1 = sorted(dict1.items(), key=lambda d: d[1], reverse=True)

if p == 1:
    fw.write(str(dict1[0][1]) + '\n')
else:
    track = 0
    check_ans = 0
    result = [dict1[0]]
    while dict1[track][1] > check_ans // p:
        stack = []
        ans = isPossible(dict1, p, track, n, check_ans)
        i = track + 1
        if ans:
            if check_ans < ans:
                check_ans = ans
        track += 1
    fw.write(str(check_ans) + '\n')

f.close()
fw.close()