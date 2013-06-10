from ex45Room import *
#from ex45db import *


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


#Iterator class:
#iterates through the map in sequential order
#this essential looks like a linked list that can only be moved
#through forward...
class Engine(object):
    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening()
        
        while True:
            print "\n --------"
            next_room = current_room.enter()
            current_room = self.room_map.next(next_room)


a_map = Map('intro')
a_game = Engine(a_map)
a_game.play()
