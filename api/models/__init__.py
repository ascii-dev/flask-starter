from sqlalchemy import event

from .base.push_id import PushID

from .user import User


def save_push_id(mapper, connection, target):
    """Function tto run the push id generator and save
    the id on insert
    """
    target.id = PushID().next_id()


database_tables = [User]

for table in database_tables:  # pragma: no cover
    event.listen(table, 'before_insert', save_push_id)
