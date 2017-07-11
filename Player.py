class Player(): # Define Player-class. Objects of this class tell the number of a round, amount of money that the player has and how many lives the player has left.
    def __init__(self, Round, Money, Lives):
        self.Round = Round
        self.Money = Money
        self.Lives = Lives
