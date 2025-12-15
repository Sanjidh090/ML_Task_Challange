x  = 0.2 + 0.1
#False if compared simply 
print("True") if  x == 0.3  else  print("False")
#Fix
print("True") if  round(x,1) == 0.3  else  print("False")
