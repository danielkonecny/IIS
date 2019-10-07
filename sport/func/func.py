def compare(l1,l2):
    s1 = set(l1)
    s2 = set(l2)

    if (s1 & s2):
        return True 
    else: 
        return False
