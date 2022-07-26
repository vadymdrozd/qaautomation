from lesson11_hw11.pupil import Pupil


class Group:
    def __init__(self, group_name, classroom_teacher):
        self.group_name = group_name
        self.classroom_teacher = classroom_teacher
        self.pupils = []

    def add_pupil_to_group(self, pupil_object: Pupil):
        """
            Function for adding pupils objects to a group
        Args:
            pupil_object: object of the Pupil class
        Returns:
            adds Pupil object to the self.pupils list
        """
        return self.pupils.append(pupil_object)

    def del_pupil_from_group(self, pupil_object: Pupil):
        """
            Function for deleting pupils objects from a group
        Args:
            pupil_object: object of the Pupil class
        Returns:
            deletes Pupil object from the self.pupils list
        """
        return self.pupils.remove(pupil_object)

    def get_pupils_list(self):
        """
        Returns:
            list with name and Surname of pupils in the group
        """
        return [f'{pupil.name} {pupil.surname}' for pupil in self.pupils]

    def get_group_average_points(self):
        """
            Function for get group average points based on pupil average points
        Returns:
            group average points
        """
        group_average_points = [pupil.get_average_points() for pupil in self.pupils]
        return sum(group_average_points) / len(group_average_points)