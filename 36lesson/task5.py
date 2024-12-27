# Task 5: Online Course Platform
# Create a Course base class with:

# Attributes:
# title (string)
# instructor (string)
# Methods:
# get_description(): Prints course title and instructor.
# Create subclasses for ProgrammingCourse and MathCourse:

# ProgrammingCourse:
# Additional attribute: languages (list of programming languages)
# Override get_description() to include languages.
# MathCourse:
# Additional attribute: difficulty_level (string)
# Override get_description() to include difficulty level.
# Add a CoursePlatform class with:

# Attributes:
# courses (list of Course objects)``
# Methods:
# add_course(course): Adds a course to the platform.
# list_all_courses(): Prints details of all courses.
# Objective: Train students to work with inheritance and manage collections of objects.

class Course:
    def __init__(self, title:str, instructor:str):
        self.title=title
        self.instructor=instructor
    def get_description(self):
        return f'corse name: {self.title}, instructor: {self.instructor}'

class ProgrammingCourse(Course):
    def __init__(self, title, instructor, languages:list):
        super().__init__(title, instructor)
        self.languages=languages
    def get_description(self):
        return f'{super().get_description()}, programming languages: {self.languages}'
    
class MathCourse(Course):
    def __init__(self, title:str, instructor:str, difficulty_level:str):
        super().__init__(title,instructor)
        self.difficulty_level=difficulty_level
    def get_description(self):
        return f'{super().get_description()}, difficulty level: {self.difficulty_level}'

class CoursePlatform:
    def __init__(self, courses:list):
        self.courses=courses
    def add_course(self, course):
        self.courses.append(course)
        return f'a new course {course.title} added to the list'
    def list_all_courses(self):
        for course in self.courses:
            print(course.get_description())

programming=ProgrammingCourse('WEB development in 30days', "Rakhim mashennik", ['HTML', "CSS", "JS"] )
math=MathCourse('ALgorithms in 2 hours', "Akobir", 'easy(complex)')

coursePlatform=CoursePlatform([])
print(coursePlatform.add_course(programming))
print(coursePlatform.add_course(math))
print('\n')
coursePlatform.list_all_courses()