function initModal(docName='') {
  if (docName) {
    // Load document to be updated
    frappe.call({
      method: 'frappe.client.get',
      args: {
        doctype: 'Book',
        name: docName
      },
      callback: function(response) {
        if (response.message) {
          const book = response.message;
          document.getElementById("formModalLabel").innerText = "Update Book";
          const submitButton = document.getElementById("submitButton");
          submitButton.innerText = "Update Book";
          submitButton.onclick = updateDoc;

          // Populate the form fields with book details
          document.getElementById("docName").value = book.name;
          document.getElementById("title").value = book.title;
          document.getElementById("author").value = book.author;
          document.getElementById("isbn").value = book.isbn;
          document.getElementById("publish_date").value = book.publish_date;
          document.getElementById("available").value = book.available;

        } else {
          console.error('Book not found');
        }
      },
      error: function(err) {
        console.error(err);
      }
    });
  } else {
    // Display an empty form for adding a new document
    document.getElementById("formModalLabel").innerText = "Add a new Book";
    const submitButton = document.getElementById("submitButton");
    submitButton.innerText = "Add Book";
    submitButton.onclick = addDoc;

    // Reset the form fields in case they have been populated from a previous update command
    document.getElementById("docName").value = '';
    document.getElementById("title").value = '';
    document.getElementById("author").value = '';
    document.getElementById("isbn").value = '';
    document.getElementById("publish_date").value = '';
    document.getElementById("available").value = '';
  }
}
  function addDoc() {
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const publishDate = document.getElementById('publish_date').value;
    const isbn = document.getElementById('isbn').value;
    const available = document.getElementById('available').value;
    console.log(docName)
  
    const bookData = {
      title:title,
      author:author,
      publish_date: publishDate,
      isbn:isbn,
      available: available, // Convert 'true'/'false' strings to boolean
    };
  
    frappe.call({
      method: 'library_management.api.api_book.create_book',
      args:{book_data:bookData,
      
    },
      callback: (response) => {
        window.location.reload(true);
        console.log('Document Added successfully:', response);
        // Optional: Display success message to user (e.g., modal dialog)
        // You can potentially avoid reloading the entire page 
        // by fetching and displaying updated data if needed
      },
      error: (error) => {
        console.error('Error adding book:', error);
        // Handle errors appropriately (e.g., display user-friendly message)
      }
    });
  }
  

// Function to delete a doc
function deleteDoc() {
  const docName = document.getElementById("docName").value;
  console.log(docName)
  frappe.call({
    method: 'library_management.api.api_book.delete_book',
    args: {
      book_name: docName,
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
// function updateDoc(title, bookData) {
//   frappe.call({
//     method: 'library_management.api.api_book.update_book',
//     args: {
//       title: title,
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
    docData['title'] = document.getElementById('title').value;
    docData['author'] = document.getElementById('author').value;
    docData['publish_date'] = document.getElementById('publish_date').value;
    docData['isbn'] = document.getElementById('isbn').value;
    docData['available'] = document.getElementById('available').value;
    console.log(docName)
    console.log(docData)
      updateDocInBackend(docName, docData);
    }
  




// // // Function to update a document in the Frappe backend
function updateDocInBackend(docName, docData) {
  frappe.call({
    method: 'library_management.api.api_book.update_book',
    args: {
      book_name: docName,
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

