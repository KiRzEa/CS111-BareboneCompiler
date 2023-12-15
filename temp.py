#--------Redefine subtract function--------

def subtract(variable,num=1):
    variable = variable - num
    if variable<0 :
        variable=0
    return variable

#--------Safe pre declare variables--------

X1 = 0
temp = 0
X = 0
Y1 = 0
Y = 0
lt = 0
invert = 0
gt = 0
result = 0

#-----------Input requirer code------------

X=5
Y=5

#-----------Compiled code------------

X1 = 0
temp = 0
while X != 0:
    X = subtract(X)
    temp += 1
    X1 += 1
while temp != 0:
    temp = subtract(temp)
    X += 1
Y1 = 0
while Y != 0:
    Y = subtract(Y)
    temp += 1
    Y1 += 1
while temp != 0:
    temp = subtract(temp)
    Y += 1
lt = 0
while Y1 != 0:
    Y1 = subtract(Y1)
    lt += 1
while X1 != 0:
    X1 = subtract(X1)
    lt = subtract(lt)
invert = 0
invert += 1
while lt != 0:
    lt = subtract(lt)
    invert = subtract(invert)
while invert != 0:
    lt += 1
    invert = subtract(invert)
gt = 0
while X != 0:
    X = subtract(X)
    gt += 1
while Y != 0:
    Y = subtract(Y)
    gt = subtract(gt)
invert += 1
while gt != 0:
    gt = subtract(gt)
    invert = subtract(invert)
while invert != 0:
    gt += 1
    invert = subtract(invert)
result = 0
while lt != 0:
    result += 1
    lt = subtract(lt)
while gt != 0:
    result += 1
    gt = subtract(gt)
result = subtract(result)
temp += 1
while result != 0:
    result = subtract(result)
    temp = subtract(temp)
while temp != 0:
    temp = subtract(temp)
    result += 1

#-----------Output variables code------------

print("Value of  X1 : " + str(X1)) 
print("Value of  temp : " + str(temp)) 
print("Value of  X : " + str(X)) 
print("Value of  Y1 : " + str(Y1)) 
print("Value of  Y : " + str(Y)) 
print("Value of  lt : " + str(lt)) 
print("Value of  invert : " + str(invert)) 
print("Value of  gt : " + str(gt)) 
print("Value of  result : " + str(result)) 

#-----------End-------------

with open('output.txt', 'w') as f:
    f.write(f"Value of X1 : " + str(X1) + "\nValue of temp : " + str(temp) + "\nValue of X : " + str(X) + "\nValue of Y1 : " + str(Y1) + "\nValue of Y : " + str(Y) + "\nValue of lt : " + str(lt) + "\nValue of invert : " + str(invert) + "\nValue of gt : " + str(gt) + "\nValue of result : " + str(result) + "\n")
    f.close()