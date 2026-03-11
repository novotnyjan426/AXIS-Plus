from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/soda_ash_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "2022"  # GROUNDTILE_MUD_TRACKS

# Animated headgear — 3 frames
headgear = ExpansionObject(
    id="soda_ash_exp_headgear",
    numeric_id=185,
    name_string="STR_OBJECT_SODA_ASH_HEADGEAR",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    animation_frames=[
        [10, 160, 64, 122, -31, -88],
        [80, 160, 64, 122, -31, -88],
        [150, 160, 64, 122, -31, -88],
    ],
    animation_speed=2,
    ground_sprite=GROUND,
    height=16,
)

crusher = ExpansionObject(
    id="soda_ash_exp_crusher",
    numeric_id=186,
    name_string="STR_OBJECT_SODA_ASH_CRUSHER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    height=16,
    animation_length=8,
    animation_speed=3,
    buildings=[
        {"file": SPRITE_FILE, "coords": [10, 10, 64, 122, -31, -90]},
        {"base_sprite": "3701 + (animation_frame % 8)", "xoffset": 3, "yoffset": 0, "zoffset": 73,
         "xextent": 15, "yextent": 7, "zextent": 7},
        {"base_sprite": "3701 + ((animation_frame + 1) % 8)", "xoffset": 12, "yoffset": 20, "zoffset": 45,
         "xextent": 15, "yextent": 7, "zextent": 7},
    ],
)

winding_house = ExpansionObject(
    id="soda_ash_exp_winding_house",
    numeric_id=187,
    name_string="STR_OBJECT_SODA_ASH_WINDING_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=16,
)

silos = ExpansionObject(
    id="soda_ash_exp_silos",
    numeric_id=188,
    name_string="STR_OBJECT_SODA_ASH_SILOS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 122, -31, -88],
    ground_sprite=GROUND,
    height=16,
)

soda_ash_pile = ExpansionObject(
    id="soda_ash_exp_pile",
    numeric_id=189,
    name_string="STR_OBJECT_SODA_ASH_PILE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
)

soda_ash_pile_small = ExpansionObject(
    id="soda_ash_exp_pile_small",
    numeric_id=190,
    name_string="STR_OBJECT_SODA_ASH_PILE_SMALL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
)

truck = ExpansionObject(
    id="soda_ash_exp_truck",
    numeric_id=191,
    name_string="STR_OBJECT_SODA_ASH_TRUCK",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[570, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=4,
)
