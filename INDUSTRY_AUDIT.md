# Secondary Industry Cargo Audit

Complete audit of all secondary industries across BASIC_TEMPERATE, BASIC_TROPIC, STEELTOWN economies.

## Legend
- **REQ** = Required input (essential raw material — production won't work without it)
- **BOOST** = Booster input (optional — improves efficiency/output)
- **SCALE** = Output gated behind scale level (medium/high expansion)
- **RCYC@scale** = Recyclables as high-scale output (large factories produce recyclable waste)
- Format: `CARGO(current → recommended)` or just `CARGO(ratio)` if unchanged

## Cargo Code Reference

### Raw Materials & Ores
| Code | Name | Code | Name |
|------|------|------|------|
| AORE | Bauxite | CHRO | Chromite Ore |
| CLAY | Clay | COAL | Coal |
| CORE | Copper Ore | DIAM | Diamonds |
| GRVL | Gravel/Stone | IORE | Iron Ore |
| KAOL | Kaolin | LIME | Limestone |
| MNO2 | Manganese | PEAT | Peat |
| PHOS | Phosphate | PORE | Pyrite Ore |
| POTA | Potash | SALT | Salt |
| SAND | Sand | SULP | Sulphur |
| WOOD | Logs | OIL_ | Oil |

### Agricultural & Organic
| Code | Name | Code | Name |
|------|------|------|------|
| BEAN | Beans | BIOM | Biomass |
| CASS | Cassava | FICR | Plant Fibres |
| FISH | Fish | FRUT | Fruits |
| GRAI | Grain | JAVA | Coffee |
| LATX | Raw Latex | LVST | Livestock |
| MAIZ | Maize | MILK | Milk |
| NUTS | Nuts | OLSD | Oil Seeds |
| SGBT | Sugar Beet | SGCN | Sugarcane |
| WOOL | Wool | | |

### Processed Metals
| Code | Name | Code | Name |
|------|------|------|------|
| ALO_ | Aluminia (Al Oxide) | ALUM | Aluminium |
| COCO | Copper Concentrate | COPR | Copper |
| CSTI | Cast Iron | FECR | Ferrochrome |
| IRON | Pig Iron | MPAR | Metal Parts |
| NICK | Nickel | RAMT | Rare Metals |
| SCMT | Scrap Metal | SLAG | Slag |
| STAL | Alloy Steel | STCB | Carbon Steel |
| STEL | Steel | STSH | Steel Sheet |
| STWR | Steel Wire Rod | STSE | Steel Sections |
| STTB | Steel Tube | STPP | Steel Pipe |
| SWRP | Steel Wire Rope | TIN_ | Tin |
| TINP | Tinplate | ZINC | Zinc |

### Chemicals & Industrial
| Code | Name | Code | Name |
|------|------|------|------|
| ACET | Acetic Acid | ACID | Acid |
| C2H4 | Ethylene | C3H6 | Propylene |
| CBLK | Carbon Black | CHLO | Chlorine |
| COKE | Coke | CTAR | Coal Tar |
| FORM | Formic Acid | H2__ | Hydrogen |
| HYAC | Hydrochloric Acid | LYE_ | Lye (NaOH) |
| MEOH | Methanol | N7__ | Nitrogen |
| NAPH | Naphtha | NH3_ | Ammonia |
| NHNO | Ammonium Nitrate | NITR | Nitrates |
| O2__ | Oxygen | PETR | Petrol |
| PHAC | Phosphoric Acid | QLME | Quicklime |
| RFPR | Chemicals | SASH | Soda Ash |
| SUAC | Sulphuric Acid | UREA | Urea |

### Manufactured & Consumer
| Code | Name | Code | Name |
|------|------|------|------|
| BAKE | Flour | BDMT | Building Materials |
| BEER | Alcohol | BOOM | Explosives |
| CCPR | Concrete Products | CMNT | Cement |
| COAT | Paints & Coatings | ENSP | Engineering Supplies |
| ENUM | Food Additives | EOIL | Edible Oil |
| FERT | Fertiliser | FMSP | Farm Supplies |
| FOCA | Forgings & Castings | FOOD | Food |
| FURN | Furniture | GLAS | Glass |
| GOOD | Goods | HWAR | Hardware |
| LFEQ | Lifting Equipment | MEAT | Meat |
| METL | Metal | MNSP | Packaging |
| PAPR | Paper | PIPE | Pipe |
| PLAS | Plastics | PPAR | Plastic Parts |
| POWR | Electrical Parts | PPWK | Pipework |
| PUMP | Pumps & Valves | RBAR | Rebar |
| RCYC | Recyclables | RUBR | Rubber |
| SOAP | Cleaning Agents | SUGR | Sugar |
| TEXT | Textiles | TYRE | Tyres |
| TYCO | Tyre Cord | VBOD | Vehicle Bodies |
| VENG | Vehicle Engines | VEHI | Vehicles |
| VPTS | Vehicle Parts | WDPR | Wood Products/Lumber |
| WELD | Welding Consumables | YARN | Yarn |

### Transport
| Code | Name |
|------|------|
| MAIL | Mail |
| PASS | Passengers |

---

## Cross-Cutting Issues

### Fix Priority (Bugs/Errors)
1. **Tyres/TYRE misuse**: Remove from Appliance Factory, Engine Plant, Electrical Works, Component Factory — tyres are vehicle-only
2. **Cement Plant TEMPERATE**: Accepts Cement/CMNT as input — circular dependency, cement plant should not accept cement
3. **Sulphuric Acid Plant STEELTOWN**: Nitrogen/N7__ and Hydrogen/H2__ are chemically wrong for contact process (uses Oxygen/O2__, not N2/H2)
4. **Sulphuric Acid Plant TEMPERATE**: Nitrates/NITR and Chemicals/RFPR are chemically wrong — same reason
5. **Pyrite Smelter STEELTOWN**: Ferrochrome/FECR output is wrong — pyrite contains no chromium, calcine is iron oxide (Iron Ore/IORE)
6. **Flour Mill TEMPERATE**: Produces Edible Oil/EOIL without any Oil Seeds/OLSD input — either add Oil Seeds or remove Edible Oil

### Systemic Patterns
- **Salt/SALT underused** in food processing — most fundamental preservation ingredient, only 2-3 industries use it
- **Packaging/MNSP ratios often too high** (3-4) — packaging should be 1-2, never rivaling primary material
- **Flat equal ratios** on many industries — primary material should clearly dominate
- **Output >> Input** on several industries — slag grinding 13:8, sheet mill 12:9, paper mill 14:8
- **Glass/GLAS over-represented** as input in non-glass industries (machine shop, lumber yard, assembly)
- **Biomass/BIOM as scale bonus underused** — most food/organic processing produces biomass waste at scale
- **Recyclables/RCYC as high-scale output** — large manufacturing plants produce significant recyclable waste (packaging, offcuts, defects)

---

## 1. FOOD PROCESSING

### 1.1 Stockyard — Slaughterhouse / Meat Processing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TEMPERATE | Livestock/LVST(6), Packaging/MNSP(2) | Livestock/LVST(6) REQ, Packaging/MNSP(1) BOOST, Salt/SALT(1) BOOST | Food/FOOD(8), Biomass/BIOM(2) | Food/FOOD(8), Biomass/BIOM(2) SCALE |
| TROPIC | Livestock/LVST(8), Cleaning Agents/SOAP(2) | Livestock/LVST(6) REQ, Cleaning Agents/SOAP(2) BOOST, Salt/SALT(2) BOOST | Meat/MEAT(8), Biomass/BIOM(2) | Meat/MEAT(8), Biomass/BIOM(2) SCALE |
| STEELTOWN | Livestock/LVST(6), Cleaning Agents/SOAP(2) | Livestock/LVST(6) REQ, Cleaning Agents/SOAP(1) BOOST, Salt/SALT(1) BOOST | Food/FOOD(8) | Food/FOOD(8) |

**Reasoning:**
- Livestock/LVST is the only required input — no animals, no meat
- Cleaning Agents/SOAP and Packaging/MNSP are boosters for sanitation/packaging
- Add Salt/SALT in all economies — fundamental for meat curing, brining, preservation
- TROPIC Livestock/LVST(8) is too high, reduce to 6 for consistency and to make room for Salt/SALT
- Biomass/BIOM (offal, blood meal, bone meal) already implemented as scale bonus — good

### 1.2 Dairy — Milk Processing (Cheese, Butter, Yogurt)

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TEMPERATE | Milk/MILK(6), Packaging/MNSP(2) | Milk/MILK(6) REQ, Packaging/MNSP(2) REQ, Salt/SALT(1) BOOST | Food/FOOD(8), Edible Oil/EOIL(2) | Food/FOOD(8), Edible Oil/EOIL(2) |
| TROPIC | Milk/MILK(6), Packaging/MNSP(2) | Milk/MILK(6) REQ, Packaging/MNSP(2) REQ, Salt/SALT(1) BOOST | Food/FOOD(8), Edible Oil/EOIL(2) | Food/FOOD(8), Edible Oil/EOIL(2) |

**Reasoning:**
- Milk/MILK and Packaging/MNSP are both required (currently enforced in code) — correct, dairy needs packaging
- Edible Oil/EOIL output is butter/butterfat — thematically excellent
- Add Salt/SALT(1) as booster — salt is essential in real cheesemaking (brining, salting curds)
- Consider Biomass/BIOM(1) SCALE for whey (major dairy byproduct, animal feed at industrial scale)
- Has `base_processing_cap=32` (warehouse system)

### 1.3 Bakery — Industrial Bread & Pastry Production

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Flour/BAKE(3), Sugar/SUGR(2), Food Additives/ENUM(1), Edible Oil/EOIL(1), Packaging/MNSP(1) | no change | Food/FOOD(8) | Food/FOOD(8), Biomass/BIOM(1) SCALE |

**Reasoning:**
- One of the best-designed industries. Five inputs with clear differentiation.
- Flour/BAKE(3) REQ — flour is the fundamental ingredient
- Sugar/SUGR(2) BOOST — sugar for pastries/sweet breads
- Food Additives/ENUM(1) BOOST — food additives (leavening, preservatives, emulsifiers)
- Edible Oil/EOIL(1) BOOST — fats for pastry/dough enrichment
- Packaging/MNSP(1) BOOST — retail packaging
- Consider Biomass/BIOM(1) SCALE — large bakeries produce waste dough, expired product, bread crusts → animal feed

### 1.4 Flour Mill — Grain Milling

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Grain/GRAI(6) | Grain/GRAI(6) REQ, Packaging/MNSP(2) BOOST | Flour/BAKE(6) | Flour/BAKE(6) |
| STEELTOWN | Grain/GRAI(6), Packaging/MNSP(4) | Grain/GRAI(6) REQ, Packaging/MNSP(2) BOOST | Food/FOOD(6) | Food/FOOD(6) |
| TEMPERATE | Grain/GRAI(6), Packaging/MNSP(4) | Grain/GRAI(6) REQ, Oil Seeds/OLSD(3) REQ, Packaging/MNSP(2) BOOST | Food/FOOD(6), Edible Oil/EOIL(4) | Food/FOOD(6), Edible Oil/EOIL(3) |

**Reasoning:**
- Grain/GRAI is the sole required input — grain milling is a simple process
- Packaging/MNSP(4) in ST/TEMP is too high — packaging shouldn't be 40% of input. Reduce to 2.
- TROPIC: add Packaging/MNSP(2) as booster — flour needs bagging
- **TEMPERATE: Edible Oil/EOIL output without oilseed input is wrong.** Add Oil Seeds/OLSD(3) REQ to justify it (combined grist mill + oil press). Otherwise remove Edible Oil/EOIL entirely.

### 1.5 Food Processor — Cannery / Food Factory

| Economy   | Current Accept                                                                                             | Rec. Accept                                                                                                                                | Current Produce | Rec. Produce |
| --------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ------------ |
| TROPIC    | Sugar/SUGR(6), Fruits/FRUT(6), Meat/MEAT(6), Food Additives/ENUM(2), Edible Oil/EOIL(2), Packaging/MNSP(2) | Fruits/FRUT(6) REQ, Meat/MEAT(4) REQ, Sugar/SUGR(3) BOOST, Packaging/MNSP(2) BOOST, Food Additives/ENUM(1) BOOST, Edible Oil/EOIL(1) BOOST | Food/FOOD(8)    | Food/FOOD(8) |
| STEELTOWN | Fruits/FRUT(4), Fish/FISH(4), Packaging/MNSP(2), Salt/SALT(2)                                              | no change                                                                                                                                  | Food/FOOD(8)    | Food/FOOD(8) |
| TEMPERATE | Fruits/FRUT(4), Fish/FISH(4), Edible Oil/EOIL(4), Packaging/MNSP(2), Salt/SALT(2)                          | Fruits/FRUT(4) REQ, Fish/FISH(4) REQ, Edible Oil/EOIL(2) BOOST, Packaging/MNSP(2) BOOST, Salt/SALT(2) BOOST                                | Food/FOOD(8)    | Food/FOOD(8) |

**Reasoning:**
- STEELTOWN variant is the best designed — two primary food inputs + processing inputs. No changes.
- TROPIC: three primary inputs all at ratio 6 is flat. Fruits/FRUT should dominate (tropical fruit canning), Meat/MEAT secondary, Sugar/SUGR is a preservation ingredient not a main product. Rebalance.
- TEMPERATE: Edible Oil/EOIL(4) is too high for a cannery — equal to the raw food inputs. Reduce to 2.
- Consider Biomass/BIOM(1) SCALE — canning waste (peels, trimmings, cores)

### 1.6 Fruit Packing Plant — Fruit Sorting, Packing, Preserving

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Fruits/FRUT(6), Packaging/MNSP(3) | Fruits/FRUT(6) REQ, Packaging/MNSP(2) BOOST | Food/FOOD(8) | Food/FOOD(8) |
| TROPIC | Fruits/FRUT(4), Flour/BAKE(4), Packaging/MNSP(2), Acetic Acid/ACET(2) | Fruits/FRUT(5) REQ, Flour/BAKE(3) BOOST, Packaging/MNSP(2) BOOST, Acetic Acid/ACET(1) BOOST | Food/FOOD(8) | Food/FOOD(8) |

**Reasoning:**
- STEELTOWN: Packaging/MNSP(3) slightly high → reduce to 2
- TROPIC: Flour/BAKE(4) is thematically odd for a "fruit packing plant" — flour has nothing to do with fruit sorting. If intent is general food packing, acceptable but Fruits/FRUT should dominate. Reduce Flour/BAKE to 3, Acetic Acid/ACET to 1, raise Fruits/FRUT to 5.
- Acetic Acid/ACET (vinegar) for preservation is a clever thematic choice
- Consider Biomass/BIOM(1) SCALE — culls, bruised fruit, trimmings

### 1.7 Fishing Harbour — Fish Processing, Filleting, Freezing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TEMPERATE | Fish/FISH(6), Packaging/MNSP(1) | Fish/FISH(6) REQ, Salt/SALT(2) BOOST, Packaging/MNSP(1) BOOST | Food/FOOD(8) | Food/FOOD(8), Edible Oil/EOIL(1) SCALE |
| TROPIC | Fish/FISH(6) | Fish/FISH(6) REQ, Salt/SALT(1) BOOST | Meat/MEAT(8) | Meat/MEAT(8) |

**Reasoning:**
- Both: Add Salt/SALT as booster — fish preservation relies heavily on salt (salted cod, curing, brining)
- TROPIC outputs Meat/MEAT (intermediate cargo for further processing) — intentional and good
- TEMPERATE: Consider Edible Oil/EOIL(1) SCALE — fish oil is a major byproduct of industrial-scale fish processing (cod liver oil, fish meal oil)
- Consider Biomass/BIOM(1) SCALE — fish heads, guts, trimmings become fish meal at scale

### 1.8 Meat Packing Plant — Meat Processing & Packaging

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Fish/FISH(6), Packaging/MNSP(3), Salt/SALT(2) | Fish/FISH(6) REQ, Packaging/MNSP(2) BOOST, Salt/SALT(2) BOOST | Food/FOOD(8) | Food/FOOD(8) |
| TROPIC | Meat/MEAT(4), Packaging/MNSP(2), Food Additives/ENUM(2) | Meat/MEAT(5) REQ, Packaging/MNSP(2) BOOST, Salt/SALT(2) BOOST, Food Additives/ENUM(1) BOOST | Food/FOOD(6), Edible Oil/EOIL(4), Biomass/BIOM(2) | Food/FOOD(7), Edible Oil/EOIL(2), Biomass/BIOM(2) SCALE |

**Reasoning:**
- STEELTOWN: Name says "meat" but accepts Fish/FISH — either rename or add Livestock/LVST. Packaging/MNSP(3→2).
- TROPIC: Edible Oil/EOIL(4) is too high — rendered fat (tallow/lard) is a byproduct, not 40% of output. Reduce to 2. Add Salt/SALT(2) for curing (ham, bacon, salami). Meat/MEAT(4→5) — primary input should dominate. Biomass/BIOM should be SCALE, not flat output.

### 1.9 Cider Mill — Fruit & Sugarcane Fermentation

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Fruits/FRUT(3), Sugarcane/SGCN(3), Packaging/MNSP(1), Food Additives/ENUM(1) | no change | Alcohol/BEER(6), Acetic Acid/ACET(3), Biomass/BIOM(2) | Alcohol/BEER(6), Acetic Acid/ACET(2), Biomass/BIOM(1), BIOM SCALE med=1 high=2 |

**Reasoning:**
- Dual primary inputs (Fruits/FRUT + Sugarcane/SGCN) at equal ratio is good — tropical distillery works with either/both
- Fruits/FRUT(3) REQ, Sugarcane/SGCN(3) REQ — both are fermentation feedstocks
- Packaging/MNSP(1) BOOST — bottles, barrels, kegs
- Food Additives/ENUM(1) BOOST — yeast, sulfites, clarifying agents
- Acetic Acid/ACET(3→2) — vinegar is a byproduct, not half the main product
- Biomass/BIOM as SCALE instead of flat output — pomace/bagasse at industrial scale

### 1.10 Sugar Refinery — Sugar Processing from Cane/Beet

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Sugarcane/SGCN(6), Phosphate/PHOS(1), Food Additives/ENUM(1) | no change | Sugar/SUGR(6), Biomass/BIOM(2) | no change |
| TEMPERATE | Packaging/MNSP(3), Sugar Beet/SGBT(5) | Sugar Beet/SGBT(6) REQ, Packaging/MNSP(2) BOOST, Limestone/LIME(1) BOOST | Food/FOOD(6), Biomass/BIOM(2) | Food/FOOD(6), Biomass/BIOM(2) |

**Reasoning:**
- TROPIC: Well designed. Phosphate/PHOS for sugar clarification (phosphatation process) is excellent thematic detail. Biomass/BIOM for bagasse is perfect — every sugar mill produces it.
- TEMPERATE: Packaging/MNSP(3) too high, Sugar Beet/SGBT(5) should be 6. Add Limestone/LIME(1) for carbonatation (lime-based clarification of beet juice).

### 1.11 Edible Oil Refinery — Oilseed Crushing & Refining

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Oil Seeds/OLSD(6) | Oil Seeds/OLSD(6) REQ, Packaging/MNSP(2) BOOST | Edible Oil/EOIL(4), Biomass/BIOM(1) | Edible Oil/EOIL(4), Biomass/BIOM(2) |
| TEMPERATE | Oil Seeds/OLSD(4) | Oil Seeds/OLSD(6) REQ, Packaging/MNSP(2) BOOST | Edible Oil/EOIL(4), Biomass/BIOM(1) | Edible Oil/EOIL(4), Biomass/BIOM(2) |

**Reasoning:**
- TEMPERATE: Oil Seeds/OLSD(4)→Edible Oil/EOIL(4) implies 100% extraction — unrealistic. Match tropic at Oil Seeds/OLSD(6).
- Both: Add Packaging/MNSP(2) BOOST — oil bottling requires containers
- Biomass/BIOM(1→2) — press cake/seed meal is a major byproduct (high-protein animal feed), more significant than current ratio suggests

### 1.12 Brewery — Beer & Spirits Production

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Grain/GRAI(4), Sugar/SUGR(2), Packaging/MNSP(1), Food Additives/ENUM(1) | no change | Alcohol/BEER(6), Biomass/BIOM(2) | no change |
| TEMPERATE | Grain/GRAI(4), Fruits/FRUT(3), Packaging/MNSP(2) | Grain/GRAI(4) REQ, Fruits/FRUT(2) BOOST, Packaging/MNSP(2) BOOST | Alcohol/BEER(6), Biomass/BIOM(2) | Alcohol/BEER(6), Biomass/BIOM(2) |

**Reasoning:**
- TROPIC: Well designed. Grain/GRAI(4) REQ, Sugar/SUGR(2) BOOST, Packaging/MNSP(1) BOOST, Food Additives/ENUM(1) BOOST (yeast, hops).
- TEMPERATE: Fruits/FRUT(3) is high for a brewery — fruit beer is niche. Reduce to 2.
- Both: Biomass/BIOM(2) for spent grain is thematically perfect (massive brewery byproduct).

---

## 2. STEEL / METAL CHAIN

### 2.1 Blast Furnace — Iron Ore Smelting

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Iron Ore/IORE(3), Coke/COKE(3), Limestone/LIME(2) | Iron Ore/IORE(3) REQ, Coke/COKE(3) REQ, Limestone/LIME(2) BOOST | Pig Iron/IRON(6), Slag/SLAG(2) | no change |
| TROPIC | Iron Ore/IORE(4), Coke/COKE(3), Limestone/LIME(2) | Iron Ore/IORE(4) REQ, Coke/COKE(3) REQ, Limestone/LIME(2) BOOST | Pig Iron/IRON(6), Slag/SLAG(2) | no change |
| TEMPERATE | Iron Ore/IORE(4), Coke/COKE(3), Limestone/LIME(2) | Iron Ore/IORE(4) REQ, Coke/COKE(3) REQ, Limestone/LIME(2) BOOST | Pig Iron/IRON(6), Slag/SLAG(2) | no change |

**Reasoning:**
- Metallurgically accurate across all economies. Iron Ore/IORE and Coke/COKE are both essential (ore is the feed, coke is both fuel and chemical reductant). Limestone/LIME is flux — improves slag chemistry but furnace can technically run without deliberate flux.
- Pig Iron/IRON(6):Slag/SLAG(2) = 3:1 ratio matches real blast furnace yields (~250-300 kg slag per tonne iron).
- No changes needed. Clean design.

### 2.2 Basic Oxygen Furnace (BOF) — Pig Iron to Steel Conversion

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Pig Iron/IRON(4), Ferrochrome/FECR(2), Quicklime/QLME(1), Oxygen/O2__(1) | Pig Iron/IRON(4) REQ, Ferrochrome/FECR(2) BOOST, Quicklime/QLME(1) BOOST, Oxygen/O2__(1) BOOST | Carbon Steel/STCB(3), Alloy Steel/STAL(3), Slag/SLAG(2) | Carbon Steel/STCB(4), Alloy Steel/STAL(2), Slag/SLAG(2) |
| TROPIC | Pig Iron/IRON(3), Scrap Metal/SCMT(3), Quicklime/QLME(1), Rare Metals/RAMT(1) | Pig Iron/IRON(4) REQ, Scrap Metal/SCMT(2) BOOST, Quicklime/QLME(1) BOOST, Rare Metals/RAMT(1) BOOST | Steel/STEL(6), Slag/SLAG(2) | no change |
| TEMPERATE | Pig Iron/IRON(4), Quicklime/QLME(2), Rare Metals/RAMT(2) | Pig Iron/IRON(4) REQ, Scrap Metal/SCMT(2) BOOST, Quicklime/QLME(1) BOOST, Rare Metals/RAMT(1) BOOST | Steel/STEL(6), Slag/SLAG(2) | no change |

**Reasoning:**
- Pig Iron/IRON is the only required input — pig iron is the primary metallic charge (70-80% of BOF)
- Ferrochrome/FECR and Rare Metals/RAMT are boosters — ferrochrome/alloy additives for specialty steels
- STEELTOWN: Carbon Steel/STCB(3):Alloy Steel/STAL(3) implies 50/50 carbon:alloy — alloy is specialty. Recommend Carbon Steel/STCB(4):Alloy Steel/STAL(2).
- TROPIC: Scrap Metal/SCMT(3) = Pig Iron/IRON(3) implies 50/50 scrap — too high for BOF (max 25-30% scrap). Reduce to Scrap Metal/SCMT(2), raise Pig Iron/IRON to 4.
- TEMPERATE: Missing Scrap Metal/SCMT entirely — a BOF without scrap is unusual. Add Scrap Metal/SCMT(2) BOOST, reduce Quicklime/QLME and Rare Metals/RAMT to 1 each.

### 2.3 Electric Arc Furnace (EAF) — Scrap Steel Recycling

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Scrap Metal/SCMT(4), Ferrochrome/FECR(2), Quicklime/QLME(1), Oxygen/O2__(1) | Scrap Metal/SCMT(4) REQ, Ferrochrome/FECR(2) BOOST, Quicklime/QLME(1) BOOST, Oxygen/O2__(1) BOOST | Carbon Steel/STCB(4), Alloy Steel/STAL(2), Slag/SLAG(2) | no change |
| TEMPERATE | Scrap Metal/SCMT(4), Quicklime/QLME(2) | Scrap Metal/SCMT(4) REQ, Quicklime/QLME(2) BOOST, Coal/COAL(2) BOOST | Steel/STEL(6), Slag/SLAG(2) | no change |

**Reasoning:**
- STEELTOWN: Well designed. Scrap Metal/SCMT dominant (EAF is defined by scrap-melting), Ferrochrome/FECR for alloy grades, Quicklime/QLME flux, Oxygen/O2__ for decarburization. No changes.
- TEMPERATE: Only 2 inputs feels thin. Add Coal/COAL(2) BOOST — carbon injection is standard EAF practice (foamy slag, carbon makeup). Creates supply chain link beyond coke oven.

### 2.4 Iron Works — Forge & Foundry

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Pig Iron/IRON(3), Aluminium/ALUM(3), Sand/SAND(2) | Pig Iron/IRON(3) REQ, Aluminium/ALUM(2) BOOST, Sand/SAND(2) BOOST, Coke/COKE(1) BOOST | Metal Parts/MPAR(7), Slag/SLAG(1) | no change |
| TROPIC | Pig Iron/IRON(3), Coal/COAL(2), Sand/SAND(2) | Pig Iron/IRON(3) REQ, Coal/COAL(2) BOOST, Sand/SAND(2) BOOST | Metal Parts/MPAR(6) | Metal Parts/MPAR(6), Slag/SLAG(1) |
| TEMPERATE | Pig Iron/IRON(3), Aluminium/ALUM(2), Sand/SAND(2) | Pig Iron/IRON(3) REQ, Aluminium/ALUM(2) BOOST, Sand/SAND(2) BOOST | Metal Parts/MPAR(6) | Metal Parts/MPAR(6), Slag/SLAG(1) |

**Reasoning:**
- Pig Iron/IRON is required — pig iron is the primary metal for castings and forgings
- Aluminium/ALUM is booster — non-ferrous casting (aluminium alloys). Reduce from 3→2 in STEELTOWN so iron dominates.
- Sand/SAND is booster — moulding sand for sand casting
- Coal/COAL or Coke/COKE is booster — cupola furnace fuel
- STEELTOWN: Add Coke/COKE(1) BOOST for cupola fuel (foundries burn coke)
- TROPIC/TEMPERATE: Add Slag/SLAG(1) output for consistency — iron foundries produce cupola slag

### 2.5 Sheet & Pipe Mill — Steel Rolling & Galvanizing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Carbon Steel/STCB(4), Zinc/ZINC(2), Acid/ACID(2) | Carbon Steel/STCB(4) REQ, Zinc/ZINC(2) BOOST, Acid/ACID(2) BOOST | Steel Sheet/STSH(8) | Steel Sheet/STSH(8), Scrap Metal/SCMT(1) SCALE |
| TEMPERATE | Steel/STEL(4), Zinc/ZINC(3), Acid/ACID(2) | Steel/STEL(4) REQ, Zinc/ZINC(2) BOOST, Acid/ACID(2) BOOST | Metal Parts/MPAR(6), Building Mat./BDMT(6) | Metal Parts/MPAR(4), Building Mat./BDMT(4) |

**Reasoning:**
- STEELTOWN: Metallurgically accurate — steel billets rolled, zinc for galvanizing, acid for pickling. No input changes.
- STEELTOWN: Consider Scrap Metal/SCMT(1) SCALE — rolling mills generate 3-5% internal scrap (crop ends, edge trim).
- TEMPERATE: Output total 12 from input 9 is too generous. Reduce Metal Parts/MPAR(6→4), Building Mat./BDMT(6→4). Also Zinc/ZINC(3→2).

### 2.6 Wire & Section Mill — Wire Drawing & Structural Rolling

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Carbon Steel/STCB(3), Cleaning Agents/SOAP(1), Aluminium/ALUM(2), Copper/COPR(2) | Carbon Steel/STCB(3) REQ, Aluminium/ALUM(2) BOOST, Copper/COPR(2) BOOST, Cleaning Agents/SOAP(1) BOOST | Metal Parts/MPAR(4), Wire Rod/STWR(3), Scrap Metal/SCMT(1) | no change |

**Reasoning:**
- Well designed. Carbon Steel/STCB for steel wire rod + sections, Aluminium/ALUM for aluminium extrusions, Copper/COPR for copper wire, Cleaning Agents/SOAP for wire drawing lubricant (realistic detail).
- Scrap Metal/SCMT(1) output for trimming/drawing scrap is excellent.
- No changes needed.

### 2.7 Alumina Refinery — Bayer Process (Bauxite to Alumina)

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Bauxite/AORE(6), Lye/LYE_(2) | Bauxite/AORE(6) REQ, Lye/LYE_(2) REQ | Aluminia/ALO_(8) | no change |

**Reasoning:**
- Textbook Bayer process: bauxite + caustic soda → alumina. Both inputs are truly required — the process fundamentally needs NaOH to dissolve alumina from bauxite.
- Bauxite/AORE(6) ratio represents the ~2-3 tonnes bauxite per tonne alumina.
- Clean, simple, correct. No changes.

### 2.8 Aluminium Plant — Hall-Héroult Smelting

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Aluminia/ALO_(4), Scrap Metal/SCMT(2), Coke/COKE(2) | Aluminia/ALO_(4) REQ, Scrap Metal/SCMT(2) BOOST, Coke/COKE(2) BOOST | Aluminium/ALUM(7), Slag/SLAG(1) | no change |
| TEMPERATE | Bauxite/AORE(4), Scrap Metal/SCMT(4), Coke/COKE(2), Acid/ACID(2) | Bauxite/AORE(5) REQ, Scrap Metal/SCMT(2) BOOST, Coke/COKE(2) BOOST, Acid/ACID(1) BOOST | Aluminium/ALUM(7), Slag/SLAG(1) | no change |

**Reasoning:**
- STEELTOWN: Aluminia/ALO_ is primary alumina feed, Coke/COKE represents carbon anodes, Scrap Metal/SCMT for scrap remelting. Good design.
- TEMPERATE: Combined refinery+smelter (takes raw bauxite). Scrap Metal/SCMT(4) = Bauxite/AORE(4) implies 50% scrap — too high. Raise Bauxite/AORE to 5, reduce Scrap Metal/SCMT to 2, Acid/ACID to 1.
- Slag/SLAG(1) represents aluminium dross (5-10% of production) — correct.

### 2.9 Copper Concentrator — Ore Crushing & Flotation

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Copper Ore/CORE(4), Sulphuric Acid/SUAC(2), Quicklime/QLME(2) | Copper Ore/CORE(4) REQ, Sulphuric Acid/SUAC(2) BOOST, Quicklime/QLME(2) BOOST | Copper Conc./COCO(6), Rare Metals/RAMT(3) | Copper Conc./COCO(7), Rare Metals/RAMT(2) |

**Reasoning:**
- Copper Ore/CORE is required — copper ore is the sole metallic feed
- Sulphuric Acid/SUAC for SX-EW leaching circuit, Quicklime/QLME for pH control in flotation — both correct boosters
- Copper Conc./COCO is copper concentrate (primary product), Rare Metals/RAMT represents precious metals recovery (gold, silver, molybdenum)
- Rare Metals/RAMT(3) is high for a byproduct. Recommend Copper Conc./COCO(7), Rare Metals/RAMT(2) — concentrate is dominant by mass.

### 2.10 Copper Refinery — Smelting & Electrolytic Refining

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Copper Conc./COCO(4), Scrap Metal/SCMT(2), Coke/COKE(2) | Copper Conc./COCO(4) REQ, Scrap Metal/SCMT(2) BOOST, Coke/COKE(2) BOOST | Copper/COPR(5), Slag/SLAG(1), Sulphuric Acid/SUAC(2) | no change |
| STEELTOWN | Copper Conc./COCO(4), Scrap Metal/SCMT(2), Acid/ACID(2) | Copper Conc./COCO(4) REQ, Scrap Metal/SCMT(2) BOOST, Acid/ACID(2) BOOST | Copper/COPR(6), Slag/SLAG(1), Sulphur/SULP(1) | no change |
| TEMPERATE | Copper Ore/CORE(4), Scrap Metal/SCMT(2), Acid/ACID(2) | Copper Ore/CORE(4) REQ, Scrap Metal/SCMT(2) BOOST, Acid/ACID(2) BOOST | Copper/COPR(7), Slag/SLAG(1) | Copper/COPR(6), Slag/SLAG(1), Sulphur/SULP(1) |

**Reasoning:**
- All economies well designed. Copper Conc./COCO or Copper Ore/CORE as primary, Scrap Metal/SCMT for scrap remelting, Coke/COKE or Acid/ACID for process.
- TROPIC: Sulphuric Acid/SUAC(2) output = acid plant capturing SO2 from smelting, creating elegant loop with copper concentrator. Excellent.
- TEMPERATE: Missing Sulphur/SULP output — copper smelting always produces SO2. Add Sulphur/SULP(1), reduce Copper/COPR(7→6).

### 2.11 Pyrite Smelter — Polymetallic Ore Roasting

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Pyrite Ore/PORE(6), Coke/COKE(1), Cleaning Agents/SOAP(1) | Pyrite Ore/PORE(6) REQ, Coke/COKE(1) BOOST, Cleaning Agents/SOAP(1) BOOST | Zinc/ZINC(2), Copper Conc./COCO(3), Slag/SLAG(1), Ferrochrome/FECR(2) | Zinc/ZINC(2), Copper Conc./COCO(3), Slag/SLAG(1), **Iron Ore/IORE(2)** |
| TEMPERATE | Pyrite Ore/PORE(6), Coke/COKE(2), Acid/ACID(2) | Pyrite Ore/PORE(6) REQ, Coke/COKE(2) BOOST, Acid/ACID(2) BOOST | Zinc/ZINC(4), Rare Metals/RAMT(3) | Zinc/ZINC(4), Rare Metals/RAMT(2), Sulphur/SULP(2) |

**Reasoning:**
- Pyrite Ore/PORE is required in both — pyrite ore is the sole metallic feed
- Coke/COKE for fuel/reductant, Cleaning Agents/SOAP for flotation reagent, Acid/ACID for hydrometallurgical leaching — all valid boosters
- **STEELTOWN: Ferrochrome/FECR(2) is wrong** — pyrite (FeS2) contains no chromium. The iron content becomes iron oxide calcine. Replace with Iron Ore/IORE(2).
- TEMPERATE: Output only 7 from input 10 is low. Add Sulphur/SULP(2) — pyrite roasting is a primary source of SO2 for sulphuric acid. Reduce Rare Metals/RAMT(3→2). Total becomes 8.

### 2.12 Slag Grinding Plant — Ground Granulated Blast Furnace Slag

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Slag/SLAG(8) | Slag/SLAG(6) REQ, Quicklime/QLME(2) BOOST | Cement/CMNT(8) | Cement/CMNT(6) |
| TEMPERATE | Slag/SLAG(8) | Slag/SLAG(6) REQ, Sand/SAND(2) BOOST | Cement/CMNT(8), Fertiliser/FERT(5) | Cement/CMNT(6), Fertiliser/FERT(3) |

**Reasoning:**
- Single-input industries are gameplay-dull. Add a second input as booster.
- STEELTOWN: Add Quicklime/QLME(2) BOOST — quicklime is an alkali activator for GGBFS (real requirement for cementitious properties). Reduce Cement/CMNT(8→6).
- TEMPERATE: Add Sand/SAND(2) BOOST — clinker/sand blended with ground slag for Portland-slag cement. Total output 13→9, much more balanced.

### 2.13 Coke Oven — Coal Carbonization

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Coal/COAL(8) | no change | Coke/COKE(6), Coal Tar/CTAR(1), Sulphur/SULP(1) | Coke/COKE(5), Coal Tar/CTAR(1), Sulphur/SULP(1), Hydrogen/H2__(1) |
| TROPIC | Coal/COAL(8) | no change | Coke/COKE(6), Sulphur/SULP(2) | no change |
| TEMPERATE | Coal/COAL(8) | no change | Coke/COKE(6), Sulphur/SULP(2) | Coke/COKE(6), Coal Tar/CTAR(1), Sulphur/SULP(1) |

**Reasoning:**
- Coal/COAL is the sole required input in all economies — correct, coking coal is the only feedstock.
- STEELTOWN: Coke oven gas is ~55% hydrogen. Add Hydrogen/H2__(1) output — creates valuable supply chain link to ammonia plant. Reduce Coke/COKE(6→5) to make room.
- TEMPERATE: **Coal Tar/CTAR exists in this economy** but isn't produced. Add Coal Tar/CTAR(1), reduce Sulphur/SULP(2→1) — harmonize with STEELTOWN's byproduct richness.
- TROPIC: No Coal Tar/CTAR cargo available — current outputs correct.

---

## 3. CHEMICAL CHAIN

### 3.1 Oil Refinery — Crude Oil Distillation & Cracking

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Oil/OIL_(7), Hydrogen/H2__(1) | Oil/OIL_(7) REQ, Hydrogen/H2__(1) BOOST | Chemicals/RFPR(4), Petrol/PETR(2), Coal Tar/CTAR(1), Sulphur/SULP(1) | no change |
| TROPIC | Oil/OIL_(8) | Oil/OIL_(8) REQ | Chemicals/RFPR(6), Petrol/PETR(4), Sulphur/SULP(2) | no change |
| TEMPERATE | Oil/OIL_(8) | Oil/OIL_(8) REQ | Chemicals/RFPR(6), Petrol/PETR(4), Coal Tar/CTAR(4) | Chemicals/RFPR(6), Petrol/PETR(4), Coal Tar/CTAR(2), Sulphur/SULP(2) |

**Reasoning:**
- STEELTOWN: Hydrogen/H2__ for hydrocracking is a real refinery upgrade — chemically accurate. Excellent design.
- TROPIC: Simple single-input topping refinery. Correct for a simpler economy.
- TEMPERATE: Coal Tar/CTAR(4) is too high — refineries produce far more light products than heavy residuum. Reduce to Coal Tar/CTAR(2), add Sulphur/SULP(2) for desulphurization (universal in real refining).

### 3.2 Biorefinery — Biomass to Biofuels & Chemicals

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Grain/GRAI(4), Fruits/FRUT(4) | Grain/GRAI(4) REQ, Fruits/FRUT(4) REQ | Chemicals/RFPR(2), Petrol/PETR(3), Ethylene/C2H4(3) | no change |
| TROPIC | Biomass/BIOM(6), Oil Seeds/OLSD(6), Grain/GRAI(6) | Biomass/BIOM(6) REQ, Oil Seeds/OLSD(4) BOOST, Grain/GRAI(4) BOOST | Chemicals/RFPR(4), Petrol/PETR(4) | no change |
| TEMPERATE | Sugar Beet/SGBT(6), Biomass/BIOM(6), Oil Seeds/OLSD(6) | Sugar Beet/SGBT(6) REQ, Biomass/BIOM(6) REQ, Oil Seeds/OLSD(4) BOOST | Chemicals/RFPR(5), Petrol/PETR(4), Plastics/PLAS(3) | Chemicals/RFPR(5), Petrol/PETR(5), Plastics/PLAS(1) SCALE |

**Reasoning:**
- All inputs at ratio 6 in TROPIC/TEMPERATE is flat — Biomass/BIOM should dominate as bulk cellulosic feedstock.
- STEELTOWN: Ethylene/C2H4 from ethanol dehydration is the key Steeltown value-add. Good design.
- **TEMPERATE: Plastics/PLAS(3) is unrealistic** — biorefineries don't directly produce plastics at this scale. Reduce to Plastics/PLAS(1) SCALE representing PLA (polylactic acid) bioplastic at expanded capacity. Increase Petrol/PETR(4→5).

### 3.3 Chemical Plant — General Chemical Synthesis

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Salt/SALT(2), Nitrates/NITR(2), Chemicals/RFPR(2) | Salt/SALT(2) REQ, Nitrates/NITR(2) REQ, Chemicals/RFPR(2) REQ, Sulphuric Acid/SUAC(2) BOOST | Acetic Acid/ACET(6), Food Additives/ENUM(4) | no change |

**Reasoning:**
- General-purpose synthesis facility. Salt/SALT for chlor-chemistry, Nitrates/NITR for amines, Chemicals/RFPR as hydrocarbon feedstock — all required.
- Add Sulphuric Acid/SUAC(2) BOOST — sulphuric acid is the most widely used industrial chemical, key reagent in nearly all chemical plants. Creates demand for sulphuric acid plant's output.
- Outputs are reasonable: Acetic Acid/ACET (solvents/acetone) and Food Additives/ENUM (food additives/specialty chemicals).

### 3.4 Chlor-Alkali Plant — Brine Electrolysis

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Salt/SALT(8) | Salt/SALT(6) REQ, Elec. Parts/POWR(2) BOOST | Acid/ACID(2), Chlorine/CHLO(2), Lye/LYE_(2), Hydrogen/H2__(2) | no change |
| TEMPERATE | Salt/SALT(8) | Salt/SALT(6) REQ, Elec. Parts/POWR(2) BOOST | Acid/ACID(4), Chlorine/CHLO(4) | no change |

**Reasoning:**
- Textbook electrolysis of NaCl brine → chlorine + sodium hydroxide + hydrogen. One of the most accurately modeled industries.
- Both: Add Elec. Parts/POWR(2) BOOST — chlor-alkali is extremely energy-intensive (2500+ kWh/tonne chlorine). Electricity as a booster reflects this reality.
- STEELTOWN: All 4 outputs are stoichiometrically correct.
- TEMPERATE: Simplified version dropping Lye/LYE_ and Hydrogen/H2__ (not in economy). Higher ratios on remaining outputs compensate.

### 3.5 Sulphuric Acid Plant — Contact Process

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Sulphur/SULP(5), Nitrogen/N7__(1), Hydrogen/H2__(2) | **Sulphur/SULP(6) REQ, Oxygen/O2__(2) BOOST** | Acid/ACID(8) | no change |
| TROPIC | Sulphur/SULP(8) | Sulphur/SULP(8) REQ | Sulphuric Acid/SUAC(6) | no change |
| TEMPERATE | Sulphur/SULP(5), Nitrates/NITR(5), Chemicals/RFPR(2) | **Sulphur/SULP(8) REQ** | Acid/ACID(8) | no change |

**Reasoning:**
- **STEELTOWN: CHEMICALLY WRONG.** Contact process burns S → SO2, oxidizes to SO3, absorbs in water → H2SO4. Neither nitrogen nor hydrogen is consumed. Replace Nitrogen/N7__ and Hydrogen/H2__ with Oxygen/O2__(2) BOOST (oxygen is the actual co-reactant).
- **TEMPERATE: CHEMICALLY WRONG.** Same issue — Nitrates/NITR and Chemicals/RFPR have no role in acid production. Simplify to Sulphur/SULP(8) single input.
- TROPIC: Correct as-is. Clean single-input design.

### 3.6 Phosphoric Acid Plant — Wet Process

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Phosphate/PHOS(4), Sulphuric Acid/SUAC(4) | Phosphate/PHOS(3) REQ, Sulphuric Acid/SUAC(5) REQ | Phosphoric Acid/PHAC(6), Food Additives/ENUM(2) | no change |

**Reasoning:**
- Textbook wet process: phosphate rock + sulphuric acid → phosphoric acid + gypsum.
- Both inputs are truly required — the reaction needs both reactants.
- Consider Phosphate/PHOS(3), Sulphuric Acid/SUAC(5) — real process needs ~2.5-3 tonnes H2SO4 per tonne phosphate rock.
- Food Additives/ENUM(2) represents gypsum byproduct — good abstraction.

### 3.7 Ammonia Plant — Haber-Bosch Process

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Chemicals/RFPR(2), Nitrogen/N7__(4), Hydrogen/H2__(2) | Chemicals/RFPR(2) BOOST, Nitrogen/N7__(2) REQ, Hydrogen/H2__(4) REQ | Ammonia/NH3_(8) | no change |
| TEMPERATE | Chemicals/RFPR(2), Nitrates/NITR(4), Biomass/BIOM(2), Acid/ACID(2) | Nitrates/NITR(4) REQ, Chemicals/RFPR(2) REQ, Acid/ACID(2) BOOST | Fertiliser/FERT(5), Explosives/BOOM(3) | no change |

**Reasoning:**
- STEELTOWN: Swap Nitrogen/N7__ and Hydrogen/H2__ ratios — hydrogen is the expensive/scarce input in Haber-Bosch, nitrogen comes free from atmosphere. Chemicals/RFPR as booster represents hydrocarbon feedstock for steam methane reforming.
- TEMPERATE: This is a combined ammonia/fertiliser/explosives facility (collapsed chain for simpler economy). Drop Biomass/BIOM(2) — not chemically relevant. Keep 3 inputs: Nitrates/NITR(4) REQ, Chemicals/RFPR(2) REQ, Acid/ACID(2) BOOST.
- TEMPERATE outputs Fertiliser/FERT + Explosives/BOOM (not Ammonia/NH3_) — makes sense for the simpler economy.

### 3.8 Fertiliser Plant — NPK Blending & Granulation

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Ammon. Nitrate/NHNO(6), Slag/SLAG(2), Acid/ACID(2) | Ammon. Nitrate/NHNO(6) REQ, Slag/SLAG(2) BOOST, Acid/ACID(2) BOOST | Farm Supplies/FMSP(8) | no change |
| TROPIC | Phosphoric Acid/PHAC(4), Biomass/BIOM(2), Slag/SLAG(2) | Phosphoric Acid/PHAC(3) REQ, Nitrates/NITR(3) REQ, Biomass/BIOM(1) BOOST, Slag/SLAG(1) BOOST | Fertiliser/FERT(6) | no change |

**Reasoning:**
- STEELTOWN: Good. Ammon. Nitrate/NHNO dominant (ammonium nitrate = primary N fertiliser), Slag/SLAG for phosphate/micronutrients (basic slag from steelmaking is real phosphate fertiliser), Acid/ACID for granulation.
- TROPIC: Add Nitrates/NITR(3) REQ — nitrogen is a major fertiliser component alongside phosphorus. Creates NPK completeness. Rebalance ratios accordingly.

### 3.9 Ethylene Cracker — Steam Cracking of Hydrocarbons

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Chemicals/RFPR(5), Coal Tar/CTAR(3) | Chemicals/RFPR(5) REQ, Coal Tar/CTAR(3) REQ | Ethylene/C2H4(5), Petrol/PETR(3) | no change |
| TEMPERATE | Chemicals/RFPR(4), Coal Tar/CTAR(4) | Chemicals/RFPR(4) REQ, Coal Tar/CTAR(4) REQ | Petrol/PETR(5), Coke/COKE(3), Sulphur/SULP(2) | no change |

**Reasoning:**
- STEELTOWN: Good. Chemicals/RFPR (naphtha) + Coal Tar/CTAR (coal tar liquids) are valid cracker feeds. Ethylene/C2H4 primary output, Petrol/PETR (pyrolysis gasoline) byproduct.
- TEMPERATE: No Ethylene/C2H4 in economy, so outputs are Petrol/PETR, Coke/COKE, Sulphur/SULP — functionally a thermal cracker/delayed coker. Outputs make sense for that process. Both inputs required.

### 3.10 Fischer-Tropsch Plant — Coal to Liquids

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Coal/COAL(8) | Coal/COAL(6) REQ, Oxygen/O2__(2) BOOST | Chemicals/RFPR(6), Hydrogen/H2__(2) | no change |
| TEMPERATE | Coal/COAL(8) | Coal/COAL(8) REQ | Chemicals/RFPR(6), Coal Tar/CTAR(2) | no change |

**Reasoning:**
- STEELTOWN: Add Oxygen/O2__(2) BOOST — oxygen-blown gasifiers are more efficient, creates demand for cryo plant output. Hydrogen/H2__(2) output = excess syngas hydrogen feeding back into Steeltown's hydrogen economy. Clever design.
- TEMPERATE: Simple coal→synfuels. Coal Tar/CTAR(2) for heavy waxes/tars from F-T synthesis. No changes.

### 3.11 Polyethylene Plant — Polymer Production

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Ethylene/C2H4(5), Chlorine/CHLO(3) | Ethylene/C2H4(5) REQ, Chlorine/CHLO(3) REQ | Plastics/PLAS(8) | no change |
| TROPIC | Chemicals/RFPR(6), Acetic Acid/ACET(2) | Chemicals/RFPR(6) REQ, Acetic Acid/ACET(2) BOOST | Plastics/PLAS(5), Rubber/RUBR(3) | no change |
| TEMPERATE | Chemicals/RFPR(6), Chlorine/CHLO(2), Acid/ACID(2) | Chemicals/RFPR(6) REQ, Chlorine/CHLO(2) BOOST, Acid/ACID(2) BOOST | Plastics/PLAS(5), Rubber/RUBR(3), Plant Fibres/FICR(3) | Plastics/PLAS(5), Rubber/RUBR(3), Plant Fibres/FICR(2) |

**Reasoning:**
- STEELTOWN: Technically this is PVC production (ethylene + chlorine → vinyl chloride → PVC), not polyethylene. Both inputs required. Output Plastics/PLAS(8) is correct abstraction.
- TROPIC: Chemicals/RFPR as catch-all monomer source. Acetic Acid/ACET as process solvent for emulsion polymerization. Rubber/RUBR(3) represents synthetic rubber co-production. Good.
- TEMPERATE: Output total 11 from input 10 is slightly generous. Consider Plant Fibres/FICR(3→2) for balance.

### 3.12 Polypropylene Plant — Synthetic Rubber & Elastomers

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Ethylene/C2H4(5), Acid/ACID(3) | Ethylene/C2H4(5) REQ, Acid/ACID(3) BOOST | Rubber/RUBR(8) | no change |

**Reasoning:**
- Ethylene/C2H4 as olefin monomer (proxy for propylene/butadiene), Acid/ACID as Ziegler-Natta catalyst activator. Rubber/RUBR output for synthetic rubber (SBR, EPDM).
- Simplified chemistry but gameplay flow works. No changes.

### 3.13 Plastics Plant — Injection Molding & Fabrication

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Plastics/PLAS(5), Metal Parts/MPAR(3) | Plastics/PLAS(5) REQ, Metal Parts/MPAR(3) REQ | Plastic Parts/PPAR(6), Packaging/MNSP(5) | no change |
| TROPIC | Plastics/PLAS(2), Steel/STEL(2), Glass/GLAS(2) | Plastics/PLAS(2) REQ, Steel/STEL(2) REQ, Glass/GLAS(2) BOOST | Packaging/MNSP(6) | Packaging/MNSP(6), Recyclables/RCYC(1) SCALE |
| TEMPERATE | Plastics/PLAS(5), Metal Parts/MPAR(3) | Plastics/PLAS(5) REQ, Metal Parts/MPAR(3) REQ | Packaging/MNSP(6) | Packaging/MNSP(6), Recyclables/RCYC(1) SCALE |

**Reasoning:**
- This is a fabrication/molding plant, not polymerization — well differentiated from polyethylene plant.
- STEELTOWN: Good. Plastic Parts/PPAR + Packaging/MNSP are fabricated products from raw resin + metal inserts.
- TROPIC/TEMPERATE: Good inputs. Consider Recyclables/RCYC(1) SCALE — large plastic fabrication plants generate significant recyclable offcuts, sprues, and defective parts.

### 3.14 Paint Factory — Coatings Manufacturing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Chemicals/RFPR(2), Quicklime/QLME(2), Carbon Black/CBLK(2), Plastics/PLAS(2), Packaging/MNSP(2) | Chemicals/RFPR(2) REQ, Quicklime/QLME(2) REQ, Carbon Black/CBLK(2) BOOST, Plastics/PLAS(2) REQ | Paints/COAT(6), Goods/GOOD(4) | no change |
| TROPIC | Chemicals/RFPR(2), Quicklime/QLME(2), Acetic Acid/ACET(2), Plastics/PLAS(2) | Chemicals/RFPR(2) REQ, Quicklime/QLME(2) REQ, Acetic Acid/ACET(2) REQ, Plastics/PLAS(2) REQ | Paints/COAT(6), Goods/GOOD(4) | no change |
| TEMPERATE | Chemicals/RFPR(2), Quicklime/QLME(2), Plastics/PLAS(2), Packaging/MNSP(2) | Chemicals/RFPR(2) REQ, Quicklime/QLME(2) REQ, Plastics/PLAS(2) REQ, Packaging/MNSP(2) BOOST | Paints/COAT(6), Goods/GOOD(4) | no change |

**Reasoning:**
- Chemicals/RFPR for solvents/binder precursors, Quicklime/QLME for calcium carbonate filler (#1 paint filler by volume), Carbon Black/CBLK for pigment, Plastics/PLAS for polymer binder, Acetic Acid/ACET for solvents.
- STEELTOWN: 5 equal-ratio inputs is heavy for players. Drop Packaging/MNSP — feeding manufactured supplies into paint to get Goods/GOOD creates an odd loop. 4 inputs is manageable.
- TROPIC/TEMPERATE: 4 inputs, well balanced. Good design.

### 3.15 Solvay Plant — Soda Ash Production

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Salt/SALT(4), Limestone/LIME(2), Ammonia/NH3_(2) | Salt/SALT(4) REQ, Limestone/LIME(2) REQ, Ammonia/NH3_(2) REQ | Soda Ash/SASH(8) | no change |
| TROPIC | Salt/SALT(4), Limestone/LIME(2), Chemicals/RFPR(2) | Salt/SALT(4) REQ, Limestone/LIME(2) REQ, Chemicals/RFPR(2) BOOST | Soda Ash/SASH(8) | no change |
| TEMPERATE | Salt/SALT(4), Limestone/LIME(2), Chemicals/RFPR(2) | Salt/SALT(4) REQ, Limestone/LIME(2) REQ, Chemicals/RFPR(2) BOOST | Soda Ash/SASH(8) | no change |

**Reasoning:**
- Textbook Solvay process: NaCl + CaCO3 + NH3 → Na2CO3. Perfect.
- STEELTOWN: All 3 inputs are required — the process needs all three.
- TROPIC/TEMPERATE: Chemicals/RFPR substitutes for Ammonia/NH3_ (not available) as energy proxy. Good simplification.
- No changes needed anywhere.

### 3.16 Carbon Black Plant — Coal Tar Pyrolysis

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Coal Tar/CTAR(8) | Coal Tar/CTAR(6) REQ, Chemicals/RFPR(2) BOOST | Carbon Black/CBLK(4), Coke/COKE(4) | no change |

**Reasoning:**
- Thermal decomposition of coal tar into carbon black + petroleum coke. Both outputs are real products.
- Consider adding Chemicals/RFPR(2) as secondary feedstock — many carbon black plants use both oil and tar. Reduce Coal Tar/CTAR(8→6).
- Alternatively keep single-input simplicity since it's co-located with coke oven.

### 3.17 Civil Explosives Facility — Ammonium Nitrate & Explosives

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Ammonia/NH3_(4), Acid/ACID(2), Plastics/PLAS(1), Petrol/PETR(1) | Ammonia/NH3_(4) REQ, Acid/ACID(2) REQ, Plastics/PLAS(1) BOOST, Petrol/PETR(1) BOOST | Ammon. Nitrate/NHNO(6), Eng. Supplies/ENSP(2) | no change |
| TROPIC | Nitrates/NITR(2), Sulphuric Acid/SUAC(2), Chemicals/RFPR(2) | Nitrates/NITR(2) REQ, Sulphuric Acid/SUAC(2) REQ, Chemicals/RFPR(2) BOOST | Explosives/BOOM(6), Fertiliser/FERT(4) | no change |

**Reasoning:**
- STEELTOWN: NH3 + acid → ammonium nitrate. Plastics/PLAS for emulsion explosive packaging, Petrol/PETR for fuel oil (ANFO). Eng. Supplies/ENSP(2) as output = explosives are key mining supplies. Good.
- TROPIC: Nitrates/NITR + Sulphuric Acid/SUAC → explosives and fertiliser (AN is dual-use). Fertiliser/FERT(4) co-product is realistic.
- Both economies well designed. No changes.

### 3.18 Cleaning Products Factory — Soap & Detergent Manufacturing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Lye/LYE_(2), Soda Ash/SASH(2), Salt/SALT(2), Ammonia/NH3_(2), Packaging/MNSP(2) | Lye/LYE_(3) REQ, Soda Ash/SASH(3) REQ, Ammonia/NH3_(1) BOOST, Packaging/MNSP(1) BOOST | Cleaning Agents/SOAP(6), Goods/GOOD(4) | no change |
| TROPIC | Soda Ash/SASH(2), Phosphoric Acid/PHAC(2), Acetic Acid/ACET(2), Edible Oil/EOIL(2) | Soda Ash/SASH(2) REQ, Phosphoric Acid/PHAC(2) REQ, Acetic Acid/ACET(2) BOOST, Edible Oil/EOIL(2) BOOST | Cleaning Agents/SOAP(6), Goods/GOOD(6) | Cleaning Agents/SOAP(6), Goods/GOOD(4) |

**Reasoning:**
- STEELTOWN: 5 equal inputs is hard for players. Drop Salt/SALT (redundant with Soda Ash/SASH — both are sodium compounds). Raise Lye/LYE_ and Soda Ash/SASH to reflect their dominance in saponification/detergent production.
- TROPIC: Well designed — Soda Ash/SASH for detergent builder, Phosphoric Acid/PHAC for phosphate cleaners, Acetic Acid/ACET for solvent cleaners, Edible Oil/EOIL for fragrance (thematic for tropics). Goods/GOOD(6) output is generous — reduce to 4.

---

## 4. MANUFACTURING

### 4.1 Appliance Factory — Household Appliance Manufacturing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Alloy Steel/STAL(2), Steel Sheet/STSH(2), Glass/GLAS(1), Plastic Parts/PPAR(1), Elec. Parts/POWR(1), Tyres/TYRE(1) | Steel Sheet/STSH(4) REQ, Elec. Parts/POWR(2) REQ, Glass/GLAS(1) BOOST, Plastic Parts/PPAR(1) BOOST | Goods/GOOD(8) | Goods/GOOD(8), Recyclables/RCYC(1) SCALE |
| TROPIC | Metal Parts/MPAR(4), Glass/GLAS(2), Plastics/PLAS(2), Tyres/TYRE(2) | Metal Parts/MPAR(4) REQ, Plastics/PLAS(2) REQ, Glass/GLAS(2) BOOST | Goods/GOOD(8) | Goods/GOOD(8), Recyclables/RCYC(1) SCALE |
| TEMPERATE | Metal Parts/MPAR(4), Elec. Parts/POWR(4), Glass/GLAS(2), Plastics/PLAS(2) | Metal Parts/MPAR(4) REQ, Elec. Parts/POWR(2) REQ, Glass/GLAS(2) BOOST, Plastics/PLAS(2) BOOST | Goods/GOOD(8) | Goods/GOOD(8), Recyclables/RCYC(1) SCALE |

**Reasoning:**
- **Remove Tyres/TYRE from all variants** — tyres have nothing to do with washing machines or refrigerators.
- STEELTOWN: Drop Alloy Steel/STAL (redundant with Steel Sheet/STSH — appliance bodies are stamped sheet steel, not alloy bar). Raise Steel Sheet/STSH to 4.
- TEMPERATE: Elec. Parts/POWR(4) too high — reduce to 2 (electrical components important but metal+plastic are bulk material).
- All: Recyclables/RCYC(1) SCALE — large appliance factories produce packaging waste, defective parts, foam offcuts.

### 4.2 Assembly Plant — Vehicle Assembly Line

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Vehicle Parts/VPTS(2), Vehicle Bodies/VBOD(2), Vehicle Engines/VENG(2), Tyres/TYRE(4) | Vehicle Bodies/VBOD(3) REQ, Vehicle Engines/VENG(3) REQ, Vehicle Parts/VPTS(2) REQ, Tyres/TYRE(2) BOOST | Vehicles/VEHI(6), Eng. Supplies/ENSP(1), Farm Supplies/FMSP(1) | Vehicles/VEHI(8), Eng. Supplies/ENSP(1) SCALE, Farm Supplies/FMSP(1) SCALE |
| TROPIC | Steel/STEL(2), Glass/GLAS(2), Vehicle Parts/VPTS(2), Tyres/TYRE(1), Paints/COAT(1) | Steel/STEL(4) REQ, Vehicle Parts/VPTS(2) REQ, Glass/GLAS(1) BOOST, Tyres/TYRE(1) BOOST, Paints/COAT(1) BOOST | Vehicles/VEHI(6) | Vehicles/VEHI(6), Recyclables/RCYC(1) SCALE |
| TEMPERATE | Steel/STEL(3), Glass/GLAS(2), Vehicle Parts/VPTS(2), Metal Parts/MPAR(2), Tyres/TYRE(2), Paints/COAT(2) | Steel/STEL(4) REQ, Vehicle Parts/VPTS(3) REQ, Metal Parts/MPAR(2) BOOST, Tyres/TYRE(2) BOOST, Glass/GLAS(1) BOOST, Paints/COAT(1) BOOST | Vehicles/VEHI(6) | Vehicles/VEHI(6), Recyclables/RCYC(1) SCALE |

**Reasoning:**
- STEELTOWN: Tyres/TYRE(4) is way too high — tyres are cheap relative to body+engine. Reduce to 2. Raise Vehicle Bodies/VBOD and Vehicle Engines/VENG (expensive critical parts). Eng. Supplies/ENSP and Farm Supplies/FMSP could be SCALE outputs — equipment assembly at large scale.
- TROPIC/TEMPERATE: Steel/STEL should dominate (structural material). Reduce Glass/GLAS (windshields are minor). Paints/COAT for paint finish.
- All: Recyclables/RCYC(1) SCALE — vehicle assembly generates packaging waste, stamping offcuts.

### 4.3 Body Plant — Vehicle Body Stamping & Welding

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Steel Sheet/STSH(4), Paints/COAT(2), Glass/GLAS(2) | Steel Sheet/STSH(5) REQ, Paints/COAT(2) REQ, Zinc/ZINC(1) BOOST | Vehicle Bodies/VBOD(7), Scrap Metal/SCMT(1) | no change |

**Reasoning:**
- Drop Glass/GLAS(2) — glass is installed at assembly, not body plant. Body plants produce bare painted shells.
- Raise Steel Sheet/STSH(4→5) — sheet steel is overwhelmingly the main material for body stamping.
- Add Zinc/ZINC(1) BOOST — for galvanization of body panels (corrosion protection).
- Scrap Metal/SCMT(1) output is excellent — stamping produces 30-40% waste sheet metal. Keep.

### 4.4 Component Factory — Automotive/Industrial Component Manufacturing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Metal Parts/MPAR(2), Plastic Parts/PPAR(2), Alloy Steel/STAL(2), Elec. Parts/POWR(2) | Alloy Steel/STAL(3) REQ, Metal Parts/MPAR(2) REQ, Plastic Parts/PPAR(2) BOOST, Elec. Parts/POWR(1) BOOST | Vehicle Parts/VPTS(8) | Vehicle Parts/VPTS(8), Recyclables/RCYC(1) SCALE |
| TROPIC | Metal Parts/MPAR(2), Tyres/TYRE(2), Plastics/PLAS(2), Textiles/TEXT(2), Paints/COAT(2) | Metal Parts/MPAR(3) REQ, Plastics/PLAS(2) REQ, Textiles/TEXT(2) BOOST, Paints/COAT(1) BOOST | Vehicle Parts/VPTS(8) | Vehicle Parts/VPTS(8) |
| TEMPERATE | Metal Parts/MPAR(2), Plastics/PLAS(2), Textiles/TEXT(2), Elec. Parts/POWR(2) | Metal Parts/MPAR(3) REQ, Elec. Parts/POWR(2) REQ, Plastics/PLAS(2) BOOST, Textiles/TEXT(1) BOOST | Vehicle Parts/VPTS(8) | Vehicle Parts/VPTS(8) |

**Reasoning:**
- STEELTOWN: Alloy Steel/STAL should be primary (precision alloy steel for drivetrain components — shafts, gears). Raise to 3, reduce Elec. Parts/POWR to 1.
- **TROPIC: Remove Tyres/TYRE(2)** — component factories don't process tyres. Metal Parts/MPAR as dominant.
- TEMPERATE: Good mix. Metal Parts/MPAR as primary (machined blanks), Elec. Parts/POWR for electrical harnesses.
- STEELTOWN: Recyclables/RCYC(1) SCALE — machining waste, packaging, defective assemblies.

### 4.5 Engine Plant — Engine Block Casting & Assembly

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Metal Parts/MPAR(2), Aluminium/ALUM(2), Tyres/TYRE(2), Chemicals/RFPR(2) | Aluminium/ALUM(3) REQ, Metal Parts/MPAR(3) REQ, Chemicals/RFPR(1) BOOST, Alloy Steel/STAL(1) BOOST | Vehicle Engines/VENG(8) | Vehicle Engines/VENG(8), Scrap Metal/SCMT(1) SCALE |

**Reasoning:**
- **Remove Tyres/TYRE(2)** — engines have absolutely nothing to do with tyres.
- Aluminium/ALUM(3) REQ — engine blocks and cylinder heads are aluminium castings (heaviest single component).
- Metal Parts/MPAR(3) REQ — precision machined internals (valves, camshafts, crankshafts).
- Add Alloy Steel/STAL(1) BOOST — crankshafts and connecting rods are high-strength alloy steel.
- Chemicals/RFPR(1) BOOST — lubricants, chemical sealants, test fuel.
- Scrap Metal/SCMT(1) SCALE — machining waste from cylinder boring at scale.

### 4.6 Electrical Works — Motors, Wiring, Panels

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Copper/COPR(2), Sulphuric Acid/SUAC(2), Plastics/PLAS(2), Rare Metals/RAMT(2) | Copper/COPR(3) REQ, Alloy Steel/STAL(2) REQ, Wire Rod/STWR(1) BOOST, Plastic Parts/PPAR(1) BOOST, Chemicals/RFPR(1) BOOST | Elec. Parts/POWR(8) | Elec. Parts/POWR(8) |
| TROPIC | Alloy Steel/STAL(3), Copper/COPR(2), Chemicals/RFPR(1), Wire Rod/STWR(1), Plastic Parts/PPAR(1) | Copper/COPR(3) REQ, Plastics/PLAS(2) REQ, Rare Metals/RAMT(1) BOOST, Steel/STEL(2) BOOST | Vehicle Parts/VPTS(6), Goods/GOOD(6) | Vehicle Parts/VPTS(6), Goods/GOOD(6) |
| TEMPERATE | Copper/COPR(2), Tyres/TYRE(2), Plastics/PLAS(2), Rare Metals/RAMT(2) | Copper/COPR(3) REQ, Plastics/PLAS(2) REQ, Rare Metals/RAMT(2) BOOST | Elec. Parts/POWR(6) | Elec. Parts/POWR(6) |

**Reasoning:**
- Copper/COPR should be primary in all variants — copper windings are the heart of every motor and transformer.
- **TEMPERATE: Remove Tyres/TYRE(2)** — motors don't need tyres.
- STEELTOWN: Needs steel for laminations/motor cores. Wire Rod/STWR for cabling. Plastic Parts/PPAR for housings.
- TROPIC: Outputs Vehicle Parts/VPTS + Goods/GOOD (no Elec. Parts/POWR cargo in tropic) — reasonable workaround.

### 4.7 Tyre Plant — Vulcanization & Tyre Building

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Rubber/RUBR(2), Carbon Black/CBLK(2), Sulphur/SULP(2), Wire Rod/STWR(2) | Rubber/RUBR(4) REQ, Carbon Black/CBLK(2) REQ, Sulphur/SULP(1) BOOST, Wire Rod/STWR(1) BOOST | Tyres/TYRE(8) | no change |
| TROPIC | Rubber/RUBR(4), Metal Parts/MPAR(2), Sulphur/SULP(2) | Rubber/RUBR(4) REQ, Sulphur/SULP(2) BOOST, Metal Parts/MPAR(1) BOOST | Tyres/TYRE(8), Plastics/PLAS(4) | Tyres/TYRE(8), Plastics/PLAS(2) |
| TEMPERATE | Rubber/RUBR(4), Metal Parts/MPAR(2), Sulphur/SULP(2) | Rubber/RUBR(4) REQ, Sulphur/SULP(2) BOOST, Metal Parts/MPAR(1) BOOST | Tyres/TYRE(8), Goods/GOOD(4) | Tyres/TYRE(8), Goods/GOOD(2) |

**Reasoning:**
- All: Rubber/RUBR should clearly dominate (70%+ of tyre by weight is rubber compound). Steeltown has all 4 correct ingredients but at equal ratios — raise Rubber/RUBR to 4.
- Carbon Black/CBLK is essential reinforcing filler (20-30% of compound). Sulphur/SULP for vulcanization and Wire Rod/STWR for bead wire/belt reinforcement — both important but small quantities.
- TROPIC/TEMPERATE: Plastics/PLAS(4)/Goods/GOOD(4) secondary outputs are too high — reduce to 2 each. Metal Parts/MPAR(2→1).

### 4.8 Machine Shop — Precision Machining & Heavy Equipment Assembly

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Elec. Parts/POWR(2), Vehicle Engines/VENG(2), Vehicle Parts/VPTS(2), Metal Parts/MPAR(1), Paints/COAT(1) | Vehicle Engines/VENG(3) REQ, Vehicle Parts/VPTS(2) REQ, Elec. Parts/POWR(2) BOOST, Metal Parts/MPAR(1) BOOST | Goods/GOOD(4), Eng. Supplies/ENSP(2), Farm Supplies/FMSP(2) | Eng. Supplies/ENSP(3), Farm Supplies/FMSP(3), Goods/GOOD(2) |
| TROPIC | Steel/STEL(3), Glass/GLAS(2), Vehicle Parts/VPTS(2), Tyres/TYRE(1) | Steel/STEL(4) REQ, Vehicle Parts/VPTS(2) REQ, Tyres/TYRE(1) BOOST | Goods/GOOD(4), Eng. Supplies/ENSP(2), Farm Supplies/FMSP(2) | no change |
| TEMPERATE | Elec. Parts/POWR(3), Vehicle Parts/VPTS(2), Metal Parts/MPAR(2), Tyres/TYRE(2), Glass/GLAS(2) | Vehicle Parts/VPTS(3) REQ, Elec. Parts/POWR(2) REQ, Metal Parts/MPAR(2) BOOST, Tyres/TYRE(1) BOOST | Goods/GOOD(4), Eng. Supplies/ENSP(2), Farm Supplies/FMSP(2) | no change |

**Reasoning:**
- This is where Eng. Supplies/ENSP and Farm Supplies/FMSP come from — heavy equipment assembly. Engines and components → finished machinery.
- **All: Remove Glass/GLAS** — heavy equipment doesn't use much glass. Drop from TROPIC and TEMPERATE.
- STEELTOWN: Raise Vehicle Engines/VENG to 3 (engines are the core of heavy equipment). Shift output emphasis to Eng. Supplies/ENSP and Farm Supplies/FMSP (primary purpose). Reduce Goods/GOOD.
- TROPIC: Raise Steel/STEL to 4 (dominant material).
- TEMPERATE: Vehicle Parts/VPTS as primary, drop Glass/GLAS, reduce Tyres/TYRE to 1.

### 4.9 Metal Workshop — General Metalworking & Fabrication

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Steel Sheet/STSH(2), Paints/COAT(2), Zinc/ZINC(2), Wire Rod/STWR(2) | Steel Sheet/STSH(3) REQ, Paints/COAT(2) BOOST, Zinc/ZINC(1) BOOST, Wire Rod/STWR(2) BOOST | Packaging/MNSP(3), Metal Parts/MPAR(4), Scrap Metal/SCMT(1) | no change |
| TROPIC | Steel/STEL(2), Copper/COPR(2), Rare Metals/RAMT(2), Cleaning Agents/SOAP(2) | Steel/STEL(4) REQ, Copper/COPR(2) BOOST, Rare Metals/RAMT(1) BOOST, Cleaning Agents/SOAP(1) BOOST | Metal Parts/MPAR(6), Goods/GOOD(4) | no change |
| TEMPERATE | Steel/STEL(6), Aluminium/ALUM(6), Paints/COAT(2) | Steel/STEL(6) REQ, Aluminium/ALUM(4) BOOST, Paints/COAT(2) BOOST | Metal Parts/MPAR(8), Packaging/MNSP(6) | Metal Parts/MPAR(8), Packaging/MNSP(6), Recyclables/RCYC(1) SCALE |

**Reasoning:**
- STEELTOWN: All 4 inputs correct (Steel Sheet/STSH for cutting/forming, Paints/COAT for finishing, Zinc/ZINC for galvanizing, Wire Rod/STWR for wire products). Steel Sheet/STSH should dominate → raise to 3, reduce Zinc/ZINC to 1.
- TROPIC: Steel/STEL should dominate → raise to 4. Reduce Rare Metals/RAMT and Cleaning Agents/SOAP to 1 each.
- TEMPERATE: Aluminium/ALUM(6) too high — reduce to 4 (steel is more common in general metalwork).
- TEMPERATE: Recyclables/RCYC(1) SCALE — large metalworking shops produce significant recyclable scrap.

### 4.10 Furniture Factory — Furniture Manufacturing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Lumber/WDPR(4), Textiles/TEXT(2), Metal Parts/MPAR(2), Glass/GLAS(2), Paints/COAT(2) | Lumber/WDPR(4) REQ, Textiles/TEXT(2) REQ, Metal Parts/MPAR(1) BOOST, Glass/GLAS(1) BOOST, Paints/COAT(1) BOOST | Goods/GOOD(6) | Goods/GOOD(6), Recyclables/RCYC(1) SCALE |
| TEMPERATE | Lumber/WDPR(4), Textiles/TEXT(2), Metal Parts/MPAR(2), Glass/GLAS(2) | Lumber/WDPR(4) REQ, Textiles/TEXT(2) REQ, Metal Parts/MPAR(1) BOOST, Glass/GLAS(1) BOOST, Paints/COAT(1) BOOST | Goods/GOOD(6) | Goods/GOOD(6), Recyclables/RCYC(1) SCALE |

**Reasoning:**
- Lumber/WDPR dominant — wood is the primary structural material. Textiles/TEXT for upholstery. Both required.
- Reduce Metal Parts/MPAR, Glass/GLAS, Paints/COAT to 1 each — minor materials relative to wood and fabric.
- TEMPERATE: Add Paints/COAT(1) BOOST — furniture needs varnish/lacquer finish.
- Both: Recyclables/RCYC(1) SCALE — large furniture plants produce packaging waste, wood offcuts, fabric scraps.

### 4.11 Textile Mill — Spinning, Weaving, Finishing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Plant Fibres/FICR(5), Plastics/PLAS(2), Acetic Acid/ACET(1) | Plant Fibres/FICR(5) REQ, Plastics/PLAS(2) BOOST, Acetic Acid/ACET(1) BOOST | Textiles/TEXT(7), Goods/GOOD(4) | Textiles/TEXT(7), Goods/GOOD(3) |
| TEMPERATE | Plant Fibres/FICR(4), Paints/COAT(2) | Plant Fibres/FICR(5) REQ, Paints/COAT(1) BOOST, Plastics/PLAS(1) BOOST | Textiles/TEXT(7), Goods/GOOD(4) | Textiles/TEXT(7), Goods/GOOD(3) |

**Reasoning:**
- Plant Fibres/FICR dominant — raw fibre IS the main input. Plastics/PLAS for synthetic fibre blends. Acetic Acid/ACET or Paints/COAT for chemical finishing/dyeing.
- TROPIC: Good design. Plant Fibres/FICR(5) REQ, Plastics/PLAS(2) BOOST (synthetic blends), Acetic Acid/ACET(1) BOOST (solvents for acetate fabrics).
- TEMPERATE: Raise Plant Fibres/FICR(4→5). Reduce Paints/COAT(2→1). Add Plastics/PLAS(1) BOOST for synthetic blends (available in BASIC_TEMPERATE).
- Both: Goods/GOOD(4→3) — textile mills primarily produce fabric (Textiles/TEXT), not finished goods.

### 4.12 Glass Works — Glass Melting, Forming, Annealing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TEMPERATE | Sand/SAND(6), Soda Ash/SASH(2), Quicklime/QLME(2) | Sand/SAND(6) REQ, Soda Ash/SASH(2) REQ, Quicklime/QLME(2) BOOST | Glass/GLAS(8), Packaging/MNSP(8) | Glass/GLAS(8), Packaging/MNSP(6) |
| STEELTOWN | Sand/SAND(4), Soda Ash/SASH(2), Quicklime/QLME(1), Plastics/PLAS(1) | Sand/SAND(4) REQ, Soda Ash/SASH(2) REQ, Quicklime/QLME(1) BOOST, Plastics/PLAS(1) BOOST | Glass/GLAS(6), Packaging/MNSP(4) | no change |
| TROPIC | Sand/SAND(4), Soda Ash/SASH(2), Quicklime/QLME(1), Plastics/PLAS(1) | Sand/SAND(4) REQ, Soda Ash/SASH(2) REQ, Quicklime/QLME(1) BOOST, Plastics/PLAS(1) BOOST | Glass/GLAS(8) | Glass/GLAS(8), Packaging/MNSP(2) |

**Reasoning:**
- Sand/SAND is the main ingredient (70-75% of glass batch). Soda Ash/SASH (soda ash) is flux (12-15%). Quicklime/QLME is stabilizer (10-12%). All correct.
- TEMPERATE: Packaging/MNSP(8) equals the main product — too high. Reduce to 6.
- STEELTOWN: Plastics/PLAS(1) for laminated safety glass (automotive). Good. Glass/GLAS(6) + Packaging/MNSP(4) balanced.
- TROPIC: No Packaging/MNSP output — consider adding Packaging/MNSP(2) for glass containers/bottles.

### 4.13 Printing Plant — Commercial Printing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TEMPERATE | Paper/PAPR(6), Paints/COAT(2) | Paper/PAPR(6) REQ, Paints/COAT(2) BOOST | Goods/GOOD(6), Mail/MAIL(6) | Goods/GOOD(5), Mail/MAIL(5), Recyclables/RCYC(1) SCALE |

**Reasoning:**
- Paper/PAPR dominant — paper is overwhelmingly the main material. Paints/COAT represents inks/printing chemicals.
- Output 12 from input 8 is generous. Reduce Goods/GOOD(6→5), Mail/MAIL(6→5) for balance.
- Mail/MAIL output for newspapers/periodicals is creative and creates mail demand. Good design.
- Recyclables/RCYC(1) SCALE — large print shops produce paper waste, ink cartridges, film waste.

### 4.14 Construction Plant — Prefab Construction & Modular Building

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Cement/CMNT(2), Metal Parts/MPAR(2), Wire Rod/STWR(2), Glass/GLAS(2) | Cement/CMNT(3) REQ, Wire Rod/STWR(2) REQ, Metal Parts/MPAR(2) BOOST, Glass/GLAS(1) BOOST | Goods/GOOD(8) | Goods/GOOD(8), Recyclables/RCYC(1) SCALE |

**Reasoning:**
- Cement/CMNT should be dominant — concrete is the bulk material in construction. Raise to 3.
- Wire Rod/STWR for reinforcement (rebar, mesh) — essential for concrete structures.
- Glass/GLAS(2→1) — windows are a minor component.
- Recyclables/RCYC(1) SCALE — construction sites produce recyclable waste (packaging, offcuts, scrap).
- Note: Nearly identical to Builders Yard — needs differentiation (see below).

### 4.15 Builders Yard — Construction Supply Distribution

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Cement/CMNT(2), Metal Parts/MPAR(2), Wire Rod/STWR(2), Glass/GLAS(2) | Cement/CMNT(2) REQ, Glass/GLAS(2) REQ, Packaging/MNSP(2) BOOST, Metal Parts/MPAR(2) BOOST | Goods/GOOD(8) | no change |

**Reasoning:**
- **Currently identical inputs to Construction Plant** — this is a problem. Two industries in same economy with same cargos creates confusion.
- Differentiate: This is a distributor (retail/hardware store), not a manufacturer. Replace Wire Rod/STWR with Packaging/MNSP (nails, screws, fixings, tools).
- Has `prod_multiplier=[0,0]` — zero base production, acts as distribution hub.

### 4.16 Supply Yard — Engineering & Farm Supply Distribution Hub

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Ammon. Nitrate/NHNO(8), Vehicles/VEHI(8), Petrol/PETR(8), Tyres/TYRE(8) | Vehicles/VEHI(8) REQ, Petrol/PETR(8) REQ, Ammon. Nitrate/NHNO(8) BOOST, Tyres/TYRE(4) BOOST | Eng. Supplies/ENSP(8) | Eng. Supplies/ENSP(6), Farm Supplies/FMSP(4) |
| TROPIC | Vehicles/VEHI(8), Petrol/PETR(8), Explosives/BOOM(8) | Vehicles/VEHI(8) REQ, Petrol/PETR(8) REQ, Explosives/BOOM(8) BOOST | Eng. Supplies/ENSP(8) | Eng. Supplies/ENSP(6), Farm Supplies/FMSP(4) |
| TEMPERATE | Vehicles/VEHI(8), Petrol/PETR(8), Explosives/BOOM(8) | Vehicles/VEHI(8) REQ, Petrol/PETR(8) REQ, Explosives/BOOM(8) BOOST | Eng. Supplies/ENSP(8) | Eng. Supplies/ENSP(6), Farm Supplies/FMSP(4) |

**Reasoning:**
- Distribution hub for heavy equipment and consumables. All-8 ratios mean any single input gives max output — distribution mechanic.
- STEELTOWN: Tyres/TYRE(8→4) — spare tyres are less important than vehicles and fuel.
- **All: Add Farm Supplies/FMSP output** — a supply yard logically distributes to both mining and farming operations. Split Eng. Supplies/ENSP(8) → Eng. Supplies/ENSP(6), Farm Supplies/FMSP(4).

### 4.17 Brick Works — Brick Firing & Forming

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Clay/CLAY(4), Sand/SAND(3), Coal/COAL(2) | Clay/CLAY(4) REQ, Coal/COAL(2) REQ, Sand/SAND(1) BOOST | Building Mat./BDMT(6) | no change |
| TEMPERATE | Clay/CLAY(4), Sand/SAND(3), Coal/COAL(2) | Clay/CLAY(4) REQ, Coal/COAL(2) REQ, Sand/SAND(1) BOOST | Building Mat./BDMT(6) | no change |

**Reasoning:**
- CLAY is the brick. Coal/COAL is kiln fuel. Both required.
- Sand/SAND(3→1) — sand is a minor release agent/additive in brick-making, not 33% of the input. This also differentiates from glass works (which is sand-dominant).
- Output Building Mat./BDMT(6) is appropriate. Consider Limestone/LIME(1) BOOST for lime-sand brick variant.

### 4.18 Cement Plant — Clinker Production & Grinding

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Petrol/PETR(2), Sand/SAND(2), Limestone/LIME(4) | Limestone/LIME(4) REQ, Sand/SAND(2) REQ, Petrol/PETR(2) BOOST | Quicklime/QLME(6), Cement/CMNT(6) | Cement/CMNT(6), Quicklime/QLME(4) |
| TROPIC | Coke/COKE(2), Sand/SAND(2), Limestone/LIME(2), Slag/SLAG(2) | Limestone/LIME(4) REQ, Coke/COKE(2) BOOST, Sand/SAND(1) BOOST, Slag/SLAG(1) BOOST | Building Mat./BDMT(6), Quicklime/QLME(2) | no change |
| TEMPERATE | Cement/CMNT(2), Coke/COKE(2), Sand/SAND(2), Limestone/LIME(2) | **Limestone/LIME(4) REQ, Coke/COKE(2) REQ, Sand/SAND(2) BOOST** | Building Mat./BDMT(6), Quicklime/QLME(2) | no change |

**Reasoning:**
- Limestone/LIME should dominate in ALL economies — limestone is 80%+ of raw material in cement production.
- STEELTOWN: Quicklime/QLME(6) = Cement/CMNT(6) total 12 from 8 input is generous. Reduce Quicklime/QLME(6→4). Cement/CMNT is the main product.
- TROPIC: Raise Limestone/LIME(2→4), reduce Sand/SAND and Slag/SLAG to 1 each (additives, not primary).
- **TEMPERATE: Cement/CMNT as input is wrong** — circular dependency. Remove. Replace with Limestone/LIME(4) REQ, Coke/COKE(2) REQ, Sand/SAND(2) BOOST.

### 4.19 Lime Kiln — Limestone Calcination

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Limestone/LIME(6), Petrol/PETR(2) | Limestone/LIME(6) REQ, Petrol/PETR(2) BOOST | Quicklime/QLME(8) | no change |
| TROPIC | Limestone/LIME(6), Petrol/PETR(2) | Limestone/LIME(6) REQ, Petrol/PETR(2) BOOST | Quicklime/QLME(6), Fertiliser/FERT(2) | no change |
| TEMPERATE | Limestone/LIME(6), Petrol/PETR(2) | Limestone/LIME(6) REQ, Petrol/PETR(2) BOOST | Quicklime/QLME(6) | Quicklime/QLME(6), Fertiliser/FERT(1) |

**Reasoning:**
- Simple and correct process: heat limestone → quicklime + CO2. Limestone/LIME is required, Petrol/PETR is fuel booster.
- STEELTOWN: Clean single output. Good.
- TROPIC: Fertiliser/FERT(2) for agricultural lime (soil pH adjustment). Good thematic addition.
- TEMPERATE: Currently no Fertiliser/FERT output — add Fertiliser/FERT(1) to match tropic (agricultural lime is used in temperate farming too).

### 4.20 Sawmill — Log Cutting into Lumber

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Logs/WOOD(6) | Logs/WOOD(6) REQ | Lumber/WDPR(8) | Lumber/WDPR(7), Biomass/BIOM(1) |
| TEMPERATE | Logs/WOOD(6) | Logs/WOOD(6) REQ | Lumber/WDPR(8) | Lumber/WDPR(7), Biomass/BIOM(1) |

**Reasoning:**
- Simple single-input process — correct for sawmilling.
- Logs/WOOD(6)→Lumber/WDPR(8) output exceeds input, which is generous. Real sawmilling loses 40-50% to sawdust/bark/slabs.
- Add Biomass/BIOM(1) output for sawdust/bark/wood chips — significant real byproduct.
- Reduce Lumber/WDPR(8→7) to make room for Biomass/BIOM.

### 4.21 Paper Mill — Wood Pulping & Papermaking

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Logs/WOOD(4), Clay/CLAY(2), Sulphuric Acid/SUAC(2) | Logs/WOOD(4) REQ, Clay/CLAY(2) BOOST, Sulphuric Acid/SUAC(1) BOOST | Goods/GOOD(4), Packaging/MNSP(7) | Goods/GOOD(4), Packaging/MNSP(6) |
| TEMPERATE | Clay/CLAY(2), Logs/WOOD(4), Sulphur/SULP(2) | Logs/WOOD(4) REQ, Sulphur/SULP(2) BOOST, Clay/CLAY(1) BOOST | Paper/PAPR(6), Packaging/MNSP(8) | Paper/PAPR(6), Packaging/MNSP(5), Recyclables/RCYC(1) SCALE |

**Reasoning:**
- Logs/WOOD is the required input — wood pulp is the main ingredient.
- CLAY for paper coating (kaolin), Sulphuric Acid/SUAC or Sulphur/SULP for chemical pulping (kraft process). Good chemistry.
- TROPIC: Sulphuric Acid/SUAC(2→1) — chemicals used in small quantities vs wood. Packaging/MNSP(7→6).
- TEMPERATE: **Packaging/MNSP(8) is extremely high** — reduce to 5. Clay/CLAY(2→1). Paper/PAPR(6) stays.
- TEMPERATE: Recyclables/RCYC(1) SCALE — large paper mills produce recyclable trim/broke.

### 4.22 Lumber Yard — Wood Treatment & Building Materials

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TROPIC | Lumber/WDPR(4), Glass/GLAS(2), Metal Parts/MPAR(1), Paints/COAT(1) | Lumber/WDPR(4) REQ, Glass/GLAS(1) BOOST, Metal Parts/MPAR(1) BOOST, Paints/COAT(1) BOOST | Building Mat./BDMT(6), Packaging/MNSP(6) | Building Mat./BDMT(6), Packaging/MNSP(5) |
| TEMPERATE | Lumber/WDPR(4), Metal Parts/MPAR(2), Paints/COAT(2) | Lumber/WDPR(4) REQ, Metal Parts/MPAR(1) BOOST, Paints/COAT(1) BOOST | Building Mat./BDMT(6), Packaging/MNSP(6) | Building Mat./BDMT(6), Packaging/MNSP(5) |

**Reasoning:**
- Lumber/WDPR is the primary material — lumber for construction.
- Glass/GLAS for window units, Metal Parts/MPAR for hardware/brackets, Paints/COAT for preservatives/paint — all boosters.
- Both: Reduce minor inputs to 1 each. Glass/GLAS(2→1) in tropic. Metal Parts/MPAR(2→1) and Paints/COAT(2→1) in temperate.
- Both: Packaging/MNSP(6→5) — secondary product shouldn't match primary.

### 4.23 Junk Yard — Scrap Sorting & Processing

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| TEMPERATE | Recyclables/RCYC(6) | Recyclables/RCYC(6) REQ | Scrap Metal/SCMT(3) | Scrap Metal/SCMT(4), Rare Metals/RAMT(1) |
| TROPIC | Recyclables/RCYC(6) | Recyclables/RCYC(6) REQ | Scrap Metal/SCMT(4), Rare Metals/RAMT(1) | no change |
| STEELTOWN | Recyclables/RCYC(6) | Recyclables/RCYC(6) REQ | Scrap Metal/SCMT(3) | Scrap Metal/SCMT(4), Rare Metals/RAMT(1) |

**Reasoning:**
- Simple single-input — correct for scrap sorting (low-tech, labor-intensive).
- TROPIC already has Rare Metals/RAMT(1) — good (copper wire, aluminium cans, brass fittings).
- **STEELTOWN/TEMPERATE: Add Rare Metals/RAMT(1)** — nonferrous metal recovery. Raise Scrap Metal/SCMT(3→4) — industrial-grade sorting is more efficient.

### 4.24 Recycling Plant — Plastics Recycling

| Economy | Current Accept | Rec. Accept | Current Produce | Rec. Produce |
|---------|---------------|-------------|-----------------|--------------|
| STEELTOWN | Recyclables/RCYC(6) | Recyclables/RCYC(6) REQ | Plastics/PLAS(3) | Plastics/PLAS(4) |
| TROPIC | Recyclables/RCYC(6) | Recyclables/RCYC(6) REQ | Plastics/PLAS(3) | Plastics/PLAS(3), Chemicals/RFPR(1) |
| TEMPERATE | Recyclables/RCYC(6) | Recyclables/RCYC(6) REQ | Plastics/PLAS(3) | Plastics/PLAS(3), Chemicals/RFPR(1) |

**Reasoning:**
- Simple single-input — correct for a recycling plant.
- STEELTOWN: Raise Plastics/PLAS(3→4) — industrial-scale recycling with better equipment is more efficient.
- TROPIC/TEMPERATE: Add Chemicals/RFPR(1) output — recycled waxes/lubricants from plastic reprocessing.

---

## RCYC as High-Scale Output — Summary

Industries that should produce Recyclables/RCYC(1) at high scale (large factories generate recyclable packaging, offcuts, defective parts):

| Industry | Economies | Reasoning |
|----------|-----------|-----------|
| Appliance Factory | ST, TR, TEMP | Packaging waste, foam offcuts, defective plastic/metal parts |
| Assembly Plant | TR, TEMP | Packaging waste, stamping offcuts |
| Component Factory | ST | Machining waste, packaging |
| Furniture Factory | TR, TEMP | Packaging, wood/fabric scraps |
| Metal Workshop | TEMP | Metal offcuts, packaging |
| Plastics Plant | TR, TEMP | Plastic offcuts, sprues, defective parts |
| Printing Plant | TEMP | Paper waste, ink containers |
| Construction Plant | ST | Packaging, material offcuts |
| Paper Mill | TEMP | Paper trim/broke |
