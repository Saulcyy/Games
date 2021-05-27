import pygame

class Settings:
    def __init__(self):
        # temps ou vitesse, en secondes, vous pouvez l'ajuster si vous n'êtes pas satisfait de la valeur par défaut.
        self.time_drop = 0.8  # période pour forcer la chute
        self.time_drop_adjust = 0.99 # chaque fois que le score augmente, le temps de chute diminue de ce facteur.
        self.time_stop = 0.5 # le joueur de temps peut ajuster la position en bas
        self.time_move = 0.05 # intervalle de temps minimum pour se déplacer
        self.time_rotate = 0.2 # intervalle de temps minimum pour la rotation
        self.time_to_quick = 0.15 # intervalle de temps pour activer le mode de déplacement rapide
        self.time_before_drop = 0.3 # temps d'attente d'un arrêt à l'autre
        self.time_quick_drop = 0.01 # intervalle de temps minimum pour tomber en mode rapide
        self.time_move_quick = 0.015 # intervalle de temps minimum pour se déplacer en mode rapide
        self.time_to_straight_drop = 0.3 # Il est temps de faire un autre down straight

        # couleurs, vous pouvez le changer pour être un artiste
        self.colors = {
            'black': (0,0,0),
            'white': (255, 255, 255),
            'red'  : (255, 0, 0),
            'green': (0, 255, 0),
            'blue' : (0, 0, 255),
            'yellow': (255, 255, 0),
            'purple': (255, 0, 255),
            'cyan' : (0, 255, 255),

            'none' : (45, 45, 45),    # dark grey
            'tip'  : (100, 100, 100)  # grey
        }

        self.bg_color = (30, 30, 30) # black
        self.square_color = (245, 245, 245) # white
        self.space_color = (35, 35, 35) # slightly lighter than bg

        # formes, ne touchez pas à cela si vous n'êtes pas clair ce que cette dose
        self.shapes = (
            {'pos':([-1, 0], [0, -1], [0, 1]), 'color':'red', 'rotate':4},    # _|_
            {'pos':([-1, 0], [0, -1], [-1, 1]), 'color':'green', 'rotate':2}, # _|-
            {'pos':([-1, 0], [-1, -1], [0, 1]), 'color':'blue', 'rotate':2},  #-|_
            {'pos':([-1, 0], [-1, 1], [0, 1]), 'color':'yellow', 'rotate':1}, # ::
            {'pos':([-1, 0], [-2, 0], [1, 0]), 'color':'purple', 'rotate':2}, # |
            {'pos':([-1, -1], [0, -1], [0, 1]), 'color':'cyan', 'rotate':4},  # |__
            {'pos':([-1, 1], [0, -1], [0, 1]), 'color':'white', 'rotate':4}   # --|
        )
        self.shape_num = len(self.shapes)

        # positions
        self.square_length = 30
        self.square_num_x = 12
        self.square_num_y = 20
        self.square_space = 5
        self.new = [1, int(self.square_num_x/2)]    # upper center

        # surfaces
        self.func_width = 300
        self.game_size = self.get_game_size(self)
        self.func_size = self.get_func_size(self)
        self.screen_size = self.get_screen_size(self)
        self.screen_name = "Tetris par Mona#6669"

        # textes
        self.text_margin = 10
        self.text_adjust_factor = 5
        self.score = "Score: "
        self.score_font = "Comic Sans MS"
        self.score_size = 120
        self.score_font_adjust = 5
        self.score_color = (255, 255, 255) # blanc
        self.score_pos = (10, 10)

        self.start = "Appuyez sur n'importe quelle touche pour démarrer, appuyez sur A pour regarder l'IA jouer."
        self.start_font = "Comic Sans MS"
        self.start_size = 200
        self.start_color = (0, 255, 0) # vert
        self.start_pos = "center"
        self.start_surface = self.adjust_start_size(self)

        self.game_over = "Appuyez sur n'importe quelle touche pour démarrer, appuyez sur A pour regarder l'IA jouer."
        self.game_over_font = self.start_font
        self.game_over_size = self.start_size
        self.game_over_color = (255, 0, 0) # rouge
        self.game_over_pos = "center"
        self.game_over_surface = self.adjust_game_over_size(self)

    def adjust_for_AI(self):
        self.time_drop = 0 # période pour forcer la chute
        self.time_drop_adjust = 0 # à chaque fois que le score augmente, le temps de chute diminue de ce facteur.
        self.time_stop = 0 # temps pendant lequel le joueur peut ajuster sa position au bas de l'échelle
        self.time_move = 0 # intervalle de temps minimum pour se déplacer
        self.time_rotate = 0 # intervalle de temps minimum pour pivoter
        self.time_before_drop = 0 # temps d'attente entre un arrêt et la chute
        self.time_quick_drop = 0 # intervalle de temps minimum pour lâcher en mode rapide
        self.time_move_quick = 0 # intervalle de temps minimum pour se déplacer en mode rapide
        self.screen_name = 'Tetris par Mona#6669, AI playing...'


    @staticmethod
    def get_game_size(self):
        x = ((self.square_length + self.square_space)\
            * self.square_num_x) + self.square_space
        y = ((self.square_length + self.square_space)\
            * self.square_num_y) + self.square_space
        return (x, y)

    @staticmethod
    def get_func_size(self):
        x = self.func_width
        y = self.game_size[1]
        return (x, y)

    @staticmethod
    def get_screen_size(self):
        x = self.game_size[0] + self.func_size[0]
        y = self.game_size[1]
        return (x, y)
    
    @staticmethod
    def adjust_start_size(self):
        adjust = True  # calculer au moins une fois la surface
        while adjust:
            font = pygame.font.SysFont(self.start_font, self.start_size)
            surface = font.render(self.start, True, self.start_color)
            # ajustez la police si elle est trop grande
            adjust = ((surface.get_width() + 2 * self.text_margin) > self.screen_size[0])
            if adjust:
                self.start_size -= self.text_adjust_factor
            else:
                return surface
    
    @staticmethod
    def adjust_game_over_size(self):
        adjust = True  # calculer au moins une fois la surface
        while adjust:
            font = pygame.font.SysFont(self.game_over_font, self.game_over_size)
            surface = font.render(self.game_over, True, self.game_over_color)
            # ajustez la police si elle est trop grande
            adjust = ((surface.get_width() + 2 * self.text_margin) > self.screen_size[0])
            if adjust:
                self.game_over_size -= self.text_adjust_factor
            else:
                return surface

