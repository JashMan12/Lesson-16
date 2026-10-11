try:
    num1,num2=eval(input("enter to numbers, seprate them with a comma"))
    result=num1/num2
    print("The result is", result)
except ZeroDivisionError:
    print("You can't divide a number with zero.")
except SyntaxError:
    print("You have to put a comma between your numbers.")
except:
    print("There is some error.")
else:
    print("Your code is error free.")
finally:
    print("Thank you for trying.")