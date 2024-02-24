# EmmanuelKpadedji-hw2
In this project I implemented a basic web feature for web application with data stored in MongoDB.

## Technologies used : HTML, CSS, Flask, and MongoDB

### Project step :

  - Create MongoDB Database :

        Set up a MongoDB database to store user credentials (login and password)

    ![wad2 1](https://github.com/itmo-wad/EmmanuelKpadedji-hw2/assets/53863110/2317a02d-a2d5-4675-b5e4-d2342503060c)

  - Render Authentication Form :

        - Create a new HTML template to render the authentication form.
        - Implement a route in Flask (/login) to render this template when the user accesses the root URL (http://localhost:5000/).
    
    ![wad2 3](https://github.com/itmo-wad/EmmanuelKpadedji-hw2/assets/53863110/5b9bbc44-ef36-4192-9fcc-d7b8e237e647)

   - Handle Authentication:

        - Implementitation of logic in the /login route to handle form submission.
        - Retrieve the entered username and password from the form.
        - Querying the MongoDB collection to find a user with the provided username and Verify the password.

   - Show Profile Page:

        - Creation of profile.html for authenticated user only.
        - Implementation of a route (/profile) to render this template.

        ![wad2 4](https://github.com/itmo-wad/EmmanuelKpadedji-hw2/assets/53863110/4a3b7253-38bb-4fb8-a283-63d0d0e8c32d)

    For unauthenticated user :
![wad2 5](https://github.com/itmo-wad/EmmanuelKpadedji-hw2/assets/53863110/da53c874-9b98-4d1b-b03f-1002fec8a341)
    
![wad2 6](https://github.com/itmo-wad/EmmanuelKpadedji-hw2/assets/53863110/c53d51ac-cf52-40cd-8fba-c52f355ed6e2)


     

## HOW To RUN ?

1- install flask (pip install flask)

2- install MongoDB and create a database name wadhw2 and collection : users

3- insert data (name and password in the database)

2- clone the repository of the project

3- navigate to the repository and run the command : python3 app.py

4- Reach the website on http://localhost:5000


## Contributor

KPADEDJI Emmanuel
