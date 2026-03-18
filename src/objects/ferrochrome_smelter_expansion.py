from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/ferrochrome_smelter_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# chimney with smoke
chimney = ExpansionObject(
    id="ferrochrome_smelter_exp_chimney",
    numeric_id=417,
    name_string="STR_OBJECT_FERROCHROME_CHIMNEY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=16,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [220, 10, 64, 130, -31, -110]},
            {"sprite_expr": SMOKE, "xoffset": 7, "yoffset": 0, "zoffset": 116,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# roaster
roaster = ExpansionObject(
    id="ferrochrome_smelter_exp_roaster",
    numeric_id=418,
    name_string="STR_OBJECT_FERROCHROME_ROASTER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=14,
)
