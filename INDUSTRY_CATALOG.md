# AXIS+ Industry Catalog

Complete reference for all industries in the AXIS+ NewGRF set.
Auto-generated from `src/industries/*.py` definitions.

## Summary

| Type | Count | Boost Mechanic |
|------|------:|----------------|
| Primary Extractive | 23 | Deliver Engineering Supplies [ENSP] |
| Primary Organic | 14 | Deliver Farm Supplies [FMSP] |
| Primary Port | 4 | Deliver any accepted cargo |
| Primary (No Supplies) | 2 | None (static production) |
| Town Producer | 1 | None (scales with town population) |
| Secondary | 77 | Combinatory: deliver more input types for higher ratio |
| Tertiary | 7 | None (consumer / black hole) |
| Informative | 1 | None (information only) |
| **Total** | **129** | |

## Exceptions and Gotchas

**Unused industries** (7) -- not enabled in any economy:
- `chromite_mine`
- `ferrochrome_smelter`
- `hotel`
- `integrated_steel_mill`
- `latex_processor`
- `potash_mine`
- `smithy_forge`

**Non-boostable primaries** -- these industries are typed as Extractive or Organic
but override `accept_cargo_types=[]`, so they do **not** accept ENSP/FMSP and
cannot be supply-boosted:
- `fish_farm` (Primary Organic)
- `salt_evaporator` (Primary Extractive)
- `seaweed_farm` (Primary Organic)
- `trading_post` (Primary Extractive)

**Informative industries** produce no cargo and exist only to display game mechanic
information to the player (e.g. `plaza`).

## Production Formulas

### Primary Industries

Primary industries produce cargo on every 256-tick cycle (~8-9 times per month).
The `multiplier` number (shown as ×N in this catalog) is the base output per cycle.

**Formula per cycle:**
```
output = (multiplier x production_level x base_prod_factor x supply_boost% x expansion_boost%)
         / (16 x 16 x 100 x 100)
```

| Variable | Default | Notes |
|----------|---------|-------|
| `multiplier` | per-industry | The ×N number listed in this catalog |
| `production_level` | 16 | Can increase via monthly prod changes (max 105 = 656%) |
| `base_prod_factor` | 16 | Randomised at construction for variation between instances |
| `supply_boost%` | 100% | Enhanced (default 200%), Crankin' It (default 400%) |
| `expansion_boost%` | 100% | Low (130%), Medium (170%), High (250%) -- configurable |

At default settings with no boosts: **output per cycle = multiplier** (e.g. coal mine ×20 = ~20 coal per cycle, ~160-180/month).

**Supply boost thresholds** (configurable via GRF parameters):
- Enhanced: deliver >= 16 crates of supplies within last 27 cycles (port-type: 128)
- Crankin' It: deliver >= 80 crates (port-type: 640)

### Secondary Industries

Secondary industries produce on cargo delivery (not on tick cycle).

**Step 1 -- Calculate production ratio (0 to 8):**
For each accepted cargo type that was delivered within the last 27 cycles,
add its `input_ratio` (the ×N on the ◀ lines) to the total.

**Step 2 -- Calculate total output:**
```
total_output = SUM( incoming_amount_per_cargo x production_ratio / 8 )
```

**Step 3 -- Distribute to output cargos:**
```
output_cargo_amount = total_output x output_ratio / 8
```
The `output_ratio` numbers (×N on the ▶ lines) always sum to 8.

**Example:** Blast furnace (Steel City) accepts Iron Ore ×3, Coke ×3, Limestone ×2.
If all three are supplied: ratio = 3+3+2 = 8 (full throughput = 100% of input).
If only Iron Ore + Coke: ratio = 6 (75% throughput).
Output split: Iron ×6/8 = 75%, Slag ×2/8 = 25% of total produced.

### Tertiary Industries

Tertiary industries consume cargo (black holes). Some also produce town-type
cargos at a constant rate unrelated to deliveries.

---

## Primary Extractive Industries

---

### Bauxite Mine (`bauxite_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Bauxite [AORE] ×20

---

### Chromite Mine (`chromite_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **UNUSED** -- not enabled in any economy

---

### Clay Pit (`clay_pit`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Engineering Supplies [ENSP]

  ▶ Clay [CLAY] ×16

---

### Coal Mine (`coal_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Coal [COAL] ×20

---

### Copper Ore Mine (`copper_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ IAHC

  ◀ Engineering Supplies [ENSP]

  ▶ Copper Ore [CORE] ×20

---

### Diamond Mine (`diamond_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: ⚠️ IAHC

  ◀ Engineering Supplies [ENSP]

  ▶ Diamonds [DIAM] ×12

---

### Dredging Site (`dredging_site`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×17

**Tropical Paradise**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×17
  ▶ Clay [CLAY] ×16

**⚠️ BLTC**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×17

**Steel City**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×17

---

### Iron Ore Mine (`iron_ore_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Iron Ore [IORE] ×20

---

### Limestone Mine (`limestone_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Limestone [LIME] ×20

---

### Manganese Mine (`manganese_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: ⚠️ IAHC

  ◀ Engineering Supplies [ENSP]

  ▶ Manganese [MNO2] ×20

---

### Nitrate Mine (`nitrate_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Engineering Supplies [ENSP]

  ▶ Nitrates [NITR] ×18

---

### Oil Rig (`oil_rig`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ IAHC, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Oil [OIL_] ×29
  ▶ Passengers [PASS] ×4

---

### Oil Wells (`oil_wells`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ IAHC, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Oil [OIL_] ×28

---

### Peatlands (`peatlands`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, ⚠️ Boreal

**Extreme Classic**
  ◀ Engineering Supplies [ENSP]

  ▶ Biomass [BIOM] ×18

**⚠️ Boreal**
  ◀ Engineering Supplies [ENSP]

  ▶ Peat [PEAT] ×14

---

### Phosphate Mine (`phosphate_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: ⚠️ Boreal, Tropical Paradise, ⚠️ IAHC

**⚠️ Boreal**
  ◀ Engineering Supplies [ENSP]

  ▶ Phosphate [PHOS] ×16

**Tropical Paradise**
  ◀ Engineering Supplies [ENSP]

  ▶ Phosphate [PHOS] ×16

**⚠️ IAHC**
  ◀ Engineering Supplies [ENSP]

  ▶ Phosphate [PHOS] ×16
  ▶ Clay [CLAY] ×10

---

### Potash Mine (`potash_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **UNUSED** -- not enabled in any economy

---

### Pyrite Mine (`pyrite_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, ⚠️ Boreal, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Pyrite Ore [PORE] ×20

---

### Quarry (`quarry`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Limestone [LIME] ×14

**Tropical Paradise**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Limestone [LIME] ×14

**⚠️ BLTC**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Limestone [LIME] ×14

**⚠️ IAHC**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Aggregates [GRVL] ×14

**Steel City**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Limestone [LIME] ×14

---

### Salt Evaporator (`salt_evaporator`)
**Type**: Primary Extractive (NOT boostable -- accept overridden) | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ BLTC, Steel City

  ▶ Salt [SALT] ×15

---

### Salt Mine (`salt_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Tropical Paradise, ⚠️ BLTC, Steel City

**Tropical Paradise**
  ◀ Engineering Supplies [ENSP]

  ▶ Salt [SALT] ×20

**⚠️ BLTC**
  ◀ Engineering Supplies [ENSP]

  ▶ Salt [SALT] ×22
  ▶ Food Additives [ENUM] ×4

**Steel City**
  ◀ Engineering Supplies [ENSP]

  ▶ Salt [SALT] ×20

---

### Shipbreaker (`trading_post`)
**Type**: Primary Extractive (NOT boostable -- accept overridden) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ▶ Scrap Metal [SCMT] ×12

---

### Soda Ash Mine (`soda_ash_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Soda Ash [SASH] ×16
  ▶ Salt [SALT] ×18

---

### Tar Sands Mine (`tar_sands_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, ⚠️ BLTC, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Tar [CTAR] ×14

---

## Primary Organic Industries

---

### Arable Farm (`arable_farm`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Farm Supplies [FMSP]

  ▶ Grain [GRAI] ×14
  ▶ Sugar Beet [SGBT] ×24

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Grain [GRAI] ×14
  ▶ Sugar Cane [SGCN] ×24

**Steel City**
  ◀ Farm Supplies [FMSP]

  ▶ Grain [GRAI] ×28

---

### Cotton Farm (`ranch`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Farm Supplies [FMSP]

  ▶ Fibres [FICR] ×18
  ▶ Oil Seeds [OLSD] ×14

---

### Dairy Farm (`dairy_farm`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC

  ◀ Farm Supplies [FMSP]

  ▶ Livestock [LVST] ×12
  ▶ Milk [MILK] ×14

---

### Fish Farm (`fish_farm`)
**Type**: Primary Organic (NOT boostable -- accept overridden) | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ BLTC, Steel City

  ▶ Fish [FISH] ×8

---

### Forest (`forest`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ IAHC

**Extreme Classic**
  ◀ Farm Supplies [FMSP]

  ▶ Logs [WOOD] ×19

**⚠️ Boreal**
  ◀ Farm Supplies [FMSP]

  ▶ Logs [WOOD] ×24

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Logs [WOOD] ×19

