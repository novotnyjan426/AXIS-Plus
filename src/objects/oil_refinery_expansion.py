from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/oil_refinery_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"

# sp2: tall refinery tower
tower = ExpansionObject(
    id="oil_refinery_exp_tower",
    numeric_id=369,
    name_string="STR_OBJECT_OIL_REFINERY_TOWER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 128, -31, -96],
    ground_sprite=GROUND,
    height=16,
)

# sp5: storage tanks
tanks = ExpansionObject(
    id="oil_refinery_exp_tanks",
    numeric_id=370,
    name_string="STR_OBJECT_OIL_REFINERY_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 66, -31, -35],
    ground_sprite=GROUND,
    height=6,
)
