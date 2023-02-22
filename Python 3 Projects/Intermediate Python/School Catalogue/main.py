class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, howmanystudents):
        self.numberOfStudents = howmanystudents

    def __repr__(self):
        return str("A {} school named {} with {} students".format(self.level, self.name, self.numberOfStudents))


test1 = School("New York City School", "middle", 850)
test1.get_name()
test1.get_level()
test1.get_numberOfStudents()
print(test1)


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + ". The pickup policy is {pickupPolicy}".format(pickupPolicy=self.pickupPolicy)


test2 = PrimarySchool("NYC Best Primary", 780, "Pick up after 4 pm.")
test2.get_pickupPolicy()
print(test2)


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + ". The sports teams are: {}".format(self.sportsTeams)


test3 = HighSchool("1 st High School NYC", 640, ["Tennis", "Basketball"])
test3.get_sportsTeams()
print(test3)class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents
  def set_numberOfStudents(self, howmanystudents):
    self.numberOfStudents = howmanystudents

  def __repr__(self):
    return str("A {} school named {} with {} students".format(self.level, self.name, self.numberOfStudents))


test1 = School("New York City School", "middle", 850)
test1.get_name()
test1.get_level()
test1.get_numberOfStudents()
print(test1)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + ". The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

test2 = PrimarySchool("NYC Best Primary", 780, "Pick up after 4 pm.")
test2.get_pickupPolicy()
print(test2)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + ". The sports teams are: {}". format(self.sportsTeams)

test3 = HighSchool("1 st High School NYC", 640, ["Tennis", "Basketball"])
test3.get_sportsTeams()
print(test3)