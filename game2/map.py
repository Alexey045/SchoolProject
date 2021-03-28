from pytmx import load_pygame


class Map:  # class for tiled map editor
    def __init__(self, filename, DATAFILE):
        self.map = load_pygame(f"{DATAFILE}/{filename}")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_height = self.map.tileheight
        self.tile_width = self.map.tilewidth

    def get_tile_id(self, pos):
        return self.map.tiledgidmap[self.map.get_tile_gid(*pos, 0)]

    def change_map(self, map_name, DATAFILE):
        self.map = load_pygame(f"{DATAFILE}/{map_name}")

    def get_rect_tiles(self):  # ToDo
        count = 1
        dict_tiles = {}
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                if image is not None:
                    img_rect = image.get_rect().move(x * self.tile_width, y * self.tile_height)
                    dict_tiles[count] = img_rect
                    count += 1
        return dict_tiles

    def render(self,
               screen):  # ToDo вынеси имаге в отдельный метод, не надо просчитывать каждый раз, я думаю
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                if image is not None:
                    image = image.convert()
                    screen.blit(image, (x * self.tile_width, y * self.tile_height))
