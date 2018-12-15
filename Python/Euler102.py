path = '/Users/mcneillc/Documents/Project Euler/Python/Text Files/triangles.txt'
triangles = open(path, 'r')

def listOfStr_to_listOfInt(n):
    n = [int(i) for i in n]
    return n

def areaOfTriangle(x1, y1, x2, y2, x3, y3): 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def originIsInside(x1, y1, x2, y2, x3, y3): 
    A = areaOfTriangle(x1, y1, x2, y2, x3, y3) 
    A1 = areaOfTriangle(0, 0, x2, y2, x3, y3)   
    A2 = areaOfTriangle(x1, y1, 0, 0, x3, y3)  
    A3 = areaOfTriangle(x1, y1, x2, y2, 0, 0) 
    if (A == A1 + A2 + A3): 
        return True
    else: 
        return False

def euler102():
    coords = triangles.readlines()
    coords = [listOfStr_to_listOfInt(i.strip('\n').split(',')) for i in coords]
    count = 0
    for i in coords:
        if originIsInside(i[0],i[1],i[2],i[3],i[4],i[5]) == True:
            count += 1
    return count

print euler102()



