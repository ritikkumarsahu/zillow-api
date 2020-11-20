from flask_restful import Resource
from app.api import api
from app.api.helpers import cityAddress

# @app.route('/city/<cityname>')
# def get_city(cityname):
#     return 'User %s' % cityname

class city(Resource):
    def get(self, cityname):
        return cityAddress.get_address(cityname)

api.add_resource(city,'/city/<string:cityname>')
