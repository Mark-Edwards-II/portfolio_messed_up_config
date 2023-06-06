from models import Project, Document
from sqlalchemy.orm import Session

def get_all_projects(db: Session):
    """_summary_

    Args:
        db (Session): current session

    Returns:
        list[project]: list of all projects
    """
    return db.query(Project).all()

def get_project(db: Session, project_id: int):
    """get poject by id

    Args:
        db (Session): Current session
        project_id (int): _description_

    Returns:
        _type_: _description_
    """
    return db.query(Project).filter(Project.id == project_id).first()

def create_project(db: Session, project: Project):
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_all_documents(db: Session):
    return db.query(Project).all()

def get_document(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def create_document(db: Session, project: Project):
    db.add(project)
    db.commit()
    db.refresh(project)
    return project