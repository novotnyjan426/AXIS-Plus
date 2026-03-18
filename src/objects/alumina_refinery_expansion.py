from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/alumina_refinery_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# chimney with smoke
chimney = ExpansionObject(
    id="alumina_refinery_exp_chimney",
    numeric_id=383,
    name_string="STR_OBJECT_ALUMINA_REFINERY_CHIMNEY",
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
            {"coords": [220, 10, 64, 128, -31, -95]},
            {"sprite_expr": SMOKE, "xoffset": 1, "yoffset": 0, "zoffset": 72,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# building
building = ExpansionObject(
    id="alumina_refinery_exp_building",
    numeric_id=384,
    name_string="STR_OBJECT_ALUMINA_REFINERY_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 64, -31, -31],
    ground_sprite=GROUND,
    height=14,
)
