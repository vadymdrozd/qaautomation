from hw18.school_functionality.pupil import Pupil
from hw18.school_functionality.group import Group
from hw18.school_functionality.school import School
from hw18.school_functionality.teacher import Teacher
from hw18.school_functionality.director import Director
from hw18.school_functionality.head_teacher import HeadTeacher

school_director = Director('Ivan', 'Vasyliovuch', 40, 0)
head_teacher = HeadTeacher('Stepan', 'Ivanovych', 35, 0)
teacher = Teacher('Dmytro', 'Petrovych', 30, 0)

vasyl = Pupil('Vasyl', 'Vaskov', 16, 0)
olga = Pupil('Olga', 'Vaskova', 16, 1)
dana = Pupil('Dana', 'Petrova', 16, 1)
petro = Pupil('Petro', 'Petrov', 16, 0)

first_school = School(school_director)
first_school.add_head_teacher(head_teacher)
first_school.add_teacher(teacher)

first_school_group = Group('First group', teacher)

first_school_group.add_pupil_to_group(vasyl)
first_school_group.add_pupil_to_group(olga)
first_school_group.add_pupil_to_group(dana)

first_school.add_group_to_school(first_school_group)


def test_pupil():
    assert vasyl.name == 'Vasyl', 'Incorrect pupil name has been returned'
    assert vasyl.surname == 'Vaskov', 'Incorrect pupil surname has been returned'
    assert vasyl.age == 16, 'Incorrect pupil age has been returned'


def test_teacher():
    assert teacher.name == 'Dmytro', 'Incorrect teacher name has been returned'
    assert teacher.surname == 'Petrovych', 'Incorrect teacher surname has been returned'
    assert teacher.age == 30, 'Incorrect teacher age has been returned'


def test_head_teacher():
    assert head_teacher.name == 'Stepan', 'Incorrect teacher name has been returned'
    assert head_teacher.surname == 'Ivanovych', 'Incorrect teacher surname has been returned'
    assert head_teacher.age == 35, 'Incorrect teacher age has been returned'


def test_school_director():
    assert school_director.name == 'Ivan', 'Incorrect teacher name has been returned'
    assert school_director.surname == 'Vasyliovuch', 'Incorrect teacher surname has been returned'
    assert school_director.age == 40, 'Incorrect teacher age has been returned'


def test_group_pupil_count():
    assert len(first_school_group.get_pupils_list()) == 3, 'Incorrect pupil count has been returned. Should be 3'


def test_add_pupil_to_group():
    first_school_group.add_pupil_to_group(petro)
    assert len(first_school_group.get_pupils_list()) == 4,  'Incorrect pupil count has been returned. Should be 4'


def test_add_pupil_to_group():
    first_school_group.del_pupil_from_group(petro)
    assert len(first_school_group.get_pupils_list()) == 3,  'Incorrect pupil count has been returned. Should be 3'
