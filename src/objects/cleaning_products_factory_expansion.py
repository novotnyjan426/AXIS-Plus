from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/cleaning_products_factory_1.png"
CLASS_ID = "AXSX"
CLASS_NAME = "STR_OBJECT_CLASS_OTHER_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Chimney with smoke
chimney = ExpansionObject(
    id="cleaning_products_exp_chimney",
    numeric_id=447,
    name_string="STR_OBJECT_CLEANING_PRODUCTS_CHIMNEY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=12,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [430, 10, 64, 94, -31, -43]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 12, "zoffset": 56,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static building
building = ExpansionObject(
    id="cleaning_products_exp_building",
    numeric_id=448,
    name_string="STR_OBJECT_CLEANING_PRODUCTS_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 94, -31, -63],
    ground_sprite=GROUND,
    height=12,
)
