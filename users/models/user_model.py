from config.mysqlconnection import  connectToMySQL
DATABASE = 'users_schema'

class User:
    def __init__(self,data) :
        self.id = data['id']
        self.first_name=data['first_name']
        self.last_name = data['last_name']
        self.email=data['email']



# Now we use class methods to query our database

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES ( %(first_name)s ,%(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results= connectToMySQL(DATABASE).query_db(query)
        users = []
        # Iterate over the db results and create instances of friends with cls
        for user in results:
            users.append(cls(user))
        return users


