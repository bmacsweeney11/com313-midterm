

def altruist_value():
    value = 0
    if egoist == left and altruist == right:
        value = 1-C

    elif altruist == left and egoist == right:
        value = 1-C
        
    elif altruist == left and altruist == right:
        value = 1-C

    else:
        value = -C

def egoist_value():
    value = 0
    if egoist == left and altruist == right:
        value = 1

    elif altruist == left and egoist == right:
        value = 1
        
    elif altruist == left and altruist == right:
        value = 2

    else:
        value = 0

def altruist_change():
    if neighbor.right == egoist and neighbor.left = egoist:
        altruist = egoist
    
def egoist_stayORchange():
    if neighbor.left == altruist:
        egoist = altruist
    elif neighbor.right == altruist:
        egoist = altruist
    else:
        egoist = egoist
