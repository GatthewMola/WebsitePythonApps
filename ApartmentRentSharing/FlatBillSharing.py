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


class Flatmates:
    """
    Object that contains data about the flatmates, such as
    the name of roomate, number of days in flat in a month,
    and, how much they pay based on given attributes.
    """  

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat
    
    def pays(self, bill, flatmate2):
        weight = (self.days_in_flat / (self.days_in_flat + flatmate2.days_in_flat))
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Generates a PDF file that contains data about the flatmates, such as
    their names and respective calculated bill for that period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("/Users/mattgola/Desktop/GitHub/Python Course/files-master/App-2-Flatmates-Bill/files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period and Month labels and values
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=175, h=40, txt=bill.period, border=0, ln=1)


        # Insert name and due amount for the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=175, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount for the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=175, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)
        # Need to debug this file path. According to lecture, I need an absolute path for this method to run, syntax is wrong right now
        # webbrowser.open('file://' + /Users/mattgola/Documents/GitHub/PythonCourse/.vscode/FlatBillSharing_App/Report1.pdf(self.filename))


amount = float(input("Hey User, enter the bill amount: "))

period = input("Enter Period (e.g. December 2020): ")

name1 = input("Name of Flatmate1: ")
days_in_flat1 = int(input(f"{name1}: Days in Flat: "))

name2 = input("Name of Flatmate2: ")
days_in_flat2 = int(input(f"{name2}: Days in Flat: "))

current_bill = Bill(amount, period)
flatmate1 = Flatmates(name1, days_in_flat1)
flatmate2 = Flatmates(name2, days_in_flat2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(current_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(current_bill, flatmate1))

pdf_report = PdfReport(filename=f"{current_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, current_bill)