any = 'y'
while any == 'y':
   print("\nCalculator Program")
   print("==================")

   n1 = float(input("Enter first number: "))
   n2 = float(input("Enter second number: "))
   op = input("Enter operation (+-*/): ")

   if op =="+":
      result = n1 + n2
   elif op == "-":
      result = n1 - n2
   elif op == "*":
      result = n1 * n2
   elif op == "/":
      result = n1 / n2
   print("Result = %f" %(result))
   any = input("\nAny more (yn): ")

