from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/latex_processor_1.png"
CLASS_ID = "AXSX"
CLASS_NAME = "STR_OBJECT_CLASS_OTHER_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Factory with smoke
factory = ExpansionObject(
    id="latex_processor_exp_factory",
    numeric_id=441,
    name_string="STR_OBJECT_LATEX_PROCESSOR_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=10,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [150, 60, 64, 90, -31, -59]},
            {"sprite_expr": SMOKE, "xoffset": 13, "yoffset": 0, "zoffset": 54,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# Static building
building = ExpansionObject(
    id="latex_processor_exp_building",
    numeric_id=442,
    name_string="STR_OBJECT_LATEX_PROCESSOR_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 60, 64, 90, -31, -71],
    ground_sprite=GROUND,
    height=10,
)
