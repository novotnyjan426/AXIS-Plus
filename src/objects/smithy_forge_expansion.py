from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/smithy_forge_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# forge with smoke
forge = ExpansionObject(
    id="smithy_forge_exp_forge",
    numeric_id=415,
    name_string="STR_OBJECT_SMITHY_FORGE_BUILDING",
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
            {"coords": [10, 10, 64, 80, -31, -49]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 1, "zoffset": 44,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# workshop
workshop = ExpansionObject(
    id="smithy_forge_exp_workshop",
    numeric_id=416,
    name_string="STR_OBJECT_SMITHY_FORGE_WORKSHOP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 80, -31, -49],
    ground_sprite=GROUND,
    height=10,
)
