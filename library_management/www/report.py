import frappe
from datetime import date

def get_context(context):
    # Get current user and their roles (optional)
    current_user = frappe.session.user
    user_roles = frappe.get_roles()

    # Fetch loan data
    loans = frappe.get_list("Loan", fields=["member", "book", "loan_date","return_date"])

    # Filter loans based on overdue status (return_date < today's date)
    overdue_loans = [loan for loan in loans if  date.fromisoformat(str(loan.return_date)) < date.today()]

    # Set context with filtered overdue loans
    context.loan = overdue_loans
    context.user = current_user  # Assuming you need user information

    # Return the updated context (optional)
    return context
