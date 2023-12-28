import webbrowser
from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total
    amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Roommates:
    """
    Object that contains data about the flatmates, such as
    the name of roomate, number of days in flat in a month,
    and, how much they pay based on given attributes.
    """  

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat
    
    def pays(self, bill, roommate2):
        weight = (self.days_in_flat / (self.days_in_flat + roommate2.days_in_flat))
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Generates a PDF file that contains data about the flatmates, such as
    their names and respective calculated bill for that period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):

        roommate1_pay = str(round(roommate1.pays(bill, roommate2), 2))
        roommate2_pay = str(round(roommate2.pays(bill, roommate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("/Users/mattgola/Desktop/GitHub/Python Course/files-master/App-2-Flatmates-Bill/files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Roommates Bill", border=0, align="C", ln=1)

        # Insert Period and Month labels and values
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=175, h=40, txt=bill.period, border=0, ln=1)


        # Insert name and due amount for the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0)
        pdf.cell(w=175, h=25, txt=roommate1_pay, border=0, ln=1)

        # Insert name and due amount for the second flatmate
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=175, h=25, txt=roommate2_pay, border=0, ln=1)

        pdf.output(self.filename)
        # Need to debug this file path. According to lecture, I need an absolute path for this method to run, syntax is wrong right now
        # webbrowser.open('file://' + /Users/mattgola/Documents/GitHub/PythonCourse/.vscode/FlatBillSharing_App/Report1.pdf(self.filename))


amount = float(input("Hey User, enter the bill amount: "))

period = input("Enter Period (e.g. December 2020): ")

name1 = input("Name of Roommate1: ")
days_in_flat1 = int(input(f"{name1}: Days in Apartment: "))

name2 = input("Name of Roommate2: ")
days_in_flat2 = int(input(f"{name2}: Days in Apartment: "))

current_bill = Bill(amount, period)
roommate1 = Roommates(name1, days_in_flat1)
roommate2 = Roommates(name2, days_in_flat2)

print(f"{roommate1.name} pays: ", roommate1.pays(current_bill, roommate2))
print(f"{roommate2.name} pays: ", roommate2.pays(current_bill, roommate1))

pdf_report = PdfReport(filename=f"{current_bill.period}.pdf")
pdf_report.generate(roommate1, roommate2, current_bill)