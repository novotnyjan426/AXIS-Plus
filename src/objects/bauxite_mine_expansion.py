from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/bauxite_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "2022"  # GROUNDTILE_MUD_TRACKS

# 1x1 objects — individual bauxite mine sprites

silo = ExpansionObject(
    id="bauxite_exp_silo",
    numeric_id=30,
    name_string="STR_OBJECT_BAUXITE_SILO",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[870, 50, 64, 64, -31, -35],
    ground_sprite=GROUND,
    height=8,
)

conveyor = ExpansionObject(
    id="bauxite_exp_conveyor",
    numeric_id=31,
    name_string="STR_OBJECT_BAUXITE_CONVEYOR",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[940, 50, 64, 64, -31, -35],
    ground_sprite=GROUND,
    height=8,
)

crusher = ExpansionObject(
    id="bauxite_exp_crusher",
    numeric_id=32,
    name_string="STR_OBJECT_BAUXITE_CRUSHER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[1010, 50, 64, 64, -31, -33],
    ground_sprite=GROUND,
    height=8,
)

pit_conveyor_a = ExpansionObject(
    id="bauxite_exp_pit_conveyor_a",
    numeric_id=33,
    name_string="STR_OBJECT_BAUXITE_PIT_CONVEYOR_A",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 130, 64, 64, -31, -22],
    ground_sprite=GROUND,
    height=6,
)

pit_conveyor_b = ExpansionObject(
    id="bauxite_exp_pit_conveyor_b",
    numeric_id=34,
    name_string="STR_OBJECT_BAUXITE_PIT_CONVEYOR_B",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 130, 64, 64, -31, -22],
    ground_sprite=GROUND,
    height=6,
)

ore_pile = ExpansionObject(
    id="bauxite_exp_ore_pile",
    numeric_id=35,
    name_string="STR_OBJECT_BAUXITE_ORE_PILE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 50, 64, 31, -31, -16],
    ground_sprite=GROUND,
)

crane = ExpansionObject(
    id="bauxite_exp_crane",
    numeric_id=36,
    name_string="STR_OBJECT_BAUXITE_CRANE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[440, 10, 64, 71, -48, -55],
    ground_sprite=GROUND,
    height=10,
)

bulldozer = ExpansionObject(
    id="bauxite_exp_bulldozer",
    numeric_id=37,
    name_string="STR_OBJECT_BAUXITE_BULLDOZER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[440, 90, 64, 31, -31, 0],
    ground_sprite=GROUND,
)

# Complete bauxite open pit — 5x4 multi-tile object
# Replicates industry layout_1 exactly:
#   Row y=0: processing buildings (crusher, conveyor, silo) at x=1,2,3
#   Row y=1-3: open pit with ground overlays + conveyors/crane/bulldozer
# Ground overlays are childsprites on GROUNDSPRITE_NORMAL (like the industry does)
# Building sprites (conveyors, crane, pile, bulldozer) on top where applicable
pit = ExpansionObject(
    id="bauxite_exp_pit",
    numeric_id=38,
    name_string="STR_OBJECT_BAUXITE_PIT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[5, 4],
    ground_sprite="GROUNDSPRITE_NORMAL",
    height=2,
    tile_grid=[
        # Row y=0: processing buildings row (x=0 and x=4 are empty)
        {"x": 0, "y": 0, "sprite": None},  # empty corner
        {"x": 1, "y": 0, "sprite": [1010, 10, 64, 34, -31, -3],  # ground near crusher
         "buildings": [{"coords": [1010, 50, 64, 64, -31, -33]}]},  # crusher
        {"x": 2, "y": 0, "sprite": [940, 10, 64, 31, -31, 0],    # ground near conveyor
         "buildings": [{"coords": [940, 50, 64, 64, -31, -35]}]},   # conveyor
        {"x": 3, "y": 0, "sprite": [870, 10, 64, 31, -31, 0],    # ground near silo
         "buildings": [{"coords": [870, 50, 64, 64, -31, -35]}]},   # silo
        {"x": 4, "y": 0, "sprite": None},  # empty corner

        # Row y=1: top edge of pit
        {"x": 0, "y": 1, "sprite": [290, 10, 64, 31, -31, 0]},         # spriteset_24
        {"x": 1, "y": 1, "sprite": [220, 10, 64, 31, -31, 0],          # spriteset_23
         "buildings": [{"coords": [220, 130, 64, 64, -31, -22]}]},      # pit_conveyor_3
        {"x": 2, "y": 1, "sprite": [150, 10, 64, 31, -31, 0],          # spriteset_22
         "buildings": [{"coords": [150, 130, 64, 64, -31, -22]}]},      # pit_conveyor_2
        {"x": 3, "y": 1, "sprite": [80, 10, 64, 31, -31, 0],           # spriteset_20
         "buildings": [{"coords": [80, 130, 64, 64, -31, -22]}]},       # pit_conveyor_1
        {"x": 4, "y": 1, "sprite": [10, 10, 64, 31, -31, 0]},          # spriteset_19

        # Row y=2: middle of pit
        {"x": 0, "y": 2, "sprite": [290, 50, 64, 31, -31, 0]},         # spriteset_12
        {"x": 1, "y": 2, "sprite": [220, 50, 64, 31, -31, 0]},         # spriteset_11
        {"x": 2, "y": 2, "sprite": [150, 50, 64, 31, -31, 0]},         # spriteset_10
        {"x": 3, "y": 2, "sprite": [80, 50, 64, 31, -31, 0],           # spriteset_8
         "buildings": [{"coords": [440, 90, 64, 31, -31, 0]}]},         # bulldozer
        {"x": 4, "y": 2, "sprite": [10, 50, 64, 31, -31, 0]},          # spriteset_7

        # Row y=3: bottom of pit
        {"x": 0, "y": 3, "sprite": [290, 90, 64, 31, -31, 0]},         # spriteset_6
        {"x": 1, "y": 3, "sprite": [220, 90, 64, 31, -31, 0],          # spriteset_5
         "buildings": [                                                   # crane + pile
             {"coords": [440, 10, 64, 71, -48, -55]},
             {"coords": [360, 50, 64, 31, -63, -16]},
         ]},
        {"x": 2, "y": 3, "sprite": [150, 90, 64, 31, -31, 0]},         # spriteset_4
        {"x": 3, "y": 3, "sprite": [80, 90, 64, 31, -31, 0],           # spriteset_2 (actually 10,90 in orig)
         "buildings": [{"coords": [10, 130, 64, 64, -31, -22]}]},       # pit_conveyor_0
        {"x": 4, "y": 3, "sprite": [10, 90, 64, 31, -31, 0]},          # spriteset_1
    ],
)
