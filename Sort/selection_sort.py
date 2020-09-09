a = [30, 10, 50, 20, 60, 40]

def selectionSort(A):
    for i in range(len(A)):
        mi = i
        for j in range(i+1, len(A)):
            if A[j]<A[mi]:
                mi = j
        if mi != i:
            A[mi], A[i] = A[i], A[mi]
    return A
if __name__ == "__main__":
    print(selectionSort(a))