# 1'den N'e kadar sayıların toplanması

def topla(n):

    if n==1:
        return 1

    return n+ topla(n-1)

print(topla(5))
