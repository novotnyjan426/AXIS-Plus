# AXIS+ Player Instructions

AXIS+ (AXIS Plus - Expandable Industries) is a fork of AXIS / FIRS 4 for OpenTTD. It adds the **Expansion** system -- boost production at your industries by placing expansion buildings nearby.

## How Industries Work

### Production Levels

Primary industries (mines, farms, forests, oil wells...) have three production levels:

| Level | Description |
|---|---|
| **Normal** | Base production, no supplies needed |
| **Enhanced** | Deliver engineering/farming supplies regularly |
| **Crankin' It** | Deliver even more supplies for maximum output |

To maintain Enhanced or Crankin' It production, deliver the required amount of supply crates **at least once every three months** (roughly 93 game days).

### The Expansion System

The Expansion system is AXIS+'s signature feature. It gives you a second, independent way to boost production -- **on top of** the supply boost.

**How it works:**

1. Open the **landscaping toolbar** and click the **Place objects** button
2. Find the **AXIS+ Expansion** category
3. Place expansion buildings on tiles **within approximately 7 tiles** of your industry
4. The industry window shows how many expansion buildings are detected and the current bonus

**Key concepts:**

- Expansion and supplies are **separate multipliers** -- they stack. An industry that is both fully supplied and fully expanded produces significantly more than either boost alone.
- Think of supplies as "better tools" (farming machines, engineering supplies) and expansion as "more capacity" (building a second mine shaft, adding fishing nets, clearing more farmland).
- The scanner checks for **any object tiles** near the industry, not just AXIS+ expansion buildings. Third-party NewGRF objects also count.
- The scan covers approximately 7 tiles from the industry in all directions. Due to technical limitations, the exact range varies slightly depending on the industry's shape and tile layout.
- The scanner updates every ~256 game ticks (periodic tile loop). Changes may take a moment to appear.

**Expansion bonus tiers (default values):**

| Tier | Expansion buildings needed | Production bonus |
|---|---|---|
| None | 0-9 | 100% (no bonus) |
| Low | 10+ | 130% (+30%) |
| Medium | 20+ | 170% (+70%) |
| High | 40+ | 250% (+150%) |

**Economics:**

Expansion buildings cost money to place, but **removing them refunds the full build cost**. This means you can freely rearrange your expansion buildings without penalty -- experiment with placement until you're happy with the layout.

## GRF Parameters

All parameters can be configured in the NewGRF settings before starting a game.

### General

| Parameter | Default | Range | Description |
|---|---|---|---|
| **Economy** | Extreme Classic | (list) | Each economy provides a different combination of cargos and industries. |
| **Allow industries spawning during gameplay** | Off | On/Off | By default, new industries do not spawn randomly. Turn on to allow random spawning based on industry density setting. |
| **Maximum coastal distance of marine industries** | No limit | 0-255 | Maximum distance of fishing grounds, oil rigs, and dredging sites from the coast. 0 = no limit. |

### Supply Boost

These parameters control the supply-based production boost for primary industries (mines, farms, etc.).

| Parameter | Default | Range | Description |
|---|---|---|---|
| **Supply crates for Enhanced** | 16 | 1-10,000 | Number of supply crates needed for Enhanced production level. Port-type industries require 8x this value. |
| **Supply crates for Crankin' It** | 80 | 1-10,000 | Number of supply crates needed for Crankin' It production level. Port-type industries require 8x this value. |
| **Enhanced production level (%)** | 150 | 100-1,000 | Production percentage at Enhanced level. 150 = +50% production. |
| **Crankin' It production level (%)** | 300 | 100-1,000 | Production percentage at Crankin' It level. 300 = +200% production. |

### Expansion Boost

These parameters control the expansion building system.

#### Thresholds

How many expansion building tiles (within ~7 tiles of the industry) are needed to reach each bonus tier.

| Parameter | Default | Range | Description |
|---|---|---|---|
| **Low threshold** | 10 | 1-225 | Expansion buildings needed for Low bonus |
| **Medium threshold** | 20 | 1-225 | Expansion buildings needed for Medium bonus |
| **High threshold** | 40 | 1-225 | Expansion buildings needed for High bonus |

#### Bonus Levels

The production multiplier at each expansion tier (as percentage, 100 = no change).

| Parameter | Default | Range | Description |
|---|---|---|---|
| **Low bonus** | 130% | 100-500% | Production at Low expansion (+30% by default) |
| **Medium bonus** | 170% | 100-500% | Production at Medium expansion (+70% by default) |
| **High bonus** | 250% | 100-500% | Production at High expansion (+150% by default) |

#### Building Cost

| Parameter | Default | Range | Description |
|---|---|---|---|
| **Cost level** | 3 (Default) | 0-6 | Controls expansion building placement cost. Each level doubles the price. Removal always refunds the full cost. |

Cost level breakdown:

| Level | Multiplier | Approximate cost per tile |
|---|---|---|
| 0 - Very Low | 1x | ~63,000 |
| 1 - Low | 2x | ~125,000 |
| 2 - Medium | 4x | ~250,000 |
| 3 - Default | 8x | ~500,000 |
| 4 - High | 16x | ~1,000,000 |
| 5 - Very High | 32x | ~2,000,000 |
| 6 - Extreme | 64x | ~4,000,000 |

*Actual costs depend on game difficulty settings and inflation.*

## Combined Boost Example

With default settings, a coal mine producing 100 units at Normal:

| Supplies | Expansion | Combined multiplier | Production |
|---|---|---|---|
| Normal | None | 1.0x | 100 |
| Enhanced | None | 1.5x | 150 |
| Crankin' It | None | 3.0x | 300 |
| Normal | Low | 1.3x | 130 |
| Normal | High | 2.5x | 250 |
| Enhanced | Low | 1.95x | 195 |
| Enhanced | High | 3.75x | 375 |
| Crankin' It | High | **7.5x** | **750** |

The two systems multiply together: `supply_boost x expansion_boost`.

## Tips

- **Start with supplies.** The supply boost is free (just deliver cargo). Expansion requires investment.
- **Place expansion buildings gradually.** You only need 10 for the first bonus tier. Build more as your profits grow.
- **Rearrange freely.** Removal refunds the full cost, so don't worry about placing buildings in the wrong spot.
- **Check the industry window.** It shows the current expansion building count and bonus percentage, so you can see exactly what's happening.
- **Any objects count.** The scanner detects all object tiles, not just AXIS+ buildings. If you have decorative objects from other NewGRFs near your industries, they count too.

## Known Limitations

- The ~7 tile scan radius is approximate. For industries with unusual layouts, the effective range may vary slightly in different directions.
- The expansion scanner updates periodically (~256 ticks), not instantly. After placing buildings, wait a moment for the count to update.
- Expansion currently applies to primary industries only (mines, farms, forests, oil wells, etc.). Secondary industries (factories, refineries) are planned for a future update.
