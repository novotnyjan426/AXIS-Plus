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

# Chromite Mine Expansions
from objects import chromite_mine_expansion
chromite_mine_expansion.headgear.register()
chromite_mine_expansion.winding_house.register()
chromite_mine_expansion.exit_trestle.register()
chromite_mine_expansion.ore_pile.register()

# Manganese Mine Expansions
from objects import manganese_mine_expansion
manganese_mine_expansion.headgear.register()
manganese_mine_expansion.winding_house.register()
manganese_mine_expansion.exit_trestle.register()
manganese_mine_expansion.ore_pile.register()

# Potash Mine Expansions
from objects import potash_mine_expansion
potash_mine_expansion.headgear.register()
potash_mine_expansion.winding_house.register()
potash_mine_expansion.exit_trestle.register()
potash_mine_expansion.ore_pile.register()

# Diamond Mine Expansions
from objects import diamond_mine_expansion
diamond_mine_expansion.headgear.register()
diamond_mine_expansion.winding_house.register()
diamond_mine_expansion.vents_shed.register()

# Phosphate Mine Expansions
from objects import phosphate_mine_expansion
phosphate_mine_expansion.pit.register()

# Salt Mine Expansions
from objects import salt_mine_expansion
salt_mine_expansion.pit.register()

# Oil Wells Expansions
from objects import oil_wells_expansion
oil_wells_expansion.pump.register()
oil_wells_expansion.shed.register()

# Cryo Plant Expansions
from objects import cryo_plant_expansion
cryo_plant_expansion.separation_tower.register()
cryo_plant_expansion.horizontal_tanks.register()
cryo_plant_expansion.storage_tank.register()

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

# Docks & Water Expansions — Bulk Terminal
from objects import bulk_terminal_expansion
bulk_terminal_expansion.tanks.register()
bulk_terminal_expansion.silos.register()
bulk_terminal_expansion.cone_silo.register()
bulk_terminal_expansion.warehouse.register()
bulk_terminal_expansion.crane.register()
bulk_terminal_expansion.crane_rails.register()

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

# Docks & Water Expansions — Wharf
from objects import wharf_expansion
wharf_expansion.tanks.register()
wharf_expansion.silos.register()
wharf_expansion.warehouse.register()

# Docks & Water Expansions — Liquids Terminal
from objects import liquids_terminal_expansion
liquids_terminal_expansion.office.register()
liquids_terminal_expansion.spherical_tank.register()
liquids_terminal_expansion.large_tank.register()

# Docks & Water Expansions — Fish Farm
from objects import fish_farm_expansion
fish_farm_expansion.warehouse.register()
fish_farm_expansion.fish_tank.register()
fish_farm_expansion.fish_tank_full.register()

# Docks & Water Expansions — Fishing Grounds
from objects import fishing_grounds_expansion
fishing_grounds_expansion.equipment.register()

# Docks & Water Expansions — Trading Post
from objects import trading_post_expansion
trading_post_expansion.warehouse.register()
trading_post_expansion.ship_hull.register()

# Agriculture Expansions — Peatlands
from objects import peatlands_expansion
peatlands_expansion.nissen_hut.register()
peatlands_expansion.tractor.register()
peatlands_expansion.harvester.register()
peatlands_expansion.crane.register()
peatlands_expansion.peat_pile.register()

# Agriculture Expansions — Vineyard
from objects import vineyard_expansion
vineyard_expansion.house.register()
vineyard_expansion.shed.register()

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

# Agriculture Expansions — Herding Coop
from objects import herding_coop_expansion
herding_coop_expansion.hut.register()
herding_coop_expansion.hut_small.register()

# Agriculture Expansions — Coffee Estate
from objects import coffee_estate_expansion
coffee_estate_expansion.house.register()
coffee_estate_expansion.shed.register()

# Agriculture Expansions — Trees (slope-aware groves & dense)
from objects import tree_expansion
tree_expansion.conifer_grove.register()
tree_expansion.deciduous_grove.register()
tree_expansion.fruit_grove.register()
tree_expansion.fruit_large_grove.register()
tree_expansion.orchard_grove.register()
tree_expansion.tropical_grove.register()
tree_expansion.coffee_grove.register()
tree_expansion.rubber_grove.register()
tree_expansion.palm_grove.register()
tree_expansion.conifer_dense.register()
tree_expansion.vine_dense.register()
tree_expansion.coffee_dense.register()

# Agriculture Expansions — Forest
from objects import forest_expansion
forest_expansion.logging_crane.register()
forest_expansion.logging_crane_alt.register()
forest_expansion.equipment.register()
forest_expansion.log_pile.register()
forest_expansion.log_pile_alt.register()

