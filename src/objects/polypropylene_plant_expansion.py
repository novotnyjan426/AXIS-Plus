from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/polypropylene_plant_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# sp1: tall tower with smoke
tower = ExpansionObject(
    id="polypropylene_plant_exp_tower",
    numeric_id=377,
    name_string="STR_OBJECT_POLYPROPYLENE_PLANT_TOWER",
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

# sp5: low tanks
tanks = ExpansionObject(
    id="polypropylene_plant_exp_tanks",
    numeric_id=378,
    name_string="STR_OBJECT_POLYPROPYLENE_PLANT_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 66, -31, -35],
    ground_sprite=GROUND,
    height=6,
)
