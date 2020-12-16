class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.map = []
        self.game_state = GameState.NONE
        self.camera = [0, 0]

    def set_up(self):
        self.objects.append(player)
        self.game_state = GameState.RUNNING
        self.load_map(f"LV0")

    def update(self):
        # clear screen first
        self.screen.fill(config.BG)
        # print("update")
        # handle all events related to the object
        self.render_map(self.screen)

    def load_map(self, file_name):
        self.map = []
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)

    def render_map(self, screen):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE - (self.camera[0] * con$
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1
