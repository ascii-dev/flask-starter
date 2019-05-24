"""Module for demo use"""

from flask_restplus import Resource

from main import api


@api.route('/demo')
class DemoResource(Resource):
    """Resource class for demo use"""

    def get(self):
        """Demo get endpoint"""
        return {
            'status': 'success',
            'message': 'get request successful',
        }
