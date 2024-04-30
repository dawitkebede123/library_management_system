### Library Management

App to manage library - contain custom api and build using frappe.

### Installation

Make sure *Bench* is installed on your machine. If you haven't installed Bench, follow the official [installation guide](https://frappeframework.com/docs/user/en/installation) to install Bench in development mode.

- Initialize the Frappe bench

  ```bash
  bench init [bench-folder-name]
  ```

- Go to the newly created bench directory

  ```bash
  cd [bench-folder-name]
  ```

- Create a new site

  ```bash
  bench new-site [site-name]
  ```

- Download and add this app to the bench

  ```bash
  bench get-app https://github.com/dawitkebede123/library_management_system
  ```

- Install this app on your newly created site

  ```bash
  bench --site [site-name] install-app [app-name]
  ```

- Add the site to hosts

  ```bash
  bench --site [site-name] add-to-hosts
  ```

- Start the development server
  
  ```bash
  bench start
  ```
- go to http://[site-name]:[port-number]

## Features

- Book Management:
  - [x] The Book DocType has the fields: Title, Author, Publish Date and ISBN.
  - [x] CRUD operations available via custom API.
  - [x] Validation has been implemented to verify correct ISBN and Publish Date.
- Membership Management:
  - [x] The Member DocType has the fields: Name, Membership ID, Email and Phone     Number.
  - [x] CRUD operations available via custom API.
  - [x] custom Validation has been implemented to verify correct email address and frappe app validation for phone number.
- Loan Management:
  - [x] The Loan DocType tracks book loans and has the fields: Member, Book, Loan Date and Return Date.
  - [x] custom Validation has been implemented to verify loan and return date
- User Interface:
  - [x] landing workspace as a home page contain shorcuts to DocTypes and report in inside a card display/
  - [x] use frappe desk forms for data entry and tables to display.
  - [x] Validation has been implemented on forms.
- Reports:
  - [x] Create a report for all currently loaned books
  - [x] Generate a report for overdue books

### Custom API 
| Endpoint | Purpose |
|----------|---------|
|api/method/library_management.api.api_book.get_books/ | return all members|

|api/method/library_management.api.api_book.get_book/ |return a single book|

|api/method/library_management.api.api_book.create_book/  | create new book|

|api/method/library_management.api.api_book.update_book/ | update book record|

|api/method/library_management.api.api_book.delete_book/ | delete book |
### member manamgement 
|api/method/library_management.api.api_member.get_members/ |  return all members|

|api/method/library_management.api.api_member.get_member/  | return a single member|

|api/method/library_management.api.api_member.create_member/ | create new member|

|api/method/library_management.api.api_member.update_member/ | update member record|

|api/method/library_management.api.api_member.delete_member/ | delete member|

### loan manamgement 
|api/method/library_management.api.api_loan.get_loans/  | return all loan records|

|api/method/library_management.api.api_loan.get_loan_By_Book/  | return a loan record of book|

|api/method/library_management.api.api_loan.get_loan_By_member/ |  return a loan record of a member|

|api/method/library_management.api.api_loan.create_loan/ | create new loan|

|api/method/library_management.api.api_loan.update_loan/ | update loan record|

|api/method/library_management.api.api_loan.delete_loan/ | delete loan|
### License

mit
