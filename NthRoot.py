epsilon = 0.001

def sqr_root(low,high,n,const_value):
  mid = (low+high)/2.0
  
  mid_2 = mid
  for _i in range(n-1):
    mid_2*=mid

  dif = mid_2 - const_value
  
  if abs(dif) <= epsilon:
    return mid
  elif mid_2 > const_value:
    return sqr_root(low,mid,n,const_value)
  elif mid_2 < const_value:
    return sqr_root(mid,high,n,const_value)

def find_nth_root(value, n):
  low = 0
  high = value
  return sqr_root(low,high,n,value)
  
def main():
  print(find_nth_root(12345,3))

if __name__ == "__main__":
  main()
