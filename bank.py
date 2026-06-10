class Bank():
    def __init__(self,money):
        self.money = money

    def print_details(self):
        print(self.money)

    def change_money(self):
        UserInput = input ("1: deposit or 2: withdraw: ")
        if UserInput == "withdraw" or UserInput == "2" :
            UserInput = input("how much: ")
            if (self.money - int(UserInput))>= 0:
                self.money -= int(UserInput)
            else :
                print("You dont have enough")
        elif UserInput == "deposit" or UserInput == "1":
            UserInput = input("how much: ")
            self.money += int(UserInput)
        
        self.print_details()

mn = Bank(2000)
mn.print_details()
mn.change_money()

mn.print_details()
