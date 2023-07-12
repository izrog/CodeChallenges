#izrog
#https://www.codechef.com/submit/FLOW009
T = int(input())

for purchase in range(T):
    quantity, price = map(int,input().split())
    if(quantity < 1000):
        print('{:.6f}'.format(quantity*price))
    else:
        print('{:.6f}'.format((quantity*price)*0.9))
