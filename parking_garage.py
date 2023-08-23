class parking_garage():

    tickets = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    parking_spaces = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    currentTickets = {}  

    def __init__(self, payment = 0):
        self.payment = payment


    def take_ticket(self):

        collecting_a_ticket = input("Parking Prices: \n$2.00 per hour \n$17.00 -all day. \nWould you like a ticket to park? (Yes/No) ")
        if collecting_a_ticket.lower() == 'yes':
            self.tickets.pop()
            self.parking_spaces.pop()
        elif collecting_a_ticket.lower() == 'no':
            print("A ticket was not collected. Have a good day.")

    def payForParking(self):
        
        cost = input("Parking Prices: \n$2.00 per hour \n$17.00 -all day \nEnter the number of hours parked or enter 'all day' for time above 8 hours.")
        if cost.lower() == 'all day':
            self.payment += 17
            self.currentTickets['paid'] = 'False'
        else:
            self.payment = int(cost) * 2
            self.currentTickets['paid'] = 'False'

        print(f"Total amount due: ${self.payment}.00")

        making_payment = input("Please enter the amount you would like your debit/credit card charged: ")
        self.payment -= int(making_payment)
        if self.payment > 0:
            print(f"You have a remaining balance of {self.payment}. Please remove your ticket and restart the payment process.")
            self.currentTickets['paid'] = 'False'
        elif self.payment == 0:
            print("Thank you. Your ticket has been paid. Please leave within 15 minutes.")
            self.currentTickets['paid'] = 'True'

    def leaveGarage(self):

        if self.currentTickets['paid'] == 'True':
            print("Thank you. Have a nice day!")
            self.tickets.append(self.tickets[-1] + 1)
            self.parking_spaces.append(self.parking_spaces[-1] + 1)
        elif self.currentTickets['paid'] == 'False':
            print(f"Your payment has not been received. Please pay the amount due: {self.payment}")


run = parking_garage()

run.take_ticket()
run.payForParking()
run.leaveGarage()






    
   