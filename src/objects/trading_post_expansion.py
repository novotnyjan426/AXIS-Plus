from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/trading_post_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"

warehouse = ExpansionObject(
    id="trading_post_exp_warehouse",
    numeric_id=287,
    name_string="STR_OBJECT_TRADING_POST_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 39, -31, -8],
    ground_sprite="GROUNDSPRITE_CONCRETE",
    height=4,
    allow_on_water=True,
)

ship_hull = ExpansionObject(
    id="trading_post_exp_hull",
    numeric_id=288,
    name_string="STR_OBJECT_TRADING_POST_HULL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 110, 64, 39, -35, -15],
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
)
