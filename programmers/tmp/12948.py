def solution(phone_number):
    
    front, back = phone_number[:-4], phone_number[-4:]
    length = len(front)
    
    return "*"*length+back