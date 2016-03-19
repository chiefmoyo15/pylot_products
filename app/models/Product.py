from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    def get_all(self):
      return self.db.query_db("SELECT * FROM products")
    def get_one(self, id):
      return self.db.query_db("SELECT * FROM products WHERE id = '{}'".format(id))[0]
    def create(self, info):
      query = "INSERT INTO products(name, description, price, created_at, updated_at) VALUES('{}', '{}', '{}', NOW(), NOW())".format(info['name'], info['description'], info['price'])
      return self.db.query_db(query)
    def update(self, info):
      query = "UPDATE products SET name='{}', description='{}', price='{}', updated_at=NOW() WHERE id = '{}'".format(info['name'], info['description'], info['price'], str(info['id']))
      return self.db.query_db(query)
    def destroy(self, id):
      return self.db.query_db("DELETE FROM products WHERE id='{}'".format(id))

    def validate_product(self, info):
      #validate that product
      errors = []
      if len(info['name']) == 0 or len(info['description']) == 0 or len(info['price']) == 0:
        errors.append('Please fill out all forms')
      elif int(info['price']) < 1:
          errors.append('You have to make them pay')
      if len(info['name']) > 45:
        errors.append('Keep your product name short')
      if len(errors) == 0:
        product_exists = self.get_by_name(info['name'])
        if len(product_exists) != 0:
          errors.append('That product already exists')
      if len(errors) > 0:
        return {'status': False, 'errors': errors}
      else:
        return {'status': True}

    def get_by_name(self, name):
      return self.db.query_db("SELECT name FROM products WHERE name = '{}'".format(name))




#       DELETE FROM table_name
# WHERE some_column=some_value;

#       UPDATE table_name
# SET column1=value1,column2=value2,...
# WHERE some_column=some_value;

      # Build the query first and then the data that goes in the query
      # query = "INSERT INTO courses (title, description, created_at) VALUES (%s, %s, NOW())"
      # data = [course['title'], course['description']] # Note that data must be an array
      # return self.db.query_db(query, data)