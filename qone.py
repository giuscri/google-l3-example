from typing import List

def find_non_dup(A: List[int]) -> int:
    if len(A) == 0:
        raise ValueError("answer is not defnd for empty list")

    if len(A) == 1:
        return A[0]

    if len(A)%2 == 0:
        raise ValueError("input doesn't seem to contain non-duplicate element")

    i = 0
    n = len(A)
    j = n-1
    while i <= j:
        mid = i+(j-i)//2
        if mid-1 >= 0 and A[mid-1] == A[mid]:
            pass
        elif mid+1 < n and A[mid+1] == A[mid]:
            mid += 1
        else:
            return A[mid]

        if (mid+1)%2 == 0:
            i, j = mid+1, j
        else:
            i, j = i, mid-1

    return A[i]
