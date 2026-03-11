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

# Port Expansions
from objects import port_expansion
port_expansion.warehouse.register()
port_expansion.crane.register()
port_expansion.cargo_crates.register()
port_expansion.cargo_goods.register()
port_expansion.concrete_pad.register()
