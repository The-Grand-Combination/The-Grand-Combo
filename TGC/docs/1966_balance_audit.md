# 1966 balance audit

**Normative diagnostic framework**

This tool is a **normative diagnostic balance auditor** for gameplay progression across the configured tech/invention timeline.

- Script: `TGC/tools/audit_1966_balance.py`
- Rules: `TGC/tools/1966_balance_rules.json`
- Nature: **non-blocking** diagnostic (`exit 0`), intended to identify implausible or internally inconsistent gameplay progression and to focus balancing work where historical and mechanical pressure is highest.

## Core methodological principle

This audit is **normative, not adaptive**.

Its purpose is to express what unit progression is considered historically plausible, mechanically coherent, and diagnostically useful across the extended campaign arc to 1966. The rules are not meant to mirror current gameplay values, and they must not be widened or softened merely to reduce the number of warnings produced by current files.

Therefore:

- `final_range`, `milestone_ranges`, and delta caps are intended to describe plausible progression envelopes, not to fit existing unit/tech/invention values.
- A warning is not evidence that the audit is too strict. A warning is desirable when current gameplay data exceeds a plausible envelope.
- Reducing warning counts is not, by itself, a success condition. It is only acceptable when it follows from a genuine improvement in the audit’s normative accuracy or from a genuine gameplay correction.
- If current gameplay values fall outside plausible envelopes, the correct outcome is to keep the warning and investigate the gameplay files, unless the rule itself is shown to be historically or internally wrong.

The audit should therefore be used to distinguish three different cases:

1. **Rule/model issue**: the audit rule is internally inconsistent, historically unsound, or too imprecise to be diagnostically useful.
2. **Correct warning**: the rule is sound, and the warning identifies a genuine gameplay progression problem.
3. **False warning**: the warning is caused by a malformed rule, bad applicability logic, or weak evidence being treated too aggressively.

The audit is valuable only if these cases remain distinguishable.

## Scope

The audit covers the broad monitored unit roster and aims at full relevant-stat coverage in `TGC/units/*.txt`.

Current monitored units (from rules):

- `aircraftcarrier`
- `artillery`
- `battleship`
- `cavalry`
- `clipper_transport`
- `commerce_raider`
- `cruiser`
- `cuirassier`
- `dragoon`
- `dreadnought`
- `engineer`
- `frigate`
- `guard`
- `hussar`
- `infantry`
- `ironclad`
- `irregular`
- `manowar`
- `monitor`
- `plane`
- `steam_transport`
- `submarine`
- `tank`

Many monitored unit names should be read as **umbrella categories** rather than as perfectly literal one-to-one historical unit labels. This is especially true in the extended late timeline. The audit should therefore judge them by **role continuity, historical plausibility, and bounded progression**, not by an overly literal assumption that the unit label must retain the exact same narrow meaning from 1836 to 1966.

Coverage tiers (rules-driven):

- `core`: high-signal units with strong diagnostic value and primary balancing importance
- `secondary`: useful but less central units
- `low_signal`: units covered for completeness, but currently with weak or sparse timed-delta evidence

Stat tiers (rules-driven):

- `primary`: balancing-critical combat/economic throughput stats (includes `maximum_speed`)
- `secondary`: useful tactical/support stats
- `structural`: unit-structure/support stats with often weaker timed-delta evidence

How tiers interact:

- unit tiers prioritize *where* to look first
- stat tiers prioritize *what* to look at first
- signal quality (`strong_signal` / `limited_signal` / `formal_coverage_only`) prioritizes *how much confidence* can be assigned to the dating evidence behind a diagnostic

These tiers are prioritization tools only. They do **not** change the underlying normative meaning of rules, and they must not be used to justify permissive calibration.

## Unified timeline model

The model uses a **single unified timeline**:

