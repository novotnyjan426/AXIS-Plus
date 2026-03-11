from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/port_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"
GROUND = "GROUNDSPRITE_CONCRETE"

# Port warehouse — tall building (64x74)
warehouse = ExpansionObject(
    id="port_exp_warehouse",
    numeric_id=90,
    name_string="STR_OBJECT_PORT_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[440, 10, 64, 74, -31, -43],
    ground_sprite=GROUND,
    height=16,
    allow_on_water=True,
)

# Port crane (64x39)
crane = ExpansionObject(
    id="port_exp_crane",
    numeric_id=91,
    name_string="STR_OBJECT_PORT_CRANE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 39, -31, 0],
    ground_sprite=GROUND,
    height=8,
    allow_on_water=True,
)

# Cargo crates (64x39)
cargo_crates = ExpansionObject(
    id="port_exp_crates",
    numeric_id=92,
    name_string="STR_OBJECT_PORT_CRATES",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 39, -31, -7],
    ground_sprite=GROUND,
    height=4,
    allow_on_water=True,
)

# Cargo goods / pallets (64x39)
cargo_goods = ExpansionObject(
    id="port_exp_goods",
    numeric_id=93,
    name_string="STR_OBJECT_PORT_GOODS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 39, -31, 0],
    ground_sprite=GROUND,
    height=4,
    allow_on_water=True,
)

# Concrete pad (64x39)
concrete_pad = ExpansionObject(
    id="port_exp_pad",
    numeric_id=94,
    name_string="STR_OBJECT_PORT_PAD",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 39, -31, -8],
    ground_sprite=GROUND,
    height=1,
    allow_on_water=True,
)
