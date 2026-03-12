from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/peatlands_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

nissen_hut = ExpansionObject(
    id="peatlands_exp_hut",
    numeric_id=205,
    name_string="STR_OBJECT_PEATLANDS_HUT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 64, -31, -31],
    ground_sprite=GROUND,
    height=5,
)

tractor = ExpansionObject(
    id="peatlands_exp_tractor",
    numeric_id=206,
    name_string="STR_OBJECT_PEATLANDS_TRACTOR",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 64, -31, -31],
    ground_sprite=GROUND,
    height=3,
)

harvester = ExpansionObject(
    id="peatlands_exp_harvester",
    numeric_id=207,
    name_string="STR_OBJECT_PEATLANDS_HARVESTER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 64, -31, -31],
    ground_sprite=GROUND,
    height=3,
)

crane = ExpansionObject(
    id="peatlands_exp_crane",
    numeric_id=208,
    name_string="STR_OBJECT_PEATLANDS_CRANE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    height=8,
    buildings=[
        {"file": SPRITE_FILE, "coords": [360, 10, 64, 64, -31, -31]},
        {"file": SPRITE_FILE, "coords": [290, 10, 64, 64, -31, -31]},
    ],
)

peat_pile = ExpansionObject(
    id="peatlands_exp_pile",
    numeric_id=209,
    name_string="STR_OBJECT_PEATLANDS_PILE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 64, -31, -31],
    ground_sprite=GROUND,
    height=3,
)
