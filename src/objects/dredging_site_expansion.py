from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/dredging_site_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"

# Industry spritelayout_1 renders pier (childsprite) + crane + barge on one tile
crane = ExpansionObject(
    id="dredging_exp_crane",
    numeric_id=177,
    name_string="STR_OBJECT_DREDGING_CRANE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
    height=8,
    buildings=[
        {"file": SPRITE_FILE, "coords": [10, 10, 64, 100, -31, -67]},  # pier/molo
        {"file": SPRITE_FILE, "coords": [150, 10, 64, 64, -33, -37]},  # crane
        {"file": SPRITE_FILE, "coords": [80, 10, 64, 39, -31, -12]},   # barge
    ],
)
