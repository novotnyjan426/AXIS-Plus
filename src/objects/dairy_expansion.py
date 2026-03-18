from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/dairy_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"

# Smoke expression: base game white_smoke_big sprites 3701-3708
SMOKE = "3701 + (animation_frame % 8)"

# Object 1: Back half — processing building with smoke (spritesets 7,5,6,4)
processing_block = ExpansionObject(
    id="dairy_exp_processing_block",
    numeric_id=303,
    name_string="STR_OBJECT_DAIRY_PROCESSING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 2],
    ground_sprite=GROUND,
    height=8,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        # (0,0) = sp7 with smoke (industry has smoke on this tile)
        {"x": 0, "y": 0, "buildings": [
            {"coords": [430, 10, 64, 94, -31, -43]},
            {"sprite_expr": SMOKE, "xoffset": 0, "yoffset": 12, "zoffset": 56,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
        {"x": 1, "y": 0, "buildings": [{"coords": [360, 10, 64, 94, -31, -43]}]},  # sp6
        {"x": 0, "y": 1, "buildings": [{"coords": [290, 10, 64, 94, -31, -43]}]},  # sp5
        {"x": 1, "y": 1, "buildings": [{"coords": [220, 10, 64, 94, -31, -43]}]},  # sp4
    ],
)

# Object 2: Front half — office & storage with animated flag
office_block = ExpansionObject(
    id="dairy_exp_office_block",
    numeric_id=304,
    name_string="STR_OBJECT_DAIRY_OFFICE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 2],
    ground_sprite=GROUND,
    height=12,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [{"coords": [500, 10, 64, 94, -31, -63]}]},  # sp8
        {"x": 1, "y": 0, "buildings": [{"coords": [10, 10, 64, 94, -31, -63]}]},   # sp1
        {"x": 0, "y": 1, "buildings": [{"coords": [150, 10, 64, 94, -31, -62]}]},  # sp3
        # sp2 base + animated flag overlay
        {"x": 1, "y": 1, "buildings": [
            {"coords": [80, 10, 64, 94, -31, -63]},
            {"anim_coords": [
                [220, 120, 64, 64, -31, -65],
                [10, 120, 64, 64, -31, -65],
                [80, 120, 64, 64, -31, -65],
                [150, 120, 64, 64, -31, -65],
                [80, 120, 64, 64, -31, -65],
                [10, 120, 64, 64, -31, -65],
            ]},
        ]},
    ],
)
