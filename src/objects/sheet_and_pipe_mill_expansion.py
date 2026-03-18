from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/sheet_and_pipe_mill_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# factory with smoke
factory = ExpansionObject(
    id="sheet_and_pipe_mill_exp_factory",
    numeric_id=403,
    name_string="STR_OBJECT_SHEET_PIPE_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=8,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [10, 10, 64, 64, -31, -34]},
            {"sprite_expr": SMOKE, "xoffset": -5, "yoffset": 0, "zoffset": 39,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# workshop
workshop = ExpansionObject(
    id="sheet_and_pipe_mill_exp_workshop",
    numeric_id=404,
    name_string="STR_OBJECT_SHEET_PIPE_WORKSHOP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 64, -31, -33],
    ground_sprite=GROUND,
    height=8,
)
