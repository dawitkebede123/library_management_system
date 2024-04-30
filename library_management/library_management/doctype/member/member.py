# Copyright (c) 2024, dawit woldu and contributors
# For license information, please see license.txt

import frappe
import re
from frappe.model.document import Document
from frappe import _

class Member(Document):
  
  def validate(self):
     if not self.email or not self.validate_email():
      frappe.throw(_("Invalid email"))
     
  def validate_email(self):
     """
    This function checks if a string is a valid email address format.

    Args:
      email (str): The email address to validate.

    Returns:
      bool: True if the email format is valid, False otherwise.
    """

    # Regular expression for email validation
     regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$"
     return bool(re.match(regex, self.email))
