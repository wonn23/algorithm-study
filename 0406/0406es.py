#0406 스터디 백준 알고리즘#


#1904 01타일###
def Tile(n):

  if n==1:
    return 1
  if n==2:
    return 2

  Table = [0] * (n+1)
  Table[1] = 1
  Table[2] = 2

  for i in range(3,n+1):
    Table[i] = (Table[i-1] + Table[i-2]) % 15746

  return (Table[n])

def main():
  n = int(input())
  print(Tile(n))
    
if __name__ == "__main__":
    main()


#1026 보물###
#왜 맞앗지 ..?

import copy

def treasure(n,treaA,treaB):
  treaBB = copy.deepcopy(treaB)
  treaAA = copy.deepcopy(treaA)

  treaAAA = [0] * (n)

  while(len(treaAA) > 0):
    minBindex = treaBB.index(min(treaBB))
    treaBB[minBindex] = 101
    maxA = max(treaAA)
    treaAA.pop(treaAA.index(maxA))
    treaAAA[minBindex] = maxA
    #print('treaBB',treaBB,minBindex,'treaAA',treaAA,maxA)

  result = 0

  for i in range(n):
      result += treaB[i] * treaAAA[i] 
  return result
  

def main():
  n = int(input())
  treaA = [int(x) for x in input().split()]
  treaB = [int(x) for x in input().split()]
  print(treasure(n,treaA,treaB))

if __name__ == "__main__":
  main()


#14495 피보나치 비스무리###
def bisFibo(n):

    if n == 1 or n == 2 or n == 3:
        return 1
    
    Table = [0] * (n+1)
    Table[1] = Table[2] = Table[3] = 1
    
    for i in range(4,n+1):
        Table[i] = Table[i-1] + Table[i-3]

    return Table[n]
  

def main():
  n = int(input())

  print(bisFibo(n))

if __name__ == "__main__":
  main()