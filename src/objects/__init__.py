registered_objects = []

# AXIS+ Expansions (generic)
from objects import test_expansion_object
test_expansion_object.obj.register()

# Mine Expansions
from objects import coal_mine_expansion
coal_mine_expansion.headframe.register()
coal_mine_expansion.mine_building.register()
coal_mine_expansion.coal_pile_small.register()
coal_mine_expansion.coal_heap.register()
coal_mine_expansion.coal_storage.register()
coal_mine_expansion.mine_equipment.register()

# Iron Ore Mine Expansions
from objects import iron_ore_mine_expansion
iron_ore_mine_expansion.headgear.register()
iron_ore_mine_expansion.crusher.register()
iron_ore_mine_expansion.winding_house.register()
iron_ore_mine_expansion.boiler_house.register()
iron_ore_mine_expansion.exit_shed.register()
iron_ore_mine_expansion.exit_trestle.register()
iron_ore_mine_expansion.ore_truck.register()
iron_ore_mine_expansion.ore_pile_front.register()
iron_ore_mine_expansion.ore_pile_rear.register()

# Bauxite Mine Expansions
from objects import bauxite_mine_expansion
bauxite_mine_expansion.silo.register()
bauxite_mine_expansion.conveyor.register()
bauxite_mine_expansion.crusher.register()
bauxite_mine_expansion.pit_conveyor_a.register()
bauxite_mine_expansion.pit_conveyor_b.register()
bauxite_mine_expansion.ore_pile.register()
bauxite_mine_expansion.crane.register()
bauxite_mine_expansion.bulldozer.register()
bauxite_mine_expansion.pit.register()

# Clay Pit Expansions
from objects import clay_pit_expansion
clay_pit_expansion.pit.register()

# Quarry Expansions
from objects import quarry_expansion
quarry_expansion.pit.register()

# Limestone Mine Expansions
from objects import limestone_mine_expansion
limestone_mine_expansion.limestone_pile.register()
limestone_mine_expansion.limestone_pile_small.register()

# Pyrite Mine Expansions
from objects import pyrite_mine_expansion
pyrite_mine_expansion.pyrite_pile.register()
pyrite_mine_expansion.pyrite_pile_small.register()

# Nitrate Mine Expansions
from objects import nitrate_mine_expansion
nitrate_mine_expansion.chimney.register()
nitrate_mine_expansion.warehouse.register()
nitrate_mine_expansion.shed.register()
nitrate_mine_expansion.crane.register()
nitrate_mine_expansion.nitrate_pile.register()

# Soda Ash Mine Expansions
from objects import soda_ash_mine_expansion
soda_ash_mine_expansion.headgear.register()
soda_ash_mine_expansion.crusher.register()
soda_ash_mine_expansion.winding_house.register()
soda_ash_mine_expansion.silos.register()
soda_ash_mine_expansion.soda_ash_pile.register()
soda_ash_mine_expansion.soda_ash_pile_small.register()
soda_ash_mine_expansion.truck.register()

# Tar Sands Mine Expansions
from objects import tar_sands_mine_expansion
tar_sands_mine_expansion.pit.register()

# Copper Mine Expansions
from objects import copper_mine_expansion
copper_mine_expansion.headgear.register()
copper_mine_expansion.crusher.register()
copper_mine_expansion.winding_house.register()
copper_mine_expansion.boiler_house.register()
copper_mine_expansion.exit_shed.register()
copper_mine_expansion.exit_trestle.register()
copper_mine_expansion.ore_truck.register()
copper_mine_expansion.ore_pile_front.register()
copper_mine_expansion.ore_pile_rear.register()

# Agriculture Expansions — Arable Farm
from objects import arable_farm_expansion
arable_farm_expansion.barn.register()
arable_farm_expansion.farm_cart.register()
arable_farm_expansion.farmhouse.register()
arable_farm_expansion.granary.register()
arable_farm_expansion.grain_silo.register()
arable_farm_expansion.barn_alt.register()
arable_farm_expansion.farm_cart_alt.register()
arable_farm_expansion.farmhouse_alt.register()
arable_farm_expansion.granary_alt.register()
arable_farm_expansion.grain_silo_alt.register()

# Agriculture Expansions — Fruit Plantation
from objects import fruit_plantation_expansion
fruit_plantation_expansion.plantation_house.register()
fruit_plantation_expansion.plantation_shed.register()

# Agriculture Expansions — Mixed Farm
from objects import farm_expansion
farm_expansion.barn.register()
farm_expansion.silos.register()
farm_expansion.farmhouse.register()
farm_expansion.large_barn.register()
farm_expansion.equipment_yard.register()
farm_expansion.farm_tools.register()
farm_expansion.livestock_pen.register()
farm_expansion.farm_vehicles.register()

# Docks & Water Expansions — Port
from objects import port_expansion
port_expansion.warehouse.register()
port_expansion.crane.register()
port_expansion.cargo_crates.register()
port_expansion.cargo_goods.register()
port_expansion.concrete_pad.register()

# Docks & Water Expansions — Salt Evaporator
from objects import salt_evaporator_expansion
salt_evaporator_expansion.shed.register()
salt_evaporator_expansion.salt_pan.register()
salt_evaporator_expansion.salt_pan_full.register()

# Docks & Water Expansions — Dredging Site
from objects import dredging_site_expansion
dredging_site_expansion.crane.register()

# Docks & Water Expansions — Seaweed Farm
from objects import seaweed_farm_expansion
seaweed_farm_expansion.seaweed_patch.register()
seaweed_farm_expansion.seaweed_dense.register()

# Agriculture Expansions — Rubber Plantation
from objects import rubber_plantation_expansion
rubber_plantation_expansion.warehouse.register()
rubber_plantation_expansion.shed.register()

# Agriculture Expansions — Sheep Farm
from objects import sheep_farm_expansion
sheep_farm_expansion.barn.register()
sheep_farm_expansion.farmhouse.register()
sheep_farm_expansion.shed.register()
sheep_farm_expansion.sheep_pen.register()
sheep_farm_expansion.sheep_pen_alt.register()

# Agriculture Expansions — Dairy Farm
from objects import dairy_farm_expansion
dairy_farm_expansion.barn.register()
dairy_farm_expansion.barn_silo.register()
dairy_farm_expansion.large_barn.register()
dairy_farm_expansion.farmhouse.register()
dairy_farm_expansion.cattle_pen.register()
dairy_farm_expansion.cattle_pen_alt.register()

# Agriculture Expansions — Ranch
from objects import ranch_expansion
ranch_expansion.ranch_house.register()
ranch_expansion.ranch_house_alt.register()
ranch_expansion.cottage.register()
ranch_expansion.hay_bales.register()
ranch_expansion.hay_bales_alt.register()

# Agriculture Expansions — Orchard Piggery
from objects import orchard_piggery_expansion
orchard_piggery_expansion.piggery.register()

# Agriculture Expansions — Trees
from objects import tree_expansion
tree_expansion.fruit_tree.register()
tree_expansion.fruit_tree_large.register()
tree_expansion.deciduous_tree.register()
tree_expansion.orchard_tree.register()
tree_expansion.tropical_tree.register()
tree_expansion.coffee_bush.register()
tree_expansion.rubber_tree.register()
tree_expansion.palm_tree.register()

# Agriculture Expansions — Forest
from objects import forest_expansion
forest_expansion.logging_crane.register()
forest_expansion.logging_crane_alt.register()
forest_expansion.equipment.register()
forest_expansion.log_pile.register()
forest_expansion.log_pile_alt.register()
