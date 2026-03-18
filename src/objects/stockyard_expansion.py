from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/stockyard_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"

# Smoke expression: base game white_smoke_big sprites 3701-3708
SMOKE = "3701 + (animation_frame % 8)"

# Stockyard — main factory is a 2x3 block matching layout_1 rows 3-4, cols 1-3
factory = ExpansionObject(
    id="stockyard_exp_factory",
    numeric_id=300,
    name_string="STR_OBJECT_STOCKYARD_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 3],
    ground_sprite=GROUND,
    height=16,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        # Back row (x=0) — sp5 chimney has smoke
        {"x": 0, "y": 0, "buildings": [
            {"coords": [290, 10, 64, 104, -31, -73]},   # sp5 chimney building
            {"sprite_expr": SMOKE, "xoffset": 17, "yoffset": 9, "zoffset": 99,
             "xextent": 15, "yextent": 7, "zextent": 7},
            {"sprite_expr": SMOKE, "xoffset": 20, "yoffset": 9, "zoffset": 100,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
        {"x": 0, "y": 1, "buildings": [{"coords": [360, 10, 64, 91, -31, -60]}]},    # sp6
        {"x": 0, "y": 2, "buildings": [{"coords": [430, 10, 64, 98, -31, -67]}]},    # sp7
        # Front row (x=1)
        {"x": 1, "y": 0, "buildings": [{"coords": [80, 10, 64, 74, -31, -43]}]},     # sp2
        {"x": 1, "y": 1, "buildings": [{"coords": [150, 10, 64, 88, -31, -57]}]},    # sp3
        {"x": 1, "y": 2, "buildings": [{"coords": [220, 10, 64, 85, -31, -54]}]},    # sp4
    ],
)

# Outbuildings — 2x2 compound
outbuildings = ExpansionObject(
    id="stockyard_exp_outbuildings",
    numeric_id=301,
    name_string="STR_OBJECT_STOCKYARD_COLD_STORAGE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 2],
    ground_sprite=GROUND,
    height=10,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [{"coords": [640, 10, 64, 32, -31, -1]}]},    # sp10
        {"x": 0, "y": 1, "buildings": [{"coords": [710, 10, 64, 49, -31, -18]}]},   # sp11
        {"x": 1, "y": 0, "buildings": [{"coords": [500, 10, 64, 54, -31, -23]}]},   # sp8
        {"x": 1, "y": 1, "buildings": [{"coords": [570, 10, 64, 76, -31, -45]}]},   # sp9
    ],
)
