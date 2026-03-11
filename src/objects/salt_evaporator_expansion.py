from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/salt_evaporator_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"

shed = ExpansionObject(
    id="salt_evap_exp_shed",
    numeric_id=170,
    name_string="STR_OBJECT_SALT_EVAP_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 39, -31, -8],
    ground_sprite="GROUNDSPRITE_NORMAL",
    height=3,
)

salt_pan = ExpansionObject(
    id="salt_evap_exp_pan",
    numeric_id=171,
    name_string="STR_OBJECT_SALT_EVAP_PAN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 110, 64, 31, -31, 0],
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
)

salt_pan_full = ExpansionObject(
    id="salt_evap_exp_pan_full",
    numeric_id=172,
    name_string="STR_OBJECT_SALT_EVAP_PAN_FULL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 110, 64, 31, -31, 0],
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
)
