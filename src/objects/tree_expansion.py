from objects.base_object import ExpansionObject

CLASS_ID = "AXPT"
CLASS_NAME = "STR_OBJECT_CLASS_TREES_PLANTS"
GROUND = "GROUNDSPRITE_NORMAL"
COST_GROVE = 15  # 4 trees
COST_DENSE = 30  # 9 trees

# Slope-aware tree positions from MagicSpritelayoutSlopeAwareTrees (industry.py)
# Format: slope_num -> tuple of (x, y) pixel offsets for each tree

SLOPES_4 = {
    0: ((2, 2), (2, 9), (9, 2), (9, 9)),
    1: ((2, 2), (2, 9), (9, 2), (9, 9)),
    2: ((2, 2), (2, 9), (9, 2), (9, 9)),
    3: ((2, 0), (0, 6), (6, 0), (6, 6)),
    4: ((2, 2), (2, 9), (9, 2), (9, 9)),
    5: ((2, 2), (2, 9), (9, 2), (9, 9)),
    6: ((2, 0), (0, 6), (8, 1), (6, 6)),
    7: ((0, 0), (0, 5), (5, 0), (5, 5)),
    8: ((2, 2), (2, 9), (9, 2), (9, 9)),
    9: ((1, 2), (2, 9), (8, 2), (9, 9)),
    10: ((2, 2), (2, 9), (9, 2), (9, 9)),
    11: ((0, 0), (0, 8), (7, 0), (7, 7)),
    12: ((2, 2), (2, 9), (9, 2), (9, 9)),
    13: ((2, 2), (2, 9), (9, 2), (9, 9)),
    14: ((1, 1), (-1, 6), (8, 2), (6, 6)),
    23: ((0, 0), (0, 5), (5, -2), (4, 4)),
    27: ((0, 0), (0, 7), (5, -2), (5, 5)),
    29: ((0, 0), (0, 7), (7, 0), (7, 7)),
    30: ((0, 0), (-1, 4), (7, 0), (6, 5)),
}

SLOPES_9 = {
    0: ((0, 0), (0, 5), (0, 11), (5, 0), (5, 5), (5, 11), (11, 0), (11, 5), (11, 11)),
    1: ((0, 0), (0, 5), (0, 11), (5, -1), (4, 4), (5, 11), (9, -2), (10, 4), (11, 11)),
    2: ((0, 0), (0, 5), (0, 9), (5, 0), (4, 4), (4, 8), (10, 0), (9, 4), (7, 7)),
    3: ((-1, -3), (-1, 3), (-1, 9), (3, -3), (3, 2), (3, 8), (7, -3), (7, 2), (7, 7)),
    4: ((0, 0), (0, 4), (-2, 9), (5, 0), (5, 4), (5, 10), (11, 0), (11, 4), (11, 11)),
    5: ((0, 0), (-2, 3), (-4, 8), (5, 0), (3, 3), (3, 9), (10, 0), (8, 3), (11, 11)),
    6: ((0, 0), (-2, 3), (-4, 8), (5, 0), (3, 3), (1, 8), (10, 0), (8, 3), (6, 8)),
    7: ((-3, -3), (-3, 3), (-3, 7), (2, -3), (2, 2), (2, 7), (7, -3), (7, 2), (7, 7)),
    8: ((0, 0), (0, 5), (0, 11), (5, 0), (5, 5), (5, 11), (11, 0), (11, 5), (11, 11)),
    9: ((-1, -1), (0, 5), (1, 10), (3, -1), (4, 5), (5, 10), (8, -1), (9, 5), (10, 10)),
    10: ((-3, -3), (-3, 3), (1, 10), (2, -3), (2, 2), (5, 9), (10, 1), (9, 5), (8, 8)),
    11: ((-3, -3), (-3, 3), (-1, 10), (2, -3), (2, 2), (3, 9), (7, -3), (7, 2), (7, 7)),
    12: ((0, 0), (-1, 4), (-3, 8), (5, 0), (5, 5), (4, 10), (11, 0), (11, 5), (11, 11)),
    13: ((0, 0), (0, 5), (-2, 9), (4, 0), (5, 5), (4, 10), (9, -2), (10, 5), (11, 11)),
    14: ((0, 0), (0, 5), (0, 10), (5, 0), (5, 5), (5, 10), (10, 0), (9, 4), (7, 7)),
    23: ((0, 0), (-2, 2), (-5, 7), (2, 0), (2, 2), (-1, 6), (8, -2), (5, 0), (4, 4)),
    27: ((0, 0), (0, 5), (-1, 11), (2, 0), (3, 5), (3, 10), (5, -5), (6, 2), (7, 8)),
    29: ((-3, 0), (-3, 4), (-3, 8), (3, 0), (1, 3), (4, 10), (8, -3), (10, 4), (11, 11)),
    30: ((-3, 0), (-5, 2), (-8, 4), (3, 0), (1, 3), (-1, 5), (10, -1), (9, 3), (7, 7)),
}


