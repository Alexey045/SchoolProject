from pytmx import load_pygame


class Map:  # class for tiled map editor
    def __init__(self, filename, DATAFILE):
        self.dict_tiles = {}
        self.map = load_pygame(f"{DATAFILE}/{filename}")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_height = self.map.tileheight
        self.tile_width = self.map.tilewidth
        self.tile_images_coordinates = {}

    def get_tile_id(self, pos):
        return self.map.tiledgidmap[self.map.get_tile_gid(*pos, 0)]

    def change_map(self, map_name, DATAFILE):
        self.map = load_pygame(f"{DATAFILE}/{map_name}")

    def get_rect_tiles(self):  # ToDo
        count = 1
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                if image is not None:
                    img_rect = image.get_rect().move(x * self.tile_width, y * self.tile_height)
                    self.dict_tiles[count] = img_rect
                    count += 1
        return self.dict_tiles

    def render(self, screen):
        for image in self.tile_images_coordinates:
            screen.blit(image, self.tile_images_coordinates[image])

    def convert_images(self):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                if image is not None:
                    self.tile_images_coordinates[image.convert()] = [x * self.tile_width,
                                                                     y * self.tile_height]