- `baseline_raw` is always the technical starting point (value read from the unit file)
- `baseline_raw` is input evidence and is **not** checked against `final_range`
- all known-year deltas are applied cumulatively up to each milestone year (`year <= milestone`)
- known-year deltas may come either from unit-specific effect blocks or from applicable global base-scope effect blocks (currently `army_base` for land units and `navy_base` for naval units)
- unknown-year deltas stay out of milestone sums and are reported separately
- source provenance is preserved in reporting so globally scoped effects can be distinguished from unit-specific effects
- milestones remain configurable and reusable, but are no longer tied to a special 1936 logic branch
- tiered coverage/watchlists are used to keep the final report practical without changing rule strictness
- the audit expands toward full per-unit stat coverage for all relevant stats detected in unit files
- current milestone grid spans the full campaign arc: `1836, 1850, 1870, 1900, 1910, 1919, 1929, 1936, 1945, 1955, 1966`

## Conceptual model

Per monitored unit stat, rules can define:

- `final_range`: normative envelope for the final estimated value (`estimated_final`)
- `max_single_delta`: largest acceptable single effect delta
- `max_cumulative_positive_delta` / `max_cumulative_negative_delta`
- `milestone_ranges`: per-year guardrails at configured milestone years

`estimated_final` and milestone estimates are built from `baseline_raw` plus all applicable dated deltas for that unit/stat, including both unit-specific effects and applicable global base-scope effects.

Per monitored unit, rules can also define:

- `historical_relevance_start_year`: first milestone year where historical milestone-range checks are meaningful for that unit

The audit distinguishes:

- **covered stat**: stat exists in the unit file and is present in that unit’s `monitored_stats` rules
- **strong-signal stat**: covered stat with meaningful readable deltas and usable placement in scanned tech/invention data

A stat can be covered but still low-signal. This is expected in broad coverage mode. However, low signal does **not** remove the need for normative discipline. It only limits the precision and confidence with which the audit can justify a particular timed progression.

When no readable deltas exist for a covered stat in scanned files, coverage is reported as formal-only. This means the diagnostic basis is weak, not that the rule may be adapted to fit current gameplay values.

## Evidence basis of milestone ranges

To avoid treating all ranges as equally well-supported, rules should be interpreted in two classes:

- **Evidence-based ranges**: stats with readable and reasonably dated deltas in scanned tech/invention files, especially core combat stats.
- **Heuristic guardrail ranges**: stats with weak or missing timed signal, where ranges are intentionally broad and prudent diagnostic boundaries rather than claims of precise historical truth.

This distinction must be applied carefully.

Heuristic guardrail ranges are acceptable only when they improve diagnostic value **without** becoming covert adaptive tolerances. They must remain bounded, historically defensible in broad terms, and cautious about false precision. They are not a license to widen ranges until warnings disappear.

Practical guidance:

- pre-1936 milestones should **not** be auto-interpolated uniformly when observed progression is step-like
- use anchor-style ranges around known jumps for core stats (`attack`, `defence`, `supply_consumption`, selected naval combat stats)
- keep structural low-signal stats (`build_time`, `default_organisation`, `max_strength`, `min_port_level`, etc.) broad and prudent to avoid false precision, but never so broad that they cease to detect genuine anomalies

## Artillery stepped-envelope philosophy

Artillery is intentionally treated as a **step-escalation** profile rather than a smooth curve.

Normative interpretation:

- **1836–1900**: conservative baseline band with modest improvement in `attack`/`defence` and manageable supply growth
- **1910–1939**: major modernization discontinuity driven by industrialized heavy guns and doctrinal/logistical improvement
- **1939–1955**: second major jump driven by self-propelled systems, improved fire direction, and heavier explosive or rocket layers, especially visible in supply burden and late combat output
- **1955–1966**: continued improvement is plausible, but late growth should increasingly flatten rather than keep accelerating
- **1966 endpoint**: high late-era cap, but still bounded so warnings remain meaningful when progression overshoots plausible late-step bands

Because of this profile, artillery milestone envelopes should be **piecewise stepped bands**, not linear trend bands. The purpose is to accept historically plausible jumps while still flagging implausible spikes, runaway cumulative growth, or suspiciously smooth progression.

### Artillery `support` interpretation note

`support` is an abstract gameplay stat, not a direct historical metric. Its ranges should therefore be calibrated by inference from doctrine and material progression, with particular care not to turn abstraction into arbitrary permissiveness.

