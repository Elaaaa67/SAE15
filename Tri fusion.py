def Fusiontri(L):
    if len(L) == 1:
        return L
    else:
        return fusion(Fusiontri(L[:len(L) // 2]), Fusiontri(L[len(L) // 2:]))


def fusion(A, B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] <= B[0]:
        return [A[0]] + fusion(A[1:], B)
    else:
        return [B[0]] + fusion(A, B[1:])