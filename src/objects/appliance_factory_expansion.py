from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/appliance_factory_1.png"
CLASS_ID = "AXSM"
CLASS_NAME = "STR_OBJECT_CLASS_MANUFACTURING"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# sp6: chimney building with smoke
chimney = ExpansionObject(
    id="appliance_factory_exp_chimney",
    numeric_id=333,
    name_string="STR_OBJECT_APPLIANCE_FACTORY_CHIMNEY",
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
            {"coords": [360, 10, 64, 80, -31, -49]},
            {"sprite_expr": SMOKE, "xoffset": 13, "yoffset": 0, "zoffset": 56,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# sp3: offices
offices = ExpansionObject(
    id="appliance_factory_exp_offices",
    numeric_id=334,
    name_string="STR_OBJECT_APPLIANCE_FACTORY_OFFICES",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 80, -31, -49],
    ground_sprite=GROUND,
    height=10,
)

# sp7: middle assembly hall
warehouse = ExpansionObject(
    id="appliance_factory_exp_warehouse",
    numeric_id=335,
    name_string="STR_OBJECT_APPLIANCE_FACTORY_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 80, -31, -49],
    ground_sprite=GROUND,
    height=10,
)
