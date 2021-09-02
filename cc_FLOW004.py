#izrog
#https://www.codechef.com/submit/FLOW004
import sys
input = sys.stdin.readlines()
arr = input[1:]

for num in arr:
    num = num.strip('\n')
    print("{}".format(int(num[0])+int(num[-1])))

#Alternative to solution
count = int(input())

for num in range(count):
    inp = input()
    first, last = inp[0], inp[-1]
    print(int(first) + int(last))
