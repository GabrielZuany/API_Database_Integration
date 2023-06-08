# Integration between API and Database

## What is the relation between a Database and an API?

- Basically, an [API (_Application Programming Interface_)](https://www.ibm.com/topics/api) is a set of defined rules that enable different applications to communicate with each other, like a bridge.
<br>
- So, if we have a database and we don't want other devices or subprograms accessing the database directly is implemented an API.
<br>
- Using an API we can guarantee security to our database, restrincting all subprograms and requests to a limited quantity of operations based on available endpoints.
<br>
- So, with an API we avoid to receive a "DROP DATABASE" comming from any application.

---

## Database

- Database: MySQL 8.0.33 (_localhost_)