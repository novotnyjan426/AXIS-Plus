from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/oil_wells_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "2022"  # GROUNDTILE_MUD_TRACKS

# Oil pump jack — animated, cycles TTD base sprites 2174-2179 (ping-pong)
pump = ExpansionObject(
    id="oil_wells_exp_pump",
    numeric_id=280,
    name_string="STR_OBJECT_OIL_PUMP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite="2173",  # oil well ground overlay
    buildings=[
        {"base_sprite": "2174 + (((animation_frame % 11) < 6) ? (animation_frame % 11) : 10 - (animation_frame % 11))",
         "xoffset": 1, "yoffset": 2,
         "xextent": 15, "yextent": 14, "zextent": 16},
    ],
    animation_length=11,
    animation_speed=3,
    purchase_sprite=2174,
    height=8,
)

# Small oil field shed
shed = ExpansionObject(
    id="oil_wells_exp_shed",
    numeric_id=281,
    name_string="STR_OBJECT_OIL_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 38, -31, -9],
    ground_sprite=GROUND,
    height=4,
)
