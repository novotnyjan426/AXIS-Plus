# AXIS+ Industry Catalog

Complete reference for all industries in the AXIS+ NewGRF set.
Auto-generated from `src/industries/*.py` definitions.

## Summary

| Type | Count | Boost Mechanic |
|------|------:|----------------|
| Primary Extractive | 21 | Deliver Engineering Supplies [ENSP] |
| Primary Organic | 13 | Deliver Farm Supplies [FMSP] |
| Primary Port | 4 | Deliver any accepted cargo |
| Primary (No Supplies) | 2 | None (static production) |
| Town Producer | 1 | None (scales with town population) |
| Secondary | 75 | Combinatory: deliver more input types for higher ratio |
| Tertiary | 7 | None (consumer / black hole) |
| Informative | 1 | None (information only) |
| **Total** | **124** | |

## Exceptions and Gotchas

**Unused industries** (7) -- not enabled in any economy:
- `chromite_mine`
- `ferrochrome_smelter`
- `hotel`
- `integrated_steel_mill`
- `latex_processor`
- `potash_mine`
- `smithy_forge`

**Removed economy-only industries** (5) -- these existed only in removed economies
(Boreal, BLTC, IAHC) and are still defined in code but not enabled anywhere.
Candidates for re-use in future economies:
- `diamond_mine` (Primary Extractive, was IAHC) -- produced Diamonds [DIAM] ×12
- `manganese_mine` (Primary Extractive, was IAHC) -- produced Manganese [MNO2] ×20
- `herding_coop` (Primary Organic, was Boreal) -- produced Food [FOOD] ×7
- `steel_mill` (Secondary, was BLTC) -- Iron Ore + Coke + Limestone + HCl + O₂ → Steel
- `tinplate_works` (Secondary, was BLTC) -- Steel + Tin + HCl → Tinplate

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

**Combinatory mode (ALL vs ANY):**

Each secondary industry is marked with a combinatory mode:

- **🔗 ALL** — Input ratios are designed to sum to 8. Supply **all** accepted cargos
  for maximum throughput. Missing inputs directly reduce the ratio.
- **⚡ ANY** — Each input independently contributes a high ratio. Supplying **any
  single** input already gives good throughput; additional inputs may push ratio
  above 8 (effectively capped at 8).

**Example (ALL):** Blast furnace (Steel City) accepts Iron Ore ×3, Coke ×3, Limestone ×2.
If all three are supplied: ratio = 3+3+2 = 8 (full throughput = 100% of input).
If only Iron Ore + Coke: ratio = 6 (75% throughput).
Output split: Iron ×6/8 = 75%, Slag ×2/8 = 25% of total produced.

**Example (ANY):** Biorefinery (Extreme Classic) accepts Sugar Beet ×6, Biomass ×6, Oil Seeds ×6.
Delivering only Sugar Beet: ratio = 6/8 (75% throughput).
Delivering Sugar Beet + Biomass: ratio = 12/8, capped at 8/8 (full throughput).
Any single input already gives strong production — no need to supply all three.

**Required vs Booster cargos (warehouse industries):**

Some secondary industries use a **warehouse model** (`base_processing_cap` > 0) where
delivered cargo is stored and processed each 256-tick cycle. Among these, some have
**required input cargos** — marked with ★ in this catalog. If any required cargo's
warehouse is empty, the industry produces **nothing**. Other inputs are **boosters**:
they increase the production ratio but are not mandatory.

In the industry window in-game, required cargos show `required` label (orange when
empty), booster cargos show `booster` label.

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
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Engineering Supplies [ENSP]

  ▶ Copper Ore [CORE] ×20

---

### Dredging Site (`dredging_site`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×17

**Tropical Paradise**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×17
  ▶ Clay [CLAY] ×16

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

### Nitrate Mine (`nitrate_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Engineering Supplies [ENSP]

  ▶ Nitrates [NITR] ×18

---

### Oil Rig (`oil_rig`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Oil [OIL_] ×29
  ▶ Passengers [PASS] ×4

---

### Oil Wells (`oil_wells`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Oil [OIL_] ×28

---

### Peatlands (`peatlands`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic

**Extreme Classic**
  ◀ Engineering Supplies [ENSP]

  ▶ Biomass [BIOM] ×18

---

### Phosphate Mine (`phosphate_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Tropical Paradise

**Tropical Paradise**
  ◀ Engineering Supplies [ENSP]

  ▶ Phosphate [PHOS] ×16

---

### Potash Mine (`potash_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **UNUSED** -- not enabled in any economy

---

### Pyrite Mine (`pyrite_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Steel City

  ◀ Engineering Supplies [ENSP]

  ▶ Pyrite Ore [PORE] ×20

---

### Quarry (`quarry`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Limestone [LIME] ×14

**Tropical Paradise**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Limestone [LIME] ×14

**Steel City**
  ◀ Engineering Supplies [ENSP]

  ▶ Sand [SAND] ×14
  ▶ Limestone [LIME] ×14

---

### Salt Evaporator (`salt_evaporator`)
**Type**: Primary Extractive (NOT boostable -- accept overridden) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ▶ Salt [SALT] ×15

---

### Salt Mine (`salt_mine`)
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Engineering Supplies [ENSP]

  ▶ Salt [SALT] ×20

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
**Type**: Primary Extractive (boost with Engineering Supplies [ENSP]) | **Economies**: Extreme Classic, Steel City

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
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Farm Supplies [FMSP]

  ▶ Livestock [LVST] ×12
  ▶ Milk [MILK] ×14

---

### Fish Farm (`fish_farm`)
**Type**: Primary Organic (NOT boostable -- accept overridden) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ▶ Fish [FISH] ×8

---

### Forest (`forest`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise

**Extreme Classic**
  ◀ Farm Supplies [FMSP]

  ▶ Logs [WOOD] ×19

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Logs [WOOD] ×19

---

### Fruit Plantation (`fruit_plantation`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×16
  ▶ Oil Seeds [OLSD] ×13

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×16
  ▶ Oil Seeds [OLSD] ×13

**Steel City**
  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×16

---

### Mixed Farm (`farm`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Farm Supplies [FMSP]

  ▶ Oil Seeds [OLSD] ×20
  ▶ Livestock [LVST] ×12

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Grain [GRAI] ×20
  ▶ Livestock [LVST] ×12

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
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise

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
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Tropical Paradise

**Tropical Paradise**
  ◀ Farm Supplies [FMSP]

  ▶ Food Additives [ENUM] ×13

---

### Vineyard (`vineyard`)
**Type**: Primary Organic (boost with Farm Supplies [FMSP]) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Farm Supplies [FMSP]

  ▶ Produce [FRUT] ×14

---

## Primary Port Industries

---

