# Copyright (c) 2024, dawit woldu and contributors
# For license information, please see license.txt

import frappe
import re
from frappe.model.document import Document
from frappe import _
from datetime import date

class Book(Document):
  def __init__(self, *args, **kwargs):
    super(Book, self).__init__(*args, **kwargs)

  def validate(self):
    """
    This function validates the Book DocType on save.

    Args:
        self (frappe.DocType): The Book DocType document.
    """

    if not self.isbn or not self.validate_isbn():
      frappe.throw(_("Invalid ISBN number. Please enter a valid ISBN-10 or ISBN-13."))
    if not self.publish_date or not self.validate_publish_date():
      frappe.throw("Incorrect publish date")
  
  
  def validate_isbn(self):

    """
  This function checks the validity of an ISBN number based on its size.

  Args:
      isbn (str): The ISBN number to validate.

  Returns:
      bool: True if the ISBN size is valid (10 or 13), False otherwise.
  """

    if not self.isbn:
      return False  # Empty ISBN is invalid

    isbn_length = len(self.isbn.replace("-", ""))  # Remove hyphens for size check

    return isbn_length in (10, 13)

  
  
  def validate_publish_date(self):
    # Get today's date
   publish_date = date.fromisoformat(self.publish_date) 
   today = date.today()

  # Check if publish date is before today
   return publish_date <= today  
  
  
  
  # CRUD operations
  @frappe.whitelist()
  def on_delete(self):
    frappe.msgprint('deleted')
  def create_book(self, title, author, isbn, published_date):
    """
    This function creates a new Book DocType record.

    Args:
        self (frappe.DocType): The Book DocType document.
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book.
        published_date (str): The publication date of the book.
    """

    self.title = title
    self.author = author
    self.isbn = isbn
    self.published_date = published_date
    self.save()  # Save the new book record

  def get_book(self, book_name):
    """
    This function retrieves a Book DocType record by name.

    Args:
        self (frappe.DocType): The Book DocType document.
        book_name (str): The name of the book to retrieve.

    Returns:
        frappe.Doc: The Book DocType record if found, None otherwise.
    """

    return frappe.get_doc("Book", book_name)

  def update_book(self, book_id, title, author, isbn, published_date):
    """
    This function updates an existing Book DocType record.

    Args:
        self (frappe.DocType): The Book DocType document.
        book_id (str): The ID of the book record to update.
        title (str): The updated title of the book.
        author (str): The updated author of the book.
        isbn (str): The updated ISBN number of the book.
        published_date (str): The updated publication date of the book.
    """

    book = frappe.get_doc("Book", book_id)
    book.title = title
    book.author = author
    book.isbn = isbn
    book.published_date = published_date
    book.save()  # Save the updated book record

  def delete_book(self, book_id):
    """
    This function deletes an existing Book DocType record.

    Args:
        self (frappe.DocType): The Book DocType document.
        book_id (str): The ID of the book record to

#  def validate_isbn(isbn):
#   """
#   This function validates the ISBN field of a Book DocType in Frappe.

#   Args:
#       isbn (str): The ISBN number to validate.

#   Returns:
#       bool: True if the ISBN is valid, False otherwise.
#   """

#   # ISBN-10 or ISBN-13 (with or without hyphens)
#   pattern = r"(?i)^ISBN (?P<prefix>(?:1[0]{3})|(?:97[89]))(?:[- ])?(?P<group>\d{1,5})[- ]?(?P<publisher>\d{1})[- ]?(?P<check_digit>\d{1})$"

#   if not isbn:
#     return False  # Empty ISBN is invalid

#   match = re.match(pattern, isbn)
#   if not match:
#     return False  # Does not match the ISBN pattern

#   # Calculate the check digit (applicable for ISBN-10 only)
#   if match.group('prefix') == '10':
#     check_sum = 0
#     for i, digit in enumerate(match.group('group') + match.group('publisher')):
#       check_sum += int(digit) * (10 - i)
#     check_sum %= 11

#     if str(check_sum) != match.group('check_digit'):
#       return False  # Check digit doesn't match calculated value

#   return True

#  def validate_book_doc(self):
#   """
#   This function validates the ISBN field of a Book DocType on DocType save.

#   Args:
#       doc (frappe.DocType): The Book DocType document.
#   """

#   if not self.isbn or not self.validate_isbn(self.isbn):
#     frappe.throw(_("Invalid ISBN number. Please enter a valid ISBN-10 or ISBN-13."))

# # Hook the validate_book_doc function on DocType save event
#  frappe.doctype.on("Book", "validate", validate_book_doc)