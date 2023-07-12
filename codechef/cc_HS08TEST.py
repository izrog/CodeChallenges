#izrog
#https://www.codechef.com/problems/HS08TEST
withdrawel, balance = input().split()
withdrawel = float(withdrawel)
balance = float(balance)

if (withdrawel%5 != 0 or withdrawel > balance-0.5):
    print("{:.2f}".format(balance))
else:
    print("{:.2f}".format((balance-withdrawel)-0.5))
