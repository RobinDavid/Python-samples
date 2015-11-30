def toList(f):
    l = list()
    while True:
        b = f.read(1)
        if b == '':
            break
        else:
            l.append(ord(b))
    return l

def countFreq(l): # return list with (decimal_char, occ) 
    d={}
    for elt in l:
        if d.has_key(elt):
            d[elt] += 1
        else:
            d[elt] = 1
    return sorted(d.items(),key=lambda x: x[1], reverse=True)

def max(d):
  m = 0
  elt = ''
  for k,v in d.items():
      if v > m:
          m = v
          elt = k
  return {elt:m}

def decipher(l,diff):
  newl = list()
  for e in l:
      val = e - diff
      if val < 0:
          newl.append(256 + (val % -256))
      else:
          newl.append(val)
  return newl

def pgcd(num,divisor,remain=0):
  rem = num % divisor
  if rem == 0:
      return remain
  else:
      return pgcd(divisor,rem,rem)

def getPrimeNb(x):
  l =[]
  for i in range (1,x):
      if pgcd(x,i) == 1:
          l.append(i)
  return l

def pgcduv(num,divisor):
  u = 1
  v = 0
  s = 0
  t = 1
  while (divisor > 0):
      rest = num % divisor
      quo = num / divisor
      #print "%s = %s * %s + %s" % (num, quo, divisor, rest)
      # a = q * b + r
      num = divisor
      divisor = rest
      
      tmp = s
      s = u - quo * s
      u = tmp
      
      tmp = t
      t = v - quo * t
      v = tmp
  return num, u, v

def inverse_possible(modulo, num):
  if pgcd(modulo, num, num) == 1:
      return True
  else:
      return False

def inverse(num, mod):
  inv = 0
  for i in range(mod):
      j = - mod
      while j < 0:
          if (mod*i)+(num*j) == 1:
              inv = j
          j = j + 1
  return inv+mod

def cI(occ,n):
    somme = Decimal(0)
    tmp = Decimal(n*(n-1))
    for i in occ:
        somme = somme + ( Decimal(i[1]*(i[1]-1)) / tmp )
    return somme
