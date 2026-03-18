from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/cement_plant_1.png"
CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Chimney with smoke
chimney = ExpansionObject(
    id="cement_plant_exp_chimney",
    numeric_id=425,
    name_string="STR_OBJECT_CEMENT_PLANT_CHIMNEY",
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
            {"coords": [80, 10, 64, 113, -31, -82]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 0, "zoffset": 81,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static building
building = ExpansionObject(
    id="cement_plant_exp_building",
    numeric_id=426,
    name_string="STR_OBJECT_CEMENT_PLANT_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 113, -31, -82],
    ground_sprite=GROUND,
    height=14,
)
