from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/bulk_terminal_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"
GROUND = "GROUNDSPRITE_CONCRETE"

# yrel formula: -(height_px - 31)
# 84px tall sprites: yrel = -(84 - 31) = -53
# 39px tall sprites: yrel = -(39 - 31) = -8

# Storage tanks (white cylindrical tanks)
tanks = ExpansionObject(
    id="bulk_terminal_exp_tanks",
    numeric_id=293,
    name_string="STR_OBJECT_BULK_TERMINAL_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[440, 10, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

# Silos (tall white silos)
silos = ExpansionObject(
    id="bulk_terminal_exp_silos",
    numeric_id=294,
    name_string="STR_OBJECT_BULK_TERMINAL_SILOS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[510, 10, 64, 84, -35, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

# Cone silo (silo with conical roof)
cone_silo = ExpansionObject(
    id="bulk_terminal_exp_cone_silo",
    numeric_id=295,
    name_string="STR_OBJECT_BULK_TERMINAL_CONE_SILO",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[580, 10, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

# Warehouse (large covered shed)
warehouse = ExpansionObject(
    id="bulk_terminal_exp_warehouse",
    numeric_id=296,
    name_string="STR_OBJECT_BULK_TERMINAL_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[650, 10, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

# Large gantry crane (NE-SW orientation)
crane = ExpansionObject(
    id="bulk_terminal_exp_crane",
    numeric_id=297,
    name_string="STR_OBJECT_BULK_TERMINAL_CRANE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[440, 110, 64, 84, -31, -53],
    ground_sprite=GROUND,
    height=12,
    allow_on_water=True,
)

# Crane rails (flat rail tracks for gantry cranes)
crane_rails = ExpansionObject(
    id="bulk_terminal_exp_crane_rails",
    numeric_id=298,
    name_string="STR_OBJECT_BULK_TERMINAL_CRANE_RAILS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 39, -31, -8],
    ground_sprite=GROUND,
    height=1,
    allow_on_water=True,
)
