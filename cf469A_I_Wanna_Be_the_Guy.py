#izrog
#greedy implementation
#https://codeforces.com/problemset/problem/469/A

import sys
input = sys.stdin.readlines()

levels = list(range(1,int(input[0])+1))

little_x = list(input[1])
little_y = list(input[2])

joint_levels = set(little_x + little_y)

if ('\n' in joint_levels):
    joint_levels.remove('\n')

for level in joint_levels:
    val = int(level)
    if (val in levels):
        levels.remove(val)

if (len(levels) == 0):
    print('I became the guy.')
else:
    print('oh, my keyboard!')
