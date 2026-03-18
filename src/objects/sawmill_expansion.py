from objects.base_object import ExpansionObject

CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"

# Shed — base game sprite
shed = ExpansionObject(
    id="sawmill_exp_shed",
    numeric_id=439,
    name_string="STR_OBJECT_SAWMILL_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=2069,
    ground_sprite=GROUND,
    height=6,
)

# Logs — base game sprite
logs = ExpansionObject(
    id="sawmill_exp_logs",
    numeric_id=440,
    name_string="STR_OBJECT_SAWMILL_LOGS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=2066,
    ground_sprite=GROUND,
    height=4,
)
