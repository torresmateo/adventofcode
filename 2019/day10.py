import numpy as np
from collections import defaultdict

class World(object):

    def __init__(self, filename, colour=True):
        self.mapfile = open(filename)
        self.map = []
        self.asteroids = []
        self.rays = {}
        self.raysteroids = defaultdict(list)
        self.asteroido = None
        self.build_map()
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
                                
                if print_terrain:
                    world += m[str(self.map[i][j])]
            world += lifes+'\n'
        print(world)
        
    def build_map(self):
        width = -1
        for line in self.mapfile:
            r = [c for c in line.strip()]
            self.map.append(r)

    def get_ray(self, o, d):
        dx = d[0] - o[0]
        dy = d[1] - o[1]
        g = np.gcd(dx, dy)
        return dx/g, dy/g, abs(dx)+abs(dy)


    def abarajarsteroid(self):
        return self.raysteroids[sorted(self.raysteroids.keys())[199]]


    def fill_raysteroids(self):
        for destination in self.asteroids:
            if destination != self.asteroido:
                ang_x, ang_y, dist = self.get_ray(self.asteroido, destination)
                ang = np.arctan2(ang_y,ang_x)
                ang = np.arctan2(ang_y,ang_x)
                if ang<0:
                    ang = 2*np.pi + ang
                ang = np.pi/2 + ang
                if ang>=2*np.pi:# - np.finfo(np.float32).eps:
                    ang -= 2*np.pi
                self.raysteroids[ang].append((destination, dist))

    def calculate_distances(self):
        for origin in self.asteroids:
            for destination in self.asteroids:
                if origin != destination:
                    ang_x, ang_y, dist = self.get_ray(origin, destination)
                    self.rays[origin].add((ang_x, ang_y))

    def map_asteroids(self):
        for j in range(len(self.map)):
            for i in range(len(self.map[j])):
                if self.map[j][i] == '#':
                    self.asteroids.append((i,j))
                    self.rays[(i,j)] = set()

    def get_best_asteroid(self):
        maxteroid = 0
        for k, i in self.rays.items():
            if maxteroid < len(i):
                maxteroid = len(i)
                self.asteroido = k
        return maxteroid




w = World('day10.input')
#w.print_status()
w.map_asteroids()
w.calculate_distances()
print(w.get_best_asteroid())
w.fill_raysteroids()
coord = w.abarajarsteroid()[0]
print(w.asteroido)
print(coord)
print(100*coord[0][0] + coord[0][1])
for e,k in enumerate(sorted(w.raysteroids.keys())):
    print(e+1, k, w.raysteroids[k])