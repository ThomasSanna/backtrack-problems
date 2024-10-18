def knightsTour(matrice, iteration=0, coos=(0, 0)):
  if iteration == len(matrice)**2:
    return True, matrice
  
  x, y = coos
  
  if matrice[x][y] != -1:
    return False, []
  
  matrice[x][y] = iteration
  
  for dx, dy in ([2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]):
    nx, ny = dx+x, dy+y
    if 0 <= nx < len(matrice) and 0 <= ny < len(matrice):
      success, result = knightsTour(matrice, iteration+1, (nx, ny))
      if success:
        return True, result
  matrice[x][y] = -1
  return False, []
  
def main(n):
    matrice = [[-1 for _ in range(n)] for _ in range(n)]
    success, result = knightsTour(matrice)
    if success:
        for row in result:
            print(row)
    else:
        print("Aucune solution trouvée")
  
main(5)