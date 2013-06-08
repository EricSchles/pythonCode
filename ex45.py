from ex45Room import *
from ex45db import *


class Map(object):

    rooms = {
        'intro':Introduction(),
        'links':LinksRoom(),
        'puzzleOne':PuzzleOne(),
        'fightOne':FightOne(),
        'puzzleTwo':PuzzleTwo(),
        'FinalBattle':FinalBattle()
        }

    def __init__(self, start):
        self.start = start

    def next(self,next_room):
        return Map.rooms.get(next_room)

    def opening(self):
        return self.next(self.start)



