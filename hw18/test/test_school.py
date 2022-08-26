import pytest
from hw18.Exceptions.School_exceptions import DuplicatePupilError
from hw18.school_functionality.pupil import Pupil


def test_add_pupil_to_school(school_object_creating):
    first_school = school_object_creating
    petro = Pupil('Petro', 'Petrov', 16, 0)
    first_school.groups[0].add_pupil_to_group(petro)
    result = first_school.get_study_cost(1000)
    assert result == 10500.0, f'Incorrect study cost is displayed - {result}. Should be 10500.0'


def test_add_existed_pupil_to_group(school_object_creating):
    first_school = school_object_creating
    petro = Pupil('Petro', 'Petrov', 16, 0)
    with pytest.raises(DuplicatePupilError):
        first_school.groups[0].add_pupil_to_group(petro)


def test_del_pupil_to_school(school_object_creating):
    first_school = school_object_creating
    petro = Pupil('Petro', 'Petrov', 16, 0)
    first_school.groups[0].del_pupil_from_group(petro)
    result = first_school.get_study_cost(1000)
    assert result == 14000.0, f'Incorrect study cost is displayed - {result}. Should be 14000.0'


def test_correct_revenue(school_object_creating):
    first_school = school_object_creating
    school_costs = first_school.get_school_costs()
    school_revenue_gross = len(first_school.get_school_pupils_list()) * first_school.get_study_cost(1000)
    school_revenue = school_revenue_gross - school_costs
    result = 1000
    assert result == school_revenue, f'Incorrect revenue value is counted - {school_revenue}. Should be {result}'

