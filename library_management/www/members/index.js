function initModal(docName='') {
  if (docName) {
    // Load document to be updated
    frappe.call({
      method: 'frappe.client.get',
      args: {
        doctype: 'Member',
        name: docName
      },
      callback: function(response) {
        if (response.message) {
          const member = response.message;
          document.getElementById("formModalLabel").innerText = "Update member";
          const submitButton = document.getElementById("submitButton");
          submitButton.innerText = "Update member";
          submitButton.onclick = updateDoc;

          // Populate the form fields with member details
          document.getElementById("docName").value = member.name;
          document.getElementById("member_name").value = member.member_name;
          document.getElementById("membership_id").value = member.membership_id;
          document.getElementById("email").value = member.email;
          document.getElementById("phone_number").value = member.phone_number;

        } else {
          console.error('member not found');
        }
      },
      error: function(err) {
        console.error(err);
      }
    });
  } else {
    // Display an empty form for adding a new document
    document.getElementById("formModalLabel").innerText = "Add a new member";
    const submitButton = document.getElementById("submitButton");
    submitButton.innerText = "Add member";
    submitButton.onclick = addDoc;

    // Reset the form fields in case they have been populated from a previous update command
    document.getElementById("docName").value = '';
    document.getElementById("member_name").value = '';
    document.getElementById("membership_id").value = '';
    document.getElementById("email").value = '';
    document.getElementById("phone_number").value = '';
  }
}
  function addDoc() {
    const member_name = document.getElementById('member_name').value;
    const membership_id = document.getElementById('membership_id').value;
    const phone_number = document.getElementById('phone_number').value;
    const email = document.getElementById('email').value;
    console.log(docName)
  
    const member_data = {
      member_name:member_name,
      membership_id:membership_id,
      phone_number: phone_number,
      email:email,
    };
  
    frappe.call({
      method: 'library_management.api.api_member.create_member',
      args:{member_data:member_data,
      
    },
      callback: (response) => {
        window.location.reload(true);
        console.log('Document Added successfully:', response);
        // Optional: Display success message to user (e.g., modal dialog)
        // You can potentially avoid reloading the entire page 
        // by fetching and displaying updated data if needed
      },
      error: (error) => {
        console.error('Error adding member:', error);
        // Handle errors appropriately (e.g., display user-friendly message)
      }
    });
  }
  

// Function to delete a doc
function deleteDoc() {
  const docName = document.getElementById("docName").value;
  console.log(docName)
  frappe.call({
    method: 'library_management.api.api_member.delete_member',
    args: {
      member_name: docName,
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
// function updateDoc(member_name, memberData) {
//   frappe.call({
//     method: 'library_management.api.api_member.update_member',
//     args: {
//       member_name: member_name,
//       update_data: memberData
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
    docData['member_name'] = document.getElementById('member_name').value;
    docData['membership_id'] = document.getElementById('membership_id').value;
    docData['phone_number'] = document.getElementById('phone_number').value;
    docData['email'] = document.getElementById('email').value;
    console.log(docName)
    console.log(docData)
      updateDocInBackend(docName, docData);
    }
  




// // // Function to update a document in the Frappe backend
function updateDocInBackend(docName, docData) {
  frappe.call({
    method: 'library_management.api.api_member.update_member',
    args: {
      member_name: docName,
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

