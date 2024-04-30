// Copyright (c) 2024, dawit woldu and contributors
// For license information, please see license.txt
frappe.ui.form.on("Loan", "refresh", function(frm) {
    const formattedDate = getFormattedDate(); // Call the function from above
    frm.set_value("loan_date", formattedDate);
  });
  function getFormattedDate() {
    const today = new Date();
    const dd = String(today.getDate()).padStart(2, '0');
    const mm = String(today.getMonth() + 1).padStart(2, '0'); // Month is zero-indexed
    const yyyy = today.getFullYear();
  
    const formattedDate = dd + '-' + mm + '-' + yyyy;
    return formattedDate;
  }
  
// frappe.ui.form.on("Loan", {
// 	refresh(frm) {

// 	},
// });
