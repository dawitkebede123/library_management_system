import frappe


def get_context(context):
    # Get current user and their roles
    current_user = frappe.session.user
    user_roles = frappe.get_roles()

    # Set context for current user
    context.members = frappe.get_list('Member', fields=['name','member_name', 'membership_id', 'email', 'phone_number'])
    context.user = current_user
    
