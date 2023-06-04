from models.project import Project 
from sqlalchemy.orm import Session

def get_all_projects(db: Session):
    return db.query(Project).all()

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def create_project(db: Session, project: Project):
    db.add(project)
    db.commit()
    db.refresh(project)
    return project