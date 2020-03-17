This is a proof of concept for a controlled data update mechanism in production.

# Problem Statement
Any production support team has to perform multiple database update. Database update is problematic. Lack of control can result in wiping off the data. However putting controls could mean delay in addressing the issue.

# DataUpdate
DataUpdate is a web-based application to control the data fixes in production database.

# Components

Web Component: Angular based web component. The web interface provides a way for a user to submit a query for execution. While the same interface provides interface for another user to execute it.

Backend : Flask based microservices which caters to web components. Currently the flask component encompasses all the logic from login to execution of queries.

# Additional Information

The application supports two roles - 
1. Submitor: User who can only submit query for execution
2. Executor: User who can execute the query 

When a query is submitted, Regex is used to parse the query and create a select query which is executed. The submitor can view the number of records that gets updated. Based on that verification, submitor can submit query for execution.

The proof of concept has been carried out with SQLite, however any database could be used

