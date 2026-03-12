from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/potash_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "2022"  # GROUNDTILE_MUD_TRACKS

headgear = ExpansionObject(
    id="potash_exp_headgear",
    numeric_id=240,
    name_string="STR_OBJECT_POTASH_HEADGEAR",
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

winding_house = ExpansionObject(
    id="potash_exp_winding_house",
    numeric_id=241,
    name_string="STR_OBJECT_POTASH_WINDING_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=16,
)

exit_trestle = ExpansionObject(
    id="potash_exp_exit_trestle",
    numeric_id=242,
    name_string="STR_OBJECT_POTASH_EXIT_TRESTLE",
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

ore_pile = ExpansionObject(
    id="potash_exp_ore_pile",
    numeric_id=243,
    name_string="STR_OBJECT_POTASH_ORE_PILE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
)
