from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/iron_works_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# factory with smoke
factory = ExpansionObject(
    id="iron_works_exp_factory",
    numeric_id=399,
    name_string="STR_OBJECT_IRON_WORKS_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=8,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [10, 10, 64, 70, -31, -40]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 4, "zoffset": 23,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# shed
shed = ExpansionObject(
    id="iron_works_exp_shed",
    numeric_id=400,
    name_string="STR_OBJECT_IRON_WORKS_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 70, -31, -39],
    ground_sprite=GROUND,
    height=8,
)