**⚠️ IAHC**
  ◀ Farm Supplies [FMSP]

  ▶ Logs [WOOD] ×19

---

### Fruit Plantation (`fruit_plantation`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×16
  ▶ Oil Seeds [OLSD] ×13

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×16
  ▶ Oil Seeds [OLSD] ×13

**⚠️ BLTC**
  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×14
  ▶ Nuts [NUTS] ×13

**⚠️ IAHC**
  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×14
  ▶ Nuts [NUTS] ×13

**Steel City**
  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×16

---

### Herding Co-op (`herding_coop`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: ⚠️ Boreal

  ◀ Farm Supplies [FMSP]

  ▶ Food [FOOD] ×7

---

### Mixed Farm (`farm`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Farm Supplies [FMSP]

  ▶ Oil Seeds [OLSD] ×20
  ▶ Livestock [LVST] ×12

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Grain [GRAI] ×20
  ▶ Livestock [LVST] ×12

**⚠️ BLTC**
  ◀ Farm Supplies [FMSP]

  ▶ Grain [GRAI] ×14
  ▶ Livestock [LVST] ×13

**⚠️ IAHC**
  ◀ Farm Supplies [FMSP]

  ▶ Maize [MAIZ] ×14
  ▶ Livestock [LVST] ×13

**Steel City**
  ◀ Farm Supplies [FMSP]

  ▶ Grain [GRAI] ×14
  ▶ Livestock [LVST] ×13

---

### Orchard and Piggery (`orchard_piggery`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Steel City

  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×9
  ▶ Livestock [LVST] ×8

---

### Rubber Plantation (`rubber_plantation`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ IAHC

  ◀ Farm Supplies [FMSP]

  ▶ Rubber [RUBR] ×16

---

### Seaweed Farm (`seaweed_farm`)
**Type**: Primary Organic (NOT boostable -- accept overridden) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ▶ Biomass [BIOM] ×18

**Tropical Paradise**
  ▶ Biomass [BIOM] ×8
  ▶ Food Additives [ENUM] ×6

**Steel City**
  ▶ Produce [FRUT] ×16

---

### Sheep Farm (`sheep_farm`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Farm Supplies [FMSP]

  ▶ Livestock [LVST] ×13
  ▶ Fibres [FICR] ×16

---

### Spice Plantation (`coffee_estate`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Tropical Paradise, ⚠️ IAHC

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Food Additives [ENUM] ×13

**⚠️ IAHC**
  ◀ Farm Supplies [FMSP]

  ▶ Coffee [JAVA] ×11
  ▶ Produce [FRUT] ×8

---

### Vineyard (`vineyard`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×14

---

## Primary Port Industries

---

### Bulk Terminal (`bulk_terminal`)
**Type**: Primary Port (boost with accepted cargo) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Zinc [ZINC]
  ◀ Fertiliser [FERT]
  ◀ Vehicles [VEHI]
  ◀ Steel [STEL]

  ▶ Iron Ore [IORE] ×19
  ▶ Coal [COAL] ×19
  ▶ Bauxite [AORE] ×16
  ▶ Copper Ore [CORE] ×16

**Tropical Paradise**
  ◀ Building Materials [BDMT]
  ◀ Fertiliser [FERT]
  ◀ Explosives [BOOM]
  ◀ Vehicles [VEHI]

  ▶ Acetic Acid [ACET] ×19
  ▶ Coal [COAL] ×19
  ▶ Rare Metals [RAMT] ×16
  ▶ Limestone [LIME] ×16

**⚠️ BLTC**
  ▶ Oil [OIL_] ×20
  ▶ Potash [POTA] ×12
  ▶ Phosphate [PHOS] ×12
  ▶ Methanol [MEOH] ×12

**⚠️ IAHC**
  ◀ Manganese [MNO2]
  ◀ Phosphate [PHOS]
  ◀ Building Materials [BDMT]

  ▶ Refined Oil [RFPR] ×12
  ▶ Farm Supplies [FMSP] ×12

**Steel City**
  ◀ Food [FOOD]
  ◀ Cement [CMNT]
  ◀ Steel Sheet [STSH]
  ◀ Vehicles [VEHI]

  ▶ Iron Ore [IORE] ×19
  ▶ Alumina [ALO_] ×19
  ▶ Ferroalloy [FECR] ×16
  ▶ Coal [COAL] ×16

---

### Liquids Terminal (`liquids_terminal`)
**Type**: Primary Port (boost with accepted cargo) | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Chlorine [CHLO]
  ◀ Rubber [RUBR]
  ◀ Edible Oil [EOIL]
  ◀ Petroleum Fuels [PETR]

  ▶ Oil [OIL_] ×20
  ▶ Acid [ACID] ×20
  ▶ Refined Oil [RFPR] ×18
  ▶ Paints & Coatings [COAT] ×18

**Tropical Paradise**
  ◀ Phosphoric Acid [PHAC]
  ◀ Cleaning Agents [SOAP]
  ◀ Rubber [RUBR]
  ◀ Edible Oil [EOIL]

  ▶ Oil [OIL_] ×20
  ▶ Sulphuric Acid [SUAC] ×20
  ▶ Petroleum Fuels [PETR] ×20
  ▶ Refined Oil [RFPR] ×20

**⚠️ BLTC**
  ▶ Oil [OIL_] ×20

**⚠️ IAHC**
  ◀ Edible Oil [EOIL]
  ◀ Oil [OIL_]

  ▶ Refined Oil [RFPR] ×11
  ▶ Petroleum Fuels [PETR] ×7

**Steel City**
  ◀ Petroleum Fuels [PETR]
  ◀ Ammonia [NH3_]
  ◀ Chlorine [CHLO]
  ◀ Paints & Coatings [COAT]

  ▶ Oil [OIL_] ×20
  ▶ Rubber [RUBR] ×20
  ▶ Acid [ACID] ×20
  ▶ Refined Oil [RFPR] ×20

---

### Port (`port`)
**Type**: Primary Port (boost with accepted cargo) | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Building Materials [BDMT]
  ◀ Food [FOOD]
  ◀ Alcohol [BEER]
  ◀ Paper [PAPR]

  ▶ Engineering Supplies [ENSP] ×19
  ▶ Farm Supplies [FMSP] ×19
  ▶ Electrical Parts [POWR] ×12
  ▶ Metal Parts [MPAR] ×12

**⚠️ Boreal**
  ◀ Paper [PAPR]
  ◀ Zinc [ZINC]
  ◀ Fertiliser [FERT]

  ▶ Kaolin [KAOL] ×16
  ▶ Ammonia [NH3_] ×17
  ▶ Engineering Supplies [ENSP] ×9
  ▶ Farm Supplies [FMSP] ×9

**Tropical Paradise**
  ◀ Goods [GOOD]
  ◀ Food [FOOD]
  ◀ Alcohol [BEER]

  ▶ Engineering Supplies [ENSP] ×9
  ▶ Farm Supplies [FMSP] ×9

**⚠️ IAHC**
  ◀ Copper [COPR]
  ◀ Produce [FRUT]
  ◀ Timber [WDPR]

  ▶ Goods [GOOD] ×14
  ▶ Engineering Supplies [ENSP] ×17

**Steel City**
  ◀ Food [FOOD]
  ◀ Goods [GOOD]

  ▶ Engineering Supplies [ENSP] ×20
  ▶ Farm Supplies [FMSP] ×20

---

### Wharf (`wharf`)
**Type**: Primary Port (boost with accepted cargo) | **Economies**: Extreme Classic, ⚠️ Boreal, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Copper [COPR]
  ◀ Explosives [BOOM]
  ◀ Goods [GOOD]
  ◀ Cement [CMNT]

  ▶ Packaging [MNSP] ×19
  ▶ Rare Metals [RAMT] ×16
  ▶ Engineering Supplies [ENSP] ×12
  ▶ Farm Supplies [FMSP] ×12

**⚠️ Boreal**
  ◀ Explosives [BOOM]
  ◀ Peat [PEAT]
  ◀ Timber [WDPR]

  ▶ Potash [POTA] ×19
  ▶ Engineering Supplies [ENSP] ×9
  ▶ Farm Supplies [FMSP] ×9

**⚠️ BLTC**
  ◀ Electrical Parts [POWR]
  ◀ Rubber [RUBR]
  ◀ Explosives [BOOM]

  ▶ Copper [COPR] ×10
  ▶ Vehicles [VEHI] ×14
  ▶ Aluminium [ALUM] ×12
  ▶ Timber [WDPR] ×14
  ▶ Steel [STEL] ×14

**Steel City**
  ◀ Cement [CMNT]
  ◀ Goods [GOOD]
  ◀ Cleaning Agents [SOAP]
  ◀ Electrical Parts [POWR]

  ▶ Engineering Supplies [ENSP] ×12
  ▶ Scrap Metal [SCMT] ×16
  ▶ Copper Concentrate [COCO] ×14
  ▶ Plastics [PLAS] ×10

---

## Primary Industries (No Supplies)

---

### Cryo Plant (`cryo_plant`)
**Type**: Primary (No Supplies) | **Economies**: Steel City

  ▶ Oxygen [O2__] ×25
  ▶ Nitrogen [N7__] ×25

---

