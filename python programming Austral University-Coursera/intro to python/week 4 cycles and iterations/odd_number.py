def odd_number(number):

   result = True

   for divisor in range(2, number):

       if (number % divisor) == 0:

           result = False

           break

   return result 

   
