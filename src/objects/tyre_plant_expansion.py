from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/tyre_plant_1.png"
CLASS_ID = "AXSX"
CLASS_NAME = "STR_OBJECT_CLASS_OTHER_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Factory with smoke
factory = ExpansionObject(
    id="tyre_plant_exp_factory",
    numeric_id=451,
    name_string="STR_OBJECT_TYRE_PLANT_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=10,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [220, 10, 64, 90, -31, -58]},
            {"sprite_expr": SMOKE, "xoffset": -3, "yoffset": 0, "zoffset": 54,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static building
building = ExpansionObject(
    id="tyre_plant_exp_building",
    numeric_id=452,
    name_string="STR_OBJECT_TYRE_PLANT_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 90, -31, -58],
    ground_sprite=GROUND,
    height=10,
)
