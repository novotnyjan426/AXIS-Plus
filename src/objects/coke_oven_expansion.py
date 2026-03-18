from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/coke_oven_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# quench tower with smoke
quench_tower = ExpansionObject(
    id="coke_oven_exp_tower",
    numeric_id=413,
    name_string="STR_OBJECT_COKE_OVEN_TOWER",
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
            {"coords": [570, 10, 64, 122, -31, -91]},
            {"sprite_expr": SMOKE, "xoffset": 8, "yoffset": 5, "zoffset": 104,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# silo
silo = ExpansionObject(
    id="coke_oven_exp_silo",
    numeric_id=414,
    name_string="STR_OBJECT_COKE_OVEN_SILO",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 122, -31, -91],
    ground_sprite=GROUND,
    height=14,
)
