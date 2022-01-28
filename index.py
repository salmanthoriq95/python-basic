# This is introduce of variable and data types
# example :
# a = 10
# that mean "a" is the variable and "10" is the value  
# Remember! python have dynamics data types!
# variable must be direct assign
# 
# to know the data type of variable you can call type(var_name)

# Integer
thisIsInt = 1234
print("integer example : ", thisIsInt)
print("data type : ", type(thisIsInt))

# Float
thisIsFloat = 3.14
print("float example : ", thisIsFloat)
print("data type : ", type(thisIsFloat))

# String
thisIsString = "Hello World !"
print("string example : ", thisIsString)
print("data type : ", type(thisIsString))

# Boolean
thisIsBoolTrue = True
thisIsBoolFalse = False
print("bool true example : ", thisIsBoolTrue)
print("data type : ", type(thisIsBoolTrue))
print("bool false example : ", thisIsBoolFalse)
print("data type : ", type(thisIsBoolFalse))

# Complex (for imaginary number)
thisIsComplex = complex(5,6)
print("complex example : ", thisIsComplex)
print("data type : ", type(thisIsComplex))

# Import from C data types
from ctypes import c_double # Importing C data types
thisIsCType = c_double(1.9827364598273645928)
print("import C data types example : ", thisIsCType)
print("data type : ", type(thisIsCType))

# Casting or changing data type of the variable
## int to str
castToString = str(thisIsInt)
print("casting int to str example : ", castToString)
print("data type : ", type(castToString))

## int to float
castToFloat = float(thisIsInt) # rounding down
print("casting int to float example : ", castToFloat)
print("data type : ", type(castToFloat))

## float to int
castToInt = int(thisIsFloat)
print("casting float to int example : ", castToInt)
print("data type : ", type(castToInt))

## int to bool
castToBool = bool(thisIsFloat) # return false if the value is 0 or empty string, except it will be true
print("casting int to bool example : ", castToBool)
print("data type : ", type(castToBool)) 

## str to bool
castToBool2 = bool(thisIsString)  # return false if the value is 0 or empty string, except it will be true
print("casting str to bool example : ", castToBool2)
print("data type : ", type(castToBool2))

# Input
inputUser = input("enter data : ") # anything that inputed data will be string
print("the input is ", inputUser)
print("data type : ", type(inputUser))

## if we want to change inputed data become integer, then :
inputUserInt = int(input("enter a number : "))
print("the input is ", inputUserInt)
print("data type : ", type(inputUserInt))

## when we want inputed data boolean typed
inputBool = bool(int(input("enter a boolean : "))) # cast to int first, if we not cast it first all inputed console will be string
print("the input is ", inputBool)
print("data type : ", type(inputBool))