#User function Template for python3

def getMinMax( a, n):
    if n==1:
        return a[0],a[0]
    else:
        minimum=a[0]
        maximum=a[0]
        for i in range(1,n):
            minimum=min(minimum,a[i])
            maximum=max(maximum,a[i])
        return minimum, maximum
