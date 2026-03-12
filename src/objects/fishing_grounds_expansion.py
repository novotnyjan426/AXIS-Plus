from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/fishing_grounds_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"

equipment = ExpansionObject(
    id="fishing_exp_equipment",
    numeric_id=275,
    name_string="STR_OBJECT_FISHING_EQUIPMENT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 31, -31, 0],
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
)
