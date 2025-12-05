# [Personal Finance Manager]

[ALI RAZA]

## Description

[This project develops a simple web-based Personal Finance Manager using Python and Flask,
combined with an SQLite database for data persistence.
The application allows users to manage their financial transactions through a user-friendly web interface.
Users can add financial transactions with details such as date, category, description, and amount.
The application provides functionality to view all transactions and a balance summary, which includes total income, expenses, and the current balance.
Functioning entirely server-side, the application ensures that all interactions and calculations are processed directly on the server, 
minimizing the need for client-side enhancing. 
This setup ensures that the application can run efficiently and reliably for personal use.
Transactions can be added through a simple form submission, and users can view their transaction history or financial summaries at the click of a button.]

## How to test


[Initial Setup:
Before testing the application, ensure that Python and Flask are installed on your system, you can do so using pip install flask.
Running the Application, Start the Flask Server:
Open your terminal, navigate to the directory containing project files, and run the following command to start the Flask application: 
"python app.py" / "python project4.py"
This command will start the Flask server, typically accessible via the URL http://127.0.0.1:5000/. 
NOTE: In the code, the HMTL file is called through the template folder which is in the same directory as the main file, project4.py.

Using the Application
Adding Transactions:
On the main page (http://127.0.0.1:5000/), you'll see a form under the "Add Transaction" section.
Fill in the fields:
Category: Type of the transaction (e.g., Income, Expense).
Description: Brief description of the transaction (e.g., Salary, Rent, etc. ).

Amount: Transaction amount (NOTE: use a positive value for income and negative for expenses).
Click the Add Transaction button to submit the form.
All previous transactions are viewed on the main page, showing the date, category, description, and amount of each transaction.

Checking Balance Summary:
The summary will be displayed at the bottom with total income, total expenses, and the current balance (Values rounded to 2 decimal place),
these values change with each added transaction. ]


## Personal contribution


[This project is very much inspired from personal insights in finance with little help from outside sources. 
The use of SQL and SQLite is added for data reliability. 
Where you import sqlite module and use the "conn" object to interact with the database. However, I used a function,
to initialize the database with similar sql syntax. And a different function that connects to the database. 
The function get_db_connection(): This function sets up a connection to the SQLite database and row_factory = sqlite3.Row makes the row objects accessible by column name.
And setup_db() ensures the necessary table for storing transactions exists. This function is called before the app starts serving requests, to prepare the database.

To call the html file for webpage display using @app.route('/'). 
The route decorator efines the URL endpoint and supported methods (GET for displaying the page, POST for submitting the form).
Depending on the HTTP method, it either inserts a new transaction into the database (POST) or fetches existing transactions and balance summaries (GET).
Redirect: After a POST request, it redirects to the same page to prevent form resubmission issues and to update the display with the new data.
Render Template: The fetched transactions and summaries are passed to the template for rendering. 

I have utilized commands from sequel query to display all transaction in the database using fetchall() in the following functions.
The get balance summary function calculates the total income, expenses, and net balance from the transactions stored in the database.

Finally, if __name__ == '__main__': app.run(debug=True), ensures that when the Flask application is run directly,
it performs the necessary initial database setup and starts the server with development-friendly settings, 
including debug mode for easier troubleshooting and live updates during code changes.

The Final component is the HMTL file, the layout is pretty easy, initially setting up the window name with proper format and style in the <head>.
Next is the <body> with first hearder Personal Finance Manager, followed by Add Transaction. Under the Add transaction are three labels, two text entry box and a number entry. 
Next to the entries is a button that utilizes the "transactionform" form

Under that is another header, Transactions which shows all transaction made with proper date time formats.
Lastly, the Balance Summary header which displays total income, total expenses and final balance, all values are rounded to two decimal places. ]


## Sources and credits


[ Online Documentation and Tutorials
Flask Documentation: 

W3Schools:
Citations: URL: W3Schools HTML Forms (https://www.w3schools.com/html/html_forms.asp)
Contribution: Used to reference HTML form creation and handling input types, and rounding numbers, which were essential for the project's user interface design.

Contribution: Caroline Dublin, helped approve the topic, aided with testing the code and make appropriate changes.

General Contribution: Reviewed multiple open-source projects related to finance management tools. Code Examples and Snippets.
These reviews helped understand common architectural patterns and user interface designs. ]





