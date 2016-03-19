from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
    def index(self):
        #get requests
        #load all products
        products = self.models['Product'].get_all()
        return self.load_view('index.html', products=products)
    def show(self, id):
        #get requests
        # find one and render it on view
        product = self.models['Product'].get_one(id)
        return self.load_view('show.html', product=product)
    def edit(self, id):
        #get requests
        # find one and render edit view
        product = self.models['Product'].get_one(id)
        return self.load_view('edit.html', product=product)
    def new(self):
        #get requests
        # renders the create page
        return self.load_view('new.html')
    def create(self):
        #post requests
        # creates a record in the DB
        create_product = {
            'name': request.form['name'].lower(),
            'description': request.form['description'],
            'price': request.form['price']
        }
        product_status = self.models['Product'].validate_product(create_product)
        if product_status['status'] == True:
            self.models['Product'].create(create_product)
            return redirect('/')
        else:
            for error in product_status['errors']:
                flash(error, 'product_errors')
            return redirect('/products/new')
    def update(self, id):
        #post requests
        #find one and update the record in the db
        update_product = {
            'id': id,
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        self.models['Product'].update(update_product)
        return redirect('/products/show/'+ str(id))
    def destroy(self, id):
        #post requests
        # finds and deletes a record from our DB
        self.models['Product'].destroy(id)
        return redirect('/')

