from objects import registered_objects


class ExpansionObject:
    """A simple placeable object for FEAT_OBJECTS in NML."""

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.numeric_id = kwargs["numeric_id"]
        self.name_string = kwargs["name_string"]
        self.class_id = kwargs["class_id"]
        self.class_name_string = kwargs["class_name_string"]
        self.size = kwargs.get("size", [1, 1])
        self.build_cost_multiplier = kwargs.get("build_cost_multiplier", 51)
        self.remove_cost_multiplier = kwargs.get("remove_cost_multiplier", 255)
        self.introduction_date = kwargs.get("introduction_date", "date(1900, 1, 1)")
        self.views = kwargs.get("views", 1)
        self.height = kwargs.get("height", 4)
        self.ground_sprite = kwargs.get("ground_sprite", "GROUNDSPRITE_CONCRETE")
        # single sprite mode: one spriteset + one building
        self.sprite_file = kwargs.get("sprite_file", None)
        self.sprite_coords = kwargs.get("sprite_coords", None)
        # multi-building mode: list of dicts with file, coords, and world offsets
        # each dict: {file, coords, xoffset, yoffset, zoffset, xextent, yextent, zextent}
        self.buildings = kwargs.get("buildings", None)
        # animation: list of sprite coord lists (one per frame)
        # if set, the spriteset has multiple frames and animation properties are added
        self.animation_frames = kwargs.get("animation_frames", None)
        self.animation_speed = kwargs.get("animation_speed", 3)
        # multi-tile mode: list of tile dicts for per-tile spritelayouts
        # each dict: {x, y, sprite: [x,y,w,h,xoff,yoff], buildings: [...]}
        self.tile_grid = kwargs.get("tile_grid", None)
        # allow placement on water tiles
        self.allow_on_water = kwargs.get("allow_on_water", False)

    def get_flags(self):
        flags = ["OBJ_FLAG_ANYTHING_REMOVE", "OBJ_FLAG_REMOVE_IS_INCOME"]
        if self.has_animation():
            flags.append("OBJ_FLAG_ANIMATED")
        if self.allow_on_water:
            flags.append("OBJ_FLAG_ON_WATER")
        return "bitmask(" + ", ".join(flags) + ")"

    def has_custom_sprite(self):
        return self.sprite_file is not None and self.sprite_coords is not None

    def has_multi_buildings(self):
        return self.buildings is not None and len(self.buildings) > 0

    def has_animation(self):
        return self.animation_frames is not None and len(self.animation_frames) > 1

    def has_tile_grid(self):
        return self.tile_grid is not None and len(self.tile_grid) > 0

    def tile_grid_items(self):
        """Return tile_grid items with switch_val computed for NML switch."""
        result = []
        for tile in self.tile_grid:
            # FEAT_OBJECTS var[0x40]: bits 0-7 = relative X, bits 8-15 = relative Y
            val = (tile["y"] << 8) | tile["x"]
            result.append({**tile, "switch_val": val})
        return result

    def preview_tile(self):
        """Return the first tile with buildings for use as purchase preview."""
        if not self.tile_grid:
            return None
        for tile in self.tile_grid:
            if tile.get('buildings'):
                return tile
        for tile in self.tile_grid:
            if tile.get('sprite'):
                return tile
        return self.tile_grid[0]

    def animation_frame_count(self):
        if self.animation_frames:
            return len(self.animation_frames)
        return 0

    def register(self):
        registered_objects.append(self)
