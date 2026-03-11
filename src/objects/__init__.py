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
