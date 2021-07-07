def solution(array, commands):
    answer = []
    array2 = array
    for i in range(len(commands)):
        array = array2[commands[i][0]-1:commands[i][1]]
        array.sort()
        answer.append(array[commands[i][2]-1])
    return answer

# 간단한 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))