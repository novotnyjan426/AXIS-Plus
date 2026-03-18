from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/meat_packing_plant_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"
# Slow rising smoke matching original industry (white_smoke_small)
SMOKE_SLOW = "3079 + (animation_frame / 4)"

# 2x2 factory block with slow rising smoke on chimney tile (sp4)
factory_block = ExpansionObject(
    id="meat_packing_exp_factory",
    numeric_id=319,
    name_string="STR_OBJECT_MEAT_PACKING_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 2],
    ground_sprite=GROUND,
    height=12,
    animation_length=20,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [220, 10, 64, 88, -31, -58]},  # sp4 chimney
            {"sprite_expr": SMOKE_SLOW,
             "hide_sprite": "animation_frame > 19",
             "xoffset": 5, "yoffset": 8, "zoffset": "72 + animation_frame",
             "xextent": 11, "yextent": 7, "zextent": 7},
        ]},
        {"x": 0, "y": 1, "buildings": [{"coords": [290, 10, 64, 88, -31, -58]}]},  # sp5
        {"x": 1, "y": 0, "buildings": [{"coords": [360, 10, 64, 88, -31, -58]}]},  # sp6
        {"x": 1, "y": 1, "buildings": [{"coords": [430, 10, 64, 88, -31, -58]}]},  # sp7
    ],
)

tanks = ExpansionObject(
    id="meat_packing_exp_tanks",
    numeric_id=320,
    name_string="STR_OBJECT_MEAT_PACKING_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[500, 10, 64, 88, -31, -58],
    ground_sprite=GROUND,
    height=12,
)
