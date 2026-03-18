from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/cider_mill_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Building with chimney + fast smoke
chimney = ExpansionObject(
    id="cider_mill_exp_chimney",
    numeric_id=321,
    name_string="STR_OBJECT_CIDER_MILL_CHIMNEY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=16,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [80, 10, 64, 114, -31, -83]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 9, "zoffset": 50,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

building = ExpansionObject(
    id="cider_mill_exp_building",
    numeric_id=322,
    name_string="STR_OBJECT_CIDER_MILL_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 114, -31, -83],
    ground_sprite=GROUND,
    height=16,
)

tanks = ExpansionObject(
    id="cider_mill_exp_tanks",
    numeric_id=323,
    name_string="STR_OBJECT_CIDER_MILL_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 114, -31, -83],
    ground_sprite=GROUND,
    height=16,
)
