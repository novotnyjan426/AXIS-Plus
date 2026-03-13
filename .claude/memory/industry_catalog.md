---
name: Industry Catalog
description: Complete list of all ~126 industries with type, produces, accepts, boost mechanism, economies — exact cargo codes from source
type: reference
---

## Industry Types — How They Work

| Type | Count | Self-produces? | Boostable? | Boost cargo | Needs input? |
|------|-------|---------------|------------|-------------|-------------|
| Primary Extractive | 23 | Yes | Yes | ENSP | No |
| Primary Organic | 14 | Yes | Yes | FMSP | No |
| Primary Port | 4 | Yes | Yes | Any accepted cargo | No |
| Primary No-Supplies | 2 | Yes | No | — | No |
| Town Producer | 1 | Yes (pop-dependent) | No | — | No |
| Secondary | 74 | No | No | — | Yes |
| Tertiary / Consumer | 7 | No | No | — | Yes (consumes) |
| Informative | 1 | No | No | — | No |

### Exceptions & Gotchas

**Unused industries** (no economy enabled): chromite_mine, potash_mine, ferrochrome_smelter, integrated_steel_mill, latex_processor, smithy_forge (expiry 1948), hotel

**Primary Extractive that override ENSP away (NOT boostable despite class)**:
- salt_evaporator — `accept_cargo_types=[]`
- trading_post — `accept_cargo_types=[]`

**Primary Organic that override FMSP away (NOT boostable despite class)**:
- fish_farm — `accept_cargo_types=[]`
- seaweed_farm — `accept_cargo_types=[]`

**Primary Port with no accepts in some economies** (self-producing only in those):
- bulk_terminal — no accepts in BETTER_LIVING_THROUGH_CHEMISTRY
- liquids_terminal — no accepts in BETTER_LIVING_THROUGH_CHEMISTRY

---

## PRIMARY EXTRACTIVE (auto-accepts ENSP for boost)

### bauxite_mine
- **Produces**: AORE(20)
- **Economies**: STEELTOWN, BASIC_TEMPERATE

### chromite_mine
- **Produces**: CHRO(20)
- **Economies**: NONE ENABLED

### clay_pit
- **Produces**: KAOL(16)
- **Economy overrides**:
  - BASIC_TEMPERATE: produces CLAY(16)
  - BASIC_TROPIC: produces CLAY(16)

### coal_mine
- **Produces**: COAL(20)
- **Economies**: BASIC_TROPIC, STEELTOWN, BASIC_TEMPERATE

### copper_mine
- **Produces**: CORE(20)
- **Economies**: IN_A_HOT_COUNTRY, BASIC_TROPIC, BASIC_TEMPERATE

### diamond_mine
- **Produces**: DIAM(12)
- **Economies**: IN_A_HOT_COUNTRY

### dredging_site
- **Produces**: SAND(17), CLAY(13)
- **Economy overrides**:
  - BASIC_TEMPERATE: SAND(17)
  - BETTER_LIVING_THROUGH_CHEMISTRY: SAND(17)
  - STEELTOWN: SAND(17)
  - BASIC_TROPIC: SAND(17), CLAY(16)

### iron_ore_mine
- **Produces**: IORE(20)
- **Economies**: BASIC_TEMPERATE, STEELTOWN, BASIC_TROPIC

### limestone_mine
- **Produces**: LIME(20)
- **Economies**: STEELTOWN, BASIC_TROPIC, BASIC_TEMPERATE

### manganese_mine
- **Produces**: MNO2(20)
- **Economies**: IN_A_HOT_COUNTRY

### nitrate_mine
- **Produces**: FMSP(12), NITR(17)
- **Economy overrides**:
  - BASIC_TROPIC: NITR(18)
  - BASIC_TEMPERATE: NITR(18)

### oil_rig
- **Produces**: OIL_(29), PASS(4)
- **Economies**: IN_A_HOT_COUNTRY, STEELTOWN, BASIC_TROPIC, BASIC_TEMPERATE

### oil_wells
- **Produces**: OIL_(28)
- **Economies**: BASIC_TROPIC, IN_A_HOT_COUNTRY, STEELTOWN, BASIC_TEMPERATE

### peatlands
- **Produces**: PEAT(14)
- **Economy overrides**:
  - BASIC_ARCTIC: PEAT(14)
  - BASIC_TEMPERATE: BIOM(18)

### phosphate_mine
- **Produces**: PHOS(16)
- **Economy overrides**:
  - IN_A_HOT_COUNTRY: PHOS(16), CLAY(10)
  - BASIC_ARCTIC: PHOS(16)
  - BASIC_TROPIC: PHOS(16)

### potash_mine
- **Produces**: POTA(20)
- **Economies**: NONE ENABLED

### pyrite_mine
- **Produces**: PORE(20)
- **Economies**: BASIC_ARCTIC, STEELTOWN, BASIC_TEMPERATE

### quarry
- **Produces**: SAND(14), LIME(14)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: SAND(14), LIME(14)
  - IN_A_HOT_COUNTRY: SAND(14), GRVL(14)
  - BASIC_TROPIC: SAND(14), LIME(14)
  - BASIC_TEMPERATE: default

### salt_evaporator
- **Produces**: SALT(15)
- **Note**: accept_cargo_types=[] (overrides auto ENSP — NOT boostable)
- **Economies**: BASIC_ARCTIC, BETTER_LIVING_THROUGH_CHEMISTRY, STEELTOWN, BASIC_TROPIC, BASIC_TEMPERATE

