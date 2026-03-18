from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/steel_mill_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# factory
factory = ExpansionObject(
    id="steel_mill_exp_factory",
    numeric_id=407,
    name_string="STR_OBJECT_STEEL_MILL_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 60, 64, 70, -31, -35],
    ground_sprite=GROUND,
    height=8,
)

# shed with smoke
shed = ExpansionObject(
    id="steel_mill_exp_shed",
    numeric_id=408,
    name_string="STR_OBJECT_STEEL_MILL_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=6,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [220, 60, 64, 51, -31, -23]},
            {"sprite_expr": SMOKE, "xoffset": -5, "yoffset": 0, "zoffset": 26,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)
