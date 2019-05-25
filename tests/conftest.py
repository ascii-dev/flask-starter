"""Module for setting up base fixtures for tests"""
# pylint: skip-file

from os import environ

import pytest
from flask import current_app

from alembic import config, command

from sqlalchemy.engine import reflection
from sqlalchemy.schema import (
    MetaData,
    Table,
    DropTable,
    ForeignKeyConstraint,
    DropConstraint,
)

from main import create_app
from config import AppConfig

from api.models.database import db

environ['FLASK_ENV'] = 'testing'


def db_drop_all(db):
    # From http://www.sqlalchemy.org/trac/wiki/UsageRecipes/DropEverything

    conn = db.engine.connect()

    # the transaction only applies if the DB supports
    # transactional DDL, i.e. Postgresql, MS SQL Server
    trans = conn.begin()

    inspector = reflection.Inspector.from_engine(db.engine)

    # gather all data first before dropping anything.
    # some DBs lock after things have been dropped in
    # a transaction.
    metadata = MetaData()

    tbs = []
    all_fks = []

    for table_name in inspector.get_table_names():
        fks = []

        for fk in inspector.get_foreign_keys(table_name):
            if not fk['name']:
                continue
            fks.append(ForeignKeyConstraint((), (), name=fk['name']))
        t = Table(table_name, metadata, *fks)
        tbs.append(t)
        all_fks.extend(fks)

    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))

    for table in tbs:
        conn.execute(DropTable(table))

    trans.commit()

    db.engine.execute("DROP TABLE IF EXISTS alembic_version CASCADE")


@pytest.yield_fixture(scope='session')
def app():
    """Sets up our flask test app

    Returns:
        Flask app
    """

    _app = create_app(AppConfig)

    # Create app context before running tests
    context = _app.app_context()
    context.push()

    yield _app

    context.pop()


@pytest.fixture(scope='function')
def client(app):
    """Sets up an app client for our test functions

    Params:
        app: Pytest fixture

    Returns:
        Flask app client
    """
    yield app.test_client()


@pytest.fixture(scope='module')
def init_db(app):
    """Initializes our database for tests

    Returns:
        Database object
    """
    db.drop_all()
    db.create_all()
    yield db
    db.sessioon.close()
    db.drop_all()


@pytest.fixture(scope='module')
def request_context():
    """Sets up a request client

    Returns:
        Flask request client
    """
    context = current_app.test_request_context()
    context.push()
    yield context
    context.pop()


@pytest.fixture(scope="function")
def set_up_db(app):
    # reset database at beginning of test
    db_drop_all(db)
    alembic_cfg = alembic.config.Config("./migrations/alembic.ini")
    alembic.command.stamp(alembic_cfg, 'base')

    yield
    # clean database at end of test
    db.session.close()
    db_drop_all(db)
