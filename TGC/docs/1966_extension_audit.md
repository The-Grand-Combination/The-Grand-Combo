# 1966 Extension Audit (submod architecture)

## Current static status

The 1966 campaign extension is now a separate runtime submod:

- Base/core mod: `TGC/` (non-1966 by default).
- Timeline runtime: `TGC_Timeline_1966/`.
- Descriptor: `TGC_Timeline_1966.mod`.
- Required launcher combination: enable `TGC - The Grand Combination` and
  `TGC Timeline 1966`.

Static checks now verify that the 1966 runtime is present in the submod and that
core cleanup remains intact:

- `TGC_Timeline_1966/common/defines.lua` keeps `end_date = '1966.1.1'`.
- `TGC_Timeline_1966/decisions/00_Setup.txt` keeps `option_end_game` aligned to
  `year = 1966` in both `potential` and `allow`.
- `TGC_Timeline_1966/interface/backend.gui` keeps `text = "The World in 1966"`.
- `TGC/common/defines.lua` no longer carries the 1966 end date.
- Timeline-only unit, invention, localisation, interface, and graphics runtime
  files are absent from core and staged in the submod.

## What is automatically enforced

- Full-tree tech scope remains complete across all five branches: 25 areas at 12
  tiers per area.
- Tracked late inventions are present in `TGC_Timeline_1966/inventions/NEW_*` and
  localized through submod localisation files.
- Carrier/submarine unit effect targets resolve using the combined core + submod
  unit set.
- Core cleanup guards catch accidental reintroduction of the old core-only 1966
  end date, backend label, or timeline-only files.

## Known limitations of static validation

Static validation does not certify gameplay quality or release balance. It
validates structural coherence for the declared tracked scope. The balance audit
is the normative diagnostic layer for tuning warnings.

Full interface and decision overrides remain necessary because Victoria 2 loads
these files as whole-file definitions rather than fine-grained patches. These
overrides can mask future core edits while the submod is active and should be
reviewed when core files change.

## Final status judgment

- **Static completion for the declared 1966 extension scope is complete in the
  submod architecture.**
- Remaining work is optional balancing iteration and maintenance of the full-file
  override carriers.
