from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/ammonia_plant_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# sp1: tall tower with smoke
chimney = ExpansionObject(
    id="ammonia_plant_exp_chimney",
    numeric_id=352,
    name_string="STR_OBJECT_AMMONIA_PLANT_CHIMNEY",
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
            {"coords": [80, 10, 64, 114, -31, -88]},
            {"sprite_expr": SMOKE, "xoffset": 5, "yoffset": 0, "zoffset": 69,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# sp6+sp5: warehouse pair (2x1)
warehouse = ExpansionObject(
    id="ammonia_plant_exp_warehouse",
    numeric_id=353,
    name_string="STR_OBJECT_AMMONIA_PLANT_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 1],
    ground_sprite=GROUND,
    height=6,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [{"coords": [430, 10, 64, 66, -31, -35]}]},  # sp6
        {"x": 1, "y": 0, "buildings": [{"coords": [360, 10, 64, 66, -31, -35]}]},  # sp5
    ],
)
