import random

def quick_sort(lst):
    if not lst: return []
    pivot = lst[-1]
    lesser = quick_sort([x for x in lst[:-1] if x < pivot])
    grater = quick_sort([x for x in lst[:-1] if x > pivot])
    return lesser + [pivot] + grater


#s = set()
#while len(s) != 100: s.add(random.randint(0,1000))
#ls = list(s)
#print(ls)


lst = []
#while len(lst) != 100 : lst.append(random.randint(0,50))
lst= [0,0,0,0]
print(quick_sort(lst))
