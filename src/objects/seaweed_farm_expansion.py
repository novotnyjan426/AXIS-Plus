from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/seaweed_farm_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"

seaweed_patch = ExpansionObject(
    id="seaweed_exp_patch",
    numeric_id=180,
    name_string="STR_OBJECT_SEAWEED_PATCH",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 31, -31, 0],
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
)

seaweed_dense = ExpansionObject(
    id="seaweed_exp_dense",
    numeric_id=181,
    name_string="STR_OBJECT_SEAWEED_DENSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 31, -31, 0],
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
)