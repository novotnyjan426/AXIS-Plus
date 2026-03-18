from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/sugar_refinery_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Split into 4 individual tiles

# sp5: chimney building with smoke
chimney = ExpansionObject(
    id="sugar_refinery_exp_chimney",
    numeric_id=324,
    name_string="STR_OBJECT_SUGAR_REFINERY_CHIMNEY",
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
            {"coords": [290, 10, 64, 88, -31, -58]},
            {"sprite_expr": SMOKE, "xoffset": 5, "yoffset": 8, "zoffset": 72,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# sp3: white factory building
factory = ExpansionObject(
    id="sugar_refinery_exp_factory",
    numeric_id=325,
    name_string="STR_OBJECT_SUGAR_REFINERY_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 88, -31, -56],
    ground_sprite=GROUND,
    height=12,
)

# sp6: red brick building
brick_building = ExpansionObject(
    id="sugar_refinery_exp_brick",
    numeric_id=330,
    name_string="STR_OBJECT_SUGAR_REFINERY_BRICK",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 88, -31, -58],
    ground_sprite=GROUND,
    height=12,
)

# sp4: silos
silos = ExpansionObject(
    id="sugar_refinery_exp_silos",
    numeric_id=331,
    name_string="STR_OBJECT_SUGAR_REFINERY_SILOS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 88, -31, -58],
    ground_sprite=GROUND,
    height=12,
)
