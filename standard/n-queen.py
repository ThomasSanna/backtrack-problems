import copy

n = 4
matrice = [['0' for _ in range(n)] for _ in range(n)]

def putQueenX(matrice, coos):
  x, y = coos
  tabCoos = []
  for i in range(-x, len(matrice)-x):
    for j in range(-y, len(matrice[0])-y):
      if (i==0 and j!=0) or (j==0 and i!=0) or (i==j):
        if matrice[x+i][y+j] == '0':
          tabCoos.append((x+i, y+j))
  return tabCoos

def ajoutTabCoos(matrice, tabCoos):
  for x, y in tabCoos:
    matrice[x][y] = 'X'

def enleveTabCoos(matrice, tabCoos):
  for x, y in tabCoos:
    matrice[x][y] = '0'
    
def reussite(matrice):
  n = len(matrice)
  return all(elt.count('X') >= n-1 for elt in matrice)

def nQueen(matrice, numQueen=1):
  n = len(matrice)
  
  if numQueen > n:
    return reussite(matrice)
  
  for i in range(numQueen-1, n):
    x, y = i, numQueen-1
    tabCoos = putQueenX(matrice, (x, y))
    matrice[x][y] = str(numQueen)
    ajoutTabCoos(matrice, tabCoos)
    if nQueen(matrice, numQueen+1):
      return True
    matrice[x][y] = '0'
    enleveTabCoos(matrice, tabCoos)
    return False

print(nQueen(matrice))
for elt in matrice:
  print(elt)