from pydantic import BaseModel, FilePath


class ProjectDetails(BaseModel):
    """Representation of what is expect in a project description.
    """
    proj_id: str
    title: str
    images: list[FilePath]  
    paragraphs: list[str]
    summary: str
    external_links: str | None = None



