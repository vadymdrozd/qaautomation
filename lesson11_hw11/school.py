from lesson11_hw11.group import Group
from director import Director
from head_teacher import HeadTeacher
from teacher import Teacher


class School:
    def __init__(self,
                 director: Director):
        self.__director = director
        self.head_teachers = []
        self.teachers = []
        self.groups = []

    @property
    def director(self):
        """
        Returns:
            class Director object as a school attribute view
        """
        return self.__director

    def add_head_teacher(self, head_teacher_object: HeadTeacher):
        """
            Function for adding a head teacher to school
        Args:
            head_teacher_object: object of the Head_Teacher class
        Returns:
            adds a head teacher object to the self.head_teachers list
        """
        return self.head_teachers.append(head_teacher_object)

    def add_teacher(self, teacher_object: Teacher):
        """
            Function for adding a teacher to school
        Args:
            teacher_object: object of the Head_Teacher class
        Returns:
            adds a teacher object to the self.head_teachers list
        """
        return self.teachers.append(teacher_object)

    def add_group_to_school(self, group_object: Group):
        """
            Function for adding a group object to school object
        Args:
            group_object: object of the Group class
        Returns:
            adds a group object to the self.groups list
        """
        return self.groups.append(group_object)

    def del_group_from_school(self, group_object):
        """
            Function for deleting a group object from school object
        Args:
            group_object: object of the Group class
        Returns:
            if there is no pupils in group object - deletes group object from school
            if there is pupils in group object - returns a message to do something with pupils in the group
        """
        if group_object.get_pupils_list():
            return f'You have pupils in this class. ' \
                   f'{"There are" if len(group_object.get_pupils_list()) > 1 else "There is"} ' \
                   f'{", ".join(group_object.get_pupils_list())}. ' \
                   f'Firstly you should make some actions with them (for example delete or reassign them to another class)'
        return self.groups.remove(group_object)

    def get_school_average_points(self):
        """
            Function for get school average points based on group average points based on pupil average points
        Returns:
            school average points
        """
        school_average_points = [group.get_group_average_points() for group in self.groups]
        return sum(school_average_points) / len(school_average_points)

    def get_school_pupils_list(self):
        """
            Function for getting all pupils in a school
        Returns:
            School pupils list
        """
        pupils_list = []
        for group in self.groups:
            for pupil in group.pupils:
                pupils_list.append(pupil)
        return pupils_list

    def get_head_teachers_cost(self):
        """
            Function for get a sum of all school head teachers salary
        Returns:
            integer - sum of all school head teachers salary
        """
        head_teachers_cost = 0
        for head_teacher in self.head_teachers:
            head_teachers_cost += head_teacher.benefit
        return head_teachers_cost

    def get_teachers_cost(self):
        """
            Function for get a sum of all school teachers salary
        Returns:
            integer - sum of all school teachers salary
        """
        teachers_cost = 0
        for teacher in self.teachers:
            teachers_cost += teacher.benefit
        return teachers_cost

    def get_study_cost(self):
        """
            Function for get a cost of study.
            Sums up teachers, head teachers and director costs and divides it on pupils' quantity
            Has an input in the infinity cycle until a user enter an integer
        Returns:
            if there is no pupils in school - returns a string message
            if there is pupils in group object - returns a float or integer - cost of studying for each pupil in school
        """
        while True:
            try:
                revenue = int(input('Please enter the revenue you need (only int digits): '))
            except ValueError:
                continue
            else:
                if self.get_school_pupils_list():
                    school_costs = self.get_teachers_cost() + self.get_head_teachers_cost() + self.__director.benefit
                    total_costs = school_costs + revenue
                    return total_costs / len(self.get_school_pupils_list())
                return 'There is no pupils in your school, so your business won\'t fly up ;)'
