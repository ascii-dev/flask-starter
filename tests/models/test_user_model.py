from api.models.user import User


class TestUserModel:
    def test_new_user_succeeds(self, init_db, new_user):
        """
        Test that user can be created successfully through the
        model
        :param init_db: initialize the database
        :param new_user: creates new user through the model
        :return: assertion
        """
        assert new_user == new_user.save()

    def test_get_a_single_user_succeeds(self, init_db, new_user):
        """
        Tests that getting a single user from the database
        through the model is successful
        :param init_db: initialize the database
        :param new_user: creates new user through the model
        :return: assertion
        """
        new_user.save()
        assert User.query.get(new_user.id) == new_user

    def test_update_a_user_succeeds(self, init_db, new_user):
        """
        Tests that updating a user from the database through
        the model is successful
        :param init_db: initialize the database
        :param new_user: creates a new user through the model
        :return: assertion
        """
        new_user.save()
        new_user.update(first_name='Olusola')
        assert new_user.first_name == 'Olusola'

    def test_delete_a_user_succeeds(self, init_db, new_user):
        """
        Tests that deleting a user from the database through the
        model is successful
        :param init_db: initialize the database
        :param new_user: creates a new user through the model
        :return: None
        """
        new_user.save()
        new_user.delete()

    def test_get_user_string_representation(self, new_user):
        """
        Tests to compute and assert string representation of
        a new user
        :param new_user: creates a new user through the model
        :return: assertion
        """
        assert repr(new_user) == \
            f'<User {new_user.first_name} {new_user.last_name}>'
