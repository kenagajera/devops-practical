from fastapi import APIRouter, Response

from models.stu_model import Student

from controllers.stu_controller import (
    create_student_controller,
    get_student_controller,
    get_student_controller_id,
    update_student_controller,
    delete_student_controller,
    get_student_controller_course
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/")
def create_student(
    student: Student,
    response: Response
):

    return create_student_controller(
        student,
        response
    )


@router.get("/")
def get_students(
    response: Response
):

    return get_student_controller(
        response
    )


@router.get("/{studentid}")
def get_student_by_id(
    studentid: int,
    response: Response
):

    return get_student_controller_id(
        studentid,
        response
    )


@router.get("/course/{course}")
def get_student_by_course(
    course: str,
    response: Response
):

    return get_student_controller_course(
        course,
        response
    )


@router.put("/{studentid}")
def update_student(
    studentid: int,
    student: Student,
    response: Response
):

    return update_student_controller(
        studentid,
        student,
        response
    )


@router.delete("/{studentid}")
def delete_student(
    studentid: int,
    response: Response
):

    return delete_student_controller(
        studentid,
        response
    )