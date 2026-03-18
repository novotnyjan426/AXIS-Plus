from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/phosphoric_acid_plant_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# fat chimney with smoke
chimney = ExpansionObject(
    id="phosphoric_acid_exp_chimney",
    numeric_id=371,
    name_string="STR_OBJECT_PHOSPHORIC_ACID_CHIMNEY",
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
            {"coords": [430, 10, 64, 114, -31, -83]},
            {"sprite_expr": SMOKE, "xoffset": 6, "yoffset": 0, "zoffset": 60,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# large building
building = ExpansionObject(
    id="phosphoric_acid_exp_building",
    numeric_id=372,
    name_string="STR_OBJECT_PHOSPHORIC_ACID_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 114, -31, -83],
    ground_sprite=GROUND,
    height=14,
)
