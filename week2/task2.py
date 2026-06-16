class Enemy:
    def __init__(self, label, x, y, dx, dy, health):
        self.label = label
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.health = health

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def is_alive(self):
        return self.health > 0


class Tower:
    def __init__(self, x, y, attack_points, attack_range):
        self.x = x
        self.y = y
        self.attack_points = attack_points
        self.range = attack_range

    def attack(self, enemies):
        for enemy in enemies:
            if enemy.is_alive():
                distance_squared = (self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2
                if distance_squared <= self.range ** 2:
                    enemy.health -= self.attack_points


class BasicTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, attack_points=1, attack_range=2)


class AdvancedTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, attack_points=2, attack_range=4)


enemy1 = Enemy("E1", -10, 2, 2, -1, 10)
enemy2 = Enemy("E2", -8, 0, 3, 1, 10)
enemy3 = Enemy("E3", -9, -1, 3, 0, 10)

t1 = BasicTower(-3, 2)
t2 = BasicTower(-1, -2)
t3 = BasicTower(4, 2)
t4 = BasicTower(7, 0)
a1 = AdvancedTower(1, 1)
a2 = AdvancedTower(4, -3)


enemies = [enemy1, enemy2, enemy3]
towers = [t1, t2, t3, t4, a1, a2]

for turn in range(10):
    for enemy in enemies:
        if enemy.is_alive():
            enemy.move()

    for tower in towers:
        tower.attack(enemies)

for enemy in enemies:
    print(f"{enemy.label} is at ({enemy.x}, {enemy.y}) with life points {enemy.health}.")