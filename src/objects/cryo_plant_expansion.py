from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/cryo_plant_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "GROUNDSPRITE_CONCRETE"

# yrel corrected: -(height - 31)

separation_tower = ExpansionObject(
    id="cryo_exp_tower",
    numeric_id=283,
    name_string="STR_OBJECT_CRYO_TOWER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 106, -31, -75],
    ground_sprite=GROUND,
    height=16,
)

horizontal_tanks = ExpansionObject(
    id="cryo_exp_tanks",
    numeric_id=284,
    name_string="STR_OBJECT_CRYO_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 64, -31, -33],
    ground_sprite=GROUND,
    height=8,
)

storage_tank = ExpansionObject(
    id="cryo_exp_storage",
    numeric_id=285,
    name_string="STR_OBJECT_CRYO_STORAGE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 64, -31, -33],
    ground_sprite=GROUND,
    height=8,
)
