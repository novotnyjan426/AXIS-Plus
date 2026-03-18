from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/fischer_tropsch_plant_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# quench tower with smoke
quench_tower = ExpansionObject(
    id="fischer_tropsch_exp_tower",
    numeric_id=367,
    name_string="STR_OBJECT_FISCHER_TROPSCH_TOWER",
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
            {"coords": [570, 10, 64, 122, -31, -91]},
            {"sprite_expr": SMOKE, "xoffset": 8, "yoffset": 5, "zoffset": 104,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# oven battery
oven = ExpansionObject(
    id="fischer_tropsch_exp_oven",
    numeric_id=368,
    name_string="STR_OBJECT_FISCHER_TROPSCH_OVEN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 122, -31, -91],
    ground_sprite=GROUND,
    height=14,
)