### salt_mine
- **Produces**: SALT(22), ENUM(4)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: SALT(20)
  - BASIC_TROPIC: SALT(20)

### soda_ash_mine
- **Produces**: SASH(16), SALT(18)
- **Economies**: STEELTOWN, BASIC_TEMPERATE

### tar_sands_mine
- **Produces**: SAND(14), CTAR(14)
- **Economies**: BETTER_LIVING_THROUGH_CHEMISTRY, STEELTOWN, BASIC_TEMPERATE

### trading_post
- **Produces**: SCMT(12)
- **Note**: accept_cargo_types=[] (overrides auto ENSP — NOT boostable)
- **Economies**: BASIC_TROPIC, STEELTOWN, BASIC_TEMPERATE

---

## PRIMARY ORGANIC (auto-accepts FMSP for boost)

### arable_farm
- **Produces**: GRAI(14), BEAN(14)
- **Economy overrides**:
  - BASIC_TROPIC: GRAI(14), SGCN(24)
  - STEELTOWN: GRAI(28)
  - BASIC_TEMPERATE: GRAI(14), SGBT(24)

### coffee_estate
- **Produces**: JAVA(11), FRUT(8)
- **Economy overrides**:
  - IN_A_HOT_COUNTRY: default
  - BASIC_TROPIC: ENUM(13)

### dairy_farm
- **Produces**: LVST(12), MILK(14)
- **Economies**: BASIC_TEMPERATE, BETTER_LIVING_THROUGH_CHEMISTRY, BASIC_TROPIC

### farm
- **Produces**: GRAI(14), LVST(13)
- **Economy overrides**:
  - IN_A_HOT_COUNTRY: MAIZ(14), LVST(13)
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: default
  - BASIC_TROPIC: GRAI(20), LVST(12)

### fish_farm
- **Produces**: FISH(8)
- **Note**: accept_cargo_types=[] (overrides auto FMSP — NOT boostable)
- **Economies**: BASIC_ARCTIC, BASIC_TROPIC, BETTER_LIVING_THROUGH_CHEMISTRY, STEELTOWN, BASIC_TEMPERATE

### forest
- **Produces**: WOOD(19)
- **Economy overrides**:
  - BASIC_ARCTIC: WOOD(24)
  - IN_A_HOT_COUNTRY: default
  - BASIC_TROPIC: default
  - BASIC_TEMPERATE: default

### fruit_plantation
- **Produces**: FRUT(14), NUTS(13)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - IN_A_HOT_COUNTRY: default
  - STEELTOWN: FRUT(16)
  - BASIC_TROPIC: FRUT(16), OLSD(13)
  - BASIC_TEMPERATE: FRUT(16), OLSD(13)

### herding_coop
- **Produces**: FOOD(7)
- **Economies**: BASIC_ARCTIC

### orchard_piggery
- **Produces**: FRUT(9), LVST(8)
- **Economies**: BASIC_TEMPERATE, STEELTOWN

### ranch
- **Produces**: LVST(14), WOOL(13)
- **Economy overrides**:
  - BASIC_TROPIC: FICR(18), OLSD(14)
  - BASIC_TEMPERATE: FICR(18), OLSD(14)

### rubber_plantation
- **Produces**: RUBR(16)
- **Economies**: IN_A_HOT_COUNTRY, BASIC_TROPIC, BASIC_TEMPERATE

### seaweed_farm
- **Produces**: BIOM(8), ENUM(6)
- **Note**: accept_cargo_types=[] (overrides auto FMSP — NOT boostable)
- **Economy overrides**:
  - BASIC_TROPIC: default
  - STEELTOWN: FRUT(16)
  - BASIC_TEMPERATE: BIOM(18)

### sheep_farm
- **Produces**: LVST(12), WOOL(14)
- **Economy overrides**:
  - BASIC_TROPIC: LVST(13), FICR(16)
  - BASIC_TEMPERATE: LVST(13), FICR(16)

### vineyard
- **Produces**: FRUT(14)
- **Economies**: BASIC_TROPIC, BASIC_TEMPERATE

---

## PRIMARY PORT (boost from any accepted cargo delivery)

### bulk_terminal
- **Default**: produces [], accepts []
- **Economy overrides**:
  - IN_A_HOT_COUNTRY: accepts MNO2/PHOS/BDMT, produces RFPR(12)/FMSP(12)
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts [], produces OIL_(20)/POTA(12)/PHOS(12)/MEOH(12)
  - STEELTOWN: accepts FOOD/CMNT/STSH/VEHI, produces IORE(19)/ALO_(19)/FECR(16)/COAL(16)
  - BASIC_TROPIC: accepts BDMT/FERT/BOOM/VEHI, produces ACET(19)/COAL(19)/RAMT(16)/LIME(16)
  - BASIC_TEMPERATE: accepts ZINC/FERT/VEHI/STEL, produces IORE(19)/COAL(19)/AORE(16)/CORE(16)

### liquids_terminal
- **Default**: produces [], accepts []
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts [], produces OIL_(20)
  - IN_A_HOT_COUNTRY: accepts EOIL/OIL_, produces RFPR(11)/PETR(7)
  - STEELTOWN: accepts PETR/NH3_/CHLO/COAT, produces OIL_(20)/RUBR(20)/ACID(20)/RFPR(20)
  - BASIC_TROPIC: accepts PHAC/SOAP/RUBR/EOIL, produces OIL_(20)/SUAC(20)/PETR(20)/RFPR(20)
  - BASIC_TEMPERATE: accepts CHLO/RUBR/EOIL/PETR, produces OIL_(20)/ACID(20)/RFPR(18)/COAT(18)

