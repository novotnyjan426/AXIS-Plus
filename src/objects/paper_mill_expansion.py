from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/paper_mill_1.png"
CLASS_ID = "AXSX"
CLASS_NAME = "STR_OBJECT_CLASS_OTHER_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Chimney with smoke
chimney = ExpansionObject(
    id="paper_mill_exp_chimney",
    numeric_id=443,
    name_string="STR_OBJECT_PAPER_MILL_CHIMNEY",
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
            {"coords": [220, 84, 64, 120, -31, -89]},
            {"sprite_expr": SMOKE, "xoffset": 10, "yoffset": 0, "zoffset": 93,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static building
building = ExpansionObject(
    id="paper_mill_exp_building",
    numeric_id=444,
    name_string="STR_OBJECT_PAPER_MILL_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 84, 64, 120, -31, -89],
    ground_sprite=GROUND,
    height=14,
)