Normative reading:

- pre-1900: limited but real uplift from early industrial artillery integration; growth should stay modest
- 1910–1939: larger jump is plausible due to indirect fire doctrine, coordination, and heavier field integration
- 1939–1955: another jump is plausible through self-propelled artillery, improved fire direction, and rocket artillery integration
- post-1945: `support` can continue rising, but usually less explosively than wartime discontinuities; late gains should remain bounded so warnings still surface if support inflation becomes runaway

In short, artillery `support` envelopes should be **step-shaped and bounded**, not flat and not permissively linearized.

## Tank normative progression note

`tank` should be interpreted as a **late-modern armored umbrella category**, covering a broad family of historically evolving armored combat formations rather than a single narrow vehicle concept. Its role-space may include early tanks, interwar armored formations, wartime armor, and early postwar main-battle-tank logic.

Normative reading:

- **1919–1929**: early armored phase; tanks are historically meaningful, but still limited by doctrine, reliability, coordination, and industrial maturity. Early envelopes should allow emergence, not full modern dominance.
- **1929–1945**: primary growth phase; this is the major discontinuity period for armored combat. Strong rises in combat performance are plausible, and logistical burden should rise meaningfully as capability expands.
- **1945–1955**: mature high-capability phase; tanks remain very strong, but progression should begin to flatten relative to the earlier explosive period.
- **1955–1966**: late consolidation; further improvement is plausible, especially in operational effectiveness and survivability, but late envelopes must remain visibly bounded and should not imply unlimited upward scaling.

Interpretation guardrails:

- tank progression should be **step-shaped**, not mechanically linear from first availability to 1966
- strong late-era capability is appropriate, but tanks should retain clear trade-offs, especially in cost and supply burden
- warnings on tank combat stats should often be read as checks against **runaway escalation**, **over-early maturity**, or **erosion of combined-arms balance**
- the existence of a strong late tank profile must not, by itself, justify permissive unlimited growth in `attack`, `defence`, or mobility

## Plane normative progression note

`plane` should be interpreted as a **broad late-modern air-power umbrella category**, not as a literal single aircraft type. In gameplay terms it may compress a wide historical spectrum of military aviation development into one monitored unit class.

Normative reading:

- **1910–1919**: early aviation phase; capability exists, but envelopes should remain low and cautious relative to later decades
- **1919–1939**: major interwar development; meaningful growth is plausible as doctrine, airframe design, engines, and coordination improve
- **1939–1945**: primary wartime discontinuity; this is the period where very large capability jumps are most plausible
- **1945–1955**: strong late-modern expansion remains plausible, but should increasingly show boundedness rather than endless wartime-style acceleration
- **1955–1966**: mature late endpoint; high capability is expected, but abstraction risk is also highest, so rules should resist inflated “super-unit” drift

Interpretation guardrails:

- plane progression should tolerate **strong discontinuities**, especially around major wartime modernization
- because `plane` is represented through abstracted gameplay stats, rules should avoid false precision while still enforcing bounded late-era behavior
- warnings on planes should often be read as checks against **overscaling**, **premature late-modern performance**, or **excessive compression of role trade-offs**
- strong late aviation growth is historically plausible; unbounded dominance is not

## Infantry / Guard / Engineer normative doctrine note

This trio should be interpreted as distinct but interacting archetypes:

- `infantry`: backbone, general-purpose line unit; reference envelope for sustained mass combat
- `guard`: evolving umbrella for elite land combat formations; initially prestige or guard infantry, later selected assault-capable or high-readiness elite infantry, but **not** a pure commando or special-forces category
- `engineer`: specialist support/fortification/siege/combat-engineering umbrella category; may improve mobility, survivability, and operational capability, but must not drift into quasi-standard offensive line infantry

Normative implication: envelope design should be **step-shaped and bounded**, not mechanically linear from 1836 to 1966.

### Infantry (backbone line unit)

Normative reading:

