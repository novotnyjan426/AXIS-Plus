from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/ethylene_cracker_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# drop tower with smoke
chimney = ExpansionObject(
    id="ethylene_cracker_exp_chimney",
    numeric_id=363,
    name_string="STR_OBJECT_ETHYLENE_CRACKER_CHIMNEY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=14,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [290, 10, 64, 114, -31, -83]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 0, "zoffset": 81,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# frac columns
columns = ExpansionObject(
    id="ethylene_cracker_exp_columns",
    numeric_id=364,
    name_string="STR_OBJECT_ETHYLENE_CRACKER_COLUMNS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 114, -31, -83],
    ground_sprite=GROUND,
    height=14,
)
