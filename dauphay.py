n= input()
s = ""
k = -2
for i in range(1, len(n)+1):
  s= n[-i]+s
  if k%3==0:
    s=","+s
  k+=1

print(s.strip(","))
