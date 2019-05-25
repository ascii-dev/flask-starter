from flask import json
from config import AppConfig

from api.utilities.constants import CHARSET

BASE_URL = AppConfig.API_BASE_URL


class TestDemoEndpoint:
    """Class for testing demo endpoint"""

    def test_get_demo_endpoint_succeeds(self, client):
        """Should return success response

        Args:
            client(flask client): fixture to get flask test client
        """
        response = client.get(
            f'{BASE_URL}/demo')
        response_data = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 200
        assert type(response_data) == dict
