# izrog
# Complete the function/method (depending on the language) to return true/True when its 
# argument is an array that has the same nesting structures and same corresponding length of
# nested arrays as the first array
# should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
# should return False 
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
# should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
# should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

def same_structure_as(original, other):
    if type(original) != type(other):
        return False
    if len(original) == len(other) == 0:
        return True
    if len(original) != len(other):
        return False
    for i, obj in enumerate(original):
        if bool(type(obj) == list) != bool(type(other[i]) == list):
            return False
        elif type(obj) == type(other[i]) == list:
            return same_structure_as(obj, other[i])
    return True

# Top Community solution
def same_structure_as2(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)