### Bulk Terminal (`bulk_terminal`)
**Type**: Primary Port (boost with accepted cargo) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

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
**Type**: Primary Port (boost with accepted cargo) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

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
**Type**: Primary Port (boost with accepted cargo) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Building Materials [BDMT]
  ◀ Food [FOOD]
  ◀ Alcohol [BEER]
  ◀ Paper [PAPR]

  ▶ Engineering Supplies [ENSP] ×19
  ▶ Farm Supplies [FMSP] ×19
  ▶ Electrical Parts [POWR] ×12
  ▶ Metal Parts [MPAR] ×12

**Tropical Paradise**
  ◀ Goods [GOOD]
  ◀ Food [FOOD]
  ◀ Alcohol [BEER]

  ▶ Engineering Supplies [ENSP] ×9
  ▶ Farm Supplies [FMSP] ×9

**Steel City**
  ◀ Food [FOOD]
  ◀ Goods [GOOD]

  ▶ Engineering Supplies [ENSP] ×20
  ▶ Farm Supplies [FMSP] ×20

---

### Wharf (`wharf`)
**Type**: Primary Port (boost with accepted cargo) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Copper [COPR]
  ◀ Explosives [BOOM]
  ◀ Goods [GOOD]
  ◀ Cement [CMNT]

  ▶ Packaging [MNSP] ×19
  ▶ Rare Metals [RAMT] ×16
  ▶ Engineering Supplies [ENSP] ×12
  ▶ Farm Supplies [FMSP] ×12

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
**Type**: Primary (No Supplies) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

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
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Livestock [LVST] ×6 ★required
  ◀ Packaging [MNSP] ×1
  ◀ Salt [SALT] ×1

  ▶ Food [FOOD] ×8
  ▶ Biomass [BIOM] ×2 (scale: medium) ×3 (scale: high)

**Tropical Paradise**
  ◀ Livestock [LVST] ×6 ★required
  ◀ Cleaning Agents [SOAP] ×1
  ◀ Salt [SALT] ×1

  ▶ Meat [MEAT] ×8
  ▶ Biomass [BIOM] ×2 (scale: medium) ×3 (scale: high)

**Steel City**
  ◀ Livestock [LVST] ×6 ★required
  ◀ Cleaning Agents [SOAP] ×1
  ◀ Salt [SALT] ×1

  ▶ Food [FOOD] ×8
---

### Acid Plant (`sulphuric_acid_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Sulphur [SULP] ×8 ★required

  ▶ Acid [ACID] ×8

**Tropical Paradise**
  ◀ Sulphur [SULP] ×8 ★required

  ▶ Sulphuric Acid [SUAC] ×8

**Steel City**
  ◀ Sulphur [SULP] ×6 ★required
  ◀ Oxygen [O2__] ×2

  ▶ Acid [ACID] ×8

---

### Alumina Refinery (`alumina_refinery`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

  ◀ Bauxite [AORE] ×6 ★required
  ◀ Sodium Hydroxide [LYE_] ×2 ★required

  ▶ Alumina [ALO_] ×8

---

### Aluminium Plant (`aluminium_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Bauxite [AORE] ×5 ★required
  ◀ Scrap Metal [SCMT] ×2
  ◀ Coke [COKE] ×2
  ◀ Acid [ACID] ×1

  ▶ Aluminium [ALUM] ×7
  ▶ Slag [SLAG] ×1

**Steel City**
  ◀ Alumina [ALO_] ×4 ★required
  ◀ Scrap Metal [SCMT] ×2
  ◀ Coke [COKE] ×2

  ▶ Aluminium [ALUM] ×7
  ▶ Slag [SLAG] ×1

---

### Ammonia Plant (`ammonia_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Nitrates [NITR] ×4 ★required
  ◀ Refined Oil [RFPR] ×2 ★required
  ◀ Acid [ACID] ×2

  ▶ Fertiliser [FERT] ×5
  ▶ Explosives [BOOM] ×2 (scale: low) ×4 (scale: high)

**Steel City**
  ◀ Nitrogen [N7__] ×2 ★required
  ◀ Hydrogen [H2__] ×4 ★required
  ◀ Refined Oil [RFPR] ×2

  ▶ Ammonia [NH3_] ×8

---

### Appliance Factory (`appliance_factory`)
**Type**: Secondary (🏭 cap 32) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Metal Parts [MPAR] ×4 ★required
  ◀ Electrical Parts [POWR] ×2 ★required
  ◀ Glass [GLAS] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Goods [GOOD] ×8
  ▶ Recyclables [RCYC] ×1–2 (scale: low=1, high=2)

**Tropical Paradise**
  ◀ Metal Parts [MPAR] ×4 ★required
  ◀ Plastics [PLAS] ×2 ★required
  ◀ Glass [GLAS] ×2
  ◀ Rubber Parts [TYRE] ×2

  ▶ Goods [GOOD] ×8
  ▶ Recyclables [RCYC] ×1–2 (scale: low=1, high=2)

**Steel City**
  ◀ Steel Sheet [STSH] ×4 ★required
  ◀ Electrical Parts [POWR] ×2 ★required
  ◀ Glass [GLAS] ×1
  ◀ Plastic Parts [PPAR] ×1
  ◀ Rubber Parts [TYRE] ×1

  ▶ Goods [GOOD] ×8
  ▶ Recyclables [RCYC] ×1–2 (scale: low=1, high=2)

---

### Appliance Factory (`factory_1`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Metal Parts [MPAR] ×4
  ◀ Glass [GLAS] ×2
  ◀ Plastics [PLAS] ×2
  ◀ Rubber Parts [TYRE] ×2

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
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Steel [STEL] ×4 ★required
  ◀ Vehicle Parts [VPTS] ×3 ★required
  ◀ Metal Parts [MPAR] ×2
  ◀ Rubber Parts [TYRE] ×2
  ◀ Glass [GLAS] ×1
  ◀ Paints & Coatings [COAT] ×1

  ▶ Vehicles [VEHI] ×6
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

**Tropical Paradise**
  ◀ Steel [STEL] ×4 ★required
  ◀ Vehicle Parts [VPTS] ×2 ★required
  ◀ Glass [GLAS] ×1
  ◀ Rubber Parts [TYRE] ×1
  ◀ Paints & Coatings [COAT] ×1

  ▶ Vehicles [VEHI] ×6
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

**Steel City**
  ◀ Vehicle Bodies [VBOD] ×3 ★required
  ◀ Vehicle Engines [VENG] ×3 ★required
  ◀ Vehicle Parts [VPTS] ×2 ★required
  ◀ Rubber Parts [TYRE] ×2
  ◀ Glass [GLAS] ×1

  ▶ Vehicles [VEHI] ×8
  ▶ Engineering Supplies [ENSP] ×1 (scale: low) ×2 (scale: high)
  ▶ Farm Supplies [FMSP] ×1 (scale: low) ×2 (scale: high)
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

---

