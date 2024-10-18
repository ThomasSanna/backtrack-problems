matrice = [
  [1, 0, 0, 0],
  [1, 1, 0, 1],
  [0, 1, 0, 0],
  [1, 1, 1, 1]
]

def ratInMaze(matrice, coos):
  x, y = coos
  if x == len(matrice)-1 and y == len(matrice[0])-1:
    return True
  if matrice[x][y] in (0, '.'):
    return False
  
  matrice[x][y] = '.'
  
  for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
    nx, ny = dx+x, dy+y
    if 0 <= nx < len(matrice) and 0 <= ny < len(matrice[0]) and ratInMaze(matrice, (nx, ny)):
      return True
  matrice[x][y] = 1
  return False

print(ratInMaze(matrice, (0, 0)))

for elt in matrice:
  print(' '.join(str(e) for e in elt))