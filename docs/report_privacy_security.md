# Privacy and Security Data Handling
## Data Collection and Storage
It is one of the developer responsibilty to ensure all data collected and stored in the database is secured and protected especially all data collected from the user is considered as a sensitive data.

SQL Alchemy is an ORM that is used for implementation of this application. It enables to sanitise all data input and output to and from user which is very useful to prevent any SQL injection attack. This act as one of protection for the database.

The database is also hosted in a private subnet to isolate and only the api gateway machine is able to interact with the database. This will eliminate the possibility of an unathorised user to access the database.

On top of that, the api endpoint require user to have a verified token or valid session to be able to input any data to the database. All user's password are hashed before storing it to the database.

In summary, below are the methods used to secure and storing the data
1.  Authorisation and Authentication
    The application is making use of flask-login, jwt, and csrf token. 
    * Flask-Login is authentication services based on a session which will help to verify its user before giving permission by using token and sessions in the front end side.
    * JWT: It will generate token for the users that will need to be included in the header for accessing the API.
    * CSRF Tokens: A token to keep forms safe and preventing cross site scripting attacks.
2.  Hashed Password Handling
    As explained above, all the password received from the user will be hashed before store in the database. It is using bcrypt to implement the slow hashing algorithm. This algorithm is chosen to help reduce the intensity of a hacker attacking the application as it will take longer time to decrypt the password.
3.  Utilising ORM SQLAlchemy to interface with database. By     using SQLAlchemy, it allows to abstract the database connection based on MVC pattern (Model, View, Controller) and not using any raw sql to get or upload data. The database is isolated and reduces the risk of SQL injections attack as the controller will also sanitise and process user input. On top of that, some validation is also applied to the models as extra layer of data sanitation.