### Bakery (`bakery`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise

  ◀ Flour [BAKE] ×3 ★required
  ◀ Sugar [SUGR] ×2 ★required
  ◀ Food Additives [ENUM] ×1
  ◀ Edible Oil [EOIL] ×1
  ◀ Packaging [MNSP] ×1

  ▶ Food [FOOD] ×8
  ▶ Biomass [BIOM] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

---

### Basic Oxygen Furnace (`basic_oxygen_furnace`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Iron [IRON] ×4 ★required
  ◀ Scrap Metal [SCMT] ×2
  ◀ Quicklime [QLME] ×1
  ◀ Rare Metals [RAMT] ×1

  ▶ Steel [STEL] ×6
  ▶ Slag [SLAG] ×2

**Tropical Paradise**
  ◀ Iron [IRON] ×4 ★required
  ◀ Scrap Metal [SCMT] ×2
  ◀ Quicklime [QLME] ×1
  ◀ Rare Metals [RAMT] ×1

  ▶ Steel [STEL] ×6
  ▶ Slag [SLAG] ×2

**Steel City**
  ◀ Iron [IRON] ×4 ★required
  ◀ Ferroalloy [FECR] ×2
  ◀ Quicklime [QLME] ×1
  ◀ Oxygen [O2__] ×1

  ▶ Carbon Steel [STCB] ×4
  ▶ Alloy Steel [STAL] ×2
  ▶ Slag [SLAG] ×2

---

### Biorefinery (`biorefinery`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Sugar Beet [SGBT] ×6 ★required
  ◀ Biomass [BIOM] ×6 ★required
  ◀ Oil Seeds [OLSD] ×4

  ▶ Refined Oil [RFPR] ×5
  ▶ Petroleum Fuels [PETR] ×5
  ▶ Plastics [PLAS] ×1 (scale: medium+)

**Tropical Paradise**
  ◀ Biomass [BIOM] ×6 ★required
  ◀ Oil Seeds [OLSD] ×4
  ◀ Grain [GRAI] ×4

  ▶ Refined Oil [RFPR] ×4
  ▶ Petroleum Fuels [PETR] ×4

**Steel City**
  ◀ Grain [GRAI] ×4
  ◀ Produce [FRUT] ×4 ★required

  ▶ Refined Oil [RFPR] ×2
  ▶ Petroleum Fuels [PETR] ×3
  ▶ Monomer [C2H4] ×3

---

### Blast Furnace (`blast_furnace`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Iron Ore [IORE] ×4 ★required
  ◀ Coke [COKE] ×3 ★required
  ◀ Limestone [LIME] ×2

  ▶ Iron [IRON] ×6
  ▶ Slag [SLAG] ×2

**Tropical Paradise**
  ◀ Iron Ore [IORE] ×4 ★required
  ◀ Coke [COKE] ×3 ★required
  ◀ Limestone [LIME] ×2

  ▶ Iron [IRON] ×6
  ▶ Slag [SLAG] ×2

**Steel City**
  ◀ Iron Ore [IORE] ×3 ★required
  ◀ Coke [COKE] ×3 ★required
  ◀ Limestone [LIME] ×2

  ▶ Iron [IRON] ×6
  ▶ Slag [SLAG] ×2

---

### Body Plant (`body_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

  ◀ Steel Sheet [STSH] ×5 ★required
  ◀ Paints & Coatings [COAT] ×2 ★required
  ◀ Zinc [ZINC] ×1

  ▶ Vehicle Bodies [VBOD] ×7
  ▶ Scrap Metal [SCMT] ×1

---

### Brewery (`brewery`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

**Extreme Classic**
  ◀ Grain [GRAI] ×4 ★required
  ◀ Produce [FRUT] ×2
  ◀ Packaging [MNSP] ×2

  ▶ Alcohol [BEER] ×6
  ▶ Biomass [BIOM] ×2

**Tropical Paradise**
  ◀ Grain [GRAI] ×4 ★required
  ◀ Sugar [SUGR] ×2
  ◀ Packaging [MNSP] ×1
  ◀ Food Additives [ENUM] ×1

  ▶ Alcohol [BEER] ×6
  ▶ Biomass [BIOM] ×2

---

### Brick Works (`brick_works`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Clay [CLAY] ×4 ★required
  ◀ Coal [COAL] ×2 ★required
  ◀ Sand [SAND] ×1

  ▶ Building Materials [BDMT] ×6
  ▶ Cement [CMNT] ×1 (scale: medium+)

---

### Cannery (`food_processor`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Produce [FRUT] ×4 ★required-any
  ◀ Fish [FISH] ×4 ★required-any
  ◀ Edible Oil [EOIL] ×2
  ◀ Packaging [MNSP] ×2
  ◀ Salt [SALT] ×2

  ▶ Food [FOOD] ×8
  ▶ Biomass [BIOM] ×2 (scale: medium+)

**Tropical Paradise**
  ◀ Produce [FRUT] ×6 ★required-any
  ◀ Meat [MEAT] ×4 ★required-any
  ◀ Sugar [SUGR] ×3
  ◀ Packaging [MNSP] ×2
  ◀ Food Additives [ENUM] ×1
  ◀ Edible Oil [EOIL] ×1

  ▶ Food [FOOD] ×8
  ▶ Biomass [BIOM] ×2 (scale: medium+)

**Steel City**
  ◀ Produce [FRUT] ×4 ★required-any
  ◀ Fish [FISH] ×4 ★required-any
  ◀ Packaging [MNSP] ×2
  ◀ Salt [SALT] ×2

  ▶ Food [FOOD] ×8

---

### Carbon Black Plant (`carbon_black_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

  ◀ Tar [CTAR] ×6 ★required
  ◀ Refined Oil [RFPR] ×2

  ▶ Carbon Black [CBLK] ×4
  ▶ Coke [COKE] ×4
  ▶ Hydrogen [H2__] ×1 (scale: high)

---

### Cement Plant (`cement_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

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

**Steel City**
  ◀ Petroleum Fuels [PETR] ×2
  ◀ Sand [SAND] ×2
  ◀ Limestone [LIME] ×4

  ▶ Quicklime [QLME] ×6
  ▶ Cement [CMNT] ×6

---

### Chemical Plant (`chemical_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise

**Tropical Paradise**
  ◀ Salt [SALT] ×2 ★required
  ◀ Nitrates [NITR] ×2 ★required
  ◀ Refined Oil [RFPR] ×2 ★required
  ◀ Sulphuric Acid [SUAC] ×2

  ▶ Acetic Acid [ACET] ×6
  ▶ Food Additives [ENUM] ×4 (scale: low+)

---

### Chlor-alkali Plant (`chlor_alkali_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Salt [SALT] ×6 ★required
  ◀ Electrical Parts [POWR] ×2

  ▶ Acid [ACID] ×4
  ▶ Chlorine [CHLO] ×4

**Steel City**
  ◀ Salt [SALT] ×6 ★required
  ◀ Electrical Parts [POWR] ×2

  ▶ Acid [ACID] ×2
  ▶ Chlorine [CHLO] ×2
  ▶ Sodium Hydroxide [LYE_] ×2
  ▶ Hydrogen [H2__] ×2

