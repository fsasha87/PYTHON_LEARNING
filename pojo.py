import json
from json import JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Student:  # full_name:str, avg_rank: float, courses:list

    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, file):
        with open(file) as json_file:
            dictionary = json.load(json_file)
        return cls(**dictionary)

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    def serialize_to_json(self, json_file):
        with open(json_file, "w") as write_file:
            json.dump(self, write_file, cls=Encoder)

    @classmethod
    def serialize_list_to_json(cls, students, file):
        with open(file, "w") as write_file:
            json.dump(students, write_file, cls=Encoder)


class Group:  # title: str, students: list
    def __init__(self, title):
        self.title = title
        self.students = []

    def __str__(self):
        return f"{self.title}: {[str(Student(**item)) for item in self.students]}"

    # def serialize_to_json(self, json_file):
    #   with open(json_file, "w") as write_file:
    #     json.dump(self, write_file, cls=Encoder)

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as read_file:
            students = json.load(read_file)
            g = Group(title=str(students_file).split(".")[0])
            if isinstance(students, list):
                g.students = students
            else:
                g.students = [students]
            return g

    @classmethod
    def serialize_to_json(cls, groups, file):
        with open(file, "w") as write_file:
            json.dump(groups, write_file, cls=Encoder)


# Class student has attributes full_name:str, avg_rank: float, courses: list
# Class Group has attributes title: str, students: list.
# Make both Classes DSON serializable.
# Json-files represent information about student (students).
# Create methods:
# student.from_json(json_fiie) that return Student instance from attributes from json-file;
# Student.serialize_to_json(filename)
# Group.serialize_to_json(list_of_groupSj filename)
# Group.create_group_from_file(students_file)
# Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension).