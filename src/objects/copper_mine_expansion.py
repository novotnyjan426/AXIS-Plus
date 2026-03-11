from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/copper_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "2022"  # GROUNDTILE_MUD_TRACKS

# 1x1 objects — individual copper mine sprites
# Same sprite sheet layout as iron_ore_mine, but different PNG (copper colors)

# Animated headgear — 3 frames
headgear = ExpansionObject(
    id="copper_exp_headgear",
    numeric_id=50,
    name_string="STR_OBJECT_COPPER_HEADGEAR",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    animation_frames=[
        [10, 310, 64, 122, -31, -88],
        [80, 310, 64, 122, -31, -88],
        [150, 310, 64, 122, -31, -88],
    ],
    animation_speed=3,
    ground_sprite=GROUND,
    height=16,
)

crusher = ExpansionObject(
    id="copper_exp_crusher",
    numeric_id=51,
    name_string="STR_OBJECT_COPPER_CRUSHER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=16,
)

winding_house = ExpansionObject(
    id="copper_exp_winding_house",
    numeric_id=52,
    name_string="STR_OBJECT_COPPER_WINDING_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=16,
)

boiler_house = ExpansionObject(
    id="copper_exp_boiler_house",
    numeric_id=53,
    name_string="STR_OBJECT_COPPER_BOILER_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[500, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=16,
)

exit_shed = ExpansionObject(
    id="copper_exp_exit_shed",
    numeric_id=54,
    name_string="STR_OBJECT_COPPER_EXIT_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=12,
)

# Animated exit trestle — 16 unique frames of conveyor belt
exit_trestle = ExpansionObject(
    id="copper_exp_exit_trestle",
    numeric_id=55,
    name_string="STR_OBJECT_COPPER_EXIT_TRESTLE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    animation_frames=[
        [10, 160, 64, 122, -31, -88],
        [80, 160, 64, 122, -31, -88],
        [150, 160, 64, 122, -31, -88],
        [220, 160, 64, 122, -31, -88],
        [290, 160, 64, 122, -31, -88],
        [360, 160, 64, 122, -31, -88],
        [430, 160, 64, 122, -31, -88],
        [500, 160, 64, 122, -31, -88],
        [570, 160, 64, 122, -31, -88],
        [640, 160, 64, 122, -31, -88],
        [710, 160, 64, 122, -31, -88],
        [780, 160, 64, 122, -31, -88],
        [850, 160, 64, 122, -31, -88],
        [920, 160, 64, 122, -31, -88],
        [990, 160, 64, 122, -31, -88],
        [1060, 160, 64, 122, -31, -88],
    ],
    animation_speed=2,
    ground_sprite=GROUND,
    height=12,
)

ore_truck = ExpansionObject(
    id="copper_exp_ore_truck",
    numeric_id=56,
    name_string="STR_OBJECT_COPPER_ORE_TRUCK",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=4,
)

ore_pile_front = ExpansionObject(
    id="copper_exp_pile_front",
    numeric_id=57,
    name_string="STR_OBJECT_COPPER_ORE_PILE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
)

ore_pile_rear = ExpansionObject(
    id="copper_exp_pile_rear",
    numeric_id=58,
    name_string="STR_OBJECT_COPPER_ORE_PILE_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
)