---

### Civil Explosives Facility (`civil_explosives_facility`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Nitrates [NITR] ×2 ★required
  ◀ Sulphuric Acid [SUAC] ×2 ★required
  ◀ Refined Oil [RFPR] ×2

  ▶ Explosives [BOOM] ×6
  ▶ Fertiliser [FERT] ×2 (scale: low) ×3 (scale: medium) ×4 (scale: high)

**Steel City**
  ◀ Ammonia [NH3_] ×4 ★required
  ◀ Acid [ACID] ×2 ★required
  ◀ Plastics [PLAS] ×1
  ◀ Petroleum Fuels [PETR] ×1

  ▶ Ammonium Nitrate [NHNO] ×6
  ▶ Engineering Supplies [ENSP] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

---

### Cleaning Products Factory (`cleaning_products_factory`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Soda Ash [SASH] ×2 ★required
  ◀ Phosphoric Acid [PHAC] ×2 ★required
  ◀ Acetic Acid [ACET] ×2
  ◀ Edible Oil [EOIL] ×2

  ▶ Cleaning Agents [SOAP] ×6
  ▶ Goods [GOOD] ×4

**Steel City**
  ◀ Sodium Hydroxide [LYE_] ×3 ★required
  ◀ Soda Ash [SASH] ×3 ★required
  ◀ Ammonia [NH3_] ×1
  ◀ Packaging [MNSP] ×1

  ▶ Cleaning Agents [SOAP] ×6
  ▶ Goods [GOOD] ×4

---

### Cleaning Products Factory (`factory_2`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

**Steel City**
  ◀ Sodium Hydroxide [LYE_] ×2
  ◀ Soda Ash [SASH] ×2
  ◀ Salt [SALT] ×2
  ◀ Ammonia [NH3_] ×2

  ▶ Cleaning Agents [SOAP] ×8

---

### Coal Liquefaction Plant (`fischer_tropsch_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Coal [COAL] ×8 ★required

  ▶ Refined Oil [RFPR] ×6
  ▶ Tar [CTAR] ×2
  ▶ Petroleum Fuels [PETR] ×1 (scale: high)

**Steel City**
  ◀ Coal [COAL] ×6 ★required
  ◀ Oxygen [O2__] ×2

  ▶ Refined Oil [RFPR] ×6
  ▶ Hydrogen [H2__] ×2
  ▶ Petroleum Fuels [PETR] ×1 (scale: high)

---

### Coke Oven (`coke_oven`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Coal [COAL] ×8 ★required

  ▶ Coke [COKE] ×6
  ▶ Tar [CTAR] ×1 (scale: low+)
  ▶ Sulphur [SULP] ×1 (scale: medium+)

**Tropical Paradise**
  ◀ Coal [COAL] ×8 ★required

  ▶ Coke [COKE] ×6
  ▶ Tar [CTAR] ×1 (scale: low+)
  ▶ Sulphur [SULP] ×1 (scale: medium+)

**Steel City**
  ◀ Coal [COAL] ×8 ★required

  ▶ Coke [COKE] ×5
  ▶ Tar [CTAR] ×1 (scale: low+)
  ▶ Sulphur [SULP] ×1 (scale: medium+)
  ▶ Hydrogen [H2__] ×1 (scale: high)

---

### Component Factory (`component_factory`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Metal Parts [MPAR] ×3 ★required
  ◀ Electrical Parts [POWR] ×2 ★required
  ◀ Plastics [PLAS] ×2
  ◀ Textiles [TEXT] ×1

  ▶ Vehicle Parts [VPTS] ×8
  ▶ Recyclables [RCYC] ×1 (scale: medium+)

**Tropical Paradise**
  ◀ Metal Parts [MPAR] ×3 ★required
  ◀ Plastics [PLAS] ×2 ★required
  ◀ Rubber Parts [TYRE] ×2
  ◀ Textiles [TEXT] ×2
  ◀ Paints & Coatings [COAT] ×1

  ▶ Vehicle Parts [VPTS] ×8
  ▶ Recyclables [RCYC] ×1 (scale: medium+)

**Steel City**
  ◀ Alloy Steel [STAL] ×3 ★required
  ◀ Metal Parts [MPAR] ×2 ★required
  ◀ Plastic Parts [PPAR] ×2
  ◀ Electrical Parts [POWR] ×1

  ▶ Vehicle Parts [VPTS] ×8
  ▶ Recyclables [RCYC] ×1 (scale: medium+)

---

### Construction Plant (`builders_yard`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

  ◀ Cement [CMNT] ×3 ★required
  ◀ Metal Wire [STWR] ×2 ★required
  ◀ Metal Parts [MPAR] ×2
  ◀ Glass [GLAS] ×1

  ▶ Goods [GOOD] ×8
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: high)

---

### Copper Concentrator (`copper_concentrator`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise

  ◀ Copper Ore [CORE] ×4 ★required
  ◀ Sulphuric Acid [SUAC] ×2
  ◀ Quicklime [QLME] ×2

  ▶ Copper Concentrate [COCO] ×7
  ▶ Rare Metals [RAMT] ×2

---

### Copper Smelter (`copper_refinery`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Copper Ore [CORE] ×4 ★required
  ◀ Scrap Metal [SCMT] ×2
  ◀ Acid [ACID] ×2

  ▶ Copper [COPR] ×6
  ▶ Slag [SLAG] ×1
  ▶ Sulphur [SULP] ×1

**Tropical Paradise**
  ◀ Copper Concentrate [COCO] ×4 ★required
  ◀ Scrap Metal [SCMT] ×2
  ◀ Coke [COKE] ×2

  ▶ Copper [COPR] ×5
  ▶ Slag [SLAG] ×1
  ▶ Sulphuric Acid [SUAC] ×2

**Steel City**
  ◀ Copper Concentrate [COCO] ×4 ★required
  ◀ Scrap Metal [SCMT] ×2
  ◀ Acid [ACID] ×2

  ▶ Copper [COPR] ×6
  ▶ Slag [SLAG] ×1
  ▶ Sulphur [SULP] ×1

---

### Dairy (`dairy`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Milk [MILK] ×6 ★required
  ◀ Packaging [MNSP] ×2 ★required
  ◀ Salt [SALT] ×1

  ▶ Food [FOOD] ×8
  ▶ Edible Oil [EOIL] ×2 (scale: low+)
  ▶ Biomass [BIOM] ×1 (scale: high)
---

### Distillery and Winery (`cider_mill`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise

  ◀ Produce [FRUT] ×3 ★required-any
  ◀ Sugar Cane [SGCN] ×3 ★required-any
  ◀ Packaging [MNSP] ×1
  ◀ Food Additives [ENUM] ×1

  ▶ Alcohol [BEER] ×6
  ▶ Acetic Acid [ACET] ×2 (scale: low) ×3 (scale: high)
  ▶ Biomass [BIOM] ×1 (scale: low) ×2 (scale: high)