### port
- **Default**: produces [], accepts []
- **Economy overrides**:
  - BASIC_TEMPERATE: accepts BDMT/FOOD/BEER/PAPR, produces ENSP(19)/FMSP(19)/POWR(12)/MPAR(12)
  - BASIC_ARCTIC: accepts PAPR/ZINC/FERT, produces KAOL(16)/NH3_(17)/ENSP(9)/FMSP(9)
  - BASIC_TROPIC: accepts GOOD/FOOD/BEER, produces ENSP(9)/FMSP(9)
  - IN_A_HOT_COUNTRY: accepts COPR/FRUT/WDPR, produces GOOD(14)/ENSP(17)
  - STEELTOWN: accepts FOOD/GOOD, produces ENSP(20)/FMSP(20)

### wharf
- **Default**: produces [], accepts []
- **Economy overrides**:
  - BASIC_ARCTIC: accepts BOOM/PEAT/WDPR, produces POTA(19)/ENSP(9)/FMSP(9)
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts POWR/RUBR/BOOM, produces COPR(10)/VEHI(14)/ALUM(12)/WDPR(14)/STEL(14)
  - STEELTOWN: accepts CMNT/GOOD/SOAP/POWR, produces ENSP(12)/SCMT(16)/COCO(14)/PLAS(10)
  - BASIC_TEMPERATE: accepts COPR/BOOM/GOOD/CMNT, produces MNSP(19)/RAMT(16)/ENSP(12)/FMSP(12)

---

## PRIMARY NO SUPPLIES (self-producing, NOT boostable)

### cryo_plant
- **Produces**: O2__(25), N7__(25)
- **Accepts**: [] (explicit)
- **Economies**: STEELTOWN

### fishing_grounds
- **Produces**: FISH(8)
- **Accepts**: [] (explicit)
- **Economies**: BASIC_TEMPERATE, BASIC_TROPIC, BASIC_ARCTIC, BETTER_LIVING_THROUGH_CHEMISTRY, STEELTOWN

---

## TOWN PRODUCER (population-dependent)

### recycling_depot
- **Produces**: RCYC(16)
- **Economies**: STEELTOWN, BASIC_TROPIC, BASIC_TEMPERATE

---

## SECONDARY (requires input to produce)

### alumina_refinery
- **Accepts**: AORE(6)/LYE_(2) → **Produces**: ALO_(8)
- **Economies**: STEELTOWN

