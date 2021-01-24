def getfunc():
   func= input("what is you function")
   func2 = func.split('+')
   print(func2)  
   numlist=[]
   for x in func2:
       print(x)
       u= (x.split('x^'))
       numlist.append(u)
   print(numlist)
   return (numlist)
def getop():
    op = input("For derivative, tpye d. For Intergal type i")
    if op == 'd':
        return 0
    elif op == 'i':
        return 1
    else: 
        print("impropper response")
def derivative(val): 
    newnumlist=[]
    for x in val:
        coef = int(x[0]) * int(x[1])
        pwr = int(x[1])-1
        newnumlist.append([coef,pwr])
    print(newnumlist)
    return newnumlist
            
        
    
def intergal(coeff, power):
    coeffint = float(coeff)
    powerint = float(power)
    new_powerstr = str(powerint+1)
    new_coeffstr = str(coeffint/(powerint+1))
    print("Integral:"+new_coeffstr+"x^"+new_powerstr)

def together(val2):
    monobuild=[]
    for x in val2:
        monobuild.append(str(x[0]) + 'x^' + str(x[1]))
    print('+'.join(monobuild))
      
   
nums = getfunc()
opan = getop()
if opan == 0:
    butt= derivative(nums)
    together(butt)
elif opan == 1:
    intergal(nums[0], nums[1])

