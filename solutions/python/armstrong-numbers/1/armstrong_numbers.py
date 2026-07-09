def is_armstrong_number(number):
    """Determines if a number is an Armstrong number"""
    if number == 0 :
        return(True)
    digits = [int(digit) for digit in str(number)] #The list where we will order the digits of the number
    Sum = 0
    for digit in digits :
        Sum+=digit**(len(digits))     #sum of digits raised to the power of the number of digits
    if Sum ==number:
        print("It's an Armstrong number !")
        return(True)
    else : 
        print("It's not an Armstrong number !")
        return(False)
        
