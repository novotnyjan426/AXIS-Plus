# Secondary Industry Cargo Audit

Complete audit of all secondary industries across BASIC_TEMPERATE, BASIC_TROPIC, STEELTOWN economies.
For each industry: input classification (REQUIRED/BOOSTER), ratio review, output review, scale bonus candidates.

## Legend
- **REQ** = Required input (essential raw material, production won't work well without it)
- **BOOST** = Booster input (optional, improves efficiency/output)
- **SCALE** = Output gated behind scale level (medium/high expansion)
- Ratios in parentheses: (current → recommended)

---

## Cross-Cutting Issues

### Fix Priority
1. **TYRE misuse**: Remove from Appliance Factory, Engine Plant, Electrical Works, Component Factory (tropic)
2. **Cement Plant TEMPERATE**: Accepts CMNT (circular) — remove
3. **Sulphuric Acid Plant ST/TEMP**: N7__, H2__, NITR, RFPR are chemically wrong for contact process
4. **Pyrite Smelter STEELTOWN**: FECR output — pyrite has no chromium, should be IORE

### Missing Outputs
- Coke Oven TEMPERATE: add CTAR(1)
- Coke Oven STEELTOWN: add H2__(1)
- Sawmill: add BIOM(1) for sawdust/bark
- Junk Yard ST/TEMP: add RAMT(1) for nonferrous metals

### Ratio Patterns
- MNSP/packaging ratios often too high (should be 1-2, not 3-4)
- SALT underused in food processing
- Many industries have flat equal ratios — primary material should dominate
- Several industries have output >> input (slag grinding 13:8, sheet mill 12:9, paper mill 14:8)

---

## FOOD PROCESSING

### Stockyard (slaughterhouse)
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TEMPERATE | LVST(6), MNSP(2) | FOOD(8), BIOM(2) scale | OK |
| TROPIC | LVST(8), SOAP(2) | MEAT(8), BIOM(2) scale | LVST too high |
| STEELTOWN | LVST(6), SOAP(2) | FOOD(8) | OK |

**Recommendations:**
- TROPIC: Add SALT(2) BOOST, reduce LVST to 6. → LVST(6) REQ, SOAP(2) BOOST, SALT(2) BOOST
- TEMPERATE: Add SALT(1) BOOST, reduce MNSP to 1. → LVST(6) REQ, MNSP(1) BOOST, SALT(1) BOOST
- STEELTOWN: Add SALT(1) BOOST, reduce SOAP to 1. → LVST(6) REQ, SOAP(1) BOOST, SALT(1) BOOST

### Dairy
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TEMPERATE | MILK(6), MNSP(2) | FOOD(8), EOIL(2) | OK |
| TROPIC | MILK(6), MNSP(2) | FOOD(8), EOIL(2) | OK |

**Recommendations:**
- Both: Add SALT(1) BOOST for cheesemaking
- Consider BIOM(1) as SCALE bonus (whey)

### Bakery
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TROPIC | BAKE(3), SUGR(2), ENUM(1), EOIL(1), MNSP(1) | FOOD(8) | Excellent design |

**Recommendations:** No changes needed. Consider BIOM(1) SCALE for waste dough.

### Flour Mill
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TROPIC | GRAI(6) | BAKE(6) | Simple, fine |
| STEELTOWN | GRAI(6), MNSP(4) | FOOD(6) | MNSP(4) too high |
| TEMPERATE | GRAI(6), MNSP(4) | FOOD(6), EOIL(4) | MNSP(4) too high, EOIL without oilseed input is wrong |

**Recommendations:**
- STEELTOWN: GRAI(6) REQ, MNSP(2) BOOST
- TEMPERATE: Add OLSD(3) REQ to justify EOIL output, or remove EOIL. → GRAI(6) REQ, OLSD(3) REQ, MNSP(2) BOOST → FOOD(6), EOIL(3)

### Food Processor (Cannery)
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TROPIC | SUGR(6), FRUT(6), MEAT(6), ENUM(2), EOIL(2), MNSP(2) | FOOD(8) | 6 inputs, all 3 primary at equal 6 |
| STEELTOWN | FRUT(4), FISH(4), MNSP(2), SALT(2) | FOOD(8) | Good design |
| TEMPERATE | FRUT(4), FISH(4), EOIL(4), MNSP(2), SALT(2) | FOOD(8) | EOIL(4) too high |

**Recommendations:**
- TROPIC: Rebalance to FRUT(6) REQ, MEAT(4) REQ, SUGR(3) BOOST, MNSP(2) BOOST, ENUM(1) BOOST, EOIL(1) BOOST
- TEMPERATE: Reduce EOIL to 2

### Fruit Packing Plant
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| STEELTOWN | FRUT(6), MNSP(3) | FOOD(8) | MNSP(3) slightly high |
| TROPIC | FRUT(4), BAKE(4), MNSP(2), ACET(2) | FOOD(8) | BAKE thematically odd for fruit packing |

**Recommendations:**
- STEELTOWN: FRUT(6) REQ, MNSP(2) BOOST
- TROPIC: FRUT(5) REQ, BAKE(3) BOOST, MNSP(2) BOOST, ACET(1) BOOST — or remove BAKE

### Fishing Harbour
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TEMPERATE | FISH(6), MNSP(1) | FOOD(8) | Missing SALT |
| TROPIC | FISH(6) | MEAT(8) | Very sparse |

**Recommendations:**
- Both: Add SALT(2) BOOST (fish curing/preservation)
- TEMPERATE: FISH(6) REQ, SALT(2) BOOST, MNSP(1) BOOST. Consider EOIL(1) SCALE (fish oil)

### Meat Packing Plant
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| STEELTOWN | FISH(6), MNSP(3), SALT(2) | FOOD(8) | Name says meat but accepts FISH |
| TROPIC | MEAT(4), MNSP(2), ENUM(2) | FOOD(6), EOIL(4), BIOM(2) | EOIL(4) too high, MEAT(4) low |

**Recommendations:**
- TROPIC: MEAT(5) REQ, MNSP(2) BOOST, SALT(2) BOOST, ENUM(1) BOOST → FOOD(7), EOIL(2), BIOM as SCALE
- STEELTOWN: MNSP(3→2). Consider adding LVST as alternative primary

### Cider Mill
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TROPIC | FRUT(3), SGCN(3), MNSP(1), ENUM(1) | BEER(6), ACET(3), BIOM(2) | ACET(3) slightly high |

**Recommendations:** ACET(3→2). Consider BIOM as SCALE instead of flat output.

### Sugar Refinery
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TROPIC | SGCN(6), PHOS(1), ENUM(1) | SUGR(6), BIOM(2) | Good |
| TEMPERATE | MNSP(3), SGBT(5) | FOOD(6), BIOM(2) | MNSP(3) too high |

**Recommendations:**
- TEMPERATE: SGBT(6) REQ, MNSP(2) BOOST. Add LIME(1) BOOST for carbonatation.

### Edible Oil Refinery
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TROPIC | OLSD(6) | EOIL(4), BIOM(1) | Sparse |
| TEMPERATE | OLSD(4) | EOIL(4), BIOM(1) | OLSD(4) unrealistically efficient |

**Recommendations:**
- Both: OLSD(6) REQ, MNSP(2) BOOST → EOIL(4), BIOM(2)
- TEMPERATE: Fix OLSD to 6 (matching tropic)

### Brewery
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| TROPIC | GRAI(4), SUGR(2), MNSP(1), ENUM(1) | BEER(6), BIOM(2) | Good |
| TEMPERATE | GRAI(4), FRUT(3), MNSP(2) | BEER(6), BIOM(2) | FRUT(3) high for brewery |

**Recommendations:**
- TEMPERATE: FRUT(3→2). Consider adding SALT(1) BOOST for water chemistry.

---

## STEEL / METAL CHAIN

### Blast Furnace
All economies: IORE(3-4) REQ, COKE(3) REQ, LIME(2) BOOST → IRON(6), SLAG(2). **No changes needed.**

### Basic Oxygen Furnace
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| STEELTOWN | IRON(4), FECR(2), QLME(1), O2__(1) | STCB(3), STAL(3), SLAG(2) | Consider adding SCMT |
| TROPIC | IRON(3), SCMT(3), QLME(1), RAMT(1) | STEL(6), SLAG(2) | SCMT(3) high for BOF |
| TEMPERATE | IRON(4), QLME(2), RAMT(2) | STEL(6), SLAG(2) | Missing SCMT |

**Recommendations:**
- STEELTOWN: Add SCMT(1) BOOST. STCB(4), STAL(2), SLAG(2) better reflects alloy is specialty
- TROPIC: IRON(4) REQ, SCMT(2) BOOST, QLME(1) BOOST, RAMT(1) BOOST
- TEMPERATE: Add SCMT(2) BOOST → IRON(4) REQ, SCMT(2) BOOST, QLME(1) BOOST, RAMT(1) BOOST

### Electric Arc Furnace
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| STEELTOWN | SCMT(4), FECR(2), QLME(1), O2__(1) | STCB(4), STAL(2), SLAG(2) | Good |
| TEMPERATE | SCMT(4), QLME(2) | STEL(6), SLAG(2) | Only 2 inputs, thin |

**Recommendations:**
- TEMPERATE: Add COAL(2) BOOST for carbon injection → SCMT(4) REQ, QLME(2) BOOST, COAL(2) BOOST

### Iron Works (Forge/Foundry)
All economies good. Minor: STEELTOWN could add COKE(1) BOOST for cupola fuel.

### Sheet & Pipe Mill
| Economy | Current Accept | Current Produce | Issues |
|---------|---------------|-----------------|--------|
| STEELTOWN | STCB(4), ZINC(2), ACID(2) | STSH(8) | Good |
| TEMPERATE | STEL(4), ZINC(3), ACID(2) | MPAR(6), BDMT(6) | Output 12 from input 9 |

**Recommendations:**
- TEMPERATE: Reduce to MPAR(4), BDMT(4) for output total of 8

### Wire & Section Mill
STEELTOWN only. Good design. No changes needed.

### Alumina Refinery
STEELTOWN: AORE(6) REQ, LYE_(2) REQ → ALO_(8). Good. No changes.

### Aluminium Plant
| Economy | Current | Issues |
|---------|---------|--------|
| STEELTOWN | ALO_(4), SCMT(2), COKE(2) → ALUM(7), SLAG(1) | Good |
| TEMPERATE | AORE(4), SCMT(4), COKE(2), ACID(2) → ALUM(7), SLAG(1) | SCMT(4) too high |

**Recommendations:** TEMPERATE: AORE(5) REQ, SCMT(2) BOOST, COKE(2) BOOST, ACID(1) BOOST

### Copper Concentrator
TROPIC: Good. Consider COCO(7), RAMT(2) instead of COCO(6), RAMT(3).

### Copper Refinery
All economies good. TEMPERATE: add SULP(1) output (copper smelting produces SO2).

### Pyrite Smelter
| Economy | Current | Issues |
|---------|---------|--------|
| STEELTOWN | PORE(6), COKE(1), SOAP(1) → ZINC(2), COCO(3), SLAG(1), FECR(2) | **FECR wrong** — pyrite has no chromium |
| TEMPERATE | PORE(6), COKE(2), ACID(2) → ZINC(4), RAMT(3) | Output 7 from input 10 low |

**Recommendations:**
- STEELTOWN: Replace FECR(2) with IORE(2) — pyrite calcine is iron oxide
- TEMPERATE: ZINC(5), RAMT(3) or add SULP(2) → ZINC(4), RAMT(2), SULP(2)

### Slag Grinding Plant
| Economy | Current | Issues |
|---------|---------|--------|
| STEELTOWN | SLAG(8) → CMNT(8) | Single input is dull |
| TEMPERATE | SLAG(8) → CMNT(8), FERT(5) | Output 13 from input 8 is very generous |

**Recommendations:**
- Both: Add QLME(2) or SAND(2) BOOST as activator, reduce SLAG to 6
- TEMPERATE: CMNT(6), FERT(3) — max output 9

### Coke Oven
| Economy | Current Produce | Issues |
|---------|-----------------|--------|
| STEELTOWN | COKE(6), CTAR(1), SULP(1) | Missing H2__(1) from coke oven gas |
| TROPIC | COKE(6), SULP(2) | Fine |
| TEMPERATE | COKE(6), SULP(2) | **Missing CTAR(1)** — cargo exists in economy |

**Recommendations:**
- STEELTOWN: COKE(5), CTAR(1), SULP(1), H2__(1) — adds ammonia plant feedstock
- TEMPERATE: COKE(6), CTAR(1), SULP(1) — harmonize with Steeltown

---

## CHEMICAL CHAIN

### Oil Refinery
- STEELTOWN: Good. No changes.
- TROPIC: Good. No changes.
- TEMPERATE: CTAR(4→2), add SULP(2)

### Biorefinery
- STEELTOWN: Good.
- TROPIC: All inputs at 6 is flat. BIOM(6) REQ, OLSD(4) BOOST, GRAI(4) BOOST
- TEMPERATE: **PLAS(3) output unrealistic**. Drop or gate behind SCALE.

### Chemical Plant (TROPIC only)
Add SUAC(2) BOOST for supply chain link. → SALT(2) REQ, NITR(2) REQ, RFPR(2) REQ, SUAC(2) BOOST

### Chlor-Alkali Plant
Add POWR(2) BOOST in both economies (electrolysis is extremely energy-intensive).

### Sulphuric Acid Plant
- **STEELTOWN: WRONG** — SULP(6) REQ, O2__(2) BOOST → ACID(8). Remove N7__ and H2__.
- **TEMPERATE: WRONG** — Simplify to SULP(8) REQ → ACID(8). Remove NITR and RFPR.
- TROPIC: Good as-is.

### Phosphoric Acid Plant (TROPIC only)
Good. Consider PHOS(3), SUAC(5) for more realistic acid consumption.

### Ammonia Plant
- STEELTOWN: Swap N7__(4) and H2__(2) ratios — hydrogen is the expensive input
- TEMPERATE: Drop BIOM(2), keep 3 inputs: NITR(4) REQ, RFPR(2) REQ, ACID(2) BOOST

### Fertiliser Plant
- STEELTOWN: Good.
- TROPIC: Add NITR(3) REQ for NPK completeness. → PHAC(3) REQ, NITR(3) REQ, BIOM(1) BOOST, SLAG(1) BOOST

### Ethylene Cracker
- STEELTOWN: Good.
- TEMPERATE: No C2H4 output (not in economy) — functionally a thermal cracker. Outputs fine.

### Fischer-Tropsch Plant
- STEELTOWN: Add O2__(2) BOOST → COAL(6) REQ, O2__(2) BOOST
- TEMPERATE: Good.

### Polyethylene Plant: All economies fine.
### Polypropylene Plant: STEELTOWN fine.
### Plastics Plant: All economies fine.

### Paint Factory
- STEELTOWN: Drop MNSP (output-as-input loop is awkward). 4 inputs is enough.
- TROPIC/TEMPERATE: Fine.

### Solvay Plant: All economies fine. Textbook Solvay process.

### Carbon Black Plant: STEELTOWN fine. Optional: add RFPR(2) as secondary feedstock.

### Civil Explosives: Both economies good.

### Cleaning Products Factory
- STEELTOWN: Drop SALT (redundant with SASH). → LYE_(3) REQ, SASH(3) REQ, NH3_(1) BOOST, MNSP(1) BOOST
- TROPIC: GOOD(6→4), otherwise fine.

---

## MANUFACTURING

### Appliance Factory
- All: **Remove TYRE** (thematically wrong for appliances)
- STEELTOWN: Drop STAL, keep STSH(4) REQ, POWR(2) REQ, GLAS(1) BOOST, PPAR(1) BOOST
- TROPIC: MPAR(4) REQ, PLAS(2) REQ, GLAS(2) BOOST (no TYRE)
- TEMPERATE: MPAR(4) REQ, POWR(2) REQ, GLAS(2) BOOST, PLAS(2) BOOST

### Assembly Plant
- All: Reduce TYRE ratio (currently 4 in ST, too high)
- STEELTOWN: VBOD(3) REQ, VENG(3) REQ, VPTS(2) REQ, TYRE(2) BOOST
- TROPIC: STEL(4) REQ, VPTS(2) REQ, GLAS(1) BOOST, TYRE(1) BOOST, COAT(1) BOOST
- TEMPERATE: STEL(4) REQ, VPTS(3) REQ, MPAR(2) BOOST, GLAS(1) BOOST, TYRE(2) BOOST, COAT(1) BOOST

### Body Plant (STEELTOWN)
Drop GLAS(2) (glass installed at assembly, not body plant). Add ZINC(1) BOOST.
→ STSH(5) REQ, COAT(2) REQ, ZINC(1) BOOST → VBOD(7), SCMT(1)

### Component Factory
- All: Remove TYRE from TROPIC variant
- STEELTOWN: STAL(3) REQ, MPAR(2) REQ, PPAR(2) BOOST, POWR(1) BOOST
- TROPIC: MPAR(3) REQ, PLAS(2) REQ, TEXT(2) BOOST, COAT(1) BOOST
- TEMPERATE: MPAR(3) REQ, POWR(2) REQ, PLAS(2) BOOST, TEXT(1) BOOST

### Engine Plant (STEELTOWN)
**Remove TYRE(2)** — engines have nothing to do with tyres.
→ ALUM(3) REQ, MPAR(3) REQ, RFPR(1) BOOST, STAL(1) BOOST

### Electrical Works
- All: **Remove TYRE** from TEMPERATE variant
- STEELTOWN: COPR(3) REQ, STAL(2) REQ, STWR(1) BOOST, PPAR(1) BOOST, RFPR(1) BOOST
- TROPIC: COPR(3) REQ, PLAS(2) REQ, RAMT(1) BOOST, SUAC(1) BOOST
- TEMPERATE: COPR(3) REQ, PLAS(2) REQ, RAMT(2) BOOST (remove TYRE)

### Tyre Plant
- STEELTOWN: RUBR(4) REQ, CBLK(2) REQ, SULP(1) BOOST, STWR(1) BOOST (rubber should dominate)
- TROPIC: RUBR(4) REQ, SULP(2) REQ, MPAR(1) BOOST → TYRE(8), PLAS(2) (reduce from 4)
- TEMPERATE: Same → TYRE(8), GOOD(2) (reduce from 4)

### Machine Shop
- All: Remove/reduce GLAS
- STEELTOWN: VENG(3) REQ, VPTS(2) REQ, POWR(2) BOOST, MPAR(1) BOOST → ENSP(3), FMSP(3), GOOD(2)
- TROPIC: STEL(4) REQ, VPTS(2) REQ, TYRE(1) BOOST (drop GLAS)
- TEMPERATE: VPTS(3) REQ, POWR(2) REQ, MPAR(2) BOOST, TYRE(1) BOOST (drop GLAS)

### Metal Workshop
- STEELTOWN: STSH(3) REQ, COAT(2) REQ, ZINC(1) BOOST, STWR(2) BOOST
- TROPIC: STEL(4) REQ, COPR(2) BOOST, RAMT(1) BOOST, SOAP(1) BOOST
- TEMPERATE: STEL(6) REQ, ALUM(4) REQ, COAT(2) BOOST

### Furniture Factory
- Both: WDPR(4) REQ, TEXT(2) REQ, MPAR(1) BOOST, GLAS(1) BOOST, COAT(1) BOOST

### Textile Mill
- TROPIC: Good. Consider GOOD(4→3).
- TEMPERATE: FICR(5) REQ, COAT(1) BOOST. Consider adding PLAS(1) BOOST.

### Glass Works
- TEMPERATE: MNSP(8→6)
- STEELTOWN: Good.
- TROPIC: Consider adding MNSP(2) output.

### Printing Plant (TEMPERATE)
Good. Consider GOOD(6→5), MAIL(6→5) for balance.

### Construction Plant (STEELTOWN)
CMNT(3) REQ, STWR(2) REQ, MPAR(2) BOOST, GLAS(1) BOOST

### Builders Yard (STEELTOWN)
Differentiate from Construction Plant: CMNT(2) REQ, GLAS(2) REQ, MNSP(2) BOOST, MPAR(2) BOOST

### Supply Yard
- All: Consider adding FMSP output alongside ENSP
- STEELTOWN: Reduce TYRE(8→4)

### Brick Works
- Both: SAND(3→1) — sand is minor additive in brick-making
- CLAY(4) REQ, COAL(2) REQ, SAND(1) BOOST

### Cement Plant
- STEELTOWN: QLME(6→4), CMNT(6) stays
- TROPIC: Raise LIME(2→4) REQ, reduce SAND/SLAG to 1 each
- **TEMPERATE: Remove CMNT input (circular)**. → LIME(4) REQ, COKE(2) REQ, SAND(2) BOOST

### Lime Kiln
All economies good. TEMPERATE: consider adding FERT(1) output like TROPIC.

### Sawmill
Both: WOOD(6) REQ → WDPR(7), BIOM(1) — add sawdust/bark byproduct

### Paper Mill
- TROPIC: SUAC(2→1), MNSP(7→6)
- TEMPERATE: CLAY(2→1), **MNSP(8→5)** — extremely high

### Lumber Yard
- Both: Reduce GLAS/MPAR/COAT to 1 each, MNSP(6→5)

### Junk Yard
- STEELTOWN/TEMPERATE: Add RAMT(1) output, raise SCMT(3→4)

### Recycling Plant
- STEELTOWN: Raise PLAS(3→4) for industrial efficiency
- TROPIC/TEMPERATE: Consider RFPR(1) secondary output
