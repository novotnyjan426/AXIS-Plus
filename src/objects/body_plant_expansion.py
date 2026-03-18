from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/body_plant_1.png"
CLASS_ID = "AXSM"
CLASS_NAME = "STR_OBJECT_CLASS_MANUFACTURING"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# 2x1 factory: sp1 (back) + sp2 (front) — complete building
factory = ExpansionObject(
    id="body_plant_exp_factory",
    numeric_id=339,
    name_string="STR_OBJECT_BODY_PLANT_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 1],
    ground_sprite=GROUND,
    height=8,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [{"coords": [10, 60, 64, 70, -31, -35]}]},   # sp1
        {"x": 1, "y": 0, "buildings": [{"coords": [80, 60, 64, 70, -31, -35]}]},   # sp2
    ],
)

# sp4: shed with smoke
shed = ExpansionObject(
    id="body_plant_exp_shed",
    numeric_id=340,
    name_string="STR_OBJECT_BODY_PLANT_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=6,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [220, 60, 64, 51, -31, -23]},
            {"sprite_expr": SMOKE, "xoffset": -5, "yoffset": 0, "zoffset": 26,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)
