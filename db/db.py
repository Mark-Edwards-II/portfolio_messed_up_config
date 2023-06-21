from typing import List, Dict, Union

import sqlalchemy
from sqlalchemy import asc, desc, inspect

from .models import Base, Project
from db import engine


class CrudTable:

    def __repr__(self) -> str:
        """Show reproducible example of this Class"""
        return f"{self.__class__.__qualname__}()"

    @staticmethod
    def add_data(
            session: sqlalchemy.orm.session.Session,
            data_list: List[Dict[str, str]]
    ) -> None:
        """Add the data into database"""
        for data in data_list:
            new_data = Project(**data)
            session.add(new_data)

    @staticmethod
    def get_data(
            session: sqlalchemy.orm.session.Session,
            ascending: bool = True,
            **kwargs: Union[int, str]
    ) -> List[Project]:
        """Get a list of data"""
        direction = asc if ascending else desc
        if kwargs:
            return session.query(Project).filter_by(**kwargs).\
                order_by(direction("id")).all()
        return session.query(Project).order_by(direction("id")).all()

    @staticmethod
    def update_data(project: Project, data: Dict[str, str]) -> None:
        """Update the data"""
        for key, value in data.items():
            setattr(project, key, value)

    @staticmethod
    def drop_table() -> None:
        """Drop the table"""
        Project.__table__.drop(engine)

    @staticmethod
    def truncate_table(session: sqlalchemy.orm.session.Session) -> None:
        """Remove all data from the table"""
        session.query(Project).delete()

    @staticmethod
    def table_exists(table_name: str = "projects") -> bool:
        """check if the table exists"""
        inspector = inspect(engine)
        return inspector.has_table(table_name)

    @staticmethod
    def create_table() -> None:
        """Create all tables, will not attempt to recreate existing tables"""
        Base.metadata.create_all(engine)