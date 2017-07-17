# 1  add two numbers and return the result
#----------------------------------------------------------------
addition <- function(number1, number2) {
  
  return (number1 + number2)


}
#---------------------------------------------------------------
# 2 subtract second number from the first number
#----------------------------------------------------------------

subtraction <- function(number1, number2) {
  
  return (number1 - number2)
  
  
}
  
#----------------------------------------------------------------
# 3  multiply first number by the second and give the result
#----------------------------------------------------------------	
multiplification <- function(first, second) {
  return (first * second)
}


#----------------------------------------------------------------
# 4  divide first number by the second number and get result
#----------------------------------------------------------------

division <- function(first,second) {  
  return (first / second)

}

#----------------------------------------------------------------
#   5  power of the number
#----------------------------------------------------------------	

power <- function(base, power)   {
  return  (base**power)
}

#----------------------------------------------------------------
# 6   square
#----------------------------------------------------------------	

square <- function(number)  {
  return (number ** 2)
  
}

#----------------------------------------------------------------
# 7  cube
#----------------------------------------------------------------	

cube <- function(num)  {
  return (num **3)
  
}

#----------------------------------------------------------------
# 8 square root
#----------------------------------------------------------------
squareroot <- function(number)   {
    if (number > 0){
      return (number ** 0.5)
    }  
    else if (number == 0){
      return (0)
    } 
    else if (number < 0){	
      return ("inf")
      
    }
  }
  
#----------------------------------------------------------------
#  9 factorial of the number
#----------------------------------------------------------------
factorial <- function (number){
  number = as.integer(readline(prompt="Please Enter a number here: "))
  factorial = 1
  if(number < 0) {
    print("That is a negative number, input a poitive number")
  } else if(number == 0) {
    print("The factorial of 0 is 1")
  } else {
    for(i in 1:number) {
      factorial = factorial * i
    }
    print(paste("The factorial of", number ,"is",factorial))
  }
}

#----------------------------------------------------------------
#  10 absolute 
#----------------------------------------------------------------
abs <- function(number) {
  return (number)
  
}


