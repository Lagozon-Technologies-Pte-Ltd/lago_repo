# **********************************************************************************************#
# File name: examples.py
# Created by: Krushna B.
# Creation Date: 25-Jun-2024
# Application Name: DBQUERY_NEW.AI
#
# Change Details:
# Version No:     Date:        Changed by     Changes Done         
# 01             25-Jun-2024   Krushna B.     Initial Creation
# 01             04-Jul-2024   Krushna B.     Added logic for data visualization 
# 01             15-Jul-2024   Krushna B.     Added more examples for the model to work more finely
# **********************************************************************************************#

examples = [
    {
        "input": "list all the employees",
        "query": "SELECT * FROM lz_employees"
    },
    {
        "input": "list all the doctors",
        "query": "SELECT * FROM lz_doctors"
    },
    {
        "input": "list all the nurses",
        "query": "SELECT * FROM lz_nurses"
    },
    {
        "input": "list all item transactions",
        "query": "SELECT * FROM lz_item_trx"
    },
    {
        "input": "count of doctors in each department",
        "query": "SELECT department_id, COUNT(*) as doctor_count FROM lz_doctors GROUP BY department_id"
    },
    {
        "input": "total number of customers",
        "query": "SELECT COUNT(*) as total_customers FROM lz_customers"
    },
    {
        "input": "average salary of employees",
        "query": "SELECT AVG(salary) as average_salary FROM lz_employees"
    },
    {
        "input": "total revenue from sales",
        "query": "SELECT SUM(total_amount) as total_revenue FROM lz_receipts"
    },
    {
        "input": "number of items in stock",
        "query": "SELECT SUM(onhand_quantity) AS total_items_in_stock FROM lz_item_onhand"
    },
    {
        "input": "number of radiology exams conducted in the last month",
        "query": "SELECT COUNT(*) as exams_last_month FROM lz_radiology_exams WHERE exam_date >= NOW() - INTERVAL '1 month'"
    },
    {
        "input": "List all invoices with their corresponding receipts",
        "query": "SELECT i.invoiceid, i.customerid, i.invoicedate, i.duedate, i.totalamount, r.receiptid, r.paymentamount FROM lz_invoices i LEFT JOIN lz_receipts r ON i.invoiceid = r.invoiceid"
    },
    {
        "input": "list of doctors by department",
        "query": "SELECT department_id, doctor_name FROM lz_doctors ORDER BY department_id, doctor_name"
    },
    {
        "input": "Get total amount invoiced and total amount paid for each customer",
        "query": "SELECT i.customerid, SUM(i.totalamount) AS total_amount_invoiced, COALESCE(SUM(r.paymentamount), 0) AS total_amount_paid FROM lz_invoices i LEFT JOIN lz_receipts r ON i.invoiceid = r.invoiceid GROUP BY i.customerid"
    },
    {
        "input": "List all receipts along with the corresponding invoice details",
        "query": """
            SELECT r.receipt_id, r.payment_amount, i.invoice_id, i.total_amount as invoice_amount
            FROM lz_receipts r
            JOIN lz_invoices i ON r.invoice_id = i.invoice_id
        """
    },
    {
        "input": "List all nurses along with their department names",
        "query": """
            SELECT n.nurse_id, n.nurse_name, d.department_name
            FROM lz_nurses n
            JOIN lz_departments d ON n.department_id = d.department_id
        """
    },
    {
        "input": "total revenue by customer",
        "query": "SELECT customerid, SUM(totalamount) AS total_revenue FROM lz_invoices GROUP BY customerid"
    },
    {
        "input": "list all the invoices in the second financial quarter of 2024",
        "query": "SELECT * FROM lz_invoices WHERE EXTRACT(QUARTER FROM invoicedate) = 2 AND EXTRACT(YEAR FROM invoicedate) = 2024"
    },
    {
        "input": "Find receipts without corresponding invoices",
        "query": "SELECT r.receiptid, r.invoiceid, r.receiptdate, r.paymentamount, r.paymentmethod, r.paymentreference, r.paymentstatus FROM lz_receipts r LEFT JOIN lz_invoices i ON r.invoiceid = i.invoiceid WHERE i.invoiceid IS NULL"
    },
    {
        "input": "total revenue by invoice date",
        "query": "SELECT invoicedate, SUM(totalamount) as total_revenue FROM lz_invoices GROUP BY invoicedate"
    },
    {
        "input": "Get total payment amount per payment method",
        "query": "SELECT paymentmethod, SUM(paymentamount) AS total_payment_amount FROM lz_receipts GROUP BY paymentmethod"
    },
    {
        "input": "Get orders with expected delivery date in the next 7 days",
        "query": "SELECT * FROM lz_sales_order WHERE expecteddeliverydate BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days"
    },
    {
        "input": "Get total orders per customer",
        "query": "SELECT customerid, COUNT(*) AS total_orders FROM lz_sales_order GROUP BY customerid"
    },
    {
    "input": "Get sales orders with notes containing specific keywords",
    "query": "SELECT SalesOrderID, SalesOrderNumber, OrderNotes FROM lz_sales_order WHERE OrderNotes LIKE '%keyword%' ORDER BY OrderDate DESC"
    },
    {
    "input": "Get total number of orders for each shipping method",
    "query": "SELECT sm.ShippingMethod, COUNT(so.SalesOrderID) AS total_orders FROM lz_sales_order so JOIN lz_shipping_methods sm ON so.ShippingMethodID = sm.ShippingMethodID GROUP BY sm.ShippingMethod ORDER BY total_orders DESC"
    },
    {
    "input": "List all sales orders with their payment methods",
    "query": "SELECT so.SalesOrderID, so.SalesOrderNumber, pm.PaymentMethod FROM lz_sales_order so JOIN lz_payment_methods pm ON so.PaymentMethodID = pm.PaymentMethodID"
    },
    {
    "input": "Get the average number of days between order date and expected delivery date",
    "query": "SELECT AVG(ExpectedDeliveryDate - OrderDate) AS avg_delivery_time FROM lz_sales_order"
    },
    {
    "input": "Get the number of orders per order status",
    "query": "SELECT OrderStatus, COUNT(*) AS total_orders FROM lz_sales_order GROUP BY OrderStatus ORDER BY total_orders DESC"
    },
    {
    "input": "Get sales order details along with customer details",
    "query": "SELECT so.SalesOrderID, so.SalesOrderNumber, so.OrderDate, c.firstname, c.lastname, c.email FROM lz_sales_order so JOIN lz_customers c ON so.CustomerID = c.customerid"
},
    {
    "input": "Get sales orders with their corresponding shipping methods",
    "query": "SELECT so.SalesOrderID, so.SalesOrderNumber, sm.ShippingMethod FROM lz_sales_order so JOIN lz_shipping_methods sm ON so.ShippingMethodID = sm.ShippingMethodID"
}
]

#Added by Aruna
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings
import streamlit as st

@st.cache_resource
def get_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        OpenAIEmbeddings(),
        Chroma,
        k=2,
        input_keys=["input"],
    )
    return example_selector