- **1836–1900**: stable baseline doctrine; modest `attack`/`defence` growth, low-to-moderate `supply_consumption`, limited `support`/`siege`, and conservative mobility (`maximum_speed` is mostly structural, not breakthrough-oriented)
- **1910–1939**: first major modernization step through industrial firepower and command/logistics improvement; meaningful uplift in `attack` and `defence`, with corresponding supply burden
- **1939–1955**: large wartime discontinuity; envelopes should tolerate stronger combat capability but should not allow permissive post-step collapses in floors, especially for `attack`, `defence`, and `supply_consumption`
- **1955–1966**: consolidation and bounded late modernization; maintain a high but capped line-combat profile, with no unlimited escalation

### Guard (elite land combat umbrella)

`guard` should not be read as a static nineteenth-century label frozen in time. It is better interpreted as an **evolving umbrella for elite land combat formations** across the campaign arc.

Normative reading:

- **1836–1900**: prestige guard infantry, selected line formations, or elite troops with discipline and status premium; quality differential is acceptable, but they are still fundamentally elite line troops
- **1900–1939**: selected high-quality infantry, often with stronger assault or readiness profile; role premium may widen somewhat, but they remain grounded in elite land combat rather than specialist commando logic
- **1939–1955**: strongest period for selected assault-capable or high-readiness elite formations; `guard` may absorb part of the historical role-space associated with especially capable elite ground troops, but it should still remain a bounded elite-combat umbrella rather than a pure special-forces unit
- **1955–1966**: late-era elite ground umbrella; higher readiness, quality, and modernization are plausible, but the category should still represent elite terrestrial combat formations, not small-scale special-operations forces in the narrow modern sense

Interpretation guardrails:

- guard may sit above infantry in combat output, but bounded ceilings are required to prevent runaway divergence
- elite status does **not** automatically justify major speed inflation or universal superiority in every stat
- guard should not evolve into a “joker” super-unit that implicitly absorbs all commandos, special forces, airborne, marine, and shock-troop roles at once
- where late-era reinterpretation is needed, it should remain within the idea of **elite land combat formations**, not pure modern special operations forces

### Engineer (specialist combat-engineering umbrella)

`engineer` should be interpreted as a **broad combat-engineering umbrella**, not as a narrow static nineteenth-century sapper concept. This may include changing emphases over time such as fortification work, bridging, demolitions, mobility support, obstacle clearing, and practical battlefield engineering.

Normative reading:

- **1836–1900**: specialist identity dominates; `attack` should remain secondary, while `defence`, `support`, and `siege` are the primary normative signals
- **1910–1939**: operational relevance rises through fortifications, bridging, and mobility support; `defence` and operational stats may step upward, with moderate mobility gains
- **1939–1955**: major capability expansion in combat engineering; `support`/`siege` may rise sharply and `maximum_speed` may improve, but offensive `attack` must remain bounded as non-primary
- **1955–1966**: mature specialist role; better survivability and operational throughput are plausible, yet envelopes must still prevent drift toward quasi-infantry offensive parity

Interpretation guardrails for warnings:

- warnings on guard vs infantry should be read as **relative-boundedness checks**: elite premium is allowed, unlimited separation is not
- warnings on engineer combat stats should be read as **role-integrity checks**: specialist evolution is allowed, offensive convergence to standard line infantry is not
- where historical jumps are expected, milestone floors and ceilings should move in discrete steps rather than smooth linear ramps

## Normative interpretation of `maximum_speed`

In Victoria, `maximum_speed` is displayed in **kph**. However, for audit purposes it should not be treated as a literal one-to-one historical top-speed metric.

Normatively, `maximum_speed` should be interpreted as a **hybrid gameplay mobility indicator** that may reflect several factors at once, depending on unit type:

- actual movement speed
- operational mobility
- transport efficiency
- readiness and responsiveness
- ability to convert technology and doctrine into practical movement performance

This means the audit should respect the in-game `kph` presentation while avoiding overly literal real-world conversion logic.

### General principles

- `maximum_speed` should remain **role-shaped**, not uniformly progressive across all units
- speed growth should usually happen through **historical discontinuities** rather than smooth linear ramps
- late-era improvement is often plausible, but late unbounded inflation is not
- where unit identity is fundamentally non-mobile or only moderately mobile, speed should stay constrained even when other stats rise

