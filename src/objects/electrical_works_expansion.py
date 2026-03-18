from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/electrical_works_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# factory with smoke
factory = ExpansionObject(
    id="electrical_works_exp_factory",
    numeric_id=419,
    name_string="STR_OBJECT_ELECTRICAL_WORKS_FACTORY",
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
            {"coords": [10, 60, 64, 70, -31, -39]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 8, "zoffset": 53,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# shed
shed = ExpansionObject(
    id="electrical_works_exp_shed",
    numeric_id=420,
    name_string="STR_OBJECT_ELECTRICAL_WORKS_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 60, 64, 70, -31, -39],
    ground_sprite=GROUND,
    height=8,
)
