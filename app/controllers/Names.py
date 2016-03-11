from system.core.controller import *

class Names(Controller):
    def __init__(self, action):
        super(Names, self).__init__(action)
        self.load_model('NameModel')
    def index(self):
        names = self.models['NameModel'].get_all_names()
        return self.load_view('index.html',names=names)
    def new(self):
        return self.load_view('new.html')
    def create(self):
        name = request.form['name']
        self.models['NameModel'].create_name(name)
        return redirect('/')