import frappe
import json


@frappe.whitelist()
def get_members():
    '''
    Fetch a list of members with details.

    This method only accepts authenticated requests.

    Returns:
    A list of dictionaries containing member details, including 'name', 'full_name',
    'membership_id', 'email', 'phone_number', and 'image'.
    '''
    # Authenticate request
    if frappe.session.user == 'Guest':
        frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

    return frappe.get_all('Member', fields=['name', 'membership_id', 'email', 'phone_number'])

@frappe.whitelist()
def get_single_member(name=None):

  if  not name:
    # Raise an exception if neither member nor book is provided
    raise ValueError("member name must be provided.")

  try:
    # Attempt to get the loan using `frappe.get_doc`
    member = frappe.get_doc("Member", {"member_name":name}).as_dict()
  except frappe.DoesNotExistError:
    # Handle case where no loan is found
    return None
  else:
    # Return the loan details as a dictionary
    return {
        'name': member['member_name'],
        'membership_id': member['membership_id'],
        'email': member['email'],
        'phone_number': member['phone_number'],
    }
  

@frappe.whitelist()
def create_member(member_data):
 

  # authentication
  if frappe.session.user == 'Guest':
      frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

  # Convert book_data to dictionary if string type
  member_data = json.loads(member_data) if type(member_data) is str else member_data

  # Create the member document with allowed attributes
  new_doc = frappe.get_doc({
      "doctype": "Member",
      "member_name": member_data.get("name"),
      "membership_id": member_data.get("membership_id"),
      "email": member_data.get("email"),
      "phone_number": member_data.get("phone_number"),
  })

  # Validate and save the document
  new_doc.validate()  # Enforces Frappe validations
  new_doc.save()

  return True


@frappe.whitelist()
def get_member(member_name):
    '''
    Fetch details of a specific Member.

    This method only accepts authenticated requests.

    Parameters:
    - member_name: The name of the Member document to retrieve.

    Returns:
    A dictionary containing details of the specified member, including 'name',
    'membership_id', 'email', 'phone_number'.
    '''
    # Authenticate request
    if frappe.session.user == 'Guest':
        frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

    member = frappe.get_doc('Member', member_name).as_dict()
    return {
        'name': member['name'],
        'membership_id': member['membership_id'],
        'email': member['email'],
        'phone_number': member['phone_number'],
    }

@frappe.whitelist()
def update_member(member_name, update_data):
    '''
    Update details of a specific Member.

    This method only accepts authenticated requests.

    Parameters:
    - member_name: The name of the Member document to update.
    - update_data: A dictionary containing the fields to update and their new values.

    Returns:
    The name of the updated Member document.
    '''
    # Authenticate request
    if frappe.session.user == 'Guest':
        frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

    doc = frappe.get_doc('Member', member_name)
    update_data = json.loads(update_data) if type(update_data) is str else update_data # If update_data is string, convert to dict
    doc.update(update_data)
    doc.save()
    return doc.name

@frappe.whitelist()
def delete_member(member_name):
    '''
    Delete a specific Member.

    This method only accepts authenticated requests.

    Parameters:
    - member_name: The name of the Member document to delete.
    '''
    # Authenticate request
    if frappe.session.user == 'Guest':
        frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

    frappe.delete_doc('Member', member_name)
