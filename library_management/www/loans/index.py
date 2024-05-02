import frappe


def get_context(context):
    # Get current user and their roles
    current_user = frappe.session.user
    user_roles = frappe.get_roles()

    # Set context for current user
    context.loans = frappe.get_list('Loan', fields=['member', 'book', 'loan_date','return_date'])
    context.books = frappe.get_list('Book', fields=['title'])
    context.members = frappe.get_list('Member', fields=['name'])
    context.user = current_user