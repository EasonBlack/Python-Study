import math

def solution(area):
  (e, d) = math.modf(math.sqrt(area))
  if e == 0 : 
    return str(int(d**2))
  return str(int(d**2)) + "," + solution(area - d**2)

  

print(solution(15324))