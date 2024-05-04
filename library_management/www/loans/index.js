function initModal(docName='') {
  if (docName) {
    // Load document to be updated
    frappe.call({
      method: 'frappe.client.get',
      args: {
        doctype: 'Loan',
        name: docName
      },
      callback: function(response) {
        if (response.message) {
          const loan = response.message;
          document.getElementById("formModalLabel").innerText = "Update Loan";
          const submitButton = document.getElementById("submitButton");
          submitButton.innerText = "Update Loan";
          submitButton.onclick = updateDoc;

          // Populate the form fields with book details
          document.getElementById("docName").value = loan.name;
          document.getElementById("member").value = loan.member;
          document.getElementById("book").value = loan.book;
          document.getElementById("loan_date").value = loan.loan_date;
          document.getElementById("return_date").value = loan.return_date;

        } else {
          console.error('Loan not found');
        }
      },
      error: function(err) {
        console.error(err);
      }
    });
  } else {
    // Display an empty form for adding a new document
    document.getElementById("formModalLabel").innerText = "Add a new Loan";
    const submitButton = document.getElementById("submitButton");
    submitButton.innerText = "Add Loan";
    submitButton.onclick = addDoc;

    // Reset the form fields in case they have been populated from a previous update command
    document.getElementById("docName").value = '';
    document.getElementById("member").value = '';
    document.getElementById("book").value = '';
    document.getElementById("loan_date").value = '';
    document.getElementById("return_date").value = '';
  }
}
  function addDoc() {
    const member = document.getElementById('member').value;
    const book = document.getElementById('book').value;
    const loan_date = document.getElementById('loan_date').value;
    const return_date = document.getElementById('return_date').value;
    console.log(docName)
  
    const loanData = {
      member:member,
      book:book,
      loan_date: loan_date,
      return_date:return_date,
    };
  
    frappe.call({
      method: 'library_management.api.api_loan.create_loan',
      args:{loan_data:loanData,
      
    },
      callback: (response) => {
        window.location.reload(true);
        console.log('Document Added successfully:', response);
        // Optional: Display success message to user (e.g., modal dialog)
        // You can potentially avoid reloading the entire page 
        // by fetching and displaying updated data if needed
      },
      error: (error) => {
        console.error('Error adding loan:', error);
        // Handle errors appropriately (e.g., display user-friendly message)
      }
    });
  }
  

// Function to delete a doc
function deleteDoc() {
  const docName = document.getElementById("docName").value;
  console.log(docName)
  frappe.call({
    method: 'library_management.api.api_loan.delete_loan',
    args: {
      loan_name: docName,
    },
    callback: () => {
      console.log('Document deleted successfully');
      window.location.reload(true);
    },
    error: (r) => {
      console.error(r);
    }
  })
}
// function updateDoc(member, bookData) {
//   frappe.call({
//     method: 'library_management.api.api_book.update_book',
//     args: {
//       member: member,
//       update_data: bookData
//     },
//     callback: (r) => {
//       window.location.reload(true);
//     },
//     error: (r) => {
//       console.error(r);
//     }
//   })
// }

// Function to update the document
function updateDoc() {
    // Prepare update data to be sent as payload in PUT request
    const docName = document.getElementById("docName").value;
    const docData = {};
    docData['member'] = document.getElementById('member').value;
    docData['book'] = document.getElementById('book').value;
    docData['loan_date'] = document.getElementById('loan_date').value;
    docData['return_date'] = document.getElementById('return_date').value;
    console.log(docName)
    console.log(docData)
      updateDocInBackend(docName, docData);
    }
  




// // // Function to update a document in the Frappe backend
function updateDocInBackend(docName, docData) {
  frappe.call({
    method: 'library_management.api.api_loan.update_loan',
    args: {
      loan_name: docName,
      update_data: docData
    },
    callback: (r) => {
      window.location.reload(true);
      console.log(r)
    },
    error: (r) => {
      console.error(r);
    }
  })
}