def _slope_grove(sprite, slopes):
    """Build slope_buildings dict: slope -> list of base_sprite building dicts."""
    return {
        slope: [
            {"base_sprite": sprite, "xoffset": x, "yoffset": y,
             "xextent": 4, "yextent": 4, "zextent": 32}
            for x, y in positions
        ]
        for slope, positions in slopes.items()
    }


# ── Grove objects (4 trees per tile, slope-aware) ────────────────────

conifer_grove = ExpansionObject(
    id="tree_exp_conifer_grove",
    numeric_id=215,
    name_string="STR_OBJECT_TREE_CONIFER_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=8,
    slope_buildings=_slope_grove(1712, SLOPES_4),
)

deciduous_grove = ExpansionObject(
    id="tree_exp_deciduous_grove",
    numeric_id=216,
    name_string="STR_OBJECT_TREE_DECIDUOUS_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=8,
    slope_buildings=_slope_grove(1620, SLOPES_4),
)

fruit_grove = ExpansionObject(
    id="tree_exp_fruit_grove",
    numeric_id=217,
    name_string="STR_OBJECT_TREE_FRUIT_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=8,
    slope_buildings=_slope_grove(1608, SLOPES_4),
)

fruit_large_grove = ExpansionObject(
    id="tree_exp_fruit_large_grove",
    numeric_id=218,
    name_string="STR_OBJECT_TREE_FRUIT_LARGE_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=8,
    slope_buildings=_slope_grove(1832, SLOPES_4),
)

orchard_grove = ExpansionObject(
    id="tree_exp_orchard_grove",
    numeric_id=219,
    name_string="STR_OBJECT_TREE_ORCHARD_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=8,
    slope_buildings=_slope_grove(1647, SLOPES_4),
)

tropical_grove = ExpansionObject(
    id="tree_exp_tropical_grove",
    numeric_id=220,
    name_string="STR_OBJECT_TREE_TROPICAL_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=8,
    slope_buildings=_slope_grove(1689, SLOPES_4),
)

coffee_grove = ExpansionObject(
    id="tree_exp_coffee_grove",
    numeric_id=221,
    name_string="STR_OBJECT_TREE_COFFEE_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=6,
    slope_buildings=_slope_grove(1850, SLOPES_4),
)

rubber_grove = ExpansionObject(
    id="tree_exp_rubber_grove",
    numeric_id=222,
    name_string="STR_OBJECT_TREE_RUBBER_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=8,
    slope_buildings=_slope_grove(1908, SLOPES_4),
)

palm_grove = ExpansionObject(
    id="tree_exp_palm_grove",
    numeric_id=223,
    name_string="STR_OBJECT_TREE_PALM_GROVE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_GROVE,
    height=10,
    slope_buildings=_slope_grove(1905, SLOPES_4),
)

# ── Dense objects (9 trees per tile, slope-aware) ────────────────────

conifer_dense = ExpansionObject(
    id="tree_exp_conifer_dense",
    numeric_id=224,
    name_string="STR_OBJECT_TREE_CONIFER_DENSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_DENSE,
    height=8,
    slope_buildings=_slope_grove(1712, SLOPES_9),
)

vine_dense = ExpansionObject(
    id="tree_exp_vine_dense",
    numeric_id=225,
    name_string="STR_OBJECT_TREE_VINE_DENSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite="3962",  # farmland ground
    build_cost_multiplier=COST_DENSE,
    height=4,
    slope_buildings=_slope_grove(1857, SLOPES_9),
)

coffee_dense = ExpansionObject(
    id="tree_exp_coffee_dense",
    numeric_id=226,
    name_string="STR_OBJECT_TREE_COFFEE_DENSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite=GROUND,
    build_cost_multiplier=COST_DENSE,
    height=6,
    slope_buildings=_slope_grove(1850, SLOPES_9),
)
