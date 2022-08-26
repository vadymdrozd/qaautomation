import pytest
from hw18.school_functionality.pupil import Pupil
from hw18.school_functionality.group import Group
from hw18.school_functionality.school import School
from hw18.school_functionality.teacher import Teacher
from hw18.school_functionality.director import Director
from hw18.school_functionality.head_teacher import HeadTeacher


@pytest.fixture(scope='session')
def school_object_creating():
    school_director = Director('Ivan', 'Vasyliovuch', 40, 0)
    head_teacher = HeadTeacher('Stepan', 'Ivanovych', 35, 0)
    teacher = Teacher('Dmytro', 'Petrovych', 30, 0)

    vasyl = Pupil('Vasyl', 'Vaskov', 16, 0)
    olga = Pupil('Olga', 'Vaskova', 16, 1)
    dana = Pupil('Dana', 'Petrova', 16, 1)

    first_school = School(school_director)
    first_school.add_head_teacher(head_teacher)
    first_school.add_teacher(teacher)

    first_school_group = Group('First group', teacher)

    first_school_group.add_pupil_to_group(vasyl)
    first_school_group.add_pupil_to_group(olga)
    first_school_group.add_pupil_to_group(dana)

    first_school.add_group_to_school(first_school_group)

    yield first_school

    del first_school
