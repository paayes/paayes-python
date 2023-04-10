import paayes
# paayes.api_key = "sk_test_UiiMzY3NDE3Mzg3NDc0MDIzMjQsKEq00Eq01Uii58082"
paayes.api_key = "MTQzMzQ1OTcxODU0MzY3MzYsKEq00Eq01UiisKa0A0UiiMTkwNzgwMTQ1OTM5NDcxNDksKEq00Eq01Uii56517"

customer = paayes.Customer.create(email="python_test@paayes.com", balance=0, invoice_prefix="825ADB9", name="Python Test Client", description="Python Test Client", tax_exempt="none")
print(customer)