### Land-unit speed

For land units, speed progression should usually be conservative and role-sensitive.

Normative reading:

- **infantry**: mild growth or long plateau; modernization may improve practical mobility somewhat, but infantry should not show aggressive speed escalation
- **guard**: similar broad logic to infantry; elite status does not automatically justify major speed divergence, although modest readiness or operational mobility premium may be plausible in some late-era interpretations
- **engineer**: moderate growth may be plausible through bridging, mobility support, and operational modernization, but engineers should not become pseudo-fast assault infantry
- **artillery**: speed should remain cautious, especially where the conceptual role is still constrained by towing, deployment burden, or heavy-equipment handling
- **tank**: strongest land-unit mobility growth is plausible here, especially from interwar to mid-century modernization, but even tank speed should remain bounded and era-appropriate

Interpretation guardrails:

- land-unit speed should not rise in near-parallel across all categories
- modernization may justify some broad upward drift, but role distinctions must remain visible
- if many land units converge toward similar high late speeds, the audit should treat that as a potential loss of role integrity
- warnings on land `maximum_speed` should often be read as checks against **linearized modernization**, **over-early mobility**, or **flattened unit differentiation**

### Naval-unit speed

For naval units, speed progression may show stronger long-run change than on land, but it should still remain class-sensitive and historically shaped.

Normative reading:

- sail-era units should remain clearly slow relative to later steam or oil-driven ships
- major propulsion transitions should produce real discontinuities
- transports should not automatically converge toward front-line combat-ship speed profiles
- capital ships may gain speed over time, but should still reflect trade-offs of size, armor, endurance, and role
- late-modern classes may be relatively fast, but not all classes should flatten into the same upper-speed band

Interpretation guardrails:

- naval `maximum_speed` should reflect technological transition and role differentiation together
- warnings on naval speed should often be read as checks against **role compression**, **suspiciously smooth progressions**, or **implausible late-class convergence**
- especially strong scrutiny is appropriate where obsolete ship classes appear too fast too late, or where support/transport classes crowd combat-class speed envelopes without a clear historical reason

## Historical applicability for milestone checks

Milestone diagnostics are most useful when evaluated only in years where the unit is historically meaningful or available.

Why this matters:

- late-era units such as `tank`, `submarine`, `plane`, and `aircraftcarrier` can look wrong in early milestones simply because they are being evaluated before historical applicability
- that creates noisy false warnings and reduces diagnostic clarity

Behavior:

- if a milestone year is **before** a unit’s `historical_relevance_start_year`, milestone-range pass/fail evaluation for that unit/stat/year is skipped
- the script emits an `INFO` diagnostic showing which pre-applicability milestone years were skipped
- `final_range`, economic checks, timeline coverage diagnostics, and non-blocking behavior remain unchanged

This rule exists to prevent false diagnostics. It must not be used to hide progression problems in years where the unit is historically relevant.

### Carrier-specific note

`aircraftcarrier` is intentionally modeled as a two-stage pre-supercarrier arc:

- **1919 early stage** via `converted_carriers` (`oil_driven_ships`): weak converted/interwar carrier entry point
- **1929 maturation stage** via `fleet_aircraft_carriers` (`mobile_capital_ships`): main fleet-carrier maturation bump

The late layer remains on top (`welded_hulls`, then `supercarriers`, `advanced_supercarriers`, `monstrous_supercarriers`).

Normative milestone interpretation for carrier stats should therefore expect:

- a low 1919 converted-carrier baseline
- a stronger 1929 fleet-carrier maturation
- a major 1939+ escalation
- bounded late growth rather than endless upward drift

### Late carrier calibration note (hull vs gun_power)

- `hull`: post-1945 growth may remain strong for carriers because of size, aviation facilities, and operational endurance, but should gradually flatten by the late endpoint rather than rise endlessly
- `gun_power`: this is an abstract combat proxy, not literal carrier main-battery gunnery; late increases may be partially justified by air-group lethality and integrated strike capability, but should be treated more cautiously than hull growth

