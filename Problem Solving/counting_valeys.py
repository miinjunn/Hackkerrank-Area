# path = 'UDDDUDUU'
path = 'DDUUUUDDDU'
steps = len(path)
print(f'{steps} <--> {path}')


def countingValleys(steps, path):
    num_path = [0]
    for i in path:
        if i == 'U':
            num_path.append(num_path[-1] + 1)
        elif i == 'D':
            num_path.append(num_path[-1] - 1)
    print(num_path)

    temp = 0
    for i in range(len(num_path)-1):
        if num_path[i] == 0 and num_path[i+1] == -1:
            temp += 1
    return temp
 

print(countingValleys(steps, path))