# Recycling Depot Expansions
from objects import recycling_depot_expansion
recycling_depot_expansion.shed.register()
recycling_depot_expansion.containers.register()

# Food Processing Expansions — Stockyard
from objects import stockyard_expansion
stockyard_expansion.factory.register()
stockyard_expansion.outbuildings.register()

# Food Processing Expansions — Dairy
from objects import dairy_expansion
dairy_expansion.processing_block.register()
dairy_expansion.office_block.register()

# Food Processing Expansions — Bakery
from objects import bakery_expansion
bakery_expansion.oven_house.register()
bakery_expansion.warehouse.register()

# Food Processing Expansions — Flour Mill
from objects import flour_mill_expansion
flour_mill_expansion.shed.register()
flour_mill_expansion.mill_building.register()
flour_mill_expansion.grain_silo.register()
flour_mill_expansion.silo_equipment.register()

# Food Processing Expansions — Food Processor
from objects import food_processor_expansion
food_processor_expansion.factory.register()
food_processor_expansion.tanks.register()
food_processor_expansion.loading_dock.register()

# Food Processing Expansions — Fruit Packing Plant
from objects import fruit_packing_plant_expansion
fruit_packing_plant_expansion.warehouse.register()
fruit_packing_plant_expansion.silo.register()

# Food Processing Expansions — Meat Packing Plant
from objects import meat_packing_plant_expansion
meat_packing_plant_expansion.factory_block.register()
meat_packing_plant_expansion.tanks.register()

# Food Processing Expansions — Cider Mill
from objects import cider_mill_expansion
cider_mill_expansion.chimney.register()
cider_mill_expansion.building.register()
cider_mill_expansion.tanks.register()

# Food Processing Expansions — Sugar Refinery
from objects import sugar_refinery_expansion
sugar_refinery_expansion.chimney.register()
sugar_refinery_expansion.factory.register()
sugar_refinery_expansion.brick_building.register()
sugar_refinery_expansion.silos.register()

# Food Processing Expansions — Edible Oil Refinery
from objects import edible_oil_refinery_expansion
edible_oil_refinery_expansion.warehouse.register()
edible_oil_refinery_expansion.loading_yard.register()
edible_oil_refinery_expansion.tanks.register()

# Food Processing Expansions — Brewery
from objects import brewery_expansion
brewery_expansion.chimney_building.register()
brewery_expansion.hall.register()

# Docks Expansions — Fishing Harbour
from objects import fishing_harbour_expansion
fishing_harbour_expansion.harbour_building.register()
fishing_harbour_expansion.dock_shed.register()

# Manufacturing Expansions — Appliance Factory
from objects import appliance_factory_expansion
appliance_factory_expansion.chimney.register()
appliance_factory_expansion.offices.register()
appliance_factory_expansion.warehouse.register()

# Manufacturing Expansions — Assembly Plant
from objects import assembly_plant_expansion
assembly_plant_expansion.offices.register()
assembly_plant_expansion.assembly_hall.register()
assembly_plant_expansion.vehicles_lot.register()

# Manufacturing Expansions — Body Plant
from objects import body_plant_expansion
body_plant_expansion.factory.register()
body_plant_expansion.shed.register()

# Manufacturing Expansions — Component Factory
from objects import component_factory_expansion
component_factory_expansion.factory.register()
component_factory_expansion.workshop.register()

# Manufacturing Expansions — Engine Plant
from objects import engine_plant_expansion
engine_plant_expansion.factory.register()
engine_plant_expansion.shed.register()

# Manufacturing Expansions — Furniture Factory
from objects import furniture_factory_expansion
furniture_factory_expansion.workshop.register()
furniture_factory_expansion.warehouse.register()

# Manufacturing Expansions — Machine Shop
from objects import machine_shop_expansion
machine_shop_expansion.chimney.register()
machine_shop_expansion.workshop.register()
machine_shop_expansion.shed.register()

# Manufacturing Expansions — Metal Workshop
from objects import metal_workshop_expansion
metal_workshop_expansion.workshop.register()
metal_workshop_expansion.shed.register()

# Chemical & Refinery Expansions — Ammonia Plant
from objects import ammonia_plant_expansion
ammonia_plant_expansion.chimney.register()
ammonia_plant_expansion.warehouse.register()

# Chemical & Refinery Expansions — Biorefinery
from objects import biorefinery_expansion
biorefinery_expansion.tower.register()
biorefinery_expansion.building.register()

# Chemical & Refinery Expansions — Carbon Black Plant
from objects import carbon_black_plant_expansion
carbon_black_plant_expansion.chimneys.register()
carbon_black_plant_expansion.tanks.register()

