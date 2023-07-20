# Creating a class for Car
class Car:
    def __init__(self, Name, Model, Release_Year, Max_speed):
        self.Name = Name
        self.Model = Model
        self.Release_Year = Release_Year
        self.Max_speed = Max_speed

    def display_details(self):
        print(f'Name: {self.Name}')
        print(f'Model: {self.Model}')
        print(f'Release Year: {self.Release_Year}')
        print(f'Max Speed: {self.Max_speed}')


#  creating an object for Car
self_driving = Car(Name="Tesla", Model="X", Release_Year="2021", Max_speed="200")
self_driving.display_details()


# creating a class for Institute
class Institute:
    def __init__(self, N_ame, Location, Course):
        self.Name = N_ame
        self.Location = Location
        self.Course = Course

    def display_details(self):
        print(f'Name: {self.Name}')
        print(f'Location: {self.Location}')
        print(f'Course: {self.Course}')


Besant = Institute(N_ame="Besant Technology", Location="Hebal", Course="Python")
Besant.display_details()
