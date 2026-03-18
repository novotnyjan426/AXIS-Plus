from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/recycling_plant_1.png"
CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Building with smoke
building = ExpansionObject(
    id="recycling_plant_exp_building",
    numeric_id=437,
    name_string="STR_OBJECT_RECYCLING_PLANT_BUILDING",
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
            {"coords": [80, 10, 64, 76, -31, -45]},
            {"sprite_expr": SMOKE, "xoffset": -5, "yoffset": 0, "zoffset": 40,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static shed
shed = ExpansionObject(
    id="recycling_plant_exp_shed",
    numeric_id=438,
    name_string="STR_OBJECT_RECYCLING_PLANT_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 63, -31, -32],
    ground_sprite=GROUND,
    height=8,
)
