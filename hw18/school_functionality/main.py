from pupil import Pupil
from group import Group
from school import School
from teacher import Teacher
from director import Director
from head_teacher import HeadTeacher

school_director = Director('Ivan', 'Vasyliovuch', 40, 0)
head_teacher1 = HeadTeacher('Stepan', 'Ivanovych', 35, 0)
teacher1 = Teacher('Dmytro', 'Petrovych', 30, 0)

vasyl = Pupil('Vasyl', 'Vaskov', 16, 0)
olga = Pupil('Olga', 'Vaskova', 16, 1)
dana = Pupil('Dana', 'Petrova', 16, 1)
petro = Pupil('Petro', 'Petrov', 16, 0)
yana = Pupil('Yana', 'Yanina', 16, 1)
dina = Pupil('Dina', 'Dinova', 16, 1)

first_school = School(school_director)
first_school.add_head_teacher(head_teacher1)
first_school.add_teacher(teacher1)

first_school_group = Group('First group', teacher1)

first_school_group.add_pupil_to_group(vasyl)
first_school_group.add_pupil_to_group(olga)
first_school_group.add_pupil_to_group(dana)

second_school_group = Group('Second group', teacher1)

second_school_group.add_pupil_to_group(petro)
second_school_group.add_pupil_to_group(yana)
second_school_group.add_pupil_to_group(dina)

first_school.add_group_to_school(first_school_group)
first_school.add_group_to_school(second_school_group)

print(first_school.get_study_cost(1000))

# print('---------------')
# print('Average points')
# vasyl.get_benefit()
# vasyl.get_benefit()
# olga.get_benefit()
# olga.get_benefit()
# dana.get_benefit()
# dana.get_benefit()
# petro.get_benefit()
# petro.get_benefit()
# yana.get_benefit()
# yana.get_benefit()
# dina.get_benefit()
# dina.get_benefit()
# print(dina.sex)
# print(yana.sex)
# print(vasyl.sex)
#
#
# print('Group average points')
# print(first_school_group.get_group_average_points())
# print(second_school_group.get_group_average_points())
#
# print('School average points')
# print(first_school.get_school_average_points())
