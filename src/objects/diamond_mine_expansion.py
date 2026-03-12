from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/diamond_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "2022"  # GROUNDTILE_MUD_TRACKS

# Diamond mine has different sprite coords from other underground mines
# Headgear at y=160 instead of y=310, no exit_trestle

headgear = ExpansionObject(
    id="diamond_exp_headgear",
    numeric_id=245,
    name_string="STR_OBJECT_DIAMOND_HEADGEAR",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    animation_frames=[
        [10, 160, 64, 122, -31, -88],
        [80, 160, 64, 122, -31, -88],
        [150, 160, 64, 122, -31, -88],
    ],
    animation_speed=3,
    ground_sprite=GROUND,
    height=16,
)

winding_house = ExpansionObject(
    id="diamond_exp_winding_house",
    numeric_id=246,
    name_string="STR_OBJECT_DIAMOND_WINDING_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=16,
)

vents_shed = ExpansionObject(
    id="diamond_exp_vents_shed",
    numeric_id=247,
    name_string="STR_OBJECT_DIAMOND_VENTS_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=12,
)
