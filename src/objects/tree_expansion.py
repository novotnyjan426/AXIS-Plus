from objects.base_object import ExpansionObject

CLASS_ID = "AXPT"
CLASS_NAME = "STR_OBJECT_CLASS_TREES_PLANTS"
GROUND = "GROUNDSPRITE_NORMAL"
COST = 5  # cheap — it's just a tree

# Base game tree sprites used across plantation/orchard industries

fruit_tree = ExpansionObject(
    id="tree_exp_fruit",
    numeric_id=135,
    name_string="STR_OBJECT_TREE_FRUIT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=1608,
    ground_sprite=GROUND,
    build_cost_multiplier=COST,
    height=8,
)

fruit_tree_large = ExpansionObject(
    id="tree_exp_fruit_large",
    numeric_id=136,
    name_string="STR_OBJECT_TREE_FRUIT_LARGE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=1832,
    ground_sprite=GROUND,
    build_cost_multiplier=COST,
    height=8,
)

deciduous_tree = ExpansionObject(
    id="tree_exp_deciduous",
    numeric_id=137,
    name_string="STR_OBJECT_TREE_DECIDUOUS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=1620,
    ground_sprite=GROUND,
    build_cost_multiplier=COST,
    height=8,
)

orchard_tree = ExpansionObject(
    id="tree_exp_orchard",
    numeric_id=138,
    name_string="STR_OBJECT_TREE_ORCHARD",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=1647,
    ground_sprite=GROUND,
    build_cost_multiplier=COST,
    height=8,
)

tropical_tree = ExpansionObject(
    id="tree_exp_tropical",
    numeric_id=139,
    name_string="STR_OBJECT_TREE_TROPICAL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=1689,
    ground_sprite=GROUND,
    build_cost_multiplier=COST,
    height=8,
)

coffee_bush = ExpansionObject(
    id="tree_exp_coffee",
    numeric_id=140,
    name_string="STR_OBJECT_TREE_COFFEE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=1850,
    ground_sprite=GROUND,
    build_cost_multiplier=COST,
    height=6,
)

rubber_tree = ExpansionObject(
    id="tree_exp_rubber",
    numeric_id=141,
    name_string="STR_OBJECT_TREE_RUBBER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=1908,
    ground_sprite=GROUND,
    build_cost_multiplier=COST,
    height=8,
)

palm_tree = ExpansionObject(
    id="tree_exp_palm",
    numeric_id=142,
    name_string="STR_OBJECT_TREE_PALM",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    base_sprite=1905,
    ground_sprite=GROUND,
    build_cost_multiplier=COST,
    height=10,
)