# Chemical & Refinery Expansions — Chemical Plant
from objects import chemical_plant_expansion
chemical_plant_expansion.chimney.register()
chemical_plant_expansion.building.register()
chemical_plant_expansion.tanks.register()

# Chemical & Refinery Expansions — Chlor-Alkali Plant
from objects import chlor_alkali_plant_expansion
chlor_alkali_plant_expansion.chimney.register()
chlor_alkali_plant_expansion.tanks.register()

# Chemical & Refinery Expansions — Ethylene Cracker
from objects import ethylene_cracker_expansion
ethylene_cracker_expansion.chimney.register()
ethylene_cracker_expansion.columns.register()

# Chemical & Refinery Expansions — Fertiliser Plant
from objects import fertiliser_plant_expansion
fertiliser_plant_expansion.chimney.register()
fertiliser_plant_expansion.tanks.register()

# Chemical & Refinery Expansions — Fischer-Tropsch Plant
from objects import fischer_tropsch_plant_expansion
fischer_tropsch_plant_expansion.quench_tower.register()
fischer_tropsch_plant_expansion.oven.register()

# Chemical & Refinery Expansions — Oil Refinery
from objects import oil_refinery_expansion
oil_refinery_expansion.tower.register()
oil_refinery_expansion.tanks.register()

# Chemical & Refinery Expansions — Phosphoric Acid Plant
from objects import phosphoric_acid_plant_expansion
phosphoric_acid_plant_expansion.chimney.register()
phosphoric_acid_plant_expansion.building.register()

# Chemical & Refinery Expansions — Plastics Plant
from objects import plastics_plant_expansion
plastics_plant_expansion.factory.register()

# Chemical & Refinery Expansions — Polyethylene Plant
from objects import polyethylene_plant_expansion
polyethylene_plant_expansion.tower.register()

# Chemical & Refinery Expansions — Polypropylene Plant
from objects import polypropylene_plant_expansion
polypropylene_plant_expansion.tower.register()
polypropylene_plant_expansion.tanks.register()

# Chemical & Refinery Expansions — Solvay Plant
from objects import solvay_plant_expansion
solvay_plant_expansion.chimneys.register()
solvay_plant_expansion.silos.register()

# Chemical & Refinery Expansions — Sulphuric Acid Plant
from objects import sulphuric_acid_plant_expansion
sulphuric_acid_plant_expansion.chimney.register()
sulphuric_acid_plant_expansion.tanks.register()

# Heavy Industry Expansions — Alumina Refinery
from objects import alumina_refinery_expansion
alumina_refinery_expansion.chimney.register()
alumina_refinery_expansion.building.register()

# Heavy Industry Expansions — Aluminium Plant
from objects import aluminium_plant_expansion
aluminium_plant_expansion.building.register()
aluminium_plant_expansion.tower.register()

# Heavy Industry Expansions — Basic Oxygen Furnace
from objects import basic_oxygen_furnace_expansion
basic_oxygen_furnace_expansion.furnace.register()
basic_oxygen_furnace_expansion.tanks.register()

# Heavy Industry Expansions — Blast Furnace
from objects import blast_furnace_expansion
blast_furnace_expansion.furnace.register()
blast_furnace_expansion.building.register()

# Heavy Industry Expansions — Copper Concentrator
from objects import copper_concentrator_expansion
copper_concentrator_expansion.chimney.register()
copper_concentrator_expansion.building.register()

# Heavy Industry Expansions — Copper Refinery
from objects import copper_refinery_expansion
copper_refinery_expansion.chimney.register()
copper_refinery_expansion.building.register()

# Heavy Industry Expansions — Electric Arc Furnace
from objects import electric_arc_furnace_expansion
electric_arc_furnace_expansion.shed.register()
electric_arc_furnace_expansion.tanks.register()

# Heavy Industry Expansions — Integrated Steel Mill
from objects import integrated_steel_mill_expansion
integrated_steel_mill_expansion.furnace.register()
integrated_steel_mill_expansion.building.register()

# Heavy Industry Expansions — Iron Works
from objects import iron_works_expansion
iron_works_expansion.factory.register()
iron_works_expansion.shed.register()

# Heavy Industry Expansions — Pyrite Smelter
from objects import pyrite_smelter_expansion
pyrite_smelter_expansion.chimney.register()
pyrite_smelter_expansion.roaster.register()

# Heavy Industry Expansions — Sheet and Pipe Mill
from objects import sheet_and_pipe_mill_expansion
sheet_and_pipe_mill_expansion.factory.register()
sheet_and_pipe_mill_expansion.workshop.register()

