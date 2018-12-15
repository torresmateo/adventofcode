from collections import defaultdict

class Unit(object):
    
    def __init__(self, location, team, world, ap=3):
        self.team = team
        self.x, self.y = location
        self.hp = 200
        self.ap = ap
        self.world = world
        self.distances = None

    def __str__(self):
        m = {'E':'\033[32mE\033[0m', 'G':'\033[31mG\033[0m'}
        return f'{m[self.team]} at ({self.x},{self.y}) HP:{self.hp} AP:{self.ap}'

    def __repr__(self):
        m = {'E':'\033[32mE\033[0m', 'G':'\033[31mG\033[0m'}
        return f'<{m[self.team]} at ({self.x},{self.y}) HP:{self.hp} AP:{self.ap}>'

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)    

    def move(self):
        pass

    def attack(self, other):
        other.hp -= self.ap
        if other.hp <= 0:
            self.world.map[other.x][other.y].unit = None
            if other.team == 'E':
                self.world.lost_elves += 1
            del other

    def compute_distances(self):
        self.distances = defaultdict(list)
        self.distances[0].append((self.x, self.y))
        visited = set([(self.x, self.y)])
        curr_dist = 0
        while curr_dist in self.distances:
            # get neighbours "in reading order"
            for x, y in self.distances[curr_dist]:
                #              north     west      east      south
                t, u = self.world.map[x][y].terrain, self.world.map[x][y].unit
                if u == None or curr_dist == 0:
                    for nx, ny in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
                        if (nx, ny) in visited:
                            continue
                        visited.add((nx, ny))
                        nt, nu = self.world.map[nx][ny].terrain, self.world.map[nx][ny].unit
                        if nt == '.': # we can step here
                            self.distances[curr_dist+1].append((nx, ny))    
            curr_dist += 1
    
    def compute_enemies(self):
        enemies = []
        for i in range(len(self.world.map)):
            for j in range(len(self.world.map[i])):
                c = self.world.map[i][j]
                if (i, j) != (self.x, self.y) and c.unit != None and c.unit.team != self.team:
                    d = self.get_distance(c.unit)
                    if d != None:
                        enemies.append((c.unit, d))
        return enemies
    
    def get_distance(self, unit):
        for d, positions in self.distances.items():
            for p in positions:
                if p == (unit.x, unit.y):
                    return d

    def play(self):
        self.compute_distances()
        enemies = self.compute_enemies()
        if len(enemies) == 0:
            return enemies
        closest_enemy, distance = sorted(enemies, key=lambda e: e[1])[0]
        if distance > 1: #move
            # backtrack to current unit
            backtrack_path = defaultdict(set)
            backtrack_path[distance].add((closest_enemy.x, closest_enemy.y))
            curr_distance = distance
            while curr_distance > 0:
                for x, y in backtrack_path[curr_distance]:
                    for nx, ny in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
                        if (nx, ny) in self.distances[curr_distance-1] and self.world.map[nx][ny].unit == None:
                            backtrack_path[curr_distance-1].add((nx, ny))
                            
                curr_distance -= 1
            direction = sorted(backtrack_path[1])[0]
            # remove myself from the world
            self.world.map[self.x][self.y].unit = None
            self.x, self.y = direction
            self.world.map[self.x][self.y].unit = self
        else: #attack
            closest = sorted([e[0] for e in enemies if e[1] == 1], key=lambda u: (u.hp, u.x, u.y))[0]
            self.attack(closest)
        if distance == 2: #attack
            self.compute_distances()
            enemies = self.compute_enemies()
            closest = sorted([e[0] for e in enemies if e[1] == 1], key=lambda u: (u.hp, u.x, u.y))[0]
            self.attack(closest)

            
        return enemies

class Cell(object):
    
    def __init__(self, terrain, unit, world):
        self.terrain = terrain
        self.unit = unit
        self.world = world
        
    def __str__(self):
        if self.unit != None:
            return self.unit.team
        return self.terrain

class World(object):

    def __init__(self, filename, powah, colour=True):
        self.mapfile = open(filename)
        self.map = []
        self.units = []
        self.powah = powah
        self.build_map()
        self.spawn_units()
        self.lost_elves = 0
        self.colour = colour

    def print_status(self, distances=None):
        world = ''
        if self.colour:
            m = {'E':'\033[32m E|\033[0m', 'G':'\033[31m G|\033[0m', '.':'   ', '#':'\033[44m   \033[0m'}
            md = {'E':'\033[32m{d:2}|\033[0m', 'G':'\033[31m{d:2}|\033[0m', '.':'{d:2}|', '#':'\033[44m   \033[0m'}
        else:
            m = {'E':' E|', 'G':' G|', '.':'   ', '#':'###'}
            md = {'E':'{d:2}|', 'G':'{d:2}|', '.':'{d:2}|', '#':'###'}

        for i in range(len(self.map)):
            lifes = ' '
            for j in range(len(self.map[i])):
                print_terrain = True
                if distances != None:
                    for d, points in distances.items():
                        for p in points:
                            if (i, j) == p:
                                world += md[str(self.map[i][j])].format(d=d)
                                print_terrain = False
                                
                if self.map[i][j].unit != None:
                    lifes += f'{self.map[i][j].unit.team}({self.map[i][j].unit.hp}), '
                if print_terrain:
                    world += m[str(self.map[i][j])]
            world += lifes+'\n'
        print(world)
        
    def build_map(self):
        width = -1
        for line in self.mapfile:
            r = [c for c in line.strip()]
            self.map.append(r)

    def spawn_units(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                unit = None
                terrain = '#'
                if self.map[i][j] == 'G':
                    unit = Unit((i, j), self.map[i][j], self) # transform the "actual position" of a unit to ground
                    terrain = '.'
                elif self.map[i][j] == 'E':
                    unit = Unit((i, j), self.map[i][j], self, ap=self.powah) # transform the "actual position" of a unit to ground
                    terrain = '.'
                elif self.map[i][j] == '.':
                    terrain = '.'
                self.map[i][j] = Cell(terrain, unit, self) 

    def play_round(self):
        self.units = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j].unit != None:
                    self.units.append(self.map[i][j].unit)
        for u in self.units:
            if u.hp > 0:
                u.play()

    def units_types(self):
        teams = set()
        self.units = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j].unit != None:
                    self.units.append(self.map[i][j].unit)
                    teams.add(self.map[i][j].unit.team)
        return teams

    def compute_outcome(self, debug = False):
        rounds = -1
        while len(self.units_types()) > 1:
            self.play_round()
            if debug:
                self.print_status()
            rounds += 1
        hps = 0
        for u in self.units:
            hps += u.hp
        return self.lost_elves, hps * rounds

# part1
print('part 1')
w = World(f'day15.input', 3, colour=False)
le, o =w.compute_outcome()
print(f'lost elves:{le}, outcome: {o}')

#part2
print('part 2')
curr_powah = 3
last_lost_elves = -1
while last_lost_elves != 0:
    curr_powah += 1
    w = World(f'day15.input', curr_powah, colour=False)
    last_lost_elves, outcome = w.compute_outcome()
print(f'lost elves:{last_lost_elves}, outcome: {outcome}')