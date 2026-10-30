from pydantic import BaseModel


class Student(BaseModel):

    id: int | None = None

    name: str

    course: str

    Mark: float
    