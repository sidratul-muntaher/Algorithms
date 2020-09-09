"""
Aut: Sidratul MT
ALG: Bubble sort
Comp: (n2)
Date: 16.Aug.2020
Time: 13:00
Done"""

ar = [2, 4, 1, 6, 3, 6, 3, 9, 2, 12, 4, 12, 78 ,34 ,43, 33, 0]
for i in range(len(ar)):
    for j in range(len(ar)-1):
        if ar[j] > ar[j+1]:
            a = ar[j+1]
            ar[j+1] = ar[j]
            ar[j] = a
            print(ar[j+1], ar[j])

print(ar)
