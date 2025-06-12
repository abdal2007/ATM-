class ATM:
    def __init__(self,naam,pin,balance):
        self.naam = naam
        self.__pin = pin
        self.__balance = balance
    def indentity_check(self,enter_pin):
        return self.__pin == enter_pin
    
    def check_balance(self):
        print(f"{self.naam} ap ky pass Rs.{self.__balance} majood han!")

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.naam}, app ky account ma Rs.{amount} jama ho gy han! ")
        else:
            print("invalid amount")

    def withdraw(self, amount):
        if amount <= 0 :
            print("invalid amount!")
        elif amount > self.__balance:
            print("insufficant balance!")
        else:
            self.__balance -= amount
            print(f"Rs.{amount} withdraw successfully!")

    def exit(self):
        print("Byee BYee ")



user = ATM(naam="Abdal", pin="12345", balance=100000)
print("hello, ki haal chal ayy ?")

user_pin = input("PIN daaliye bhai: ")

if user.indentity_check(user_pin):
    while True:
        print("/n ap kia karna chahty han?")
        print("1. balance check")
        print("2. deposit money")
        print("3. withdraw money")
        print("4. exit from ATM")

        choice = int(input("chose from 1-4: "))

        if choice == 1:
            user.check_balance()
        elif choice == 2:
            
            amount = int(input("kitny paisy jama kar wany han?"))
            user.deposit(amount)   
        elif choice == 3 :
            amount = int(input("kitny paisy nikalwany han?"))
            user.withdraw(amount)
        elif choice == 4:

            user.exit()
            break

        else:
            print("invalid option!")

else:
    print("inavlid pin!")
