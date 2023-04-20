# NLPtoSQL

NLP to SQL Sales Data App
This application is designed to convert natural language queries into SQL queries and fetch desired results from a sales data CSV file using the OpenAI Davinci API.

Features
Converts natural language queries into SQL queries
Fetches desired results from a sales data CSV file
User-friendly interface
Prerequisites
Python 3.6 or higher
OpenAI API key
CSV file containing sales data
Installation
Clone the repository
Install the required packages by running pip install -r requirements.txt
Set up the OpenAI API key by creating a new file called .env and adding the following line:
javascript
Copy code
OPENAI_API_KEY=<your API key here>
Replace the sales_data.csv file in the data folder with your own sales data CSV file
Usage
Run the app.py file using the command python app.py
Enter your natural language query in the input field and press enter
The application will convert the query into an SQL query and fetch the desired results from the sales data CSV file
The results will be displayed in the output field
Examples
"What was the total revenue in January 2022?"
"What were the top selling products in Q3 2021?"
"How many orders were placed by customer John Doe?"
License
This project is licensed under the MIT License.