### Fishing Grounds (`fishing_grounds`)
**Type**: Primary (No Supplies) | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ BLTC, Steel City

  ▶ Fish [FISH] ×8

---

## Town Producer Industries

---

### Recycling Depot (`recycling_depot`)
**Type**: Town Producer | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ▶ Recyclables [RCYC] ×16

---

## Secondary Industries

---

### Abattoir (`stockyard`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Livestock [LVST] ×6
  ◀ Packaging [MNSP] ×2

  ▶ Food [FOOD] ×8

**Tropical Paradise**
  ◀ Livestock [LVST] ×8
  ◀ Cleaning Agents [SOAP] ×2

  ▶ Meat [MEAT] ×8

**⚠️ BLTC**
  ◀ Livestock [LVST] ×6
  ◀ Packaging [MNSP] ×1
  ◀ Food Additives [ENUM] ×1

  ▶ Food [FOOD] ×8

**⚠️ IAHC**
  ◀ Livestock [LVST] ×6

  ▶ Food [FOOD] ×8

**Steel City**
  ◀ Livestock [LVST] ×6
  ◀ Cleaning Agents [SOAP] ×2

  ▶ Fish [FISH] ×8

---

### Acid Plant (`sulphuric_acid_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Sulphur [SULP] ×5
  ◀ Nitrates [NITR] ×5
  ◀ Refined Oil [RFPR] ×2

  ▶ Acid [ACID] ×8

**Tropical Paradise**
  ◀ Sulphur [SULP] ×8

  ▶ Sulphuric Acid [SUAC] ×6

**⚠️ BLTC**
  ◀ Sulphur [SULP] ×8

  ▶ Sulphuric Acid [SUAC] ×6

**Steel City**
  ◀ Sulphur [SULP] ×5
  ◀ Nitrogen [N7__] ×1
  ◀ Hydrogen [H2__] ×2

  ▶ Acid [ACID] ×8

---

### Alumina Refinery (`alumina_refinery`)
**Type**: Secondary | **Economies**: Steel City

  ◀ Bauxite [AORE] ×6
  ◀ Sodium Hydroxide [LYE_] ×2

  ▶ Alumina [ALO_] ×8

---

### Aluminium Plant (`aluminium_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Bauxite [AORE] ×4
  ◀ Scrap Metal [SCMT] ×4
  ◀ Coke [COKE] ×2
  ◀ Acid [ACID] ×2

  ▶ Aluminium [ALUM] ×7
  ▶ Slag [SLAG] ×1

**⚠️ BLTC**
  ◀ Alumina [ALO_] ×8

  ▶ Aluminium [ALUM] ×8

**Steel City**
  ◀ Alumina [ALO_] ×4
  ◀ Scrap Metal [SCMT] ×2
  ◀ Coke [COKE] ×2

  ▶ Aluminium [ALUM] ×7
  ▶ Slag [SLAG] ×1

---

### Ammonia Plant (`ammonia_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Refined Oil [RFPR] ×2
  ◀ Nitrates [NITR] ×4
  ◀ Biomass [BIOM] ×2
  ◀ Acid [ACID] ×2

  ▶ Fertiliser [FERT] ×5
  ▶ Explosives [BOOM] ×3

**⚠️ BLTC**
  ◀ Naphtha [NAPH] ×8

  ▶ Ammonia [NH3_] ×3
  ▶ Urea [UREA] ×2
  ▶ Ammonium Nitrate [NHNO] ×3

**Steel City**
  ◀ Refined Oil [RFPR] ×2
  ◀ Nitrogen [N7__] ×4
  ◀ Hydrogen [H2__] ×2

  ▶ Ammonia [NH3_] ×8

---

### Appliance Factory (`appliance_factory`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Metal Parts [MPAR] ×4
  ◀ Electrical Parts [POWR] ×4
  ◀ Glass [GLAS] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Goods [GOOD] ×8

**Tropical Paradise**
  ◀ Metal Parts [MPAR] ×4
  ◀ Glass [GLAS] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Rubber Parts [TYRE] ×2

  ▶ Goods [GOOD] ×8

**⚠️ BLTC**
  ◀ Glass [GLAS] ×2
  ◀ Steel [STEL] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Goods [GOOD] ×8

**Steel City**
  ◀ Alloy Steel [STAL] ×2
  ◀ Steel Sheet [STSH] ×2
  ◀ Glass [GLAS] ×1
  ◀ Plastic Parts [PPAR] ×1
  ◀ Electrical Parts [POWR] ×1
  ◀ Rubber Parts [TYRE] ×1

  ▶ Goods [GOOD] ×8

---

### Appliance Factory (`factory_1`)
**Type**: Secondary | **Economies**: Tropical Paradise, ⚠️ BLTC, Steel City

**Tropical Paradise**
  ◀ Metal Parts [MPAR] ×4
  ◀ Glass [GLAS] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Rubber Parts [TYRE] ×2

  ▶ Goods [GOOD] ×8

**⚠️ BLTC**
  ◀ Glass [GLAS] ×2
  ◀ Steel [STEL] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Goods [GOOD] ×8

**Steel City**
  ◀ Alloy Steel [STAL] ×2
  ◀ Steel Sheet [STSH] ×2
  ◀ Glass [GLAS] ×1
  ◀ Plastic Parts [PPAR] ×1
  ◀ Electrical Parts [POWR] ×1
  ◀ Rubber Parts [TYRE] ×1

  ▶ Goods [GOOD] ×8

---

### Assembly Plant (`assembly_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Steel [STEL] ×3
  ◀ Glass [GLAS] ×2
  ◀ Vehicle Parts [VPTS] ×2
  ◀ Metal Parts [MPAR] ×2
  ◀ Rubber Parts [TYRE] ×2
  ◀ Paints & Coatings [COAT] ×2

  ▶ Vehicles [VEHI] ×6

**Tropical Paradise**
  ◀ Steel [STEL] ×2
  ◀ Glass [GLAS] ×2
  ◀ Vehicle Parts [VPTS] ×2
  ◀ Rubber Parts [TYRE] ×1
  ◀ Paints & Coatings [COAT] ×1

  ▶ Vehicles [VEHI] ×6

**Steel City**
  ◀ Vehicle Parts [VPTS] ×2
  ◀ Vehicle Bodies [VBOD] ×2
  ◀ Vehicle Engines [VENG] ×2
  ◀ Rubber Parts [TYRE] ×4

  ▶ Vehicles [VEHI] ×6
  ▶ Engineering Supplies [ENSP] ×1
  ▶ Farm Supplies [FMSP] ×1

---

### Bakery (`bakery`)
**Type**: Secondary | **Economies**: Tropical Paradise

  ◀ Flour [BAKE] ×3
  ◀ Sugar [SUGR] ×2
  ◀ Food Additives [ENUM] ×1
  ◀ Edible Oil [EOIL] ×1
  ◀ Packaging [MNSP] ×1

  ▶ Food [FOOD] ×8

---

### Basic Oxygen Furnace (`basic_oxygen_furnace`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Iron [IRON] ×4
  ◀ Quicklime [QLME] ×2
  ◀ Rare Metals [RAMT] ×2

  ▶ Steel [STEL] ×6
  ▶ Slag [SLAG] ×2

**Tropical Paradise**
  ◀ Iron [IRON] ×3
  ◀ Scrap Metal [SCMT] ×3
  ◀ Quicklime [QLME] ×1
  ◀ Rare Metals [RAMT] ×1

  ▶ Steel [STEL] ×6
  ▶ Slag [SLAG] ×2

**Steel City**
  ◀ Iron [IRON] ×4
  ◀ Ferroalloy [FECR] ×2
  ◀ Quicklime [QLME] ×1
  ◀ Oxygen [O2__] ×1

  ▶ Carbon Steel [STCB] ×3
  ▶ Alloy Steel [STAL] ×3
  ▶ Slag [SLAG] ×2

---

### Biorefinery (`biorefinery`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Sugar Beet [SGBT] ×6
  ◀ Biomass [BIOM] ×6
  ◀ Oil Seeds [OLSD] ×6

  ▶ Refined Oil [RFPR] ×5
  ▶ Petroleum Fuels [PETR] ×4
  ▶ Plastics [PLAS] ×3

**Tropical Paradise**
  ◀ Biomass [BIOM] ×6
  ◀ Oil Seeds [OLSD] ×6
  ◀ Grain [GRAI] ×6

  ▶ Refined Oil [RFPR] ×4
  ▶ Petroleum Fuels [PETR] ×4

**Steel City**
  ◀ Grain [GRAI] ×4
  ◀ Produce [FRUT] ×4

  ▶ Refined Oil [RFPR] ×2
  ▶ Petroleum Fuels [PETR] ×3
  ▶ Monomer [C2H4] ×3

---

### Blast Furnace (`blast_furnace`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Iron Ore [IORE] ×4
  ◀ Coke [COKE] ×3
  ◀ Limestone [LIME] ×2

  ▶ Iron [IRON] ×6
  ▶ Slag [SLAG] ×2

**Tropical Paradise**
  ◀ Iron Ore [IORE] ×4
  ◀ Coke [COKE] ×3
  ◀ Limestone [LIME] ×2

  ▶ Iron [IRON] ×6
  ▶ Slag [SLAG] ×2

