from tkinter import *
from tkinter import messagebox
# Mikayla Beelders
root=Tk()
root.geometry("500x500")
root.title("Ticket Sales")
root.config(bg="skyblue")
variable = StringVar()
variable.set("Select Ticket")

class clsTicketSales():
    def __init__(self, root):
        # Frame for text
        frame = Frame(root, width=500, height=400, bg="#0A94A5")
        frame.place(x=0, y=300)

        # cellphone entry and label
        self.cellNumber_label = Label(root, text="Please enter cell number", bg="skyblue")
        self.cellNumber_label.place(x=10, y=20)
        self.cellNumber_entry = Entry(root)
        self.cellNumber_entry.place(x=250, y=20)

        # ticket price OptionMenu and label
        self.price_label = Label(root, text="Select Ticket Category", bg="skyblue")
        self.price_label.place(x=10, y=70)
        self.price_menu = OptionMenu(root, variable, "Soccer", "Movie", "Theatre")
        self.price_menu.config(width=20)
        self.price_menu.place(x=250, y=70)

        # number of tickets spinbox and label
        self.nr_ticket_label = Label(root, text="Number of Tickets Bought", bg="skyblue")
        self.nr_ticket_label.place(x=10, y=120)
        self.nr_ticket_entry = Spinbox(root, from_=0, to=10)
        self.nr_ticket_entry.place(x=250, y=120)

        # calculating button
        self.calculate_amount_btn = Button(root, text="Calculate Amount", command=self.CalcPrepayment, bg="#0A94A5")
        self.calculate_amount_btn.place(x=80, y=250)

        # text lines
        self.line1 = Label(frame, text="~~~~~~~~~~~~~~~~~~~~~~~~~~", bg="#0A94A5")
        self.line1.place(x=80, y=20)
        self.line2 = Label(frame, text=" ", bg="#0A94A5")
        self.line2.place(x=100, y=50)
        self.line3 = Label(frame, text=" ", bg="#0A94A5")
        self.line3.place(x=100, y=90)
        self.line4 = Label(frame, text=" ", bg="#0A94A5")
        self.line4.place(x=100, y=130)
        self.line5 = Label(frame, text="~~~~~~~~~~~~~~~~~~~~~~~~~~", bg="#0A94A5")
        self.line5.place(x=80, y=160)

        # clear button and position
        self.clear_btn = Button(root, text="Clear Inputs", command=self.clear, bg="#0A94A5")
        self.clear_btn.place(x=280, y=250)

        # prices
        self.soccer_price = 40.00
        self.movie_price = 75.00
        self.theatre_price = 100.00
    def CalcPrepayment(self):
        try:
            if variable.get()== "Soccer":
                cellnr = int(self.cellNumber_entry.get())
                #  nrtickets = int(self.nrticketsentry.get())
                soccerPrice = float(self.soccer_price)
                #  total = soccerprice * nrtickets
                tickets = float(self.nr_ticket_entry.get())
                total = 40 * tickets
                Vat = (14/100 * total)
                result = total + Vat
                self.line2.config(text="Amount due: R" + str(result))
                self.line3.config(text="Reservation for " + variable.get() + " for " + str(self.nr_ticket_entry.get()))
                self.line4.config(text="Was done by +27" + str(cellnr))
                self.amount_answer_label.config(textvariable=result)
            elif variable.get() == "Movie":
                cellnr = int(self.cellNumber_entry.get())
                #  nrtickets = int(self.nrticketsentry.get())
                moviePrice = float(self.movie_price)
                #  total = movieprice * nrtickets
                tickets = float(self.nr_ticket_entry.get())
                total = 75 * tickets
                Vat = (14/100 * total)
                result = total + Vat
                self.line2.config(text="Amount due: R" + str(result))
                self.line3.config(text="Reservation for " + variable.get() + " for " + str(self.nr_ticket_entry.get()))
                self.line4.config(text="Was done by +27" + str(cellnr))
                self.amount_answer_label.config(textvariable=result)
            elif variable.get() == "Theatre":
                cellnr = int(self.cellNumber_entry.get())
                #  nrtickets = int(self.nrticketsentry.get())
                theatrePrice = float(self.theatre_price)
                #  total = theatreprice * nrtickets
                tickets = float(self.nr_ticket_entry.get())
                total = 100 * tickets
                Vat = (14/100 * total)
                result = total + Vat
                self.line2.config(text="Amount due: R" + str(result))
                self.line3.config(text="Reservation for " + variable.get() + " for " + str(self.nr_ticket_entry.get()))
                self.line4.config(text="Was done by +27" + str(cellnr))
                self.amount_answer_label.config(textvariable=result)
        except ValueError:
            messagebox.showerror("error", "Invalid input. Please enter the correct details.")
            self.cellNumber_entry.delete(0, END)
            self.nr_ticket_entry.delete(0, END)
            variable.set("Select Ticket")
            self.line2.config(text="")
            self.line3.config(text="")
            self.line4.config(text="")
    # Clear invalid input
    def clear(self):
        self.cellNumber_entry.delete(0, END)
        self.nr_ticket_entry.delete(0, END)
        variable.set("Select Ticket")
        self.line2.config(text="")
        self.line3.config(text="")
        self.line4.config(text="")
x = clsTicketSales(root)
root.mainloop()