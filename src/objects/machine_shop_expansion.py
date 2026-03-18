from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/machine_shop_1.png"
CLASS_ID = "AXSM"
CLASS_NAME = "STR_OBJECT_CLASS_MANUFACTURING"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# sp9: tall red brick building with chimney + smoke
chimney = ExpansionObject(
    id="machine_shop_exp_chimney",
    numeric_id=347,
    name_string="STR_OBJECT_MACHINE_SHOP_CHIMNEY",
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
            {"coords": [570, 10, 64, 85, -31, -54]},
            {"sprite_expr": SMOKE, "xoffset": 13, "yoffset": 0, "zoffset": 60,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# sp7: large red brick warehouse
workshop = ExpansionObject(
    id="machine_shop_exp_workshop",
    numeric_id=348,
    name_string="STR_OBJECT_MACHINE_SHOP_WORKSHOP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 78, -31, -47],
    ground_sprite=GROUND,
    height=10,
)

# sp5: red brick factory building
shed = ExpansionObject(
    id="machine_shop_exp_shed",
    numeric_id=349,
    name_string="STR_OBJECT_MACHINE_SHOP_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 78, -31, -47],
    ground_sprite=GROUND,
    height=10,
)
