"""String length validator"""
from marshmallow import ValidationError

from api.utilities.messages.serialization import serialization_messages


def string_length_validator(length):
    """ Returns a function that checks data over a given length
    Args:
        length (Integer): Length a string must not exceed
    Returns:
        Function which validates length of the data
    """

    def length_validator(data):
        """ Checks if data does not exceed a given length
            Args:
                data (String): data to be validated
            Raises:
                validation error if data exceeds a given length
        """

        if len(data) > length:
            raise ValidationError(
                serialization_messages['string_length'])

    return length_validator


def empty_string_validator(string):
    """Checks if string is not empty
    Args:
        string (str): the string to be validated
    """
    if len(string.strip()) < 1:
        raise ValidationError(
            serialization_messages['not_empty'])


def min_length_validator(data):
    """ Checks if data is less than a given length
                    Args:
                        data (str): data to be validated
                    Raises:
                        validation error if data is less than a given length
                """
    if len(data) < 5:
        raise ValidationError(
            serialization_messages['field_length'].format(5))
