def catAndMouse(x, y, z):
    distA =abs (z - x)
    distB = abs(z - y)

    
    if distA < distB:
        return "Cat A"
    elif distB < distA:
        return "Cat B"
    else:
        return "Mouse C"