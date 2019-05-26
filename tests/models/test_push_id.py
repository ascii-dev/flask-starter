from unittest.mock import patch, Mock
from api.models.base.push_id import PushID
from api.models import save_push_id


class TestPushIdGenerator:
    """Test PushId Generator."""
    @patch(
        'api.models.base.push_id.time', Mock(return_value=1234)
    )
    def initialize_push_id(self):
        """Create an instance of class PushID"""
        push_id = PushID()
        return push_id

    def generate_random_unique_id(self):
        """Generate random uniques ids"""
        push_id = self.initialize_push_id()
        unique_id1 = bytes(push_id.next_id(), 'utf-8')
        unique_id2 = unique_id1
        return unique_id1, unique_id2

    def test_duplicate_time_succeeds(self):
        """Should update the last random characters if time is duplicate."""
        unique_id1, unique_id2 = self.generate_random_unique_id()
        assert unique_id1[19] == unique_id2[19]

    def test_duplicate_time_last_random_char_is_63_succeeds(self):
        """
        Should set the last random character to zero if time is duplicate
        and the last random character is 63
        """
        push_id = self.initialize_push_id()
        self.generate_random_unique_id()
        push_id.last_rand_chars[-1] = 63
        push_id.set_last_rand_char(True)
        push_id.get_previous_rand_char()
        assert push_id.last_rand_chars[-1] == push_id.last_rand_chars[-1]

    def test_save_push_id(self):
        """
        Should test that save_push_id returns a push ID
        """
        PushID.next_id = Mock(return_value=1234)
        mapper = connection = target = Mock()
        target.configure_mock(id='')
        save_push_id(mapper, connection, target)
        assert target.id == 1234
