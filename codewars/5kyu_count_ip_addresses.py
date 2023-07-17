# izrog
# https://www.codewars.com/kata/526989a41034285187000de4/train/python
# Implement a function that receives two IPv4 addresses, and returns the number of 
# addresses between them (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be 
# greater than the first one.

from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))

#another solution I liked.
def ips_between2(start, end):
    a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
    return abs(a-b)