notation = '0123456789ABCDEF'
def turnToStr(num,base):
    q,r = divmod(num,base)
    n = notation[r]
    return turnToStr(q,base) + n if q else n 
print(turnToStr(0,2))