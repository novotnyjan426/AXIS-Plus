from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/textile_mill_1.png"
CLASS_ID = "AXSX"
CLASS_NAME = "STR_OBJECT_CLASS_OTHER_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Chimney with smoke
chimney = ExpansionObject(
    id="textile_mill_exp_chimney",
    numeric_id=453,
    name_string="STR_OBJECT_TEXTILE_MILL_CHIMNEY",
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
            {"coords": [10, 60, 64, 103, -31, -74]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 9, "zoffset": 78,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static warehouse
warehouse = ExpansionObject(
    id="textile_mill_exp_warehouse",
    numeric_id=454,
    name_string="STR_OBJECT_TEXTILE_MILL_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 60, 64, 103, -31, -72],
    ground_sprite=GROUND,
    height=12,
)
