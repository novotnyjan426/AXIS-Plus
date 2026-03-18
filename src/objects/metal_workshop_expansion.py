from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/metal_workshop_1.png"
CLASS_ID = "AXSM"
CLASS_NAME = "STR_OBJECT_CLASS_MANUFACTURING"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# sp1: workshop with smoke
workshop = ExpansionObject(
    id="metal_workshop_exp_workshop",
    numeric_id=350,
    name_string="STR_OBJECT_METAL_WORKSHOP_BUILDING",
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
            {"coords": [10, 60, 64, 70, -31, -39]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 8, "zoffset": 53,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# sp3: shed
shed = ExpansionObject(
    id="metal_workshop_exp_shed",
    numeric_id=351,
    name_string="STR_OBJECT_METAL_WORKSHOP_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 60, 64, 51, -31, -20],
    ground_sprite=GROUND,
    height=6,
)
