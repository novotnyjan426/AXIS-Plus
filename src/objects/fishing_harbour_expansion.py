from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/fishing_harbour_1.png"
CLASS_ID = "AXPD"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"
GROUND = "GROUNDSPRITE_CONCRETE"

harbour_building = ExpansionObject(
    id="fishing_harbour_exp_building",
    numeric_id=317,
    name_string="STR_OBJECT_FISHING_HARBOUR_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[510, 110, 64, 74, -31, -42],
    ground_sprite=GROUND,
    height=10,
)

dock_shed = ExpansionObject(
    id="fishing_harbour_exp_shed",
    numeric_id=318,
    name_string="STR_OBJECT_FISHING_HARBOUR_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 39, -31, -8],
    ground_sprite=GROUND,
    height=4,
)