**Steel City**
  ◀ Iron Ore [IORE] ×3
  ◀ Coke [COKE] ×3
  ◀ Limestone [LIME] ×2

  ▶ Iron [IRON] ×6
  ▶ Slag [SLAG] ×2

---

### Body Plant (`body_plant`)
**Type**: Secondary | **Economies**: Steel City

  ◀ Steel Sheet [STSH] ×4
  ◀ Paints & Coatings [COAT] ×2
  ◀ Glass [GLAS] ×2

  ▶ Vehicle Bodies [VBOD] ×7
  ▶ Scrap Metal [SCMT] ×1

---

### Brewery (`brewery`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC

**Extreme Classic**
  ◀ Grain [GRAI] ×4
  ◀ Produce [FRUT] ×3
  ◀ Packaging [MNSP] ×2

  ▶ Alcohol [BEER] ×6
  ▶ Biomass [BIOM] ×2

**Tropical Paradise**
  ◀ Grain [GRAI] ×4
  ◀ Sugar [SUGR] ×2
  ◀ Packaging [MNSP] ×1
  ◀ Food Additives [ENUM] ×1

  ▶ Alcohol [BEER] ×6
  ▶ Biomass [BIOM] ×2

**⚠️ BLTC**
  ◀ Grain [GRAI] ×4
  ◀ Packaging [MNSP] ×4

  ▶ Alcohol [BEER] ×8

**⚠️ IAHC**
  ◀ Produce [FRUT] ×4
  ◀ Maize [MAIZ] ×4

  ▶ Alcohol [BEER] ×8

---

### Brick Works (`brick_works`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Clay [CLAY] ×4
  ◀ Sand [SAND] ×3
  ◀ Coal [COAL] ×2

  ▶ Building Materials [BDMT] ×6

---

### Cannery (`food_processor`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Produce [FRUT] ×4
  ◀ Fish [FISH] ×4
  ◀ Edible Oil [EOIL] ×4
  ◀ Packaging [MNSP] ×2
  ◀ Salt [SALT] ×2

  ▶ Food [FOOD] ×8

**Tropical Paradise**
  ◀ Sugar [SUGR] ×6
  ◀ Produce [FRUT] ×6
  ◀ Meat [MEAT] ×6
  ◀ Food Additives [ENUM] ×2
  ◀ Edible Oil [EOIL] ×2
  ◀ Packaging [MNSP] ×2

  ▶ Food [FOOD] ×8

**⚠️ IAHC**
  ◀ Nuts [NUTS] ×6
  ◀ Produce [FRUT] ×6

  ▶ Edible Oil [EOIL] ×4
  ▶ Food [FOOD] ×4

**Steel City**
  ◀ Produce [FRUT] ×4
  ◀ Fish [FISH] ×4
  ◀ Packaging [MNSP] ×2
  ◀ Salt [SALT] ×2

  ▶ Food [FOOD] ×8

---

### Carbon Black Plant (`carbon_black_plant`)
**Type**: Secondary | **Economies**: Steel City

  ◀ Tar [CTAR] ×8

  ▶ Carbon Black [CBLK] ×4
  ▶ Coke [COKE] ×4

---

### Cement Plant (`cement_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Cement [CMNT] ×2
  ◀ Coke [COKE] ×2
  ◀ Sand [SAND] ×2
  ◀ Limestone [LIME] ×2

  ▶ Building Materials [BDMT] ×6
  ▶ Quicklime [QLME] ×2

**Tropical Paradise**
  ◀ Coke [COKE] ×2
  ◀ Sand [SAND] ×2
  ◀ Limestone [LIME] ×2
  ◀ Slag [SLAG] ×2

  ▶ Building Materials [BDMT] ×6
  ▶ Quicklime [QLME] ×2

**⚠️ BLTC**
  ◀ Coal [COAL] ×2
  ◀ Clay [CLAY] ×2
  ◀ Limestone [LIME] ×4

  ▶ Cement [CMNT] ×8

**⚠️ IAHC**
  ◀ Petroleum Fuels [PETR] ×2
  ◀ Clay [CLAY] ×2
  ◀ Aggregates [GRVL] ×4

  ▶ Building Materials [BDMT] ×8

**Steel City**
  ◀ Petroleum Fuels [PETR] ×2
  ◀ Sand [SAND] ×2
  ◀ Limestone [LIME] ×4

  ▶ Quicklime [QLME] ×6
  ▶ Cement [CMNT] ×6

---

### Chemical Plant (`chemical_plant`)
**Type**: Secondary | **Economies**: ⚠️ Boreal, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC

**⚠️ Boreal**
  ◀ Sulphur [SULP] ×2
  ◀ Phosphate [PHOS] ×2
  ◀ Ammonia [NH3_] ×2
  ◀ Potash [POTA] ×2

  ▶ Fertiliser [FERT] ×4
  ▶ Explosives [BOOM] ×4

**Tropical Paradise**
  ◀ Salt [SALT] ×2
  ◀ Nitrates [NITR] ×2
  ◀ Refined Oil [RFPR] ×2

  ▶ Acetic Acid [ACET] ×6
  ▶ Food Additives [ENUM] ×4

**⚠️ BLTC**
  ◀ Soda Ash [SASH] ×1
  ◀ Sodium Hydroxide [LYE_] ×2
  ◀ Ammonia [NH3_] ×2
  ◀ Chlorine [CHLO] ×2
  ◀ Phosphoric Acid [PHAC] ×1

  ▶ Cleaning Agents [SOAP] ×4
  ▶ Food Additives [ENUM] ×4

**⚠️ IAHC**
  ◀ Sulphur [SULP] ×2
  ◀ Phosphate [PHOS] ×2
  ◀ Ammonia [NH3_] ×2
  ◀ Potash [POTA] ×2

  ▶ Farm Supplies [FMSP] ×4
  ▶ Explosives [BOOM] ×4

---

### Chlor-alkali Plant (`chlor_alkali_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Salt [SALT] ×8

  ▶ Acid [ACID] ×4
  ▶ Chlorine [CHLO] ×4

**⚠️ BLTC**
  ◀ Salt [SALT] ×8

  ▶ Hydrochloric Acid [HYAC] ×4
  ▶ Chlorine [CHLO] ×2
  ▶ Sodium Hydroxide [LYE_] ×2

**Steel City**
  ◀ Salt [SALT] ×8

  ▶ Acid [ACID] ×2
  ▶ Chlorine [CHLO] ×2
  ▶ Sodium Hydroxide [LYE_] ×2
  ▶ Hydrogen [H2__] ×2

---

### Civil Explosives Facility (`civil_explosives_facility`)
**Type**: Secondary | **Economies**: Tropical Paradise, ⚠️ BLTC, Steel City

**Tropical Paradise**
  ◀ Nitrates [NITR] ×2
  ◀ Sulphuric Acid [SUAC] ×2
  ◀ Refined Oil [RFPR] ×2

  ▶ Explosives [BOOM] ×6
  ▶ Fertiliser [FERT] ×4

**⚠️ BLTC**
  ◀ Ammonium Nitrate [NHNO] ×6
  ◀ Petroleum Fuels [PETR] ×2

  ▶ Explosives [BOOM] ×8

**Steel City**
  ◀ Ammonia [NH3_] ×4
  ◀ Acid [ACID] ×2
  ◀ Plastics [PLAS] ×1
  ◀ Petroleum Fuels [PETR] ×1

  ▶ Ammonium Nitrate [NHNO] ×6
  ▶ Engineering Supplies [ENSP] ×2

---

### Cleaning Products Factory (`cleaning_products_factory`)
**Type**: Secondary | **Economies**: Tropical Paradise, ⚠️ BLTC, Steel City

**Tropical Paradise**
  ◀ Soda Ash [SASH] ×2
  ◀ Phosphoric Acid [PHAC] ×2
  ◀ Acetic Acid [ACET] ×2
  ◀ Edible Oil [EOIL] ×2

  ▶ Cleaning Agents [SOAP] ×6
  ▶ Goods [GOOD] ×6

**⚠️ BLTC**
  ◀ Copper [COPR] ×2
  ◀ Steel [STEL] ×2
  ◀ Metal Wire [STWR] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Electrical Parts [POWR] ×8

**Steel City**
  ◀ Sodium Hydroxide [LYE_] ×2
  ◀ Soda Ash [SASH] ×2
  ◀ Salt [SALT] ×2
  ◀ Ammonia [NH3_] ×2
  ◀ Packaging [MNSP] ×2

  ▶ Cleaning Agents [SOAP] ×6
  ▶ Goods [GOOD] ×4

---

### Cleaning Products Factory (`factory_2`)
**Type**: Secondary | **Economies**: ⚠️ BLTC, Steel City

**⚠️ BLTC**
  ◀ Copper [COPR] ×2
  ◀ Steel [STEL] ×2
  ◀ Metal Wire [STWR] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Electrical Parts [POWR] ×8

**Steel City**
  ◀ Sodium Hydroxide [LYE_] ×2
  ◀ Soda Ash [SASH] ×2
  ◀ Salt [SALT] ×2
  ◀ Ammonia [NH3_] ×2

  ▶ Cleaning Agents [SOAP] ×8

---

