import frappe
import json


@frappe.whitelist()
def get_books():
    '''
    Fetch a list of books with details.

    This method only accepts authenticated requests.

    Returns:
    A list of dictionaries containing book details, including 'name', 'title', 'author',
    'genre', 'publication_year', 'isbn', 'status', and 'image'.
    '''
    # Authenticate request
    if frappe.session.user == 'Guest':
        frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

    return frappe.get_all('Book', fields=['name', 'title', 'author', 'publish_date', 'isbn', 'available',])

@frappe.whitelist()
def get_single_book(name=None):
  """
  This function retrieves a single book based on the provided book name.

  Args:
      member (str, optional): Name of the member (linked DocType field). Defaults to None.
      book (str, optional): Name of the book (linked DocType field). Defaults to None.

  Returns:
      dict or None: A dictionary containing the loan details if found, otherwise None.
  """

  if  not name:
    # Raise an exception if neither member nor book is provided
    raise ValueError("book name must be provided.")

  try:
    # Attempt to get the loan using `frappe.get_doc`
    book = frappe.get_doc("Book", {"name":name}).as_dict()
  except frappe.DoesNotExistError:
    # Handle case where no loan is found
    return None
  else:
    # Return the loan details as a dictionary
    return {
        'title': book['title'],
        'author': book['author'],
        'publish_date': book['publish_date'],
        'isbn': book['isbn'],
    }
  
@frappe.whitelist()
def create_book(book_data):
  """
  Create a new Book document with the provided data.

  This method only accepts authenticated requests (consider enabling).

  Parameters:
      book_data: A dictionary containing data for the new book, including 'title', 'author',
                 'publish_year', 'isbn', 'available'.

  Returns:
      The name of the newly created Book document.
  """

  # authentication
  if frappe.session.user == 'Guest':
      frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

  # Convert book_data to dictionary if string type
  book_data = json.loads(book_data) if type(book_data) is str else book_data

  # Create the Book document with allowed attributes
  new_doc = frappe.get_doc({
      "doctype": "Book",
      "title": book_data.get("title"),
      "author": book_data.get("author"),
      "publish_date": book_data.get("publish_date"),
      "isbn": book_data.get("isbn"),
      "available": book_data.get("available"),
  })

  # Validate and save the document
  new_doc.validate()  # Enforces Frappe validations
  new_doc.save()

  return new_doc.name


@frappe.whitelist()
def get_book(book_name):
    '''
    Fetch details of a specific Book.

    This method only accepts authenticated requests.

    Parameters:
    - book_name: The name of the Book document to retrieve.

    Returns:
    A dictionary containing details of the specified book, including 'name', 'title', 'author',
    'genre', 'publication_year', 'isbn', 'status', and 'image'.
    '''
    # Authenticate request
    if frappe.session.user == 'Guest':
        frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

    book = frappe.get_doc('Book', book_name).as_dict()
    return {
        'name': book['name'],
        'title': book['title'],
        'author': book['author'],
        'publish_date': book['publish_date'],
        'isbn': book['isbn'],
        'available': book['available'],
    }

@frappe.whitelist()
def update_book(book_name, update_data):
    '''
    Update details of a specific Book.

    This method only accepts authenticated requests.

    Parameters:
    - book_name: The name of the Book document to update.
    - update_data: A dictionary containing the fields to update and their new values.

    Returns:
    The name of the updated Book document.
    '''
    # Authenticate request
    if frappe.session.user == 'Guest':
        frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

    doc = frappe.get_doc('Book', book_name)
    update_data = json.loads(update_data) if type(update_data) is str else update_data # If update_data is string, convert to dict
    doc.update(update_data)
    doc.save()
    return doc.name

@frappe.whitelist()
def delete_book(book_name):
    '''
    Delete a specific Book.

    This method only accepts authenticated requests.

    Parameters:
    - book_name: The name of the Book document to delete.
    '''
    # Authenticate request
    if frappe.session.user == 'Guest':
        frappe.throw(frappe._('Error: Unauthenticated request'), frappe.AuthenticationError)

    frappe.delete_doc('Book', book_name)