# Heavy Industry Expansions — Slag Grinding Plant
from objects import slag_grinding_plant_expansion
slag_grinding_plant_expansion.tower.register()
slag_grinding_plant_expansion.silos.register()

# Heavy Industry Expansions — Steel Mill
from objects import steel_mill_expansion
steel_mill_expansion.factory.register()
steel_mill_expansion.shed.register()

# Heavy Industry Expansions — Tinplate Works
from objects import tinplate_works_expansion
tinplate_works_expansion.factory.register()
tinplate_works_expansion.shed.register()

# Heavy Industry Expansions — Wire and Section Mill
from objects import wire_and_section_mill_expansion
wire_and_section_mill_expansion.factory.register()
wire_and_section_mill_expansion.workshop.register()

# Heavy Industry Expansions — Coke Oven
from objects import coke_oven_expansion
coke_oven_expansion.quench_tower.register()
coke_oven_expansion.silo.register()

# Heavy Industry Expansions — Smithy Forge
from objects import smithy_forge_expansion
smithy_forge_expansion.forge.register()
smithy_forge_expansion.workshop.register()

# Heavy Industry Expansions — Ferrochrome Smelter
from objects import ferrochrome_smelter_expansion
ferrochrome_smelter_expansion.chimney.register()
ferrochrome_smelter_expansion.roaster.register()

# Heavy Industry Expansions — Electrical Works
from objects import electrical_works_expansion
electrical_works_expansion.factory.register()
electrical_works_expansion.shed.register()

# Building Materials Expansions — Brick Works
from objects import brick_works_expansion
brick_works_expansion.kiln.register()
brick_works_expansion.building.register()

# Building Materials Expansions — Builders Yard
from objects import builders_yard_expansion
builders_yard_expansion.shed.register()
builders_yard_expansion.silo.register()

# Building Materials Expansions — Cement Plant
from objects import cement_plant_expansion
cement_plant_expansion.chimney.register()
cement_plant_expansion.building.register()

# Building Materials Expansions — Glass Works
from objects import glass_works_expansion
glass_works_expansion.factory.register()
glass_works_expansion.building.register()

# Building Materials Expansions — Junk Yard
from objects import junk_yard_expansion
junk_yard_expansion.shed.register()
junk_yard_expansion.scrap.register()

# Building Materials Expansions — Lime Kiln
from objects import lime_kiln_expansion
lime_kiln_expansion.kiln.register()
lime_kiln_expansion.shed.register()

# Building Materials Expansions — Lumber Yard
from objects import lumber_yard_expansion
lumber_yard_expansion.warehouse.register()
lumber_yard_expansion.shed.register()

# Building Materials Expansions — Printing Plant
from objects import printing_plant_expansion
printing_plant_expansion.building.register()
printing_plant_expansion.warehouse.register()

# Building Materials Expansions — Recycling Plant
from objects import recycling_plant_expansion
recycling_plant_expansion.building.register()
recycling_plant_expansion.shed.register()

# Building Materials Expansions — Sawmill
from objects import sawmill_expansion
sawmill_expansion.shed.register()
sawmill_expansion.logs.register()

# Other Industry Expansions — Latex Processor
from objects import latex_processor_expansion
latex_processor_expansion.factory.register()
latex_processor_expansion.building.register()

# Other Industry Expansions — Paper Mill
from objects import paper_mill_expansion
paper_mill_expansion.chimney.register()
paper_mill_expansion.building.register()

# Other Industry Expansions — Paint Factory
from objects import paint_factory_expansion
paint_factory_expansion.factory.register()
paint_factory_expansion.shed.register()

# Other Industry Expansions — Cleaning Products Factory
from objects import cleaning_products_factory_expansion
cleaning_products_factory_expansion.chimney.register()
cleaning_products_factory_expansion.building.register()

# Other Industry Expansions — Civil Explosives Facility
from objects import civil_explosives_facility_expansion
civil_explosives_facility_expansion.chimney.register()
civil_explosives_facility_expansion.building.register()

# Other Industry Expansions — Tyre Plant
from objects import tyre_plant_expansion
tyre_plant_expansion.factory.register()
tyre_plant_expansion.building.register()

# Other Industry Expansions — Textile Mill
from objects import textile_mill_expansion
textile_mill_expansion.chimney.register()
textile_mill_expansion.warehouse.register()

# Other Industry Expansions — Farm Supply Yard
from objects import farm_supply_yard_expansion
farm_supply_yard_expansion.shed.register()
farm_supply_yard_expansion.warehouse.register()

# Other Industry Expansions — Supply Yard
from objects import supply_yard_expansion
supply_yard_expansion.shed.register()
supply_yard_expansion.warehouse.register()