### Coal Liquefaction Plant (`fischer_tropsch_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Coal [COAL] ×8

  ▶ Refined Oil [RFPR] ×6
  ▶ Tar [CTAR] ×2

**⚠️ BLTC**
  ◀ Coal [COAL] ×8

  ▶ Ammonia [NH3_] ×2
  ▶ Petroleum Fuels [PETR] ×6

**Steel City**
  ◀ Coal [COAL] ×8

  ▶ Refined Oil [RFPR] ×6
  ▶ Hydrogen [H2__] ×2

---

### Coke Oven (`coke_oven`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Coal [COAL] ×8

  ▶ Coke [COKE] ×6
  ▶ Sulphur [SULP] ×2

**Tropical Paradise**
  ◀ Coal [COAL] ×8

  ▶ Coke [COKE] ×6
  ▶ Sulphur [SULP] ×2

**Steel City**
  ◀ Coal [COAL] ×8

  ▶ Coke [COKE] ×6
  ▶ Tar [CTAR] ×1
  ▶ Sulphur [SULP] ×1

---

### Component Factory (`component_factory`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Metal Parts [MPAR] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Textiles [TEXT] ×2
  ◀ Electrical Parts [POWR] ×2

  ▶ Vehicle Parts [VPTS] ×8

**Tropical Paradise**
  ◀ Metal Parts [MPAR] ×2
  ◀ Rubber Parts [TYRE] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Textiles [TEXT] ×2
  ◀ Paints & Coatings [COAT] ×2

  ▶ Vehicle Parts [VPTS] ×8

**⚠️ IAHC**
  ◀ Fibres [FICR] ×6
  ◀ Soda Ash [SASH] ×2

  ▶ Yarn [YARN] ×8

**Steel City**
  ◀ Metal Parts [MPAR] ×2
  ◀ Plastic Parts [PPAR] ×2
  ◀ Alloy Steel [STAL] ×2
  ◀ Electrical Parts [POWR] ×2

  ▶ Vehicle Parts [VPTS] ×8

---

### Construction Plant (`builders_yard`)
**Type**: Secondary | **Economies**: ⚠️ BLTC, ⚠️ IAHC, Steel City

  ◀ Cement [CMNT] ×2
  ◀ Metal Parts [MPAR] ×2
  ◀ Metal Wire [STWR] ×2
  ◀ Glass [GLAS] ×2

  ▶ Goods [GOOD] ×8

---

### Construction Plant (`construction_plant`)
**Type**: Secondary | **Economies**: ⚠️ BLTC, Steel City

  ◀ Cement [CMNT] ×2
  ◀ Metal Parts [MPAR] ×2
  ◀ Metal Wire [STWR] ×2
  ◀ Glass [GLAS] ×2

  ▶ Goods [GOOD] ×8

---

### Copper Concentrator (`copper_concentrator`)
**Type**: Secondary | **Economies**: Tropical Paradise

  ◀ Copper Ore [CORE] ×4
  ◀ Sulphuric Acid [SUAC] ×2
  ◀ Quicklime [QLME] ×2

  ▶ Copper Concentrate [COCO] ×6
  ▶ Rare Metals [RAMT] ×3

---

### Copper Smelter (`copper_refinery`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Copper Ore [CORE] ×4
  ◀ Scrap Metal [SCMT] ×2
  ◀ Acid [ACID] ×2

  ▶ Copper [COPR] ×7
  ▶ Slag [SLAG] ×1

**Tropical Paradise**
  ◀ Copper Concentrate [COCO] ×4
  ◀ Scrap Metal [SCMT] ×2
  ◀ Coke [COKE] ×2

  ▶ Copper [COPR] ×5
  ▶ Slag [SLAG] ×1
  ▶ Sulphuric Acid [SUAC] ×2

**⚠️ IAHC**
  ◀ Copper Ore [CORE] ×5
  ◀ Refined Oil [RFPR] ×3

  ▶ Copper [COPR] ×8

**Steel City**
  ◀ Copper Concentrate [COCO] ×4
  ◀ Scrap Metal [SCMT] ×2
  ◀ Acid [ACID] ×2

  ▶ Copper [COPR] ×6
  ▶ Slag [SLAG] ×1
  ▶ Sulphur [SULP] ×1

---

### Dairy (`dairy`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC

**Extreme Classic**
  ◀ Milk [MILK] ×6
  ◀ Packaging [MNSP] ×2

  ▶ Food [FOOD] ×8
  ▶ Edible Oil [EOIL] ×2

**Tropical Paradise**
  ◀ Milk [MILK] ×6
  ◀ Packaging [MNSP] ×2

  ▶ Food [FOOD] ×8
  ▶ Edible Oil [EOIL] ×2

**⚠️ BLTC**
  ◀ Milk [MILK] ×6
  ◀ Packaging [MNSP] ×2

  ▶ Food [FOOD] ×8

---

### Distillery and Winery (`cider_mill`)
**Type**: Secondary | **Economies**: Tropical Paradise

  ◀ Produce [FRUT] ×3
  ◀ Sugar Cane [SGCN] ×3
  ◀ Packaging [MNSP] ×1
  ◀ Food Additives [ENUM] ×1

  ▶ Alcohol [BEER] ×6
  ▶ Acetic Acid [ACET] ×3
  ▶ Biomass [BIOM] ×2

---

### Edible Oil Refinery (`edible_oil_refinery`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise

**Extreme Classic**
  ◀ Oil Seeds [OLSD] ×4

  ▶ Edible Oil [EOIL] ×4
  ▶ Biomass [BIOM] ×1

**Tropical Paradise**
  ◀ Oil Seeds [OLSD] ×6

  ▶ Edible Oil [EOIL] ×4
  ▶ Biomass [BIOM] ×1

---

### Electric Arc Furnace (`electric_arc_furnace`)
**Type**: Secondary | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Scrap Metal [SCMT] ×4
  ◀ Quicklime [QLME] ×2

  ▶ Steel [STEL] ×6
  ▶ Slag [SLAG] ×2

**Steel City**
  ◀ Scrap Metal [SCMT] ×4
  ◀ Ferroalloy [FECR] ×2
  ◀ Quicklime [QLME] ×1
  ◀ Oxygen [O2__] ×1

  ▶ Carbon Steel [STCB] ×4
  ▶ Alloy Steel [STAL] ×2
  ▶ Slag [SLAG] ×2

---

### Electrical Works (`electrical_works`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Copper [COPR] ×2
  ◀ Rubber Parts [TYRE] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Rare Metals [RAMT] ×2

  ▶ Electrical Parts [POWR] ×6

**Tropical Paradise**
  ◀ Copper [COPR] ×2
  ◀ Sulphuric Acid [SUAC] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Rare Metals [RAMT] ×2

  ▶ Vehicle Parts [VPTS] ×6
  ▶ Goods [GOOD] ×6

**Steel City**
  ◀ Alloy Steel [STAL] ×3
  ◀ Copper [COPR] ×2
  ◀ Refined Oil [RFPR] ×1
  ◀ Metal Wire [STWR] ×1
  ◀ Plastic Parts [PPAR] ×1

  ▶ Electrical Parts [POWR] ×8

---

### Engine Plant (`engine_plant`)
**Type**: Secondary | **Economies**: Steel City

  ◀ Metal Parts [MPAR] ×2
  ◀ Aluminium [ALUM] ×2
  ◀ Rubber Parts [TYRE] ×2
  ◀ Refined Oil [RFPR] ×2

  ▶ Vehicle Engines [VENG] ×8

---

### Engineering Supply Yard (`supply_yard`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Vehicles [VEHI] ×8
  ◀ Petroleum Fuels [PETR] ×8
  ◀ Explosives [BOOM] ×8

  ▶ Engineering Supplies [ENSP] ×8

**Tropical Paradise**
  ◀ Vehicles [VEHI] ×8
  ◀ Petroleum Fuels [PETR] ×8
  ◀ Explosives [BOOM] ×8

  ▶ Engineering Supplies [ENSP] ×8

**⚠️ BLTC**
  ◀ Vehicles [VEHI] ×8
  ◀ Petroleum Fuels [PETR] ×8

  ▶ Engineering Supplies [ENSP] ×4
  ▶ Farm Supplies [FMSP] ×4

**⚠️ IAHC**
  ◀ Building Materials [BDMT] ×8
  ◀ Petroleum Fuels [PETR] ×8
  ◀ Goods [GOOD] ×8

  ▶ Engineering Supplies [ENSP] ×4
  ▶ Farm Supplies [FMSP] ×4

**Steel City**
  ◀ Ammonium Nitrate [NHNO] ×8
  ◀ Vehicles [VEHI] ×8
  ◀ Petroleum Fuels [PETR] ×8
  ◀ Rubber Parts [TYRE] ×8

  ▶ Engineering Supplies [ENSP] ×8

---

### Farm Supply Yard (`farm_supply_yard`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Vehicles [VEHI] ×8
  ◀ Petroleum Fuels [PETR] ×8
  ◀ Fertiliser [FERT] ×8

  ▶ Farm Supplies [FMSP] ×8

**Tropical Paradise**
  ◀ Vehicles [VEHI] ×8
  ◀ Petroleum Fuels [PETR] ×8
  ◀ Fertiliser [FERT] ×8

  ▶ Farm Supplies [FMSP] ×8