---

### Edible Oil Refinery (`edible_oil_refinery`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Oil Seeds [OLSD] ×6 ★required
  ◀ Packaging [MNSP] ×2

  ▶ Edible Oil [EOIL] ×4
  ▶ Biomass [BIOM] ×2

---

### Electric Arc Furnace (`electric_arc_furnace`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Scrap Metal [SCMT] ×4 ★required
  ◀ Quicklime [QLME] ×2
  ◀ Coal [COAL] ×2

  ▶ Steel [STEL] ×6
  ▶ Slag [SLAG] ×2

**Steel City**
  ◀ Scrap Metal [SCMT] ×4 ★required
  ◀ Ferroalloy [FECR] ×2
  ◀ Quicklime [QLME] ×1
  ◀ Oxygen [O2__] ×1

  ▶ Carbon Steel [STCB] ×4
  ▶ Alloy Steel [STAL] ×2
  ▶ Slag [SLAG] ×2

---

### Electrical Works (`electrical_works`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Copper [COPR] ×3 ★required
  ◀ Plastics [PLAS] ×2 ★required
  ◀ Rare Metals [RAMT] ×2
  ◀ Rubber Parts [TYRE] ×1

  ▶ Electrical Parts [POWR] ×6

**Tropical Paradise**
  ◀ Copper [COPR] ×3 ★required
  ◀ Plastics [PLAS] ×2 ★required
  ◀ Rare Metals [RAMT] ×1
  ◀ Steel [STEL] ×2

  ▶ Vehicle Parts [VPTS] ×6
  ▶ Goods [GOOD] ×6

**Steel City**
  ◀ Copper [COPR] ×3 ★required
  ◀ Plastic Parts [PPAR] ×2 ★required
  ◀ Rare Metals [RAMT] ×2
  ◀ Steel Sheet [STSH] ×1
  ◀ Refined Oil [RFPR] ×1

  ▶ Electrical Parts [POWR] ×8

---

### Engine Plant (`engine_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

  ◀ Aluminium [ALUM] ×3 ★required
  ◀ Metal Parts [MPAR] ×3 ★required
  ◀ Rubber Parts [TYRE] ×1
  ◀ Refined Oil [RFPR] ×1
  ◀ Alloy Steel [STAL] ×1

  ▶ Vehicle Engines [VENG] ×8
  ▶ Scrap Metal [SCMT] ×1 (scale: medium+)

---

### Engineering Supply Yard (`supply_yard`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Vehicles [VEHI] ×8 ★required
  ◀ Petroleum Fuels [PETR] ×8 ★required
  ◀ Explosives [BOOM] ×8

  ▶ Engineering Supplies [ENSP] ×8
  ▶ Farm Supplies [FMSP] ×2 (scale: low) ×4 (scale: high)

**Tropical Paradise**
  ◀ Vehicles [VEHI] ×8 ★required
  ◀ Petroleum Fuels [PETR] ×8 ★required
  ◀ Explosives [BOOM] ×8

  ▶ Engineering Supplies [ENSP] ×8
  ▶ Farm Supplies [FMSP] ×2 (scale: low) ×4 (scale: high)

**Steel City**
  ◀ Vehicles [VEHI] ×8 ★required
  ◀ Petroleum Fuels [PETR] ×8 ★required
  ◀ Ammonium Nitrate [NHNO] ×8
  ◀ Rubber Parts [TYRE] ×4

  ▶ Engineering Supplies [ENSP] ×8
  ▶ Farm Supplies [FMSP] ×2 (scale: low) ×4 (scale: high)

---

### Farm Supply Yard (`farm_supply_yard`)
**Type**: Secondary (⚡ ANY) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

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
**Type**: Secondary (⚡ ANY) | **UNUSED** -- not enabled in any economy

---

### Fertiliser Plant (`fertiliser_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Phosphoric Acid [PHAC] ×3 ★required
  ◀ Nitrates [NITR] ×3 ★required
  ◀ Biomass [BIOM] ×1
  ◀ Slag [SLAG] ×1

  ▶ Fertiliser [FERT] ×6

**Steel City**
  ◀ Ammonium Nitrate [NHNO] ×6 ★required
  ◀ Slag [SLAG] ×2
  ◀ Acid [ACID] ×2

  ▶ Farm Supplies [FMSP] ×8

---

### Fishing Harbour (`fishing_harbour`)
**Type**: Secondary (🏭 cap 32) | **Economies**: Extreme Classic, Tropical Paradise

**Extreme Classic**
  ◀ Fish [FISH] ×6 ★required
  ◀ Salt [SALT] ×2
  ◀ Packaging [MNSP] ×1

  ▶ Food [FOOD] ×8
  ▶ Edible Oil [EOIL] ×1–2 (scale: low=1, high=2)

**Tropical Paradise**
  ◀ Fish [FISH] ×6 ★required
  ◀ Salt [SALT] ×1

  ▶ Meat [MEAT] ×8

---

### Flour Mill (`flour_mill`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Grain [GRAI] ×6 ★required
  ◀ Packaging [MNSP] ×2

  ▶ Food [FOOD] ×6
  ▶ Edible Oil [EOIL] ×2 (scale: low) ×3 (scale: medium) ×4 (scale: high)

**Tropical Paradise**
  ◀ Grain [GRAI] ×6 ★required
  ◀ Packaging [MNSP] ×2

  ▶ Flour [BAKE] ×6

**Steel City**
  ◀ Grain [GRAI] ×6 ★required
  ◀ Packaging [MNSP] ×2

  ▶ Food [FOOD] ×6

---

### Forge and Foundry (`iron_works`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Iron [IRON] ×4 ★required
  ◀ Aluminium [ALUM] ×3
  ◀ Sand [SAND] ×2
  ◀ Coke [COKE] ×1

  ▶ Metal Parts [MPAR] ×7
  ▶ Slag [SLAG] ×1

**Tropical Paradise**
  ◀ Iron [IRON] ×4 ★required
  ◀ Coal [COAL] ×3
  ◀ Sand [SAND] ×2

  ▶ Metal Parts [MPAR] ×7
  ▶ Slag [SLAG] ×1

**Steel City**
  ◀ Iron [IRON] ×4 ★required
  ◀ Aluminium [ALUM] ×3
  ◀ Sand [SAND] ×2
  ◀ Coke [COKE] ×1

  ▶ Metal Parts [MPAR] ×7
  ▶ Slag [SLAG] ×1

---

### Fruit Packing Plant (`fruit_packing_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Produce [FRUT] ×5 ★required
  ◀ Flour [BAKE] ×3
  ◀ Packaging [MNSP] ×2
  ◀ Acetic Acid [ACET] ×1

  ▶ Food [FOOD] ×8
  ▶ Biomass [BIOM] ×2 (scale: medium+)

