---
name: Expansion Objects Status
description: Tracks which primary industries have FEAT_OBJECTS expansion objects (Phase 2)
type: project
---

## Expansion Objects — Coverage (as of 2026-03-13)

43 of 44 primary industries have expansion objects. 1 intentionally skipped.

### Mining & Oil (AXPM)
| Industry | Status | Objects |
|---|---|---|
| coal_mine | DONE | headframe, mine_building, coal_pile_small, coal_heap, coal_storage, mine_equipment |
| iron_ore_mine | DONE | headgear, crusher, winding_house, boiler_house, exit_shed, exit_trestle (anim), ore_truck, ore_pile_front, ore_pile_rear |
| bauxite_mine | DONE | silo, conveyor, crusher, pit_conveyor_a/b, ore_pile, crane, bulldozer, pit (5x4 multi-tile) |
| copper_mine | DONE | headgear, crusher, winding_house, boiler_house, exit_shed, exit_trestle, ore_truck, ore_pile_front/rear |
| chromite_mine | DONE | headgear, winding_house, exit_trestle, ore_pile |
| manganese_mine | DONE | headgear, winding_house, exit_trestle, ore_pile |
| potash_mine | DONE | headgear, winding_house, exit_trestle, ore_pile |
| diamond_mine | DONE | headgear, winding_house, vents_shed |
| soda_ash_mine | DONE | headgear, crusher, winding_house, silos, soda_ash_pile, soda_ash_pile_small, truck |
| nitrate_mine | DONE | chimney, warehouse, shed, crane, nitrate_pile |
| phosphate_mine | DONE | pit (5x3 multi-tile) |
| salt_mine | DONE | pit (5x3 multi-tile) |
| limestone_mine | DONE | limestone_pile, limestone_pile_small |
| pyrite_mine | DONE | pyrite_pile, pyrite_pile_small |
| clay_pit | DONE | pit |
| quarry | DONE | pit |
| tar_sands_mine | DONE | pit |
| oil_wells | DONE | pump (animated, base_sprite 2174-2179), shed |
| cryo_plant | DONE | separation_tower, horizontal_tanks, storage_tank |
| recycling_depot | DONE | shed, containers |

### Docks & Water (AXPP)
| Industry | Status | Objects |
|---|---|---|
| port | DONE | warehouse, crane, cargo_crates, cargo_goods, concrete_pad |
| wharf | DONE | tanks, silos, warehouse |
| liquids_terminal | DONE | office, spherical_tank, large_tank |
| trading_post | DONE | warehouse, ship_hull |
| salt_evaporator | DONE | shed, salt_pan, salt_pan_full |
| dredging_site | DONE | crane |
| fish_farm | DONE | warehouse, fish_tank, fish_tank_full |
| fishing_grounds | DONE | equipment |
| seaweed_farm | DONE | seaweed_patch, seaweed_dense |

### Agriculture (AXPA)
| Industry | Status | Objects |
|---|---|---|
| arable_farm | DONE | barn, farm_cart, farmhouse, granary, grain_silo (+ alt variants) |
| farm (mixed) | DONE | barn, silos, farmhouse, large_barn, equipment_yard, farm_tools, livestock_pen, farm_vehicles |
| fruit_plantation | DONE | plantation_house, plantation_shed |
| dairy_farm | DONE | barn, barn_silo, large_barn, farmhouse, cattle_pen, cattle_pen_alt |
| sheep_farm | DONE | barn, farmhouse, shed, sheep_pen, sheep_pen_alt |
| ranch | DONE | ranch_house, ranch_house_alt, cottage, hay_bales, hay_bales_alt |
| orchard_piggery | DONE | piggery |
| herding_coop | DONE | hut, hut_small |
| coffee_estate | DONE | house, shed |
| vineyard | DONE | house, shed |
| rubber_plantation | DONE | warehouse, shed |
| peatlands | DONE | nissen_hut, tractor, harvester, crane, peat_pile |
| forest | DONE | logging_crane, logging_crane_alt, equipment, log_pile, log_pile_alt |
| trees (shared) | DONE | 12 slope-aware grove/dense objects (conifer, deciduous, fruit, tropical, coffee, rubber, palm, vine) |

### Not Covered
| Industry | Status | Reason |
|---|---|---|
| oil_rig | SKIPPED | Deep ocean industry, TTD base sprites only, object deleted by user request |
| bulk_terminal | MISSING | Not yet created |
