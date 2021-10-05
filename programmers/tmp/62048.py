def solution(w,h):
    if w > h:
        g = gcd(w, h)
    else:
        g = gcd(h, w)
    
    return w * h - (w + h - g)
        
def gcd(a, b):
    
    while b != 0:
        remain = a % b
        a, b = b, remain
        
    return abs(a)