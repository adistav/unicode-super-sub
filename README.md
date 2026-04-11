# unicode-super-sub

Mac keyboard chords for Unicode superscript and subscript characters, via [Karabiner-Elements](https://karabiner-elements.pqrs.org/).

## How it works

- **⌥⌃=** enters superscript mode, **⌥⌃-** enters subscript mode
- Type the next character to insert its super/subscript version; Escape cancels
- Works in iTerm2 (direct injection) and all other apps (clipboard paste with restore)

## Character coverage

| Input | Superscript | Subscript |
|-------|-------------|-----------|
| 0–9 | ⁰¹²³⁴⁵⁶⁷⁸⁹ | ₀₁₂₃₄₅₆₇₈₉ |
| `- = + ( )` | ⁻⁼⁺⁽⁾ | ₋₌₊₍₎ |
| a–z | ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ‌ʳˢᵗᵘᵛʷˣʸᶻ (all 26) | ₐ‌ₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ (17; b c d f g q w y z have no Unicode subscript) |
| A–Z (Shift) | ᴬᴮꟲᴰᴱꟳᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾꟴᴿᵀᵁⱽᵂ (22; S X Y Z have none) | — (no uppercase subscripts in Unicode) |
| ⌥s ⌥g ⌥r ⌥f ⌥x | — | ᵦᵧᵨᵩᵪ (Greek β γ ρ φ χ) |

## Files

| File | Purpose |
|------|---------|
| `type-unicode.swift` | Swift source for the helper binary |
| `gen_karabiner.py` | Generates `superscript_subscript.json` |
| `superscript_subscript.json` | Karabiner complex modification (generated) |
| `Makefile` | Build, install, symlink management |

System symlinks point into this repo:
- `~/.local/bin/type-unicode.swift` → `type-unicode.swift`
- `~/.config/karabiner/assets/complex_modifications/superscript_subscript.json` → `superscript_subscript.json`

The compiled binary lives at `~/.local/bin/type-unicode` (not in the repo).

## Install on a new machine

1. Install [Karabiner-Elements](https://karabiner-elements.pqrs.org/)
2. Clone this repo somewhere, e.g. `~/unicode-super-sub`
3. Run:
   ```
   make install
   ```
4. In Karabiner-Elements: **Complex Modifications → Add rule → "Superscript and Subscript" → Enable**

Grant Accessibility and Automation permissions when macOS prompts (needed for AppleScript paste).

## Updating

After editing `type-unicode.swift`:
```
make build
```

After editing `gen_karabiner.py`:
```
make karabiner
```
Then remove and re-add the rule in Karabiner-Elements for the change to take effect.