**Steel City**
  ◀ Ammonium Nitrate [NHNO] ×8
  ◀ Vehicles [VEHI] ×8
  ◀ Petroleum Fuels [PETR] ×8
  ◀ Rubber Parts [TYRE] ×8

  ▶ Farm Supplies [FMSP] ×8

---

### Ferroalloy Smelter (`ferrochrome_smelter`)
**Type**: Secondary | **UNUSED** -- not enabled in any economy

---

### Fertiliser Plant (`fertiliser_plant`)
**Type**: Secondary | **Economies**: Tropical Paradise, ⚠️ BLTC, Steel City

**Tropical Paradise**
  ◀ Phosphoric Acid [PHAC] ×4
  ◀ Biomass [BIOM] ×2
  ◀ Slag [SLAG] ×2

  ▶ Fertiliser [FERT] ×6

**⚠️ BLTC**
  ◀ Urea [UREA] ×2
  ◀ Potash [POTA] ×2
  ◀ Phosphoric Acid [PHAC] ×2
  ◀ Ammonium Nitrate [NHNO] ×2

  ▶ Farm Supplies [FMSP] ×8

**Steel City**
  ◀ Ammonium Nitrate [NHNO] ×6
  ◀ Slag [SLAG] ×2
  ◀ Acid [ACID] ×2

  ▶ Farm Supplies [FMSP] ×8

---

### Fishing Harbour (`fishing_harbour`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ BLTC

**Extreme Classic**
  ◀ Fish [FISH] ×6
  ◀ Packaging [MNSP] ×1

  ▶ Food [FOOD] ×8

**⚠️ Boreal**
  ◀ Fish [FISH] ×6

  ▶ Food [FOOD] ×8

**Tropical Paradise**
  ◀ Fish [FISH] ×6

  ▶ Meat [MEAT] ×8

**⚠️ BLTC**
  ◀ Fish [FISH] ×6
  ◀ Packaging [MNSP] ×1
  ◀ Food Additives [ENUM] ×1

  ▶ Food [FOOD] ×8

---

### Flour Mill (`flour_mill`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Grain [GRAI] ×6
  ◀ Packaging [MNSP] ×4

  ▶ Food [FOOD] ×6
  ▶ Edible Oil [EOIL] ×4

**Tropical Paradise**
  ◀ Grain [GRAI] ×6

  ▶ Flour [BAKE] ×6

**⚠️ BLTC**
  ◀ Grain [GRAI] ×6
  ◀ Packaging [MNSP] ×4

  ▶ Food [FOOD] ×6

**⚠️ IAHC**
  ◀ Cassava [CASS] ×6
  ◀ Maize [MAIZ] ×6

  ▶ Food [FOOD] ×6

**Steel City**
  ◀ Grain [GRAI] ×6
  ◀ Packaging [MNSP] ×4

  ▶ Food [FOOD] ×6

---

### Forge and Foundry (`iron_works`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Iron [IRON] ×3
  ◀ Aluminium [ALUM] ×2
  ◀ Sand [SAND] ×2

  ▶ Metal Parts [MPAR] ×6

**Tropical Paradise**
  ◀ Iron [IRON] ×3
  ◀ Coal [COAL] ×2
  ◀ Sand [SAND] ×2

  ▶ Metal Parts [MPAR] ×6

**Steel City**
  ◀ Iron [IRON] ×3
  ◀ Aluminium [ALUM] ×3
  ◀ Sand [SAND] ×2

  ▶ Metal Parts [MPAR] ×7
  ▶ Slag [SLAG] ×1

---

### Fruit Packing Plant (`fruit_packing_plant`)
**Type**: Secondary | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Produce [FRUT] ×4
  ◀ Flour [BAKE] ×4
  ◀ Packaging [MNSP] ×2
  ◀ Acetic Acid [ACET] ×2

  ▶ Food [FOOD] ×8

**Steel City**
  ◀ Produce [FRUT] ×6
  ◀ Packaging [MNSP] ×3

  ▶ Food [FOOD] ×8

---

### Furniture Factory (`furniture_factory`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC

**Extreme Classic**
  ◀ Timber [WDPR] ×4
  ◀ Textiles [TEXT] ×2
  ◀ Metal Parts [MPAR] ×2
  ◀ Glass [GLAS] ×2

  ▶ Goods [GOOD] ×6

**Tropical Paradise**
  ◀ Timber [WDPR] ×4
  ◀ Textiles [TEXT] ×2
  ◀ Metal Parts [MPAR] ×2
  ◀ Glass [GLAS] ×2
  ◀ Paints & Coatings [COAT] ×2

  ▶ Goods [GOOD] ×6

**⚠️ BLTC**
  ◀ Timber [WDPR] ×6
  ◀ Paints & Coatings [COAT] ×2

  ▶ Furniture [FURN] ×8

---

### Glass Works (`glass_works`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Sand [SAND] ×6
  ◀ Soda Ash [SASH] ×2
  ◀ Quicklime [QLME] ×2

  ▶ Glass [GLAS] ×8
  ▶ Packaging [MNSP] ×8

**Tropical Paradise**
  ◀ Sand [SAND] ×4
  ◀ Soda Ash [SASH] ×2
  ◀ Quicklime [QLME] ×1
  ◀ Plastics [PLAS] ×1

  ▶ Glass [GLAS] ×8

**⚠️ BLTC**
  ◀ Sand [SAND] ×6
  ◀ Soda Ash [SASH] ×2

  ▶ Glass [GLAS] ×8

**⚠️ IAHC**
  ◀ Sand [SAND] ×6
  ◀ Refined Oil [RFPR] ×2

  ▶ Building Materials [BDMT] ×4
  ▶ Goods [GOOD] ×4

**Steel City**
  ◀ Sand [SAND] ×4
  ◀ Soda Ash [SASH] ×2
  ◀ Quicklime [QLME] ×1
  ◀ Plastics [PLAS] ×1

  ▶ Glass [GLAS] ×6
  ▶ Packaging [MNSP] ×4

---

### Latex Processor (`latex_processor`)
**Type**: Secondary | **UNUSED** -- not enabled in any economy

---

### Lime Kiln (`lime_kiln`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Limestone [LIME] ×6
  ◀ Petroleum Fuels [PETR] ×2

  ▶ Quicklime [QLME] ×6

**Tropical Paradise**
  ◀ Limestone [LIME] ×6
  ◀ Petroleum Fuels [PETR] ×2

  ▶ Quicklime [QLME] ×6
  ▶ Fertiliser [FERT] ×2

**⚠️ BLTC**
  ◀ Limestone [LIME] ×8

  ▶ Quicklime [QLME] ×6
  ▶ Farm Supplies [FMSP] ×2

**Steel City**
  ◀ Limestone [LIME] ×6
  ◀ Petroleum Fuels [PETR] ×2

  ▶ Quicklime [QLME] ×8

---

### Machinery Factory (`machine_shop`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Electrical Parts [POWR] ×3
  ◀ Vehicle Parts [VPTS] ×2
  ◀ Metal Parts [MPAR] ×2
  ◀ Rubber Parts [TYRE] ×2
  ◀ Glass [GLAS] ×2

  ▶ Goods [GOOD] ×4
  ▶ Engineering Supplies [ENSP] ×2
  ▶ Farm Supplies [FMSP] ×2

**Tropical Paradise**
  ◀ Steel [STEL] ×3
  ◀ Glass [GLAS] ×2
  ◀ Vehicle Parts [VPTS] ×2
  ◀ Rubber Parts [TYRE] ×1

  ▶ Goods [GOOD] ×4
  ▶ Engineering Supplies [ENSP] ×2
  ▶ Farm Supplies [FMSP] ×2

**Steel City**
  ◀ Electrical Parts [POWR] ×2
  ◀ Vehicle Engines [VENG] ×2
  ◀ Vehicle Parts [VPTS] ×2
  ◀ Metal Parts [MPAR] ×1
  ◀ Paints & Coatings [COAT] ×1

  ▶ Goods [GOOD] ×4
  ▶ Engineering Supplies [ENSP] ×2
  ▶ Farm Supplies [FMSP] ×2

---

### Meat Packing Plant (`meat_packing_plant`)
**Type**: Secondary | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Meat [MEAT] ×4
  ◀ Packaging [MNSP] ×2
  ◀ Food Additives [ENUM] ×2

  ▶ Food [FOOD] ×6
  ▶ Edible Oil [EOIL] ×4
  ▶ Biomass [BIOM] ×2

**Steel City**
  ◀ Fish [FISH] ×6
  ◀ Packaging [MNSP] ×3
  ◀ Salt [SALT] ×2

  ▶ Food [FOOD] ×8

---

### Metal Workshop (`metal_workshop`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Steel [STEL] ×6
  ◀ Aluminium [ALUM] ×6
  ◀ Paints & Coatings [COAT] ×2

  ▶ Metal Parts [MPAR] ×8
  ▶ Packaging [MNSP] ×6

**Tropical Paradise**
  ◀ Steel [STEL] ×2
  ◀ Copper [COPR] ×2
  ◀ Rare Metals [RAMT] ×2
  ◀ Cleaning Agents [SOAP] ×2

  ▶ Metal Parts [MPAR] ×6
  ▶ Goods [GOOD] ×4

