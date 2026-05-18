# 1966 extension static validator

This repository includes a lightweight static validator for the separated 1966
timeline architecture.

- Script: `TGC/tools/validate_1966_extension.py`
- Scope manifest: `TGC/tools/1966_extension_scope.json`
- Default core root: `TGC/`
- Default 1966 runtime root: `TGC_Timeline_1966/`

The base `TGC/` mod is intentionally non-1966. The runtime content for the
extended timeline lives in the `TGC Timeline 1966` submod. To play the extended
timeline, enable both `TGC - The Grand Combination` and `TGC Timeline 1966`.

## What it checks

The validator is manifest-driven and now checks two layers:

1. **Timeline submod runtime presence and coherence**
   - `TGC_Timeline_1966/common/defines.lua` keeps `end_date = '1966.1.1'`.
   - `TGC_Timeline_1966/decisions/00_Setup.txt` keeps `option_end_game` aligned
     with `year = 1966` in both `potential` and `allow`.
   - `TGC_Timeline_1966/interface/backend.gui` keeps `text = "The World in 1966"`.
   - The five timeline technology files have the expected 25 areas at 12 tiers
     each.
   - Tracked `NEW_*_inventions.txt` files are present and localized.
   - Carrier/submarine units and key binary assets exist in the submod.
   - Unit-target effects in tracked technology/invention files resolve against
     units from both `TGC/units` and `TGC_Timeline_1966/units`.

2. **Core cleanup**
   - `TGC/common/defines.lua` must not contain the 1966 end date.
   - `TGC/interface/backend.gui` must not show `The World in 1966`.
   - Timeline-only runtime files such as `TGC/units/aircraftcarrier.txt`,
     `TGC/units/submarine.txt`, `TGC/inventions/NEW_*_inventions.txt`, and the
     old `TGC/localisation/00_SUP_technology.csv` / `00_other_tech.csv` must not
     remain in core.

Known false positives such as historical Hunley submarine flavour text, province
id `1966`, and pre-existing `submarine_warfare` modifiers are not represented as
forbidden validator patterns; they are documented in the submod manifest.

## Run

From repository root:

```bash
python TGC/tools/validate_1966_extension.py
```

Optional roots are available for compatibility/testing:

```bash
python TGC/tools/validate_1966_extension.py --core-root TGC --timeline-root TGC_Timeline_1966
```

The script exits with code `0` when all targeted checks pass, and `1` with a
failure list otherwise.

## CI automation

GitHub Actions runs this validator on `push` and `pull_request` when the tool,
manifest, submod runtime, core cleanup guard files, or related docs change.

## Timeline override drift check

Some `TGC_Timeline_1966/` files are full-file overrides or carrier files. They
should behave like "current core plus the 1966 timeline hunk" when the submod is
enabled, so a later core-only fix can be hidden if the matching timeline override
is not refreshed.

When changing a core file that has a timeline override, run the default
core-to-submod read-only drift check from the repository root:

```bash
python TGC/tools/check_1966_submod_drift.py
```

This default mode compares changed core hunks against the timeline override and
warns when a core change is not present in the submod and does not look clearly
1966-specific.

When changing a timeline override directly, also run the reverse submod-to-core
check:

```bash
python TGC/tools/check_1966_submod_drift.py --reverse
```

Reverse mode compares changed submod hunks against core and warns when a submod
change looks like a generic bugfix, typo/encoding cleanup, UI fix, or other
non-timeline edit that is not present in `TGC/`. Non-timeline changes found only
in the submod must be ported to core or removed from the submod.

By default both directions compare changed hunks against `HEAD`, which is useful
while reviewing local edits. For already-committed branch work, pass the branch
base explicitly, for example:

```bash
python TGC/tools/check_1966_submod_drift.py --base-ref origin/main
python TGC/tools/check_1966_submod_drift.py --reverse --base-ref origin/main
```

`OK` means the watched override is currently coherent for the checked hunks,
`INFO` marks expected timeline differences or carrier files without a current
core counterpart, `WARN` marks possible drift that must be reviewed manually, and
`FAIL` marks missing override files, invalid roots, or an invalid base ref. The
drift check is conservative: it does not attempt to prove gameplay intent, and
WARN diagnostics should be inspected before deciding whether to port a hunk into
the timeline override, port it back to core, or remove it from the submod.

CI runs both drift directions automatically for `pull_request`, `push`, and
manual `workflow_dispatch` events. CI uses `--fail-on-warn`, so drift WARNs after
a core/submod sync block the workflow until the hunk is ported to the appropriate
counterpart, removed from the wrong side, or the checker/rules are intentionally
adapted. Local runs without `--fail-on-warn` keep WARN diagnostics non-blocking
for review.
