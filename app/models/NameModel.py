from system.core.model import Model

class NameModel(Model):
    def __init__(self):
        super(NameModel, self).__init__()
    def get_all_names(self):
        return self.db.query_db("SELECT * FROM names")
    def create_name(self, info):
        query = "INSERT INTO names(name) VALUES(%s)"
        return self.db.query_db(query, [info])



      # Build the query first and then the data that goes in the query
      # query = "INSERT INTO courses (title, description, created_at) VALUES (%s, %s, NOW())"
      # data = [course['title'], course['description']] # Note that data must be an array
      # return self.db.query_db(query, data)