import csv
from fpdf import FPDF

#Read data
with open("sales_data.csv") as file:
    reader = csv.DictReader(file)
    data = []
    for row in reader:
        row['Quantity'] = int(row['Quantity'])
        row['Price'] = float(row['Price'])
        row['Total'] = row['Quantity'] * row['Price']
        data.append(row)

#Analyze data
total_sales = sum(item['Total'] for item in data)
product_sales = {}
for item in data:
    product = item['Product']
    product_sales[product] = product_sales.get(product, 0) + item['Total']

#Generate PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "CODTECH - Sales Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Total Sales: Rs. {total_sales:.2f}", ln=True)
pdf.ln(5)

pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Product-wise Sales:", ln=True)
pdf.set_font("Arial", size=12)
for product, total in product_sales.items():
    pdf.cell(200, 10, f"{product}: Rs. {total:.2f}", ln=True)

pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Detailed Transactions:", ln=True)
pdf.set_font("Arial", size=10)
for item in data:
    line = f"{item['Date']} - {item['Product']} - Qty: {item['Quantity']} - Rs. {item['Total']:.2f}"
    pdf.cell(200, 10, line, ln=True)

pdf.output("sales_report.pdf")
print(" PDF report generated successfully.")
