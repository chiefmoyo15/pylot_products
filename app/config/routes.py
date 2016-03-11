from system.core.router import routes

routes['default_controller'] = 'Names'
routes['GET']['/new'] = 'Names#new'
routes['POST']['/create'] = 'Names#create'