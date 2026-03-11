from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/coal_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "2022"  # GROUNDTILE_MUD_TRACKS

# 1x1 objects — individual coal mine sprites
# sprite coords from coal_mine.py: (x, y, w, h, xoff, yoff)

headframe = ExpansionObject(
    id="coal_mine_exp_headframe",
    numeric_id=10,
    name_string="STR_OBJECT_COAL_HEADFRAME",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 110, -31, -70],
    ground_sprite=GROUND,
    height=16,
)

mine_building = ExpansionObject(
    id="coal_mine_exp_building",
    numeric_id=11,
    name_string="STR_OBJECT_COAL_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 110, -31, -70],
    ground_sprite=GROUND,
    height=12,
)

coal_pile_small = ExpansionObject(
    id="coal_mine_exp_pile_small",
    numeric_id=12,
    name_string="STR_OBJECT_COAL_PILE_SMALL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 64, -31, -30],
    ground_sprite=GROUND,
)

coal_heap = ExpansionObject(
    id="coal_mine_exp_heap",
    numeric_id=13,
    name_string="STR_OBJECT_COAL_HEAP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 64, -31, -33],
    ground_sprite=GROUND,
)

coal_storage = ExpansionObject(
    id="coal_mine_exp_storage",
    numeric_id=14,
    name_string="STR_OBJECT_COAL_STORAGE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 64, -31, -33],
    ground_sprite=GROUND,
)

mine_equipment = ExpansionObject(
    id="coal_mine_exp_equipment",
    numeric_id=15,
    name_string="STR_OBJECT_COAL_EQUIPMENT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 64, -31, -33],
    ground_sprite=GROUND,
)