**Steel City**
  ◀ Steel Sheet [STSH] ×2
  ◀ Paints & Coatings [COAT] ×2
  ◀ Zinc [ZINC] ×2
  ◀ Metal Wire [STWR] ×2

  ▶ Packaging [MNSP] ×3
  ▶ Metal Parts [MPAR] ×4
  ▶ Scrap Metal [SCMT] ×1

---

### Moulding Plant (`plastics_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Plastics [PLAS] ×5
  ◀ Metal Parts [MPAR] ×3

  ▶ Packaging [MNSP] ×6

**Tropical Paradise**
  ◀ Plastics [PLAS] ×2
  ◀ Steel [STEL] ×2
  ◀ Glass [GLAS] ×2

  ▶ Packaging [MNSP] ×6

**⚠️ BLTC**
  ◀ Chlorine [CHLO] ×4
  ◀ Monomer [C2H4] ×4

  ▶ Plastics [PLAS] ×3
  ▶ Paints & Coatings [COAT] ×3

**Steel City**
  ◀ Plastics [PLAS] ×5
  ◀ Metal Parts [MPAR] ×3

  ▶ Plastic Parts [PPAR] ×6
  ▶ Packaging [MNSP] ×5

---

### Naphtha Cracker (`ethylene_cracker`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Refined Oil [RFPR] ×4
  ◀ Tar [CTAR] ×4

  ▶ Petroleum Fuels [PETR] ×5
  ▶ Coke [COKE] ×3
  ▶ Sulphur [SULP] ×2

**⚠️ BLTC**
  ◀ Naphtha [NAPH] ×8

  ▶ Monomer [C2H4] ×4
  ▶ Propylene [C3H6] ×3

**Steel City**
  ◀ Refined Oil [RFPR] ×5
  ◀ Tar [CTAR] ×3

  ▶ Monomer [C2H4] ×5
  ▶ Petroleum Fuels [PETR] ×3

---

### Oil Refinery (`oil_refinery`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Oil [OIL_] ×8

  ▶ Refined Oil [RFPR] ×6
  ▶ Petroleum Fuels [PETR] ×4
  ▶ Tar [CTAR] ×4

**Tropical Paradise**
  ◀ Oil [OIL_] ×8

  ▶ Refined Oil [RFPR] ×6
  ▶ Petroleum Fuels [PETR] ×4
  ▶ Sulphur [SULP] ×2

**⚠️ BLTC**
  ◀ Oil [OIL_] ×8

  ▶ Petroleum Fuels [PETR] ×3
  ▶ Naphtha [NAPH] ×3
  ▶ Sulphur [SULP] ×2

**Steel City**
  ◀ Oil [OIL_] ×7
  ◀ Hydrogen [H2__] ×1

  ▶ Refined Oil [RFPR] ×4
  ▶ Petroleum Fuels [PETR] ×2
  ▶ Tar [CTAR] ×1
  ▶ Sulphur [SULP] ×1

---

### Paint Factory (`factory_3`)
**Type**: Secondary | **Economies**: ⚠️ BLTC, Steel City

**⚠️ BLTC**
  ◀ Glass [GLAS] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Aluminium [ALUM] ×2
  ◀ Tinplate [TINP] ×2

  ▶ Packaging [MNSP] ×8

**Steel City**
  ◀ Refined Oil [RFPR] ×2
  ◀ Quicklime [QLME] ×2
  ◀ Carbon Black [CBLK] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Paints & Coatings [COAT] ×8

---

### Paint Factory (`paint_factory`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Refined Oil [RFPR] ×2
  ◀ Quicklime [QLME] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Packaging [MNSP] ×2

  ▶ Paints & Coatings [COAT] ×6
  ▶ Goods [GOOD] ×4

**Tropical Paradise**
  ◀ Refined Oil [RFPR] ×2
  ◀ Quicklime [QLME] ×2
  ◀ Acetic Acid [ACET] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Paints & Coatings [COAT] ×6
  ▶ Goods [GOOD] ×4

**⚠️ BLTC**
  ◀ Glass [GLAS] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Aluminium [ALUM] ×2
  ◀ Tinplate [TINP] ×2

  ▶ Packaging [MNSP] ×8

**Steel City**
  ◀ Refined Oil [RFPR] ×2
  ◀ Quicklime [QLME] ×2
  ◀ Carbon Black [CBLK] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Packaging [MNSP] ×2

  ▶ Paints & Coatings [COAT] ×6
  ▶ Goods [GOOD] ×4

---

### Paper Mill (`paper_mill`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise

**Extreme Classic**
  ◀ Clay [CLAY] ×2
  ◀ Logs [WOOD] ×4
  ◀ Sulphur [SULP] ×2

  ▶ Paper [PAPR] ×6
  ▶ Packaging [MNSP] ×8

**⚠️ Boreal**
  ◀ Kaolin [KAOL] ×2
  ◀ Logs [WOOD] ×4
  ◀ Sulphur [SULP] ×2

  ▶ Paper [PAPR] ×8

**Tropical Paradise**
  ◀ Logs [WOOD] ×4
  ◀ Clay [CLAY] ×2
  ◀ Sulphuric Acid [SUAC] ×2

  ▶ Goods [GOOD] ×4
  ▶ Packaging [MNSP] ×7

---

### Phosphoric Acid Plant (`phosphoric_acid_plant`)
**Type**: Secondary | **Economies**: Tropical Paradise, ⚠️ BLTC

**Tropical Paradise**
  ◀ Phosphate [PHOS] ×4
  ◀ Sulphuric Acid [SUAC] ×4

  ▶ Phosphoric Acid [PHAC] ×6
  ▶ Food Additives [ENUM] ×2

**⚠️ BLTC**
  ◀ Phosphate [PHOS] ×4
  ◀ Sulphuric Acid [SUAC] ×4

  ▶ Phosphoric Acid [PHAC] ×4

---

### Polymerisation Plant (`polyethylene_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Refined Oil [RFPR] ×6
  ◀ Chlorine [CHLO] ×2
  ◀ Acid [ACID] ×2

  ▶ Plastics [PLAS] ×5
  ▶ Rubber [RUBR] ×3
  ▶ Fibres [FICR] ×3

**Tropical Paradise**
  ◀ Refined Oil [RFPR] ×6
  ◀ Acetic Acid [ACET] ×2

  ▶ Plastics [PLAS] ×5
  ▶ Rubber [RUBR] ×3

**⚠️ BLTC**
  ◀ Monomer [C2H4] ×8

  ▶ Plastics [PLAS] ×8

**Steel City**
  ◀ Monomer [C2H4] ×5
  ◀ Chlorine [CHLO] ×3

  ▶ Plastics [PLAS] ×8

---

### Printing Plant (`printing_plant`)
**Type**: Secondary | **Economies**: Extreme Classic

  ◀ Paper [PAPR] ×6
  ◀ Paints & Coatings [COAT] ×2

  ▶ Goods [GOOD] ×6
  ▶ Mail [MAIL] ×6

---

### Pyrite Smelter (`pyrite_smelter`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ Boreal, Steel City

**Extreme Classic**
  ◀ Pyrite Ore [PORE] ×6
  ◀ Coke [COKE] ×2
  ◀ Acid [ACID] ×2

  ▶ Zinc [ZINC] ×4
  ▶ Rare Metals [RAMT] ×3

**⚠️ Boreal**
  ◀ Pyrite Ore [PORE] ×8

  ▶ Zinc [ZINC] ×4
  ▶ Sulphur [SULP] ×4

**Steel City**
  ◀ Pyrite Ore [PORE] ×6
  ◀ Coke [COKE] ×1
  ◀ Cleaning Agents [SOAP] ×1

  ▶ Zinc [ZINC] ×2
  ▶ Copper Concentrate [COCO] ×3
  ▶ Slag [SLAG] ×1
  ▶ Ferroalloy [FECR] ×2

---

### Recycling Plant (`recycling_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Recyclables [RCYC] ×6

  ▶ Plastics [PLAS] ×3

---

### Sawmill (`sawmill`)
**Type**: Secondary | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ IAHC

  ◀ Logs [WOOD] ×6

  ▶ Timber [WDPR] ×8

---

### Scrap Yard (`junk_yard`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Recyclables [RCYC] ×6

  ▶ Scrap Metal [SCMT] ×3

**Tropical Paradise**
  ◀ Recyclables [RCYC] ×6

  ▶ Scrap Metal [SCMT] ×4
  ▶ Rare Metals [RAMT] ×1

**Steel City**
  ◀ Recyclables [RCYC] ×6

  ▶ Scrap Metal [SCMT] ×3

---

### Sheet Mill (`sheet_and_pipe_mill`)
**Type**: Secondary | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Steel [STEL] ×4
  ◀ Zinc [ZINC] ×3
  ◀ Acid [ACID] ×2

  ▶ Metal Parts [MPAR] ×6
  ▶ Building Materials [BDMT] ×6

**Steel City**
  ◀ Carbon Steel [STCB] ×4
  ◀ Zinc [ZINC] ×2
  ◀ Acid [ACID] ×2

  ▶ Steel Sheet [STSH] ×8

---

