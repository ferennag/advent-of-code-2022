from enum import Enum

class Hand:
    pass

class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    def backtrack(self, other):
        if self == Outcome.DRAW:
            return other

        if self == Outcome.WIN:
            if other == Hand.ROCK: return Hand.PAPER
            if other == Hand.PAPER: return Hand.SCISSORS
            if other == Hand.SCISSORS: return Hand.ROCK

        if self == Outcome.LOSS:
            if other == Hand.ROCK: return Hand.SCISSORS
            if other == Hand.PAPER: return Hand.ROCK
            if other == Hand.SCISSORS: return Hand.PAPER


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def fight(self, other):
        if self == other:
            return Outcome.DRAW

        if self == Hand.ROCK:
            if other == Hand.PAPER: return Outcome.LOSS
            if other == Hand.SCISSORS: return Outcome.WIN
        
        if self == Hand.PAPER:
            if other == Hand.SCISSORS: return Outcome.LOSS
            if other == Hand.ROCK: return Outcome.WIN

        if self == Hand.SCISSORS:
            if other == Hand.ROCK: return Outcome.LOSS
            if other == Hand.PAPER: return Outcome.WIN

    
def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return list(map(lambda line: line.strip(), lines))

def evaluate_game(input: str):
    opponent = {
        'A': Hand.ROCK,
        'B': Hand.PAPER,
        'C': Hand.SCISSORS
    }

    me = {
        'X': Hand.ROCK,
        'Y': Hand.PAPER,
        'Z': Hand.SCISSORS
    }

    hands = input.split(' ')
    left = opponent[hands[0]]
    right = me[hands[1]]
    return right.value + right.fight(left).value

def evaluate_game2(input: str):
    opponent = {
        'A': Hand.ROCK,
        'B': Hand.PAPER,
        'C': Hand.SCISSORS
    }

    outcome = {
        'X': Outcome.LOSS,
        'Y': Outcome.DRAW,
        'Z': Outcome.WIN
    }

    hands = input.split(' ')
    left = opponent[hands[0]]
    right = outcome[hands[1]]
    return right.value + right.backtrack(left).value

def main():
    games = read_input('input1.txt')
    scores = list(map(lambda game: evaluate_game(game), games))
    print('First solution: %d' % sum(scores))

    scores2 = list(map(lambda game: evaluate_game2(game), games))
    print('Second solution: %d' % sum(scores2))

if __name__ == '__main__':
    main()