from __future__ import annotations
from exceptions import CreationError
from typing import Dict, List
from gender import Gender
from random import randint
from dict2xml import dict2xml


class User:
    def __init__(
        self, first_name: str, last_name: str, email: str, gender: Gender
    ) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = gender

    @classmethod
    def from_csv(cls, csv_data: Dict[str, List[str]]) -> List[User]:
        users_list = []
        for user_data in csv_data["data"]:
            user_data_list = user_data.split(",")
            user = User(
                first_name=user_data_list[0],
                last_name=user_data_list[1],
                email=user_data_list[2],
                gender=Gender.MALE if user_data_list[3] == "male" else Gender.FEMALE
            )
            users_list.append(user)
        return users_list

    def __add__(self, other: User) -> User:
        if self.__gender == other.__gender:
            raise CreationError(f'There is no ability to create a new user '
                                f'because {self.__first_name} and {other.__first_name} have the same gender')
        random_gender = randint(1, 2)
        new_user = User(
            first_name="New"+self.__first_name,
            last_name=self.__last_name if self.__gender == 'MALE' else other.__last_name,
            email=("new"+self.__first_name).lower() + "." + (self.__last_name if self.__gender == 'MALE' else other.__last_name).lower() + "@gmail.com",
            gender=Gender.MALE if random_gender == 1 else Gender.FEMALE
        )
        return new_user

    def __str__(self) -> Dict:
        return {
                "first_name": self.__first_name,
                "last_name": self.__last_name,
                "email": self.__email,
                "gender": self.__gender.name
            }

    def __sub__(self, other: User) -> str:
        message = f"{self.__first_name} {self.__last_name} is deleted"
        del self
        return message

    def to_xml(self):
        return dict2xml(self.__str__())
