# izrog
# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

def increment_string(strng):
    if strng == "" or not strng[-1].isdigit():
        strng = strng + "1"
    else:
        num = []
        txt = ''
        for char in reversed(strng):
            if char.isdigit():
                num.append(char)
            else:
                txt = strng[:-(len(num))]
                break
        
        strng = txt + str(int("".join(reversed(num))) + 1).zfill(len(num))
    
    return strng

# other solution I liked
def increment_string2(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))