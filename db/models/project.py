from pydantic import BaseModel, FilePath


class ProjectSummary(BaseModel):
    """The summary of a Project.
    """
    project_id: int
    title: str
    image: FilePath
    summary: str
    tags: list[str]


class Document(BaseModel):
    """Details documenting the projecit
    """
    document_id: int
    project_id: int
    large_text: str

