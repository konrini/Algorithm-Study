from itertools import product

def solution(word):
    word_list = ['A', 'E', 'I', 'O', 'U']
    lst = []
    for i in range(5):
        for j in list(product(word_list, repeat=i+1)):
            lst.append((''.join(j)))
    lst.sort()
    for i in range(len(lst)):
        if word == lst[i]:
            return i+1