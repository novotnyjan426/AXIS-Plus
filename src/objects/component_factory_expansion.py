from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/component_factory_1.png"
CLASS_ID = "AXSM"
CLASS_NAME = "STR_OBJECT_CLASS_MANUFACTURING"
GROUND = "GROUNDSPRITE_CONCRETE"

# sp1: large factory building
factory = ExpansionObject(
    id="component_factory_exp_factory",
    numeric_id=341,
    name_string="STR_OBJECT_COMPONENT_FACTORY_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 60, 64, 100, -31, -66],
    ground_sprite=GROUND,
    height=12,
)

# sp4: workshop shed
workshop = ExpansionObject(
    id="component_factory_exp_workshop",
    numeric_id=342,
    name_string="STR_OBJECT_COMPONENT_FACTORY_WORKSHOP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 60, 64, 51, -31, -20],
    ground_sprite=GROUND,
    height=6,
)
