from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/basic_oxygen_furnace_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# furnace with smoke
furnace = ExpansionObject(
    id="basic_oxygen_furnace_exp_furnace",
    numeric_id=387,
    name_string="STR_OBJECT_BOF_FURNACE",
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
            {"coords": [220, 10, 64, 122, -31, -90]},
            {"sprite_expr": SMOKE, "xoffset": 1, "yoffset": 0, "zoffset": 61,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# tanks
tanks = ExpansionObject(
    id="basic_oxygen_furnace_exp_tanks",
    numeric_id=388,
    name_string="STR_OBJECT_BOF_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=14,
)
