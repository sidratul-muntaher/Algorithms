from  math import sqrt, ceil
a = [10, 50, 40, 30, 20, 70, 60]
def B(a):
    Bucket = []
    so = []
    for i in range(ceil(sqrt(len(a)))):
        Bucket.append([])
    m = max(a)
    #for j in range(3):
    for i in a:
        
        Bucket[ceil(i*len(Bucket)/m)-1].append(i)

    for i in Bucket:
        for j in range(len(i)):
            for k in range(len(i)):
                if i[j] < i[k]:
                    i[k], i[j] = i[j], i[k]

    for i in Bucket:
        so = so + i
    return so
if __name__ == "__main__":
    
    print(B(a))
