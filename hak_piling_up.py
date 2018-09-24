from collections import deque


for i in range(int(input())):
    num_of_cubes = int(input())
    cubes = deque(list(map(int, input().split())))

    if cubes[0] > cubes[-1]:
        del_cube = cubes.popleft()
    else:
        del_cube = cubes.pop()

    while(len(cubes) > 0):
        if cubes[0] >= cubes[-1] and cubes[0] <= del_cube:
            del_cube = cubes.popleft()
        elif cubes[-1] >= cubes[0] and cubes[1] <= del_cube:
            del_cube = cubes.pop()
        else:
            break
    print("Yes" if len(cubes) == 0 else "No")