### aluminium_plant
- **Accepts**: ALO_(8) → **Produces**: ALUM(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts ALO_(4)/SCMT(2)/COKE(2), produces ALUM(7)/SLAG(1)
  - BASIC_TEMPERATE: accepts AORE(4)/SCMT(4)/COKE(2)/ACID(2), produces ALUM(7)/SLAG(1)

### ammonia_plant
- **Accepts**: NAPH(8) → **Produces**: NH3_(3)/UREA(2)/NHNO(3)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts RFPR(2)/N7__(4)/H2__(2), produces NH3_(8)
  - BASIC_TEMPERATE: accepts RFPR(2)/NITR(4)/BIOM(2)/ACID(2), produces FERT(5)/BOOM(3)

### appliance_factory
- **Accepts**: GLAS(2)/STEL(2)/PLAS(2) → **Produces**: GOOD(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts STAL(2)/STSH(2)/GLAS(1)/PPAR(1)/POWR(1)/TYRE(1)
  - BASIC_TROPIC: accepts MPAR(4)/GLAS(2)/PLAS(2)/TYRE(2)
  - BASIC_TEMPERATE: accepts MPAR(4)/POWR(4)/GLAS(2)/PLAS(2)

### assembly_plant
- **Accepts**: VPTS(2)/VBOD(2)/VENG(2)/TYRE(4) → **Produces**: VEHI(6)/ENSP(1)/FMSP(1)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TROPIC: accepts STEL(2)/GLAS(2)/VPTS(2)/TYRE(1)/COAT(1), produces VEHI(6)
  - BASIC_TEMPERATE: accepts STEL(3)/GLAS(2)/VPTS(2)/MPAR(2)/TYRE(2)/COAT(2), produces VEHI(6)

### bakery
- **Accepts**: BAKE(3)/SUGR(2)/ENUM(1)/EOIL(1)/MNSP(1) → **Produces**: FOOD(8)
- **Economies**: BASIC_TROPIC

### basic_oxygen_furnace
- **Accepts**: IRON(4)/FECR(2)/QLME(1)/O2__(1) → **Produces**: STCB(3)/STAL(3)/SLAG(2)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TROPIC: accepts IRON(3)/SCMT(3)/QLME(1)/RAMT(1), produces STEL(6)/SLAG(2)
  - BASIC_TEMPERATE: accepts IRON(4)/QLME(2)/RAMT(2), produces STEL(6)/SLAG(2)

### biorefinery
- **Accepts**: GRAI(6)/SGBT(6) → **Produces**: RFPR(4)/PETR(4)
- **Economy overrides**:
  - STEELTOWN: accepts GRAI(4)/FRUT(4), produces RFPR(2)/PETR(3)/C2H4(3)
  - BASIC_TROPIC: accepts BIOM(6)/OLSD(6)/GRAI(6)
  - BASIC_TEMPERATE: accepts SGBT(6)/BIOM(6)/OLSD(6), produces RFPR(5)/PETR(4)/PLAS(3)

### blast_furnace
- **Accepts**: IORE(3)/COAL(2)/SCMT(3) → **Produces**: STEL(8)
- **Economy overrides**:
  - STEELTOWN: accepts IORE(3)/COKE(3)/LIME(2), produces IRON(6)/SLAG(2)
  - BASIC_TROPIC: accepts IORE(4)/COKE(3)/LIME(2), produces IRON(6)/SLAG(2)
  - BASIC_TEMPERATE: accepts IORE(4)/COKE(3)/LIME(2), produces IRON(6)/SLAG(2)

### body_plant
- **Accepts**: STSH(4)/COAT(2)/GLAS(2) → **Produces**: VBOD(7)/SCMT(1)
- **Economies**: STEELTOWN

### brewery
- **Accepts**: FRUT(6) → **Produces**: BEER(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts GRAI(4)/MNSP(4)
  - IN_A_HOT_COUNTRY: accepts FRUT(4)/MAIZ(4)
  - BASIC_TROPIC: accepts GRAI(4)/SUGR(2)/MNSP(1)/ENUM(1), produces BEER(6)/BIOM(2)
  - BASIC_TEMPERATE: accepts GRAI(4)/FRUT(3)/MNSP(2), produces BEER(6)/BIOM(2)

### brick_works
- **Accepts**: COAL(2)/SAND(2)/CLAY(4) → **Produces**: BDMT(8)
- **Economy overrides**:
  - BASIC_TROPIC: accepts CLAY(4)/SAND(3)/COAL(2), produces BDMT(6)
  - BASIC_TEMPERATE: accepts CLAY(4)/SAND(3)/COAL(2), produces BDMT(6)

### builders_yard
- **Accepts**: CMNT(2)/MPAR(2)/STWR(2)/GLAS(2) → **Produces**: GOOD(8)
- **Economies**: BETTER_LIVING_THROUGH_CHEMISTRY, STEELTOWN, IN_A_HOT_COUNTRY

### carbon_black_plant
- **Accepts**: CTAR(8) → **Produces**: CBLK(4)/COKE(4)
- **Economies**: STEELTOWN

### cement_plant
- **Accepts**: COAL(2)/CLAY(2)/LIME(4) → **Produces**: CMNT(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts PETR(2)/SAND(2)/LIME(4), produces QLME(6)/CMNT(6)
  - IN_A_HOT_COUNTRY: accepts PETR(2)/CLAY(2)/GRVL(4), produces BDMT(8)
  - BASIC_TROPIC: accepts COKE(2)/SAND(2)/LIME(2)/SLAG(2), produces BDMT(6)/QLME(2)
  - BASIC_TEMPERATE: accepts CMNT(2)/COKE(2)/SAND(2)/LIME(2), produces BDMT(6)/QLME(2)

### chemical_plant
- **Accepts**: OIL_(4)/NITR(4) → **Produces**: RFPR(8)
- **Economy overrides**:
  - BASIC_TROPIC: accepts SALT(2)/NITR(2)/RFPR(2), produces ACET(6)/ENUM(4)
  - BASIC_ARCTIC: accepts SULP(2)/PHOS(2)/NH3_(2)/POTA(2), produces FERT(4)/BOOM(4)
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts SASH(1)/LYE_(2)/NH3_(2)/CHLO(2)/PHAC(1), produces SOAP(4)/ENUM(4)

### chlor_alkali_plant
- **Accepts**: SALT(8) → **Produces**: ACID(2)/CHLO(2)/LYE_(2)/H2__(2)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: produces HYAC(4)/CHLO(2)/LYE_(2)
  - STEELTOWN: default
  - BASIC_TEMPERATE: produces ACID(4)/CHLO(4)

### cider_mill
- **Accepts**: FRUT(3)/SGCN(3)/MNSP(1)/ENUM(1) → **Produces**: BEER(6)/ACET(3)/BIOM(2)
- **Economies**: BASIC_TROPIC

### civil_explosives_facility
- **Accepts**: NHNO(6)/PETR(2) → **Produces**: BOOM(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts NH3_(4)/ACID(2)/PLAS(1)/PETR(1), produces NHNO(6)/ENSP(2)
  - BASIC_TROPIC: accepts NITR(2)/SUAC(2)/RFPR(2), produces BOOM(6)/FERT(4)

### cleaning_products_factory
- **Accepts**: COPR(2)/STEL(2)/STWR(2)/PLAS(2) → **Produces**: POWR(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts LYE_(2)/SASH(2)/SALT(2)/NH3_(2)/MNSP(2), produces SOAP(6)/GOOD(4)
  - BASIC_TROPIC: accepts SASH(2)/PHAC(2)/ACET(2)/EOIL(2), produces SOAP(6)/GOOD(6)

### coke_oven
- **Accepts**: COAL(8) → **Produces**: COKE(6)/CTAR(1)/SULP(1)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TROPIC: produces COKE(6)/SULP(2)
  - BASIC_TEMPERATE: produces COKE(6)/SULP(2)

### component_factory
- **Accepts**: MPAR(2)/PPAR(2)/STAL(2)/POWR(2) → **Produces**: VPTS(8)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TROPIC: accepts MPAR(2)/TYRE(2)/PLAS(2)/TEXT(2)/COAT(2)
  - BASIC_TEMPERATE: accepts MPAR(2)/PLAS(2)/TEXT(2)/POWR(2)

### construction_plant
- **Accepts**: CMNT(2)/MPAR(2)/STWR(2)/GLAS(2) → **Produces**: GOOD(8)
- **Economies**: BETTER_LIVING_THROUGH_CHEMISTRY, STEELTOWN

### copper_concentrator
- **Accepts**: CORE(4)/SUAC(2)/QLME(2) → **Produces**: COCO(8)
- **Economy overrides**:
  - BASIC_TROPIC: produces COCO(6)/RAMT(3)

### copper_refinery
- **Accepts**: CORE(5)/RFPR(3) → **Produces**: COPR(8)
- **Economy overrides**:
  - BASIC_TROPIC: accepts COCO(4)/SCMT(2)/COKE(2), produces COPR(5)/SLAG(1)/SUAC(2)
  - IN_A_HOT_COUNTRY: default
  - STEELTOWN: accepts COCO(4)/SCMT(2)/ACID(2), produces COPR(6)/SLAG(1)/SULP(1)
  - BASIC_TEMPERATE: accepts CORE(4)/SCMT(2)/ACID(2), produces COPR(7)/SLAG(1)

### dairy
- **Accepts**: MILK(6) → **Produces**: FOOD(8)
- **Economy overrides**:
  - BASIC_TEMPERATE: accepts MILK(6)/MNSP(2), produces FOOD(8)/EOIL(2)
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts MILK(6)/MNSP(2)
  - BASIC_TROPIC: accepts MILK(6)/MNSP(2), produces FOOD(8)/EOIL(2)

### edible_oil_refinery
- **Accepts**: OLSD(6) → **Produces**: EOIL(4)/BIOM(1)
- **Economy overrides**:
  - BASIC_TROPIC: default
  - BASIC_TEMPERATE: accepts OLSD(4)

### electric_arc_furnace
- **Accepts**: SCMT(4)/FECR(2)/QLME(1)/O2__(1) → **Produces**: STCB(4)/STAL(2)/SLAG(2)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TEMPERATE: accepts SCMT(4)/QLME(2), produces STEL(6)/SLAG(2)

### electrical_works
- **Accepts**: STAL(3)/COPR(2)/RFPR(1)/STWR(1)/PPAR(1) → **Produces**: POWR(8)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TROPIC: accepts COPR(2)/SUAC(2)/PLAS(2)/RAMT(2), produces VPTS(6)/GOOD(6)
  - BASIC_TEMPERATE: accepts COPR(2)/TYRE(2)/PLAS(2)/RAMT(2), produces POWR(6)

### engine_plant
- **Accepts**: MPAR(2)/ALUM(2)/TYRE(2)/RFPR(2) → **Produces**: VENG(8)
- **Economies**: STEELTOWN

### ethylene_cracker
- **Accepts**: NAPH(8) → **Produces**: C2H4(4)/C3H6(3)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts RFPR(5)/CTAR(3), produces C2H4(5)/PETR(3)
  - BASIC_TEMPERATE: accepts RFPR(4)/CTAR(4), produces PETR(5)/COKE(3)/SULP(2)

### factory_1
- **Accepts**: GLAS(2)/STEL(2)/PLAS(2) → **Produces**: GOOD(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts STAL(2)/STSH(2)/GLAS(1)/PPAR(1)/POWR(1)/TYRE(1)
  - BASIC_TROPIC: accepts MPAR(4)/GLAS(2)/PLAS(2)/TYRE(2)

### factory_2
- **Accepts**: COPR(2)/STEL(2)/STWR(2)/PLAS(2) → **Produces**: POWR(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts LYE_(2)/SASH(2)/SALT(2)/NH3_(2), produces SOAP(8)

### factory_3
- **Accepts**: GLAS(2)/PLAS(2)/ALUM(2)/TINP(2) → **Produces**: MNSP(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts RFPR(2)/QLME(2)/CBLK(2)/PLAS(2), produces COAT(8)

### farm_supply_yard
- **Default**: accepts [], produces FMSP(4)
- **Economy overrides**:
  - BASIC_TROPIC: accepts VEHI(8)/PETR(8)/FERT(8), produces FMSP(8)
  - STEELTOWN: accepts NHNO(8)/VEHI(8)/PETR(8)/TYRE(8), produces FMSP(8)
  - BASIC_TEMPERATE: accepts VEHI(8)/PETR(8)/FERT(8), produces FMSP(8)

### ferrochrome_smelter
- **Accepts**: CHRO(4)/COAL(4) → **Produces**: FECR(8)
- **Economies**: NONE ENABLED

### fertiliser_plant
- **Accepts**: UREA(2)/POTA(2)/PHAC(2)/NHNO(2) → **Produces**: FMSP(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts NHNO(6)/SLAG(2)/ACID(2)
  - BASIC_TROPIC: accepts PHAC(4)/BIOM(2)/SLAG(2), produces FERT(6)

### fischer_tropsch_plant
- **Accepts**: COAL(8) → **Produces**: NH3_(2)/PETR(6)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: produces RFPR(6)/H2__(2)
  - BASIC_TEMPERATE: produces RFPR(6)/CTAR(2)

### fishing_harbour
- **Accepts**: FISH(6) → **Produces**: FOOD(8)
- **Economy overrides**:
  - BASIC_TEMPERATE: accepts FISH(6)/MNSP(1)
  - BASIC_TROPIC: produces MEAT(8)
  - BASIC_ARCTIC: default
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts FISH(6)/MNSP(1)/ENUM(1)

### flour_mill
- **Accepts**: GRAI(6)/MNSP(4) → **Produces**: FOOD(6)
- **Economy overrides**:
  - BASIC_TROPIC: accepts GRAI(6), produces BAKE(6)
  - STEELTOWN: default
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - IN_A_HOT_COUNTRY: accepts CASS(6)/MAIZ(6)
  - BASIC_TEMPERATE: produces FOOD(6)/EOIL(4)

### food_processor
- **Accepts**: BEAN(6)/FRUT(6) → **Produces**: FOOD(8)
- **Economy overrides**:
  - BASIC_TROPIC: accepts SUGR(6)/FRUT(6)/MEAT(6)/ENUM(2)/EOIL(2)/MNSP(2)
  - IN_A_HOT_COUNTRY: accepts NUTS(6)/FRUT(6), produces EOIL(4)/FOOD(4)
  - STEELTOWN: accepts FRUT(4)/FISH(4)/MNSP(2)/SALT(2)
  - BASIC_TEMPERATE: accepts FRUT(4)/FISH(4)/EOIL(4)/MNSP(2)/SALT(2)

### fruit_packing_plant
- **Accepts**: FRUT(6)/MNSP(3) → **Produces**: FOOD(8)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TROPIC: accepts FRUT(4)/BAKE(4)/MNSP(2)/ACET(2)

### furniture_factory
- **Accepts**: WDPR(6)/COAT(2) → **Produces**: FURN(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - BASIC_TROPIC: accepts WDPR(4)/TEXT(2)/MPAR(2)/GLAS(2)/COAT(2), produces GOOD(6)
  - BASIC_TEMPERATE: accepts WDPR(4)/TEXT(2)/MPAR(2)/GLAS(2), produces GOOD(6)

### glass_works
- **Accepts**: SAND(6)/SASH(2) → **Produces**: GLAS(8)
- **Economy overrides**:
  - BASIC_TEMPERATE: accepts SAND(6)/SASH(2)/QLME(2), produces GLAS(8)/MNSP(8)
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - IN_A_HOT_COUNTRY: accepts SAND(6)/RFPR(2), produces BDMT(4)/GOOD(4)
  - STEELTOWN: accepts SAND(4)/SASH(2)/QLME(1)/PLAS(1), produces GLAS(6)/MNSP(4)
  - BASIC_TROPIC: accepts SAND(4)/SASH(2)/QLME(1)/PLAS(1)

### integrated_steel_mill
- **Accepts**: IORE(3)/COAL(2)/SCMT(3) → **Produces**: STEL(8)
- **Economies**: NONE ENABLED (marked "delete")

### iron_works
- **Accepts**: IORE(3)/WOOD(3)/SAND(2) → **Produces**: STEL(8)
- **Economy overrides**:
  - STEELTOWN: accepts IRON(3)/ALUM(3)/SAND(2), produces MPAR(7)/SLAG(1)
  - BASIC_TROPIC: accepts IRON(3)/COAL(2)/SAND(2), produces MPAR(6)
  - BASIC_TEMPERATE: accepts IRON(3)/ALUM(2)/SAND(2), produces MPAR(6)

### junk_yard
- **Accepts**: RCYC(6) → **Produces**: SCMT(3)
- **Economy overrides**:
  - BASIC_TEMPERATE: default
  - BASIC_TROPIC: produces SCMT(4)/RAMT(1)
  - STEELTOWN: default

### latex_processor
- **Accepts**: LATX(6)/FORM(2) → **Produces**: RUBR(8)
- **Economies**: NONE ENABLED

### lime_kiln
- **Accepts**: LIME(8) → **Produces**: QLME(6)/FMSP(2)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts LIME(6)/PETR(2), produces QLME(8)
  - BASIC_TROPIC: accepts LIME(6)/PETR(2), produces QLME(6)/FERT(2)
  - BASIC_TEMPERATE: accepts LIME(6)/PETR(2), produces QLME(6)

### lumber_yard
- **Accepts**: WDPR(6)/COAT(2) → **Produces**: ENSP(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - IN_A_HOT_COUNTRY: accepts WDPR(6)/RFPR(2), produces BDMT(8)
  - BASIC_TROPIC: accepts WDPR(4)/GLAS(2)/MPAR(1)/COAT(1), produces BDMT(6)/MNSP(6)
  - BASIC_TEMPERATE: accepts WDPR(4)/MPAR(2)/COAT(2), produces BDMT(6)/MNSP(6)

### machine_shop
- **Accepts**: STEL(8)/PETR(8) → **Produces**: FMSP(4)/ENSP(4)
- **Economy overrides**:
  - STEELTOWN: accepts POWR(2)/VENG(2)/VPTS(2)/MPAR(1)/COAT(1), produces GOOD(4)/ENSP(2)/FMSP(2)
  - BASIC_TROPIC: accepts STEL(3)/GLAS(2)/VPTS(2)/TYRE(1), produces GOOD(4)/ENSP(2)/FMSP(2)
  - BASIC_TEMPERATE: accepts POWR(3)/VPTS(2)/MPAR(2)/TYRE(2)/GLAS(2), produces GOOD(4)/ENSP(2)/FMSP(2)

### meat_packing_plant
- **Accepts**: FISH(6)/MNSP(3)/SALT(2) → **Produces**: FOOD(8)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TROPIC: accepts MEAT(4)/MNSP(2)/ENUM(2), produces FOOD(6)/EOIL(4)/BIOM(2)

### metal_workshop
- **Accepts**: STEL(6)/RFPR(2) → **Produces**: GOOD(8)
- **Economy overrides**:
  - BASIC_TEMPERATE: accepts STEL(6)/ALUM(6)/COAT(2), produces MPAR(8)/MNSP(6)
  - STEELTOWN: accepts STSH(2)/COAT(2)/ZINC(2)/STWR(2), produces MNSP(3)/MPAR(4)/SCMT(1)
  - BASIC_TROPIC: accepts STEL(2)/COPR(2)/RAMT(2)/SOAP(2), produces MPAR(6)/GOOD(4)

### oil_refinery
- **Accepts**: OIL_(8) → **Produces**: PETR(3)/NAPH(3)/SULP(2)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts OIL_(7)/H2__(1), produces RFPR(4)/PETR(2)/CTAR(1)/SULP(1)
  - BASIC_TROPIC: produces RFPR(6)/PETR(4)/SULP(2)
  - BASIC_TEMPERATE: produces RFPR(6)/PETR(4)/CTAR(4)

### paint_factory
- **Accepts**: GLAS(2)/PLAS(2)/ALUM(2)/TINP(2) → **Produces**: MNSP(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts RFPR(2)/QLME(2)/CBLK(2)/PLAS(2)/MNSP(2), produces COAT(6)/GOOD(4)
  - BASIC_TROPIC: accepts RFPR(2)/QLME(2)/ACET(2)/PLAS(2), produces COAT(6)/GOOD(4)
  - BASIC_TEMPERATE: accepts RFPR(2)/QLME(2)/PLAS(2)/MNSP(2), produces COAT(6)/GOOD(4)

### paper_mill
- **Accepts**: KAOL(2)/WOOD(4)/SULP(2) → **Produces**: GOOD(8)
- **Economy overrides**:
  - BASIC_ARCTIC: produces PAPR(8)
  - BASIC_TROPIC: accepts WOOD(4)/CLAY(2)/SUAC(2), produces GOOD(4)/MNSP(7)
  - BASIC_TEMPERATE: accepts CLAY(2)/WOOD(4)/SULP(2), produces PAPR(6)/MNSP(8)

### phosphoric_acid_plant
- **Accepts**: PHOS(4)/SUAC(4) → **Produces**: PHAC(4)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - BASIC_TROPIC: produces PHAC(6)/ENUM(2)

### plastics_plant
- **Accepts**: CHLO(4)/C2H4(4) → **Produces**: PLAS(3)/COAT(3)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts PLAS(5)/MPAR(3), produces PPAR(6)/MNSP(5)
  - BASIC_TROPIC: accepts PLAS(2)/STEL(2)/GLAS(2), produces MNSP(6)
  - BASIC_TEMPERATE: accepts PLAS(5)/MPAR(3), produces MNSP(6)

### polyethylene_plant
- **Accepts**: C2H4(8) → **Produces**: PLAS(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts C2H4(5)/CHLO(3)
  - BASIC_TROPIC: accepts RFPR(6)/ACET(2), produces PLAS(5)/RUBR(3)
  - BASIC_TEMPERATE: accepts RFPR(6)/CHLO(2)/ACID(2), produces PLAS(5)/RUBR(3)/FICR(3)

### polypropylene_plant
- **Accepts**: C3H6(8) → **Produces**: PLAS(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts C2H4(5)/ACID(3), produces RUBR(8)

### printing_plant
- **Accepts**: PAPR(6)/COAT(2) → **Produces**: GOOD(6)/MAIL(6)
- **Economies**: BASIC_TEMPERATE

### pyrite_smelter
- **Accepts**: PORE(8) → **Produces**: ZINC(4)/SULP(4)
- **Economy overrides**:
  - BASIC_ARCTIC: default
  - STEELTOWN: accepts PORE(6)/COKE(1)/SOAP(1), produces ZINC(2)/COCO(3)/SLAG(1)/FECR(2)
  - BASIC_TEMPERATE: accepts PORE(6)/COKE(2)/ACID(2), produces ZINC(4)/RAMT(3)

### recycling_plant
- **Accepts**: RCYC(6) → **Produces**: PLAS(3)
- **Economies**: STEELTOWN, BASIC_TROPIC, BASIC_TEMPERATE

### sawmill
- **Accepts**: WOOD(6) → **Produces**: WDPR(8)
- **Economies**: IN_A_HOT_COUNTRY, BASIC_ARCTIC, BASIC_TROPIC, BASIC_TEMPERATE

### sheet_and_pipe_mill
- **Accepts**: STCB(4)/ZINC(2)/ACID(2) → **Produces**: STSH(8)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TEMPERATE: accepts STEL(4)/ZINC(3)/ACID(2), produces MPAR(6)/BDMT(6)

### slag_grinding_plant
- **Accepts**: SLAG(8) → **Produces**: CMNT(8)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TEMPERATE: produces CMNT(8)/FERT(5)

### smithy_forge
- **Accepts**: STEL(8) → **Produces**: ENSP(4)/FMSP(4)
- **Economies**: NONE ENABLED (expiry 1948)

### solvay_plant
- **Accepts**: SALT(8) → **Produces**: SASH(6)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts SALT(4)/LIME(2)/NH3_(2), produces SASH(8)
  - BASIC_TROPIC: accepts SALT(4)/LIME(2)/RFPR(2), produces SASH(8)
  - BASIC_TEMPERATE: accepts SALT(4)/LIME(2)/RFPR(2), produces SASH(8)

### steel_mill
- **Accepts**: IORE(2)/COKE(2)/LIME(2)/HYAC(1)/O2__(1) → **Produces**: STEL(8)
- **Economies**: BETTER_LIVING_THROUGH_CHEMISTRY

### stockyard
- **Accepts**: LVST(6) → **Produces**: FOOD(8)
- **Economy overrides**:
  - BASIC_TEMPERATE: accepts LVST(6)/MNSP(2)
  - BASIC_TROPIC: accepts LVST(8)/SOAP(2), produces MEAT(8)
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts LVST(6)/MNSP(1)/ENUM(1)
  - IN_A_HOT_COUNTRY: default
  - STEELTOWN: accepts LVST(6)/SOAP(2), produces FISH(8)

### sugar_refinery
- **Accepts**: MNSP(3)/SGBT(5) → **Produces**: FOOD(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - BASIC_TROPIC: accepts SGCN(6)/PHOS(1)/ENUM(1), produces SUGR(6)/BIOM(2)
  - BASIC_TEMPERATE: produces FOOD(6)/BIOM(2)

### sulphuric_acid_plant
- **Accepts**: SULP(8) → **Produces**: SUAC(6)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts SULP(5)/N7__(1)/H2__(2), produces ACID(8)
  - BASIC_TROPIC: default
  - BASIC_TEMPERATE: accepts SULP(5)/NITR(5)/RFPR(2), produces ACID(8)

### supply_yard
- **Default**: accepts [], produces ENSP(4)/FMSP(4)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: accepts VEHI(8)/PETR(8)
  - IN_A_HOT_COUNTRY: accepts BDMT(8)/PETR(8)/GOOD(8)
  - STEELTOWN: accepts NHNO(8)/VEHI(8)/PETR(8)/TYRE(8), produces ENSP(8)
  - BASIC_TROPIC: accepts VEHI(8)/PETR(8)/BOOM(8), produces ENSP(8)
  - BASIC_TEMPERATE: accepts VEHI(8)/PETR(8)/BOOM(8), produces ENSP(8)

### textile_mill
- **Accepts**: FICR(6) → **Produces**: TEXT(8)
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - IN_A_HOT_COUNTRY: accepts YARN(6)
  - BASIC_TROPIC: accepts FICR(5)/PLAS(2)/ACET(1), produces TEXT(7)/GOOD(4)
  - BASIC_TEMPERATE: accepts FICR(4)/COAT(2), produces TEXT(7)/GOOD(4)

### tinplate_works
- **Accepts**: STEL(4)/TIN_(2)/HYAC(2) → **Produces**: TINP(8)
- **Economies**: BETTER_LIVING_THROUGH_CHEMISTRY

### tyre_plant
- **Accepts**: RUBR(2)/CBLK(2)/SULP(2)/STWR(2) → **Produces**: TYRE(8)
- **Economy overrides**:
  - STEELTOWN: default
  - BASIC_TROPIC: accepts RUBR(4)/MPAR(2)/SULP(2), produces TYRE(8)/PLAS(4)
  - BASIC_TEMPERATE: accepts RUBR(4)/MPAR(2)/SULP(2), produces TYRE(8)/GOOD(4)

### wire_and_section_mill
- **Accepts**: STCB(3)/SOAP(1)/ALUM(2)/COPR(2) → **Produces**: MPAR(4)/STWR(3)/SCMT(1)
- **Economies**: STEELTOWN

---

## TERTIARY (town consumers)

### food_market
- **Accepts**: FOOD/FRUT/BEER → **Produces**: nothing
- **Economy overrides**:
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts FOOD
  - BASIC_TEMPERATE: default

### general_store
- **Accepts**: FOOD/GOOD/BEER → **Produces**: nothing
- **Economy overrides**:
  - BASIC_TEMPERATE: default
  - BASIC_ARCTIC: accepts FOOD
  - BASIC_TROPIC: default
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - IN_A_HOT_COUNTRY: default
  - STEELTOWN: accepts FOOD

### hardware_store
- **Default accepts**: []
- **Economy overrides**:
  - IN_A_HOT_COUNTRY: accepts GOOD/BDMT
  - BASIC_TROPIC: accepts GOOD/BDMT
  - BETTER_LIVING_THROUGH_CHEMISTRY: default
  - STEELTOWN: accepts GOOD
  - BASIC_TEMPERATE: accepts GOOD/BDMT

### hotel
- **Accepts**: FOOD/BEER/PASS → **Produces**: PASS(17)
- **Economies**: NONE ENABLED

### petrol_pump
- **Accepts**: FOOD/GOOD/PETR → **Produces**: nothing
- **Economies**: IN_A_HOT_COUNTRY, STEELTOWN, BASIC_TROPIC, BASIC_TEMPERATE

### power_plant
- **Accepts**: COAL/PETR → **Produces**: nothing
- **Economy overrides**:
  - BASIC_ARCTIC: accepts PEAT
  - STEELTOWN: default
  - BASIC_TROPIC: accepts COAL/PETR/BIOM
  - BASIC_TEMPERATE: accepts COAL/PETR/BIOM

### vehicle_distributor
- **Accepts**: VEHI → **Produces**: nothing
- **Economies**: STEELTOWN, BASIC_TROPIC, BASIC_TEMPERATE

---

## INFORMATIVE

### plaza
- No production, no acceptance
- **Economies**: all 6
