from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/lime_kiln_1.png"
CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Kiln with smoke
kiln = ExpansionObject(
    id="lime_kiln_exp_kiln",
    numeric_id=431,
    name_string="STR_OBJECT_LIME_KILN_BUILDING",
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
            {"coords": [10, 10, 64, 110, -31, -70]},
            {"sprite_expr": SMOKE, "xoffset": 10, "yoffset": 5, "zoffset": 73,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static shed
shed = ExpansionObject(
    id="lime_kiln_exp_shed",
    numeric_id=432,
    name_string="STR_OBJECT_LIME_KILN_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 92, -31, -60],
    ground_sprite=GROUND,
    height=10,
)