Therefore, carrier `gun_power` envelopes should be calibrated with stricter mid-century scrutiny than `hull`, while `hull` envelopes may allow clearer but still bounded late-era expansion.

Interpretation rule:

- `milestone_ranges` are historical guardrails only for years at or after `historical_relevance_start_year`

## Economic checks

Economic checks per unit can define:

- `estimated_build_cost_range`
- `estimated_upkeep_cost_range`
- `key_goods_expectations`

These checks are normative as well. Their function is not to reproduce whatever cost structure the current mod happens to have, but to detect implausible or internally inconsistent economic profiles.

## Data extraction and dating

The auditor scans configured tech and invention files and reads unit stat deltas from effect blocks.

Extraction scope includes:

- unit-specific effect blocks (for example `tank = { attack = 1 defence = 1 }`)
- applicable global base-scope effect blocks that target whole domains rather than named units
  - `army_base` for land units
  - `navy_base` for naval units

Global base-scope effects are included only when they are relevant to the monitored unit domain and monitored stat catalog. They are folded into milestone and final-value estimation, but their source remains explicitly distinguishable in the report.

Year placement:

- `direct`: `year = XXXX` found directly in a block
- `inferred_strong`: inferred from clear dated prerequisites, especially hard `limit = { ... }` anchors tied to direct-year tech/invention gates
- `inferred_weak`: inferred from multiple or weaker propagated references

Confidence refinement note:

- when an invention has multiple mixed references, such as chance modifiers, neighbor checks, or war context, the auditor prioritizes hard `limit` anchors for confidence classification
- this improves attribution for clearly tech-anchored chains without globally relabeling all inferred years as strong-confidence

Coverage metrics:

- `time_coverage`: share of absolute delta with any known year
- `high_conf_coverage`: share of absolute delta with high-confidence dating (`direct + inferred_strong`)
- `signal assignments / touched_stats`: per-unit signal-strength summary to distinguish high-value monitored units from baseline-only or low-evidence coverage

Reporting provenance:
- the report preserves whether a timed delta came from a unit-specific block or from an applicable global base-scope block
- this exists to improve diagnosis, so the user can distinguish progression driven by direct unit edits from progression driven by shared doctrinal/base effects

Dating confidence should improve the interpretation of a diagnostic. It must not be used as a justification for adapting envelopes to current values.

## Implemented checks

- Unknown monitored unit targets in rules (`FAIL`)
- Missing/unreadable monitored baseline stats in unit files (`FAIL`)
- Single stat delta beyond `max_single_delta` (`WARN`)
- Cumulative positive/negative delta beyond configured caps (`WARN`)
- Estimated final (`baseline_raw + cumulative delta`) outside `final_range` (`WARN`)
- Milestone estimate outside per-year `milestone_ranges` (`WARN`)
- Build/upkeep estimate not calculable due to missing goods costs (`FAIL`)
- Build/upkeep estimates outside configured economic ranges (`WARN`)
- Key-good expectation mismatch (`WARN`)
- Timeline coverage / confidence coverage diagnostics (`INFO` / `WARN`)
- Source-separated provenance in stat-progression reporting for unit-specific vs applicable global base-scope deltas (`INFO`)

## Example report lines

Unified stat summary example:

`tank attack: baseline_raw 16.000, first_known_year 1929, last_known_year 1966, cumulative +20.000, cumulative -0.000, milestones[1836:16.000, 1850:16.000, 1870:16.000, 1900:16.000, 1910:16.000, 1919:16.000, 1929:18.000, 1936:28.000, 1945:32.000, 1955:32.000, 1966:36.000], estimated_final 36.000, time_direct 2.000, time_inferred_strong 11.000, time_inferred_weak 7.000, time_unknown 0.000, time_coverage 100.0%, high_conf_coverage 65.0%`

Economic summary example:

`tank: economic upkeep_est=32.10; top3_upkeep=[barrels=16.66, fuel=7.50, artillery=5.20]`

## Running

From repo root:

```bash
python TGC/tools/audit_1966_balance.py
```

