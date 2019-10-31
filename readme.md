# Data Generation Service

A RESTful web service for data generation

### Usage
<br>generate a given number of users</br>
<br>create a user for Adhoc use </br>

## Start the Service
<br>make sure [Docker](https://docs.docker.com/docker-for-windows/install/) is installed in your computer</br>

<br>`git clone <this project url>` </br>

<br>`cd <project folder>`</br>

<br>`docker-compose up`</br>

<br> for first time start up, pass `--build` to docker compose </br>

## Database
### <br>Current database schema: </br>
<br>A good tutorial of MongoDB can be found [here](https://www.tutorialspoint.com/mongodb/index.htm)</br>
<br>Database name: user_db</br>
<br>Collection: user_collection, book_collection</br>
<br>**DB username: admin**</br>
<br>**DB password: pwd**</br>
<br>Connection link: see settings.py</br>
<br>**Please DO NOT write any records to the database as this will create unbalanced records in the database!!!**</br>

### How to connect the database
<br>1. Download MongoDB Client on your laptop</br>
<br>2. Use the given connection link (MONGO_DB_CONNECTION_SHELL)</br>
<br>3. [MongoDB](https://www.mongodb.com/download-center/compass) compass is a great tool to explore the data</br>
<br>4. If you need to run the query, it is recommended to have shell instead </br>
<br>5. Once you connected with the database, you will be asked to enter your username and password and they are stated above</br>

## Development Rules

<br>Create a branch based on the latest version</br>
<br>After the changes have been made, create a pull request</br>
<br>If the group member all agree with this change, it will be merged</br>

**Don't push to master directly** 
