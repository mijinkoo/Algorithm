def solution(array, commands):
    answer = []
    array2 = array
    for i in range(len(commands)):
        array = array2[commands[i][0]-1:commands[i][1]]
        array.sort()
        answer.append(array[commands[i][2]-1])
    return answer