The command prints `FAIL/WARN/INFO`, a priority summary, and a playtest focus shortlist. Stat progression summaries also preserve source provenance for applicable global base-scope effects.

## Reading broad coverage quality

When the audit covers many units, not all units have equal diagnostic signal.

- units with many assignments and several touched monitored stats are typically higher-value for balance monitoring
- units with `signal assignments=0` are still covered, but currently provide baseline or economic checks only and should be treated as lower-priority diagnostic targets until more dated deltas are available in scanned files

This hierarchy is practical only. It does not alter the normative meaning of the audit, and it must not be interpreted as a reason to soften rules for low-signal areas.

## Tiered end-of-report watchlists

The final report includes three practical sections:

- `CORE WATCHLIST`
- `SECONDARY WATCHLIST`
- `LOW-SIGNAL COVERAGE`

Each line summarizes:

- unit
- tier
- signal assignments
- touched stats
- top warning (if any)

This hierarchy does **not** remove detailed diagnostics. It exists only to organize review effort so core units are inspected first, while low-signal units remain visible without dominating practical triage unless they produce real `FAIL`s or clear anomalies.

Rules naming note: unit group names are version-neutral (for example `legacy_baseline_units`, `all_monitored_units`).

## STAT COVERAGE SUMMARY

The report includes a dedicated section:

- `STAT COVERAGE SUMMARY`

It prints:

- total covered stat entries
- total detected stat entries (from unit files, limited to monitored catalog)
- global detected vs covered stat types
- per-unit `covered_stats / detected_stats`
- explicit list of missing coverage when detected stats are not yet covered by rules

This section exists to show what is and is not monitored. It is not a claim that all covered stats are equally well evidenced.

## STAT DIAGNOSTIC QUALITY

The report also includes:

- `STAT DIAGNOSTIC QUALITY`

Grouped by `primary` / `secondary` / `structural`, with per-stat:

- covered units
- assignment count
- units with signal
- quality label:
  - `strong_signal`
  - `limited_signal`
  - `formal_coverage_only`

This section makes it explicit when a stat is fully covered in rules but still weak diagnostically because readable timed deltas are sparse or absent.

Structural stats remain visible, but they are de-prioritized in top summaries unless they produce strong anomalies or `FAIL`-level issues. De-prioritization is a reporting choice only; it is not a reason to make structural rules adaptively permissive.

## TOP STAT WATCHLIST

The final report includes:

- `TOP STAT WATCHLIST`

This is a compact cross-unit stat-priority list ordered by diagnostic priority, combining:

- stat tier weight (`primary` > `secondary` > `structural`)
- signal quality weight (`strong_signal` > `limited_signal` > `formal_coverage_only`)
- unit tier context (issues on `core` units are boosted)

Each line includes:

- stat
- stat tier
- units with signal
- signal quality label
- score
- top issue example

This section is a triage convenience. It is not a measure of whether the audit is “good” based on warning-count reduction.

## Interpreting current warning concentrations

Current warning concentrations should be read as **areas requiring diagnosis**, not as evidence that the rules in those areas are too strict.

In practice, recurring concentrations tend to fall into one of three categories:

1. **Rule/model issues**: ranges, milestone logic, or applicability assumptions are internally inconsistent or historically weak.
2. **Correct gameplay pressure**: current unit/tech/invention values are genuinely pushing beyond plausible bounded progression.
3. **Weak-evidence noise**: low-signal or poor-dating areas where a warning may require more caution before being judged substantive.

Any future revision should preserve this distinction. The next review target should always be chosen by diagnostic value, not by the convenience of reducing warnings.

## Practical use

Use this audit to answer the following questions in order:

1. Is the rule internally coherent?
2. Is the rule historically and mechanically plausible?
3. If yes, does the warning identify a real gameplay problem?
4. If not, is the warning caused by weak evidence, applicability logic, or malformed guardrails?

Do **not** begin from the assumption that current gameplay values are the benchmark.

The benchmark is the strongest defensible combination of:

- historical plausibility
- role integrity
- coherent inter-era progression
- bounded mechanical balance
- diagnostic usefulness
