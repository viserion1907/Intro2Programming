"""
Written by: Michael Chitwa (u7199577@anu.edu.au)
This is a simple tax calculating program. It calculates taxes within different salary brackets and saves the result to
an HTML File. Income thresholds and the rate per bracket are given below:
Income thresholds   Rate
$0 - $18,200        0%
$18,201 - $37,000   19%
$37,001 - $90,000   32.5%
$90,001 - $180,000  37%
>= $180,001         45%
"""

# import sys
# Function to calculate the tax on income threshold
def tax_rate(income):
    if income <= 18200:
        tax = 0.0
        return tax
    elif income <= 37000:
        tax = 0.19
        return tax
    elif income <= 90000:
        tax = 0.325
        return tax
    elif income <= 180000:
        tax = 0.37
        return tax
    else:
        tax = 0.45
        return tax

# prompt for user input
netPay = input("Please enter your annual income ($): ")
netPay = float(netPay)  # convert the variable to float

if not netPay < 0:  # check that user input is not negative
    # Calculate tax due
    if netPay <= 18200:
        taxRate = 0.0
        taxableIncome = taxRate * netPay
        amountAfterTax = netPay - taxableIncome
    elif netPay <= 37000:
        taxRate = 0.19
        taxableIncome = taxRate * netPay
        amountAfterTax = netPay - taxableIncome
    elif netPay <= 90000:
        taxRate = 0.325
        taxableIncome = taxRate * netPay
        amountAfterTax = netPay - taxableIncome
    elif netPay <= 180000:
        taxRate = 0.37
        taxableIncome = taxRate * netPay
        amountAfterTax = netPay - taxableIncome
    else:
        taxRate = 0.45
        taxableIncome = taxRate * netPay
        amountAfterTax = netPay - taxableIncome
    # sys.stdout = open("test.txt", "w")
    print("You have entered: ${:.2f}".format(netPay))
    print("Your tax rate is:", tax_rate(netPay) * 100, "%")
    print("Your taxable income is: ${:.2f}".format(taxableIncome))
    print("Amount after tax: ${:.2f}".format(amountAfterTax))
    # sys.stdout.close()
else:  # exit program and display message
    print("You have entered an invalid value!!! Exiting...")

report_list = [netPay, tax_rate(netPay), taxableIncome, amountAfterTax] # create a list of values
print("\nYour report list is shown below:")
print(report_list)

# store details to an HTML file
fh = open("income_report.html", "w")
fh.write("<html>\n<head><title>Your Income Report</title></head>\n")
fh.write("<body>\n")
fh.write("<table border=1><tr><th>Description</th><th>Amount ($)</th></tr>")
fh.write("<tr><td>You have entered:</td><td>{:.2f}</td></tr>".format(netPay))
fh.write("\n<tr><td>Your tax rate is:</td><td>{:f}%</td></tr>".format((tax_rate(netPay) * 100)))
fh.write("\n<tr><td>Your taxable income is:</td><td>{:.2f}</td></tr>".format(taxableIncome))
fh.write("<tr><td>Amount after tax:</td><td>{:.2f}</td></tr></table>".format(amountAfterTax))
fh.write("</body>\n")
fh.write("</html>\n")
fh.close()