### Slag Grinding Plant (`slag_grinding_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Slag [SLAG] ×8

  ▶ Cement [CMNT] ×8
  ▶ Fertiliser [FERT] ×5

**Steel City**
  ◀ Slag [SLAG] ×8

  ▶ Cement [CMNT] ×8

---

### Smithy Forge (`smithy_forge`)
**Type**: Secondary | **UNUSED** -- not enabled in any economy

---

### Solvay Plant (`solvay_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Salt [SALT] ×4
  ◀ Limestone [LIME] ×2
  ◀ Refined Oil [RFPR] ×2

  ▶ Soda Ash [SASH] ×8

**Tropical Paradise**
  ◀ Salt [SALT] ×4
  ◀ Limestone [LIME] ×2
  ◀ Refined Oil [RFPR] ×2

  ▶ Soda Ash [SASH] ×8

**⚠️ BLTC**
  ◀ Salt [SALT] ×8

  ▶ Soda Ash [SASH] ×6

**Steel City**
  ◀ Salt [SALT] ×4
  ◀ Limestone [LIME] ×2
  ◀ Ammonia [NH3_] ×2

  ▶ Soda Ash [SASH] ×8

---

### Steel Mill (`integrated_steel_mill`)
**Type**: Secondary | **UNUSED** -- not enabled in any economy

---

### Steel Mill (`steel_mill`)
**Type**: Secondary | **Economies**: ⚠️ BLTC

  ◀ Iron Ore [IORE] ×2
  ◀ Coke [COKE] ×2
  ◀ Limestone [LIME] ×2
  ◀ Hydrochloric Acid [HYAC] ×1
  ◀ Oxygen [O2__] ×1

  ▶ Steel [STEL] ×8

---

### Sugar Refinery (`sugar_refinery`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC

**Extreme Classic**
  ◀ Packaging [MNSP] ×3
  ◀ Sugar Beet [SGBT] ×5

  ▶ Food [FOOD] ×6
  ▶ Biomass [BIOM] ×2

**Tropical Paradise**
  ◀ Sugar Cane [SGCN] ×6
  ◀ Phosphate [PHOS] ×1
  ◀ Food Additives [ENUM] ×1

  ▶ Sugar [SUGR] ×6
  ▶ Biomass [BIOM] ×2

**⚠️ BLTC**
  ◀ Packaging [MNSP] ×3
  ◀ Sugar Beet [SGBT] ×5

  ▶ Food [FOOD] ×8

---

### Synthetic Rubber Plant (`polypropylene_plant`)
**Type**: Secondary | **Economies**: ⚠️ BLTC, Steel City

**⚠️ BLTC**
  ◀ Propylene [C3H6] ×8

  ▶ Plastics [PLAS] ×8

**Steel City**
  ◀ Monomer [C2H4] ×5
  ◀ Acid [ACID] ×3

  ▶ Rubber [RUBR] ×8

---

### Textile Mill (`textile_mill`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC

**Extreme Classic**
  ◀ Fibres [FICR] ×4
  ◀ Paints & Coatings [COAT] ×2

  ▶ Textiles [TEXT] ×7
  ▶ Goods [GOOD] ×4

**Tropical Paradise**
  ◀ Fibres [FICR] ×5
  ◀ Plastics [PLAS] ×2
  ◀ Acetic Acid [ACET] ×1

  ▶ Textiles [TEXT] ×7
  ▶ Goods [GOOD] ×4

**⚠️ BLTC**
  ◀ Fibres [FICR] ×6

  ▶ Textiles [TEXT] ×8

**⚠️ IAHC**
  ◀ Yarn [YARN] ×6

  ▶ Textiles [TEXT] ×8

---

### Timber Yard (`lumber_yard`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC

**Extreme Classic**
  ◀ Timber [WDPR] ×4
  ◀ Metal Parts [MPAR] ×2
  ◀ Paints & Coatings [COAT] ×2

  ▶ Building Materials [BDMT] ×6
  ▶ Packaging [MNSP] ×6

**Tropical Paradise**
  ◀ Timber [WDPR] ×4
  ◀ Glass [GLAS] ×2
  ◀ Metal Parts [MPAR] ×1
  ◀ Paints & Coatings [COAT] ×1

  ▶ Building Materials [BDMT] ×6
  ▶ Packaging [MNSP] ×6

**⚠️ BLTC**
  ◀ Timber [WDPR] ×6
  ◀ Paints & Coatings [COAT] ×2

  ▶ Engineering Supplies [ENSP] ×8

**⚠️ IAHC**
  ◀ Timber [WDPR] ×6
  ◀ Refined Oil [RFPR] ×2

  ▶ Building Materials [BDMT] ×8

---

### Tinplate Works (`tinplate_works`)
**Type**: Secondary | **Economies**: ⚠️ BLTC

  ◀ Steel [STEL] ×4
  ◀ Tin [TIN_] ×2
  ◀ Hydrochloric Acid [HYAC] ×2

  ▶ Tinplate [TINP] ×8

---

### Tyre and Rubber Plant (`tyre_plant`)
**Type**: Secondary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Rubber [RUBR] ×4
  ◀ Metal Parts [MPAR] ×2
  ◀ Sulphur [SULP] ×2

  ▶ Rubber Parts [TYRE] ×8
  ▶ Goods [GOOD] ×4

**Tropical Paradise**
  ◀ Rubber [RUBR] ×4
  ◀ Metal Parts [MPAR] ×2
  ◀ Sulphur [SULP] ×2

  ▶ Rubber Parts [TYRE] ×8
  ▶ Plastics [PLAS] ×4

**Steel City**
  ◀ Rubber [RUBR] ×2
  ◀ Carbon Black [CBLK] ×2
  ◀ Sulphur [SULP] ×2
  ◀ Metal Wire [STWR] ×2

  ▶ Rubber Parts [TYRE] ×8

---

### Wire and Section Mill (`wire_and_section_mill`)
**Type**: Secondary | **Economies**: Steel City

  ◀ Carbon Steel [STCB] ×3
  ◀ Cleaning Agents [SOAP] ×1
  ◀ Aluminium [ALUM] ×2
  ◀ Copper [COPR] ×2

  ▶ Metal Parts [MPAR] ×4
  ▶ Metal Wire [STWR] ×3
  ▶ Scrap Metal [SCMT] ×1

---

## Tertiary Industries

---

### General Store (`general_store`)
**Type**: Tertiary | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Food [FOOD]
  ◀ Goods [GOOD]
  ◀ Alcohol [BEER]

**⚠️ Boreal**
  ◀ Food [FOOD]

**Tropical Paradise**
  ◀ Food [FOOD]
  ◀ Goods [GOOD]
  ◀ Alcohol [BEER]

**⚠️ BLTC**
  ◀ Food [FOOD]
  ◀ Goods [GOOD]
  ◀ Alcohol [BEER]

**⚠️ IAHC**
  ◀ Food [FOOD]
  ◀ Goods [GOOD]
  ◀ Alcohol [BEER]

**Steel City**
  ◀ Food [FOOD]

---

### Grocer's Shop (`food_market`)
**Type**: Tertiary | **Economies**: Extreme Classic, ⚠️ BLTC, Steel City

**Extreme Classic**
  ◀ Food [FOOD]
  ◀ Produce [FRUT]
  ◀ Alcohol [BEER]

**⚠️ BLTC**
  ◀ Food [FOOD]
  ◀ Produce [FRUT]
  ◀ Alcohol [BEER]

**Steel City**
  ◀ Food [FOOD]

---

### Hardware Store (`hardware_store`)
**Type**: Tertiary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

**Extreme Classic**
  ◀ Goods [GOOD]
  ◀ Building Materials [BDMT]

**Tropical Paradise**
  ◀ Goods [GOOD]
  ◀ Building Materials [BDMT]

**⚠️ BLTC**

**⚠️ IAHC**
  ◀ Goods [GOOD]
  ◀ Building Materials [BDMT]

**Steel City**
  ◀ Goods [GOOD]

---

### Hotel (`hotel`)
**Type**: Tertiary | **UNUSED** -- not enabled in any economy

---

### Petrol Station (`petrol_pump`)
**Type**: Tertiary | **Economies**: Extreme Classic, Tropical Paradise, ⚠️ IAHC, Steel City

  ◀ Food [FOOD]
  ◀ Goods [GOOD]
  ◀ Petroleum Fuels [PETR]

---

### Power Plant (`power_plant`)
**Type**: Tertiary | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Coal [COAL]
  ◀ Petroleum Fuels [PETR]
  ◀ Biomass [BIOM]

**⚠️ Boreal**
  ◀ Peat [PEAT]

**Tropical Paradise**
  ◀ Coal [COAL]
  ◀ Petroleum Fuels [PETR]
  ◀ Biomass [BIOM]

**Steel City**
  ◀ Coal [COAL]
  ◀ Petroleum Fuels [PETR]

---

### Vehicle Distributor (`vehicle_distributor`)
**Type**: Tertiary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Vehicles [VEHI]

---

## Informative Industries

---

### Plaza (`plaza`)
**Type**: Informative | **Economies**: Extreme Classic, ⚠️ Boreal, Tropical Paradise, ⚠️ BLTC, ⚠️ IAHC, Steel City

