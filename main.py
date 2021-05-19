from tkinter import *
from tkinter import messagebox
# Mikayla Beelders
root=Tk()
root.geometry("400x600")
root.title("Ticket Sales")
myresult = IntVar()
# OptionsList = [
#         "Soccer"
#         "Movie"
#         "Theater"
# ]
variable = StringVar()
variable.set("Select Ticket")

class clsTicketSales():
    def __init__(self, root):
        frame2 = Frame(root)
        frame2.place(x=0, y=300)
        self.cellNumber_label = Label(root, text="Please enter cell number")
        self.cellNumber_label.place(x=10, y=20)
        self.cellNumber_entry = Entry(root)
        self.cellNumber_entry.place(x=180, y=20)

        self.price_label = Label(root, text="Select Ticket Category")
        self.price_label.place(x=10, y=70)
        self.price_menu = OptionMenu(root, variable, "Soccer", "Movie", "Theatre")
        self.price_menu.config(width=20)
        self.price_menu.place(x=180, y=70)

        self.nr_ticket_label = Label(root, text="Number of Tickets Bought")
        self.nr_ticket_label.place(x=10, y=120)
        self.nr_ticket_entry = Spinbox(root, from_=0, to=10, state="readonly")
        self.nr_ticket_entry.place(x=180, y=120)

        self.calculate_amount_btn = Button(root, text="Calculate Amount", command=self.CalcPrepayment)
        self.calculate_amount_btn.place(x=100, y=200)

        self.clear_btn = Button(root, text="Clear Inputs", command=self.clear)
        self.calculate_amount_btn.place(x=150, y=200)

        self.amount_label = Label (root, text="Amount Due")
        self.amount_label.place(x=10, y=300)
        self.amount_answer_label = Label (root, text= " ", width = 20)
        self.amount_answer_label.place(x=180, y=300)

        self.soccer_price = 40.00
        self.movie_price = 75.00
        self.theatre_price = 100.00
    def activate(self):
        try:
            if variable.get()== "Soccer":
                # return (40 * int(self.nr_ticket_entry.get()))
                cellnr = int(self.cellNumber_entry.get())
                #  nrtickets = int(self.nrticjetsentry.get())
                soccerPrice =  (40)
                #  total = sccoerpr * nrticjets
                self.total = 40 * int(self.nr_ticket_entry.get())
                Vat = 14/100 * self.total
                result = self.total + Vat
                self.amount_answer_label.config(textvariable=result)
            elif variable.get() == "Movie":
                # return (40 * int(self.nr_ticket_entry.get()))
                cellnr = int(self.cellNumber_entry.get())
                #  nrtickets = int(self.nrticketsentry.get())
                moviePrice = (75)
                number_of_tickets = int(self.nr_ticket_entry)
                #  total = moviepr * nrtickets
                self.total = moviePrice * number_of_tickets
                Vat = 14 / 100 * self.total
                result = self.total + Vat
                self.amount_answer_label.config(textvariable=result)

            elif variable.get() == "Theatre":
                # return (40 * int(self.nr_ticket_entry.get()))
                cellnr = int(self.cellNumber_entry.get())
                #  nrtickets = int(self.nrticketsentry.get())
                theatrePrice = (100)
                number_of_tickets = int(self.nr_ticket_entry)
                #  total = theatre * nrtickets
                self.total = theatrePrice * number_of_tickets
                Vat = 14 / 100 * self.total
                result = self.total + Vat
                self.amount_answer_label.config(textvariable=result)
        except ValueError:
            messagebox.showerror = ("error", "Invalid Input. Please enter the correct details.")
            self.cellNumber_entry.delete(0, END)
            self.nr_ticket_entry.delete(0, END)
            variable.get().delete(0, END)


    def clear(self):
        self.cellNumber_entry.delete(0, END)
        self.nr_ticket_entry.delete(0, END)
        variable.get().delete(0 ,END)

    def CalcPrepayment(self):
        myresult = (int(self.nr_ticket_entry.get()) * int(self.price_menu.get())) + 0.14*(int(self.nr_ticket_entry.get()) * int(self.price_menu.get()))
        self.result.set(myresult)
        return self.result

# obj_ticket = clsTicketSales("0826889551", 4, 80)
# print("The amount is " + str(obj_ticket.CalcPrepayment()))
# self.myresult.set(result)

# class nr_tickets(clsTicketSales):
#     def __init__(self, master):
#         self.nr_tickets_label = Label(root, text="Number of Tickets")
#         self.nr_tickets_label.place(x=10, y=90)
#         self.nr_tickets_menu = OptionMenu(master, price, 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#         self.nr_tickets_menu.place(x=120, y=90)

x = clsTicketSales(root)
root.mainloop()