**Steel City**
  ◀ Produce [FRUT] ×6 ★required
  ◀ Packaging [MNSP] ×2

  ▶ Food [FOOD] ×8
  ▶ Biomass [BIOM] ×2 (scale: medium+)

---

### Furniture Factory (`furniture_factory`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

**Extreme Classic**
  ◀ Timber [WDPR] ×4 ★required
  ◀ Textiles [TEXT] ×2 ★required
  ◀ Metal Parts [MPAR] ×1
  ◀ Glass [GLAS] ×1
  ◀ Paints & Coatings [COAT] ×1

  ▶ Goods [GOOD] ×6
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: high)

**Tropical Paradise**
  ◀ Timber [WDPR] ×4 ★required
  ◀ Textiles [TEXT] ×2 ★required
  ◀ Metal Parts [MPAR] ×1
  ◀ Glass [GLAS] ×1
  ◀ Paints & Coatings [COAT] ×1

  ▶ Goods [GOOD] ×6
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: high)

---

### Glass Works (`glass_works`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Sand [SAND] ×6 ★required
  ◀ Soda Ash [SASH] ×2 ★required
  ◀ Quicklime [QLME] ×2 ★required

  ▶ Glass [GLAS] ×8
  ▶ Recyclables [RCYC] ×1 (scale: low+)
  ▶ Packaging [MNSP] ×2 (scale: low) ×4 (scale: medium) ×6 (scale: high)

**Tropical Paradise**
  ◀ Sand [SAND] ×4 ★required
  ◀ Soda Ash [SASH] ×2 ★required
  ◀ Quicklime [QLME] ×1 ★required
  ◀ Plastics [PLAS] ×1

  ▶ Glass [GLAS] ×8
  ▶ Recyclables [RCYC] ×1 (scale: low+)
  ▶ Packaging [MNSP] ×2 (scale: low) ×4 (scale: medium) ×6 (scale: high)

**Steel City**
  ◀ Sand [SAND] ×4 ★required
  ◀ Soda Ash [SASH] ×2 ★required
  ◀ Quicklime [QLME] ×1 ★required
  ◀ Plastics [PLAS] ×1

  ▶ Glass [GLAS] ×6
  ▶ Recyclables [RCYC] ×1 (scale: low+)
  ▶ Packaging [MNSP] ×2 (scale: low) ×4 (scale: medium) ×6 (scale: high)

---

### Latex Processor (`latex_processor`)
**Type**: Secondary (🔗 ALL) | **UNUSED** -- not enabled in any economy

---

### Lime Kiln (`lime_kiln`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Limestone [LIME] ×6
  ◀ Petroleum Fuels [PETR] ×2

  ▶ Quicklime [QLME] ×6

**Tropical Paradise**
  ◀ Limestone [LIME] ×6
  ◀ Petroleum Fuels [PETR] ×2

  ▶ Quicklime [QLME] ×6
  ▶ Fertiliser [FERT] ×2

**Steel City**
  ◀ Limestone [LIME] ×6
  ◀ Petroleum Fuels [PETR] ×2

  ▶ Quicklime [QLME] ×8

---

### Machinery Factory (`machine_shop`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Vehicle Parts [VPTS] ×3 ★required
  ◀ Electrical Parts [POWR] ×2 ★required
  ◀ Metal Parts [MPAR] ×2
  ◀ Rubber Parts [TYRE] ×1

  ▶ Goods [GOOD] ×4
  ▶ Engineering Supplies [ENSP] ×2
  ▶ Farm Supplies [FMSP] ×2
  ▶ Scrap Metal [SCMT] ×1 (scale: medium+)

**Tropical Paradise**
  ◀ Steel [STEL] ×4 ★required
  ◀ Vehicle Parts [VPTS] ×2 ★required
  ◀ Rubber Parts [TYRE] ×1

  ▶ Goods [GOOD] ×4
  ▶ Engineering Supplies [ENSP] ×2
  ▶ Farm Supplies [FMSP] ×2
  ▶ Scrap Metal [SCMT] ×1 (scale: medium+)

**Steel City**
  ◀ Vehicle Engines [VENG] ×3 ★required
  ◀ Vehicle Parts [VPTS] ×2 ★required
  ◀ Electrical Parts [POWR] ×2
  ◀ Metal Parts [MPAR] ×1

  ▶ Engineering Supplies [ENSP] ×3
  ▶ Farm Supplies [FMSP] ×3
  ▶ Goods [GOOD] ×2
  ▶ Scrap Metal [SCMT] ×1 (scale: medium+)

---

### Meat Packing Plant (`meat_packing_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise, Steel City

**Tropical Paradise**
  ◀ Meat [MEAT] ×5 ★required
  ◀ Packaging [MNSP] ×2
  ◀ Salt [SALT] ×2
  ◀ Food Additives [ENUM] ×1

  ▶ Food [FOOD] ×7
  ▶ Edible Oil [EOIL] ×2 (scale: low) ×3 (scale: high)
  ▶ Biomass [BIOM] ×2 (scale: medium+)

**Steel City**
  ◀ Fish [FISH] ×6 ★required
  ◀ Packaging [MNSP] ×2
  ◀ Salt [SALT] ×2

  ▶ Food [FOOD] ×8

---

### Metal Workshop (`metal_workshop`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Steel [STEL] ×6 ★required
  ◀ Aluminium [ALUM] ×4
  ◀ Paints & Coatings [COAT] ×2

  ▶ Metal Parts [MPAR] ×8
  ▶ Packaging [MNSP] ×6
  ▶ Recyclables [RCYC] ×1 (scale: medium+)

**Tropical Paradise**
  ◀ Steel [STEL] ×4 ★required
  ◀ Copper [COPR] ×2
  ◀ Rare Metals [RAMT] ×1
  ◀ Cleaning Agents [SOAP] ×1

  ▶ Metal Parts [MPAR] ×6
  ▶ Goods [GOOD] ×4
  ▶ Recyclables [RCYC] ×1 (scale: medium+)

**Steel City**
  ◀ Steel Sheet [STSH] ×3 ★required
  ◀ Paints & Coatings [COAT] ×2
  ◀ Zinc [ZINC] ×1
  ◀ Metal Wire [STWR] ×2

  ▶ Packaging [MNSP] ×3
  ▶ Metal Parts [MPAR] ×4
  ▶ Scrap Metal [SCMT] ×1 (scale: low) ×2 (scale: medium)

---

### Moulding Plant (`plastics_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Plastics [PLAS] ×5 ★required
  ◀ Metal Parts [MPAR] ×3 ★required

  ▶ Packaging [MNSP] ×6
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

**Tropical Paradise**
  ◀ Plastics [PLAS] ×2 ★required
  ◀ Steel [STEL] ×2 ★required
  ◀ Glass [GLAS] ×2

  ▶ Packaging [MNSP] ×6
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

