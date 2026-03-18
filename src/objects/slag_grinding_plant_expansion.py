from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/slag_grinding_plant_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# tower with smoke
tower = ExpansionObject(
    id="slag_grinding_plant_exp_tower",
    numeric_id=405,
    name_string="STR_OBJECT_SLAG_GRINDING_TOWER",
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
            {"coords": [150, 10, 64, 120, -31, -89]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 2, "zoffset": 76,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# silos
silos = ExpansionObject(
    id="slag_grinding_plant_exp_silos",
    numeric_id=406,
    name_string="STR_OBJECT_SLAG_GRINDING_SILOS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 120, -31, -89],
    ground_sprite=GROUND,
    height=14,
)
