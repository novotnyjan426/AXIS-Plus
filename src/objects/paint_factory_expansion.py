from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/paint_factory_1.png"
CLASS_ID = "AXSX"
CLASS_NAME = "STR_OBJECT_CLASS_OTHER_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Factory with smoke
factory = ExpansionObject(
    id="paint_factory_exp_factory",
    numeric_id=445,
    name_string="STR_OBJECT_PAINT_FACTORY_BUILDING",
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

# Static shed
shed = ExpansionObject(
    id="paint_factory_exp_shed",
    numeric_id=446,
    name_string="STR_OBJECT_PAINT_FACTORY_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 60, 64, 55, -31, -24],
    ground_sprite=GROUND,
    height=6,
)