**Steel City**
  ◀ Plastics [PLAS] ×5 ★required
  ◀ Metal Parts [MPAR] ×3 ★required

  ▶ Plastic Parts [PPAR] ×6
  ▶ Packaging [MNSP] ×5

---

### Naphtha Cracker (`ethylene_cracker`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Refined Oil [RFPR] ×4 ★required
  ◀ Tar [CTAR] ×4 ★required

  ▶ Petroleum Fuels [PETR] ×5
  ▶ Coke [COKE] ×3
  ▶ Sulphur [SULP] ×2

**Steel City**
  ◀ Refined Oil [RFPR] ×5 ★required
  ◀ Tar [CTAR] ×3 ★required

  ▶ Monomer [C2H4] ×5
  ▶ Petroleum Fuels [PETR] ×3
  ▶ Hydrogen [H2__] ×1 (scale: medium+)

---

### Oil Refinery (`oil_refinery`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

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

**Steel City**
  ◀ Oil [OIL_] ×7
  ◀ Hydrogen [H2__] ×1

  ▶ Refined Oil [RFPR] ×4
  ▶ Petroleum Fuels [PETR] ×2
  ▶ Tar [CTAR] ×1
  ▶ Sulphur [SULP] ×1

---

### Paint Factory (`factory_3`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

**Steel City**
  ◀ Refined Oil [RFPR] ×2
  ◀ Quicklime [QLME] ×2
  ◀ Carbon Black [CBLK] ×2
  ◀ Plastics [PLAS] ×2

  ▶ Paints & Coatings [COAT] ×8

---

### Paint Factory (`paint_factory`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Refined Oil [RFPR] ×2 ★required
  ◀ Quicklime [QLME] ×2 ★required
  ◀ Plastics [PLAS] ×2 ★required
  ◀ Packaging [MNSP] ×2

  ▶ Paints & Coatings [COAT] ×6
  ▶ Goods [GOOD] ×4

**Tropical Paradise**
  ◀ Refined Oil [RFPR] ×2 ★required
  ◀ Quicklime [QLME] ×2 ★required
  ◀ Acetic Acid [ACET] ×2 ★required
  ◀ Plastics [PLAS] ×2 ★required

  ▶ Paints & Coatings [COAT] ×6
  ▶ Goods [GOOD] ×4

**Steel City**
  ◀ Refined Oil [RFPR] ×2 ★required
  ◀ Quicklime [QLME] ×2 ★required
  ◀ Plastics [PLAS] ×2 ★required
  ◀ Carbon Black [CBLK] ×2
  ◀ Packaging [MNSP] ×2

  ▶ Paints & Coatings [COAT] ×6
  ▶ Goods [GOOD] ×4

---

### Paper Mill (`paper_mill`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

**Extreme Classic**
  ◀ Clay [CLAY] ×2
  ◀ Logs [WOOD] ×4
  ◀ Sulphur [SULP] ×2

  ▶ Paper [PAPR] ×6
  ▶ Packaging [MNSP] ×8

**Tropical Paradise**
  ◀ Logs [WOOD] ×4
  ◀ Clay [CLAY] ×2
  ◀ Sulphuric Acid [SUAC] ×2

  ▶ Goods [GOOD] ×4
  ▶ Packaging [MNSP] ×7

---

### Phosphoric Acid Plant (`phosphoric_acid_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Tropical Paradise

**Tropical Paradise**
  ◀ Phosphate [PHOS] ×3 ★required
  ◀ Sulphuric Acid [SUAC] ×5 ★required

  ▶ Phosphoric Acid [PHAC] ×6
  ▶ Food Additives [ENUM] ×2 (scale: low+)

---

### Polymerisation Plant (`polyethylene_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Refined Oil [RFPR] ×6 ★required
  ◀ Chlorine [CHLO] ×2
  ◀ Acid [ACID] ×2

  ▶ Plastics [PLAS] ×5
  ▶ Rubber [RUBR] ×3
  ▶ Fibres [FICR] ×1 (scale: low) ×2 (scale: medium)

**Tropical Paradise**
  ◀ Refined Oil [RFPR] ×6 ★required
  ◀ Acetic Acid [ACET] ×2

  ▶ Plastics [PLAS] ×5
  ▶ Rubber [RUBR] ×3
  ▶ Fibres [FICR] ×1 (scale: low) ×2 (scale: medium)

**Steel City**
  ◀ Monomer [C2H4] ×5 ★required
  ◀ Chlorine [CHLO] ×3

  ▶ Plastics [PLAS] ×8
  ▶ Rubber [RUBR] ×2

---

### Printing Plant (`printing_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic

  ◀ Paper [PAPR] ×6 ★required
  ◀ Paints & Coatings [COAT] ×2

  ▶ Goods [GOOD] ×5
  ▶ Mail [MAIL] ×5
  ▶ Recyclables [RCYC] ×1 (scale: low) ×2 (scale: high)

---

### Pyrite Smelter (`pyrite_smelter`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Pyrite Ore [PORE] ×6 ★required
  ◀ Coke [COKE] ×2
  ◀ Acid [ACID] ×2

  ▶ Zinc [ZINC] ×4
  ▶ Rare Metals [RAMT] ×2
  ▶ Slag [SLAG] ×1 (scale: low) ×2 (scale: high)
  ▶ Sulphur [SULP] ×1 (scale: medium) ×2 (scale: high)

**Steel City**
  ◀ Pyrite Ore [PORE] ×6 ★required
  ◀ Coke [COKE] ×1
  ◀ Cleaning Agents [SOAP] ×1

  ▶ Zinc [ZINC] ×2
  ▶ Copper Concentrate [COCO] ×3
  ▶ Iron Ore [IORE] ×2
  ▶ Slag [SLAG] ×1 (scale: low) ×2 (scale: high)
  ▶ Sulphur [SULP] ×1 (scale: medium) ×2 (scale: high)

---

### Recycling Plant (`recycling_plant`)
**Type**: Secondary (⚡ ANY) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Recyclables [RCYC] ×6

  ▶ Plastics [PLAS] ×3

---

### Sawmill (`sawmill`)
**Type**: Secondary (⚡ ANY) | **Economies**: Extreme Classic, Tropical Paradise

  ◀ Logs [WOOD] ×6

  ▶ Timber [WDPR] ×8

---

### Scrap Yard (`junk_yard`)
**Type**: Secondary (⚡ ANY) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

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
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Steel [STEL] ×4 ★required
  ◀ Zinc [ZINC] ×2
  ◀ Acid [ACID] ×2

  ▶ Metal Parts [MPAR] ×6
  ▶ Building Materials [BDMT] ×4
  ▶ Scrap Metal [SCMT] ×1 (scale: medium+)

**Steel City**
  ◀ Carbon Steel [STCB] ×4 ★required
  ◀ Zinc [ZINC] ×2
  ◀ Acid [ACID] ×2

  ▶ Steel Sheet [STSH] ×8
  ▶ Scrap Metal [SCMT] ×1 (scale: medium+)

