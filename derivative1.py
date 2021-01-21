def getfunc():
    coeffstr = input("what is your coefficient")
    powerstr = input("what is your power")
    print("Initial function:" + coeffstr + "x^" + powerstr)
    return (coeffstr,powerstr)
def getop():
    op = input("For derivative, tpye d. For Intergal type i")
    if op == 'd':
        return 0
    elif op == 'i':
        return 1
    else: 
        print("impropper response")
def derivative(coeff, power): 
    coeffint = float(coeff)
    powerint = float(power)
    new_coeffstr = str(coeffint*powerint)
    new_powerstr = str(powerint-1)
    print("derivative:"+new_coeffstr+"x^"+new_powerstr)  
def intergal(coeff, power):
    coeffint = float(coeff)
    powerint = float(power)
    new_powerstr = str(powerint+1)
    new_coeffstr = str(coeffint/(powerint+1))
    print("Integral:"+new_coeffstr+"x^"+new_powerstr)
    
nums = getfunc()
opan = getop()
if opan == 0:
    derivative(nums[0], nums[1])
elif opan == 1:
    intergal(nums[0], nums[1])

