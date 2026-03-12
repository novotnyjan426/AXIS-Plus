from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/wharf_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"
GROUND = "GROUNDSPRITE_CONCRETE"

# yrel corrected: -(height - 31) = -(84 - 31) = -53
# industry uses -43/-61 but those are for multi-sprite industry rendering

tanks = ExpansionObject(
    id="wharf_exp_tanks",
    numeric_id=260,
    name_string="STR_OBJECT_WHARF_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[440, 10, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

silos = ExpansionObject(
    id="wharf_exp_silos",
    numeric_id=261,
    name_string="STR_OBJECT_WHARF_SILOS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[510, 10, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

warehouse = ExpansionObject(
    id="wharf_exp_warehouse",
    numeric_id=262,
    name_string="STR_OBJECT_WHARF_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[650, 10, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)
