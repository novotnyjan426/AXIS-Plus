from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/nitrate_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

chimney = ExpansionObject(
    id="nitrate_exp_chimney",
    numeric_id=165,
    name_string="STR_OBJECT_NITRATE_CHIMNEY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 110, -31, -70],
    ground_sprite=GROUND,
    height=12,
)

warehouse = ExpansionObject(
    id="nitrate_exp_warehouse",
    numeric_id=166,
    name_string="STR_OBJECT_NITRATE_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 64, -31, -32],
    ground_sprite=GROUND,
    height=6,
)

shed = ExpansionObject(
    id="nitrate_exp_shed",
    numeric_id=167,
    name_string="STR_OBJECT_NITRATE_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 64, -31, -31],
    ground_sprite=GROUND,
    height=5,
)

crane = ExpansionObject(
    id="nitrate_exp_crane",
    numeric_id=168,
    name_string="STR_OBJECT_NITRATE_CRANE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 64, -31, -31],
    ground_sprite=GROUND,
    height=6,
)

nitrate_pile = ExpansionObject(
    id="nitrate_exp_pile",
    numeric_id=169,
    name_string="STR_OBJECT_NITRATE_PILE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[570, 10, 64, 64, -31, -31],
    ground_sprite=GROUND,
)
