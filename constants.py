class Constants(object):
    CANCEL = 'CANCEL'
    SWITCH = 'SWITCH'

class MeritsFlawsConstants(object):
    MENTAL = 'MENTAL'
    PHYSICAL = 'PHYSICAL'
    SOCIAL = 'SOCIAL'
    STATS = 'STATS'
    CHANGE_LIST = 'CHANGE LIST'

class SpeciesConstants(object):
    LAND = 'LAND'
    AIR = 'AIR'

class NavigationConstants(object):
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'
    EAST = 'EAST'
    WEST = 'WEST'
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    FORWARD = 'FORWARD'
    BACKWARDS = 'BACKWARDS'
    CENTER = 'CENTER'
    DIRECTIONS_LIST = [LEFT, RIGHT, CENTER, FORWARD, BACKWARDS, UP, DOWN, NORTH, EAST, SOUTH, WEST]
    COMPASS_DIRECTIONS_LIST = [NORTH, EAST, SOUTH, WEST]
    DIRECTIONS_DICT = {NORTH: NORTH, SOUTH: SOUTH, EAST: EAST, WEST: WEST, 'N': NORTH, 'S': SOUTH, 'E':EAST, 'W': WEST}
    COMPASS_DIRECTIONS_INTERPRETER = {NORTH: {WEST: LEFT, EAST: RIGHT, SOUTH: BACKWARDS, RIGHT: EAST, LEFT: WEST, BACKWARDS: SOUTH, FORWARD: NORTH},
                                      EAST: {NORTH: LEFT, SOUTH: RIGHT, WEST: BACKWARDS, RIGHT: SOUTH, LEFT: NORTH, BACKWARDS: WEST, FORWARD:EAST},
                                      SOUTH: {EAST: LEFT, WEST: RIGHT, NORTH: BACKWARDS, RIGHT: WEST, LEFT: EAST, BACKWARDS: NORTH, FORWARD: SOUTH},
                                      WEST: {SOUTH: LEFT, NORTH: RIGHT, EAST: BACKWARDS, RIGHT: NORTH, LEFT: SOUTH, BACKWARDS: EAST, FORWARD: WEST}}
    MOVE_CONVERTER_DICT = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}

class MapConstants(object):
    LEVEL_00 = 'MAP_LEVEL_00'
    LEVEL_00_ITEMS = 'MAP_LEVEL_00_ITEMS'

class TileConstants(object):
    # 0 - floor (generic)
    # 00 - dirt floor, 001 - stone floor, 002 - wet floor
    # 01 - traped tile
    # 1 - wall (generic)
    # 10 - stone wall, 100 - dirt wall, 101 - wood wall
    # 11 - breakable wall
    # 2 - object-container
    # 3 - object-item
    # 4 -
    # 5 -
    # 6 -
    # 7 - basic portal, 70 - basic door(open), 700 - basic door (closed), 701 - heavy wood door(open), 702 - heavy wood door(closed),
    # 71 - basic stairs
    # 8 -
    # 9 - special-instance
    pass

class PlayerCommands(object):
    MOVE = 'MOVE'
    TURN = 'TURN'
    CLIMB = 'CLIMB'
    JUMP = 'JUMP'
    LOOK = 'LOOK'
    SEARCH = 'SEARCH'
    USE = 'USE'
    TAKE = 'TAKE'
    INVENTORY = 'INVENTORY'
    EQUIP = 'EQUIP'
    UNEQUIP = 'UNEQUIP'
    ATTACK = 'ATTACK'
    BLOCK = 'BLOCK'
    FLEE = 'FLEE'
    CANCEL = 'CANCEL'
    EXIT = 'EXIT'
    ALL = 'ALL'
    DROP = 'DROP'
    PLAYER_EXIT = {CANCEL, EXIT}
    PLAYER_COMMANDS_SET = {MOVE, TURN, JUMP, LOOK, SEARCH, USE, TAKE,
                           INVENTORY, EQUIP, UNEQUIP, ATTACK, BLOCK, FLEE}

class ObjectConstants(object):
    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    LARGE = 'LARGE'
    FLOOR = 'FLOOR'
    GROUND = 'GROUND'
    TILE = 'TILE'
    WALL = 'WALL'
    STONE = 'STONE'
    ROCK = 'ROCK'
    CONTAINER = 'CONTAINER'
    CRATE = 'CRATE'
    BOX = 'BOX'
    CHEST = 'CHEST'
    VALUABLES = 'VALUABLES'
    TARNISHED_COINS = 'TARNISHED_COINS'
    OPALS = 'OPALS'
    OBJECTS_SET = {FLOOR, GROUND, TILE, WALL, STONE, ROCK, CONTAINER, CHEST, CRATE}

class WeaponConstant(object):
    WEAPON = 'WEAPON'
    MELEE = 'MELEE'
    RANGED = 'RANGED'
    RANGE = 'range'
    DMG = 'dmg'
    KNIFE = 'KNIFE'


class MessagesConstants(object):
    MESSAGES = 'messages'
    COLOR = 'color'
    SEARCH = 'search'
    KEYWORDS = 'keywords'
    CONTENTS = 'contents'
    INVENTORY = 'inventory'
    DEFAULT = 'default'
    MODEL = 'model'


