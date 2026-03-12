from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/liquids_terminal_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"
GROUND = "GROUNDSPRITE_CONCRETE"

# yrel corrected: -(height - 31) = -(84 - 31) = -53

office = ExpansionObject(
    id="liquids_exp_office",
    numeric_id=265,
    name_string="STR_OBJECT_LIQUIDS_OFFICE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[440, 10, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

spherical_tank = ExpansionObject(
    id="liquids_exp_spherical_tank",
    numeric_id=266,
    name_string="STR_OBJECT_LIQUIDS_SPHERICAL_TANK",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[510, 10, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

large_tank = ExpansionObject(
    id="liquids_exp_large_tank",
    numeric_id=267,
    name_string="STR_OBJECT_LIQUIDS_LARGE_TANK",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[510, 110, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)
