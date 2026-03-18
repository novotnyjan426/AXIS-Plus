from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/brick_works_1.png"
CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Kiln with smoke
kiln = ExpansionObject(
    id="brick_works_exp_kiln",
    numeric_id=421,
    name_string="STR_OBJECT_BRICK_WORKS_KILN",
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
            {"coords": [150, 10, 64, 101, -31, -71]},
            {"sprite_expr": SMOKE, "xoffset": 8, "yoffset": 0, "zoffset": 70,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static building
building = ExpansionObject(
    id="brick_works_exp_building",
    numeric_id=422,
    name_string="STR_OBJECT_BRICK_WORKS_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 101, -31, -64],
    ground_sprite=GROUND,
    height=12,
)
