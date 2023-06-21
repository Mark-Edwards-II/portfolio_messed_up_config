import json

import pytest

from db import Session
from db.db import CrudTable


@pytest.fixture
def get_example_data():
    with open("test_data.json") as f:
        data = json.loads(f.read())
    return data


def test_table_exists():
    assert CrudTable.table_exists()


def test_truncate_table():
    with Session.begin() as s:
        CrudTable().truncate_table(s)
    with Session.begin() as s:
        assert len(CrudTable.get_data(s)) == 0


def test_drop_table():
    CrudTable.drop_table()
    assert not CrudTable.table_exists()


def test_create_table():
    CrudTable.create_table()
    assert CrudTable.table_exists()


def test_add_and_get_data(get_example_data):
    with Session.begin() as s:
        CrudTable().add_data(s, get_example_data)
    with Session.begin() as s:
        assert len(CrudTable().get_data(s)) == 6
        assert len(CrudTable().get_data(s, title="Tom Cat")) == 1
        assert len(CrudTable().get_data(s, title="Jerry Mouse")) == 1


def test_update_data():
    new_data = {
        "title": "new title"
    }
    with Session.begin() as s:
        check_title_not_found = CrudTable().get_data(s, title="new title")
        assert len(check_title_not_found) == 0
        project = CrudTable().get_data(s, title="Tom Cat")[0]
        CrudTable().update_data(project, new_data)
    with Session.begin() as s:
        target = CrudTable().get_data(s, title="new title")
        assert len(target) == 1