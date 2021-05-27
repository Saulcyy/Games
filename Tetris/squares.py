from random import randrange
from pygame import Rect, draw
from clock import Clock

class Squares:
    """méthode de manipulation de carrés dans le jeu"""
    def __init__(self, st, status, screen):
        self.st = st
        self.status = status
        self.screen = screen
        self.empty_line = ['none' for i in range(st.square_num_x)]
        self.squares = [self.empty_line.copy() for i in range(st.square_num_y)]
        self.new_sq(self)
        self.clock = Clock(st)

    # dessiner tous les carrés
    def draw_squares(self):
        self.screen.fill(self.st.space_color)
        self.draw_tip(self)
        self.draw_exist_sq(self)
        self.draw_curr_sq(self)

    # mise à jour de l'information sur les carrés
    def update(self):
        updated = False # for update screen
        # chute verticale, chute droite
        if self.status.straight_drop and self.clock.is_time_to_straight_drop():
            updated = True
            self.drop_straight(self)
            self.clock.update_straight_drop()
        # chute verticale, chute de force
        elif self.clock.is_time_to_drop():
            updated = True
            self.drop(self)
            self.clock.update_drop()
        # chute verticale, chute rapide
        elif self.status.down and self.clock.is_time_to_quick_drop():
            updated = True
            self.drop(self)
            self.clock.update_quick_drop()
        # rotation
        if self.status.rotate and self.clock.is_time_to_rotate():
            updated = True
            self.rotate(self)
            self.clock.update_rotate()
        # déplacement horizontal
        if self.status.right:
            updated = True
            if self.clock.is_time_to_move() or self.clock.is_time_to_quick_right():
                self.right(self)
            self.clock.update_move()
        if self.status.left:
            updated = True
            if self.clock.is_time_to_move() or self.clock.is_time_to_quick_left():
                self.left(self)
            self.clock.update_move()
        # crash detection
        if self.should_stop(self):
            updated = True
            self.stop(self)
        return updated

    # renouveler la place actuelle
    @staticmethod
    def new_sq(self):
        self.curr_sq = self.st.new.copy()
        shape = self.get_shape(self)
        self.origin_shape = shape['pos']
        self.curr_shape = shape['pos']
        self.curr_color = shape['color']
        self.rotate_limit = shape['rotate']
        self.rotate_curr = 1
        # si de nouveaux carrés sont écrasés, le jeu est terminé.
        if not self.valid(self, self.curr_sq, self.curr_shape):
            self.status.game_status = self.status.GAMEOVER

    # retourne un dictionnaire de formes aléatoires
    @staticmethod
    def get_shape(self):
        shape_index = randrange(0, self.st.shape_num)
        return self.st.shapes[shape_index].copy()

    @staticmethod
    def drop_straight(self):
        while not self.should_stop(self):
            self.curr_sq[0] += 1

    @staticmethod
    def drop(self):
        new_sq = self.curr_sq.copy()
        new_sq[0] += 1
        if self.valid(self, new_sq, self.curr_shape):
            self.curr_sq = new_sq

    @staticmethod
    def rotate(self):
        new_shape = self.get_rotated_shape(self)
        # contrôle régulier
        if self.valid(self, self.curr_sq, new_shape):
            self.curr_shape = new_shape
        # déplacer horizontalement si non valide
        else:
            tolerance = 2
            for i in range(tolerance):
                # gauche
                new_sq_left = self.curr_sq.copy()
                new_sq_left[1] -= 1
                if self.valid(self, new_sq_left, new_shape):
                    self.curr_sq = new_sq_left
                    self.curr_shape = new_shape
                    return
                # droite
                new_sq_right = self.curr_sq.copy()
                new_sq_right[1] += 1
                if self.valid(self, new_sq_right, new_shape):
                    self.curr_sq = new_sq_right
                    self.curr_shape = new_shape
                    return


    @staticmethod
    def get_rotated_shape(self):
        # la limite de rotation ne doit pas être dépassée, si elle est dépassée, il faut la réinitialiser
        if self.rotate_curr >= self.rotate_limit:
            self.rotate_curr = 1
            new_shape = self.origin_shape
        else:
            self.rotate_curr += 1
            new_shape = []
            for sq in self.curr_shape:
                new_shape.append([sq[1], -sq[0]])
        return new_shape

    @staticmethod
    def right(self):
        new_sq = self.curr_sq.copy()
        new_sq[1] += 1
        if self.valid(self, new_sq, self.curr_shape):
            self.curr_sq = new_sq

    @staticmethod
    def left(self):
        new_sq = self.curr_sq.copy()
        new_sq[1] -= 1
        if self.valid(self, new_sq, self.curr_shape):
            self.curr_sq = new_sq

    @staticmethod
    def stop(self):
        # attendre un moment avant de s'arrêter, donner au joueur le temps de s'adapter
        if not self.clock.is_time_to_stop():
            self.clock.update_should_stop(True)
            return
        else:
            self.clock.update_should_stop(None)
            self.clock.update_stop()
        # copier les carrés sur la carte
        for sq in self.curr_shape:
            x = sq[1] + self.curr_sq[1]
            y = sq[0] + self.curr_sq[0]
            if y >= 0:
                self.squares[y][x] = self.curr_color
        x = self.curr_sq[1]
        y = self.curr_sq[0]
        if y >= 0:
            self.squares[y][x] = self.curr_color
        full_lines = self.clean_full_lines(self)
        self.status.score += full_lines  # ajouter une note
        self.new_sq(self)

    # supprimer les lignes pleines et insérer des lignes vides en tête de ligne
    @staticmethod
    def clean_full_lines(self):
        full_lines = 0
        for index, line in enumerate(self.squares):
            if line.count('none') == 0:
                full_lines += 1
                self.st.time_drop *= self.st.time_drop_adjust # adjust time
                self.squares.pop(index)
                self.squares.insert(0, self.empty_line.copy())
        return full_lines

    # valider les carrés actuels des formes par rapport au centre avec une goutte verticalement
    @staticmethod
    def should_stop(self):
        # carrés de forme de contrôle
        for sq in self.curr_shape:
            x = sq[1] + self.curr_sq[1]
            y = sq[0] + self.curr_sq[0] + 1
            if y - 1 >= 0 and not self.valid_sq(self, [y, x]):
                return True
        # contrôle de l'équerre centrale
        x = self.curr_sq[1]
        y = self.curr_sq[0] + 1
        return not (self.valid_sq(self, [y, x]))

    # valider la case centrale donnée et les cases de forme par rapport à la case centrale
    @staticmethod
    def valid(self, square, shape):
        # carrés de forme de contrôle
        for sq in shape:
            x = sq[1] + square[1]
            y = sq[0] + square[0]
            if y >= 0 and not (self.valid_sq(self, [y, x])):
                return False
        # contrôle de l'équerre centrale
        return self.valid_sq(self, square)

    @staticmethod
    def valid_sq(self, sq):
        # Frontière de contrôle
        if sq[0] >= self.st.square_num_y or \
                        sq[1] >= self.st.square_num_x or \
                        sq[1] < 0:
            return False
        # check crash
        return self.squares[sq[0]][sq[1]] == 'none'

    @staticmethod
    def draw_exist_sq(self):
        for y, row in enumerate(self.squares):
            for x, square in enumerate(row):
                color = self.st.colors[self.squares[y][x]]
                self.draw_square(self, y, x, color)

    @staticmethod
    def draw_tip(self):
        # trouver la position basse
        curr_sq = self.curr_sq.copy()
        while not self.should_stop(self):
            self.curr_sq[0] += 1
        curr_sq, self.curr_sq = self.curr_sq, curr_sq

        # dessiner leurs pointes
        color = self.st.colors['tip']
        self.draw_square(self, curr_sq[0], curr_sq[1], color, True)
        self.draw_square(self, curr_sq[0], curr_sq[1], self.st.colors['none'])
        for y, x in self.curr_shape:
            curr_y, curr_x = curr_sq[0], curr_sq[1]
            self.draw_square(self, y + curr_y, x + curr_x, color, True)
            self.draw_square(self, y + curr_y, x + curr_x, self.st.colors['none'])

    @staticmethod
    def draw_curr_sq(self):
        # centre de tirage
        color = self.st.colors[self.curr_color]
        self.draw_square(self, self.curr_sq[0], self.curr_sq[1], color)
        # dessiner des formes
        curr_y, curr_x = self.curr_sq[0], self.curr_sq[1]
        for y, x in self.curr_shape:
            self.draw_square(self, y + curr_y, x + curr_x, color)

    # dessiner un seul carré avec les informations données
    @staticmethod
    def draw_square(self, y, x, color, border=False):
        x_pos = x * (self.st.square_space + self.st.square_length)
        y_pos = y * (self.st.square_space + self.st.square_length)
        length = self.st.square_length
        # ajouter des bordures
        if border:
            y_pos -= self.st.square_space
            x_pos -= self.st.square_space
            length += 2 * self.st.square_space
        rect = Rect(x_pos + self.st.square_space, y_pos + self.st.square_space, length, length)
        draw.rect(self.screen, color, rect)