matriceH = [ # Matrice hamiltonienne
  [0, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0]
]

matriceNH = [ # Matrice non hamiltonienne
  [0, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1],
  [1, 0, 0, 1, 1, 0]
]


def getSommetPossible(matrice, sommet, ls):
  return [i for i in range(len(matrice)) if matrice[sommet][i] == 1 and i not in ls]

def isHamiltonian(matrice, sommet=0, ls=[]):
  n = len(matrice)
  if len(ls) == n-1:
    return 0 in getSommetPossible(matrice, sommet, [])
  
  somPossible = getSommetPossible(matrice, sommet, ls)
  if not somPossible:
    return False
  
  for elt in somPossible:
    if isHamiltonian(matrice, elt, ls + [sommet]):
      return True
  return False

print(isHamiltonian(matriceH))
print(isHamiltonian(matriceNH))