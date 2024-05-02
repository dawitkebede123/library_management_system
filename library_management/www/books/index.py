import frappe


def get_context(context):
    # Get current user and their roles
    current_user = frappe.session.user

    # Set context for current user
    context.books = frappe.get_list('Book', fields=['name', 'title', 'author', 'publication_date', 'isbn', 'available'])
    context.user = current_user
   
