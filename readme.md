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
### <br>current database schema: </br>
<br>A good tutorial of MongoDB can be found [here](https://www.tutorialspoint.com/mongodb/index.htm)</br>
<br>Database name: user_db</br>
<br>Collection: user_collection, book_collection</br>
<br>DB username: admin</br>
<br>DB password: pwd</br>
<br>Connection link: see settings.py</br>
<br>**Please DO NOT write any records to the database as this will create unbalanced records in the database!!!**</br>

## Development Rules

<br>Create a branch based on the latest version</br>
<br>After the changes have been made, create a pull request</br>
<br>If the group member all agree with this change, it will be merged</br>

**Don't push to master directly** 
