# method 1
#User function Template for python3

def reverseWord(s):
    a=s[::-1]
    return a
  
  
#method 2
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A
