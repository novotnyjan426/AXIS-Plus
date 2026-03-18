from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/blast_furnace_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# furnace with smoke
furnace = ExpansionObject(
    id="blast_furnace_exp_furnace",
    numeric_id=389,
    name_string="STR_OBJECT_BLAST_FURNACE_BUILDING",
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
            {"coords": [80, 10, 64, 122, -31, -91]},
            {"sprite_expr": SMOKE, "xoffset": 5, "yoffset": 6, "zoffset": 68,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# building
building = ExpansionObject(
    id="blast_furnace_exp_building",
    numeric_id=390,
    name_string="STR_OBJECT_BLAST_FURNACE_BRICK",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 122, -31, -91],
    ground_sprite=GROUND,
    height=14,
)