---

### Slag Grinding Plant (`slag_grinding_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Slag [SLAG] ×6 ★required
  ◀ Quicklime [QLME] ×2
  ◀ Coke [COKE] ×2

  ▶ Cement [CMNT] ×6
  ▶ Fertiliser [FERT] ×3

**Steel City**
  ◀ Slag [SLAG] ×6 ★required
  ◀ Quicklime [QLME] ×2
  ◀ Coke [COKE] ×1

  ▶ Cement [CMNT] ×6

---

### Smithy Forge (`smithy_forge`)
**Type**: Secondary (⚡ ANY) | **UNUSED** -- not enabled in any economy

---

### Solvay Plant (`solvay_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Salt [SALT] ×4 ★required
  ◀ Limestone [LIME] ×2 ★required
  ◀ Refined Oil [RFPR] ×2 ★required

  ▶ Soda Ash [SASH] ×8

**Tropical Paradise**
  ◀ Salt [SALT] ×4 ★required
  ◀ Limestone [LIME] ×2 ★required
  ◀ Refined Oil [RFPR] ×2 ★required

  ▶ Soda Ash [SASH] ×8

**Steel City**
  ◀ Salt [SALT] ×4 ★required
  ◀ Limestone [LIME] ×2 ★required
  ◀ Ammonia [NH3_] ×2 ★required

  ▶ Soda Ash [SASH] ×8

---

### Steel Mill (`integrated_steel_mill`)
**Type**: Secondary (🔗 ALL) | **UNUSED** -- not enabled in any economy

---

### Sugar Refinery (`sugar_refinery`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

**Extreme Classic**
  ◀ Sugar Beet [SGBT] ×6 ★required
  ◀ Packaging [MNSP] ×2
  ◀ Limestone [LIME] ×1

  ▶ Food [FOOD] ×6
  ▶ Biomass [BIOM] ×2 (scale: low+)

**Tropical Paradise**
  ◀ Sugar Cane [SGCN] ×6 ★required
  ◀ Phosphate [PHOS] ×1
  ◀ Food Additives [ENUM] ×1

  ▶ Sugar [SUGR] ×6
  ▶ Biomass [BIOM] ×2 (scale: low+)

---

### Synthetic Rubber Plant (`polypropylene_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

**Steel City**
  ◀ Monomer [C2H4] ×5 ★required
  ◀ Acid [ACID] ×3

  ▶ Rubber [RUBR] ×8

---

### Textile Mill (`textile_mill`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

**Extreme Classic**
  ◀ Fibres [FICR] ×5 ★required
  ◀ Paints & Coatings [COAT] ×1
  ◀ Plastics [PLAS] ×1

  ▶ Textiles [TEXT] ×7
  ▶ Goods [GOOD] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

**Tropical Paradise**
  ◀ Fibres [FICR] ×5 ★required
  ◀ Plastics [PLAS] ×2
  ◀ Acetic Acid [ACET] ×1

  ▶ Textiles [TEXT] ×7
  ▶ Goods [GOOD] ×1 (scale: low) ×2 (scale: medium) ×3 (scale: high)

---

### Timber Yard (`lumber_yard`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise

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

---

### Tyre and Rubber Plant (`tyre_plant`)
**Type**: Secondary (🔗 ALL) | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Rubber [RUBR] ×4 ★required
  ◀ Sulphur [SULP] ×2
  ◀ Metal Parts [MPAR] ×1

  ▶ Rubber Parts [TYRE] ×8
  ▶ Recyclables [RCYC] ×1 (scale: low)
  ▶ Goods [GOOD] ×1 (scale: medium)
  ▶ Plastics [PLAS] ×2 (scale: high)

**Tropical Paradise**
  ◀ Rubber [RUBR] ×4 ★required
  ◀ Sulphur [SULP] ×2
  ◀ Metal Parts [MPAR] ×1

  ▶ Rubber Parts [TYRE] ×8
  ▶ Recyclables [RCYC] ×1 (scale: low)
  ▶ Goods [GOOD] ×1 (scale: medium)
  ▶ Plastics [PLAS] ×2 (scale: high)

**Steel City**
  ◀ Rubber [RUBR] ×4 ★required
  ◀ Carbon Black [CBLK] ×2 ★required
  ◀ Sulphur [SULP] ×1
  ◀ Metal Wire [STWR] ×1

  ▶ Rubber Parts [TYRE] ×8
  ▶ Recyclables [RCYC] ×1 (scale: low)
  ▶ Goods [GOOD] ×1 (scale: medium)
  ▶ Plastics [PLAS] ×2 (scale: high)

---

### Wire and Section Mill (`wire_and_section_mill`)
**Type**: Secondary (🔗 ALL) | **Economies**: Steel City

  ◀ Carbon Steel [STCB] ×3 ★required
  ◀ Aluminium [ALUM] ×2
  ◀ Copper [COPR] ×2
  ◀ Cleaning Agents [SOAP] ×1

  ▶ Metal Parts [MPAR] ×4
  ▶ Metal Wire [STWR] ×3
  ▶ Scrap Metal [SCMT] ×1 (scale: low+)

---

## Tertiary Industries

---

### General Store (`general_store`)
**Type**: Tertiary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Food [FOOD]
  ◀ Goods [GOOD]
  ◀ Alcohol [BEER]

**Tropical Paradise**
  ◀ Food [FOOD]
  ◀ Goods [GOOD]
  ◀ Alcohol [BEER]

**Steel City**
  ◀ Food [FOOD]

---

### Grocer's Shop (`food_market`)
**Type**: Tertiary | **Economies**: Extreme Classic, Steel City

**Extreme Classic**
  ◀ Food [FOOD]
  ◀ Produce [FRUT]
  ◀ Alcohol [BEER]

**Steel City**
  ◀ Food [FOOD]

---

### Hardware Store (`hardware_store`)
**Type**: Tertiary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Goods [GOOD]
  ◀ Building Materials [BDMT]

**Tropical Paradise**
  ◀ Goods [GOOD]
  ◀ Building Materials [BDMT]

**Steel City**
  ◀ Goods [GOOD]

---

### Hotel (`hotel`)
**Type**: Tertiary | **UNUSED** -- not enabled in any economy

---

### Petrol Station (`petrol_pump`)
**Type**: Tertiary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

  ◀ Food [FOOD]
  ◀ Goods [GOOD]
  ◀ Petroleum Fuels [PETR]

---

### Power Plant (`power_plant`)
**Type**: Tertiary | **Economies**: Extreme Classic, Tropical Paradise, Steel City

**Extreme Classic**
  ◀ Coal [COAL]
  ◀ Petroleum Fuels [PETR]
  ◀ Biomass [BIOM]

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
**Type**: Informative | **Economies**: Extreme Classic, Tropical Paradise, Steel City

