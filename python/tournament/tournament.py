class Team():
    def __init__(self, name):
        self.name = name
        self.mp = 0
        self.w = 0
        self.d = 0
        self.l = 0
        self.p = 0
    def win(self):
        self.mp += 1
        self.w += 1
        self.p += 3
    def draw(self):
        self.mp += 1
        self.d += 1
        self.p += 1
    def loss(self):
        self.mp += 1
        self.l += 1
    def __repr__(self):
        return "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}".format(self.name, self.mp, self.w, self.d, self.l, self.p)
    def __lt__(self, other):
        if self.p != other.p:
            return self.p < other.p
        else:
            return self.name > other.name

def draw(team1, team2):
        team1.draw()
        team2.draw()
def win(team1, team2):
        team1.win()
        team2.loss()
def loss(team1, team2):
        team1.loss()
        team2.win()

Results = {"draw" : draw, "win" : win, "loss": loss}

def tally(rows):
    Teams = {}
    for x in rows:
        x = x.split(";")
        team1 = x[0]
        team2 = x[1]
        result = x[2]
        if team1 not in Teams:
            Teams[team1] = Team(team1)
        if team2 not in Teams:
            Teams[team2] = Team(team2)
        team1 = Teams[team1]
        team2 = Teams[team2]
        Results[result](team1, team2)
    headline = ["{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}".format("Team", "MP", "W", "D", "L", "P")]
    Teams = sorted(list(Teams.values()), reverse = True)
    Teams = headline + [str(x) for x in Teams]
    return Teams