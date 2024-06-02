def media(p1,p2,p3,p4, rec=None):
    media4 = (3*p1 + 4*p2 + 5*p3 + 6*p4) / 18
    if rec == None:
        return round(media4 , 1)
    else:
        return round((media4 + rec ) / 2, 1)

print(media(2,3,4,5,10))