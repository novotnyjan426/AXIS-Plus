from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/biorefinery_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# sp5+sp6: refinery tower pair (1x2), smoke on sp6
tower = ExpansionObject(
    id="biorefinery_exp_tower",
    numeric_id=354,
    name_string="STR_OBJECT_BIOREFINERY_TOWER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 2],
    ground_sprite=GROUND,
    height=12,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [{"coords": [150, 10, 64, 88, -31, -59]}]},  # sp5
        {"x": 0, "y": 1, "buildings": [
            {"coords": [220, 10, 64, 88, -31, -64]},
            {"sprite_expr": SMOKE, "xoffset": 1, "yoffset": 0, "zoffset": 62,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},  # sp6
    ],
)

# sp7: medium building
building = ExpansionObject(
    id="biorefinery_exp_building",
    numeric_id=355,
    name_string="STR_OBJECT_BIOREFINERY_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 73, -31, -45],
    ground_sprite=GROUND,
    height=8,
)
