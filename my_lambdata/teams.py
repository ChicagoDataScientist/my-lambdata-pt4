# example teams.py (functional approach)

class Team():
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def advertise(self):
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR GAMES!!!")

    def full_name(self):
        return f"{self.city} {self.name}"

if __name__ == "__main__":
    teams = [
        {"city": "New York", "name": "Yankees"},
        {"city": "New York", "name": "Mets"},
        {"city": "Boston", "name": "Red Sox"},
        {"city": "New Haven", "name": "Ravens"},
        {"city": "Washington", "name": "Nationals"}
    ]
    for team_attributes in teams:
        team = Team(name=team_attributes["name"], city=team_attributes["city"])
        print("-------")
        # print(full_name(team))
        print(team.city)
        print(team.full_name())
        team.advertise()


    #     advertise(team)

    # team = Team(city="Washington", name="Wizards") # Initialize / create an instance of the object
    # print (team)
    # print(type(team))
    # print(team.name) # invoking attributes
    # print(team.city) # invoking attributes

    # team2 = Team("Giants", "New York") # Initialize / create an instance of the object
    # print (team2)
    # print(type(team2))
    # print(team2.name) # invoking attributes
    # print(team2.city) # invoking attributes