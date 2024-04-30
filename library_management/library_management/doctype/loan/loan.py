# Copyright (c) 2024, dawit woldu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from datetime import date

class Loan(Document):
 
 def validate(self):
   self.validate_loan_book()
  #  self.validate_Return_date()
 
 
 def validate_loan_book(self):
  """
  This function checks if a book is available for loan and exists in the system.

  Args:
      book_name (str): The name of the book to check.

  Returns:
      bool: True if the book is available and exists, False otherwise.
  """

  book = frappe.get_doc("Book", self.book)
  if not book:
    frappe.throw(_("Book not found!"))

  # Check if book exists and availability is "Available"
  if book.get("available") != "Available":
    frappe.throw(_("Book is not available for loan! Please try a different book."))
  # change availability of the book

  frappe.db.set_value("Book", self.book, "available", "Issued")
  return True
 

#  def validate_Return_date(self):
#     # Get today's date
#    return_date = date.fromisoformat(self.return_date) 
#    today = date.today()

#   # Check if return date is after today
#    if(return_date <= today):
#      frappe.throw(_("incorrect return date"))
     
   

