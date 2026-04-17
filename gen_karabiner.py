import json

BINARY = "/Users/adistav/.local/bin/type-unicode"

# ── superscript / subscript ────────────────────────────────────────────────────

# Shift (more specific) rules MUST come before non-shift rules so Karabiner
# picks the right one. optional:any lets these fire even if ⌥⌃ is still held.
CHARS = []
CHARS.append(("9",           ["shift"], ord('(')))
CHARS.append(("0",           ["shift"], ord(')')))
CHARS.append(("equal_sign",  ["shift"], ord('+')))
for c in "abcdefghijklmnopqrstuvwxyz":
    CHARS.append((c, ["shift"], ord(c.upper())))
for d in range(10):
    CHARS.append((str(d), [], ord('0') + d))
CHARS.append(("hyphen",     [], ord('-')))
CHARS.append(("equal_sign", [], ord('=')))
for c in "abcdefghijklmnopqrstuvwxyz":
    CHARS.append((c, [], ord(c)))

# ⌥+key in subscript mode → Greek subscripts
GREEK_SUBS = [
    ("s", 0x03B2),  # ᵦ
    ("g", 0x03B3),  # ᵧ
    ("r", 0x03C1),  # ᵨ
    ("f", 0x03C6),  # ᵩ
    ("x", 0x03C7),  # ᵪ
]

# ── single-key mode (⌥⌃\) ─────────────────────────────────────────────────────
# Shift rules before non-shift rules (more specific first).

SINGLE_KEY_SYMBOLS = [
    # key_code                  mandatory       codepoint
    # Logic / set operators (shifted keys)
    ("1",                       ["shift"],      0x00AC),    # ¬  !
    ("6",                       ["shift"],      0x2295),    # ⊕  ^
    ("7",                       ["shift"],      0x2227),    # ∧  &
    ("8",                       ["shift"],      0x00D7),    # ×  *
    ("backslash",               ["shift"],      0x2228),    # ∨  |
    ("comma",                   ["shift"],      0x2282),    # ⊂  <
    ("period",                  ["shift"],      0x2283),    # ⊃  >
    # Kept punctuation (shifted)
    ("n",                       ["shift"],      0x2116),    # №  N
    ("quote",                   ["shift"],      0x2033),    # ″  "
    # Arrows
    ("h",                       [],             0x2190),    # ←
    ("j",                       [],             0x2193),    # ↓
    ("k",                       [],             0x2191),    # ↑
    ("l",                       [],             0x2192),    # →
    # Quantifiers
    ("a",                       [],             0x2200),    # ∀
    ("e",                       [],             0x2203),    # ∃
    # Set operators
    ("u",                       [],             0x222A),    # ∪
    ("i",                       [],             0x2229),    # ∩
    ("open_bracket",            [],             0x2208),    # ∈  [
    ("close_bracket",           [],             0x220B),    # ∋  ]
    ("0",                       [],             0x2205),    # ∅
    ("backslash",               [],             0x2216),    # ∖  \
    ("d",                       [],             0x25B3),    # △
    ("p",                       [],             0x1D4AB),   # 𝒫
    # Number sets
    ("n",                       [],             0x2115),    # ℕ
    ("z",                       [],             0x2124),    # ℤ
    ("q",                       [],             0x211A),    # ℚ
    ("r",                       [],             0x211D),    # ℝ
    ("c",                       [],             0x2102),    # ℂ
    # Primes / misc
    ("quote",                   [],             0x2032),    # ′  '
    ("grave_accent_and_tilde",  [],             0x2034),    # ‴  `
]

# ── two-key mode (⌥⌃/) ────────────────────────────────────────────────────────

# Negation (⌥⌃/ → !): shift rules before non-shift.
NEGATION_SYMBOLS = [
    # key_code          mandatory       codepoint
    ("comma",           ["shift"],      0x2284),    # ⊄  <
    ("period",          ["shift"],      0x2285),    # ⊅  >
    ("open_bracket",    [],             0x2209),    # ∉  [
    ("close_bracket",   [],             0x220C),    # ∌  ]
    ("comma",           [],             0x2288),    # ⊈  ,
    ("period",          [],             0x2289),    # ⊉  .
    ("equal_sign",      [],             0x2260),    # ≠  =
    ("e",               [],             0x2204),    # ∄
]

# Or-equal (⌥⌃/ → =): shift rules before non-shift.
OR_EQUAL_SYMBOLS = [
    # key_code          mandatory       codepoint
    ("comma",           ["shift"],      0x2286),    # ⊆  <
    ("period",          ["shift"],      0x2287),    # ⊇  >
    ("equal_sign",      [],             0x2261),    # ≡  =
]

# Currencies: (iso3166_two_letter_code, codepoint)
CURRENCIES = [
    ("us", 0x00A2),  # ¢  cent (US)
    ("gb", 0x00A3),  # £  pound (UK)
    ("jp", 0x00A5),  # ¥  yen (Japan)
    ("cr", 0x20A1),  # ₡  colon (Costa Rica)
    ("ng", 0x20A6),  # ₦  naira (Nigeria)
    ("pk", 0x20A8),  # ₨  rupee (Pakistan / generic)
    ("kr", 0x20A9),  # ₩  won (Korea)
    ("il", 0x20AA),  # ₪  shekel (Israel)
    ("vn", 0x20AB),  # ₫  dong (Vietnam)
    ("eu", 0x20AC),  # €  euro
    ("la", 0x20AD),  # ₭  kip (Laos)
    ("mn", 0x20AE),  # ₮  tugrik (Mongolia)
    ("ph", 0x20B1),  # ₱  peso (Philippines)
    ("py", 0x20B2),  # ₲  guaraní (Paraguay)
    ("ua", 0x20B4),  # ₴  hryvnia (Ukraine)
    ("gh", 0x20B5),  # ₵  cedi (Ghana)
    ("kz", 0x20B8),  # ₸  tenge (Kazakhstan)
    ("in", 0x20B9),  # ₹  rupee (India)
    ("tr", 0x20BA),  # ₺  lira (Turkey)
    ("az", 0x20BC),  # ₼  manat (Azerbaijan)
    ("ru", 0x20BD),  # ₽  ruble (Russia)
    ("ge", 0x20BE),  # ₾  lari (Georgia)
    ("bt", 0x20BF),  # ₿  bitcoin
    ("th", 0x0E3F),  # ฿  baht (Thailand)
    ("am", 0x058F),  # ֏  dram (Armenia)
    ("bd", 0x09F3),  # ৳  taka (Bangladesh)
    ("kh", 0x17DB),  # ៛  riel (Cambodia)
    ("sa", 0xFDFC),  # ﷼  riyal (Saudi Arabia)
    ("ir", 0xFDFC),  # ﷼  rial (Iran)
    # Historical
    ("br", 0x20A2),  # ₢  cruzeiro (Brazil)
    ("fr", 0x20A3),  # ₣  franc (France)
    ("it", 0x20A4),  # ₤  lira (Italy)
    ("es", 0x20A7),  # ₧  peseta (Spain)
    ("gr", 0x20AF),  # ₯  drachma (Greece)
    ("ar", 0x20B3),  # ₳  austral (Argentina)
]

# Fractions: (numerator, denominator, codepoint)
# denominator 0 stands for 10 (typed as the '0' key)
FRACTIONS = [
    (1, 2, 0x00BD),  # ½
    (1, 3, 0x2153),  # ⅓
    (2, 3, 0x2154),  # ⅔
    (1, 4, 0x00BC),  # ¼
    (3, 4, 0x00BE),  # ¾
    (1, 5, 0x2155),  # ⅕
    (2, 5, 0x2156),  # ⅖
    (3, 5, 0x2157),  # ⅗
    (4, 5, 0x2158),  # ⅘
    (1, 6, 0x2159),  # ⅙
    (5, 6, 0x215A),  # ⅚
    (1, 7, 0x2150),  # ⅐
    (1, 8, 0x215B),  # ⅛
    (3, 8, 0x215C),  # ⅜
    (5, 8, 0x215D),  # ⅝
    (7, 8, 0x215E),  # ⅞
    (1, 9, 0x2151),  # ⅑
    (1, 0, 0x2152),  # ⅒  (0 key = denominator 10)
]

LETTERS = "abcdefghijklmnopqrstuvwxyz"

def letter_index(c):
    return LETTERS.index(c) + 1  # a=1 … z=26

def direct(cp):
    return {"shell_command": f"{BINARY} direct {cp}"}

def reset_mode():
    return {"set_variable": {"name": "ss_mode", "value": 0}}

def reset_key1():
    return {"set_variable": {"name": "ss_key1", "value": 0}}

def cond(name, value):
    return {"type": "variable_if", "name": name, "value": value}

def from_key(key_code, mandatory=None):
    mods = {"optional": ["any"]}
    if mandatory:
        mods["mandatory"] = mandatory
    return {"key_code": key_code, "modifiers": mods}

def escape_rule(mode_val, also_reset_key1=False):
    to = [{"key_code": "escape"}, reset_mode()]
    if also_reset_key1:
        to.append(reset_key1())
    return {
        "type": "basic",
        "conditions": [cond("ss_mode", mode_val)],
        "from": from_key("escape"),
        "to": to,
    }

# ── rule generators ────────────────────────────────────────────────────────────

def greek_sub_rules():
    rules = []
    for key_code, cp in GREEK_SUBS:
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", 2)],
            "from": {"key_code": key_code, "modifiers": {"mandatory": ["option"], "optional": ["any"]}},
            "to": [{"shell_command": f"{BINARY} sub {cp}"}, reset_mode()],
        })
    return rules

def body_rules(mode_val, mode_str):
    rules = []
    for key_code, mandatory, cp in CHARS:
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", mode_val)],
            "from": from_key(key_code, mandatory),
            "to": [{"shell_command": f"{BINARY} {mode_str} {cp}"}, reset_mode()],
        })
    return rules

def single_key_rules():
    rules = []
    for key_code, mandatory, cp in SINGLE_KEY_SYMBOLS:
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", 3)],
            "from": from_key(key_code, mandatory),
            "to": [direct(cp), reset_mode()],
        })
    return rules

def two_key_first_rules():
    """mode 10 → dispatch to sub-modes."""
    rules = []
    # Shift rules first (more specific)
    rules.append({
        "type": "basic",
        "conditions": [cond("ss_mode", 10)],
        "from": from_key("1", ["shift"]),   # ! → negation mode
        "to": [{"set_variable": {"name": "ss_mode", "value": 13}}],
    })
    # Non-shift
    rules.append({
        "type": "basic",
        "conditions": [cond("ss_mode", 10)],
        "from": from_key("equal_sign"),     # = → or-equal mode
        "to": [{"set_variable": {"name": "ss_mode", "value": 14}}],
    })
    for c in LETTERS:
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", 10)],
            "from": from_key(c),
            "to": [
                {"set_variable": {"name": "ss_mode", "value": 11}},
                {"set_variable": {"name": "ss_key1", "value": letter_index(c)}},
            ],
        })
    for d in range(10):
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", 10)],
            "from": from_key(str(d)),
            "to": [
                {"set_variable": {"name": "ss_mode", "value": 12}},
                {"set_variable": {"name": "ss_key1", "value": d}},
            ],
        })
    return rules

def negation_rules():
    """mode 13: negate a relation symbol."""
    rules = []
    for key_code, mandatory, cp in NEGATION_SYMBOLS:
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", 13)],
            "from": from_key(key_code, mandatory),
            "to": [direct(cp), reset_mode()],
        })
    return rules

def or_equal_rules():
    """mode 14: or-equal / equivalence variant."""
    rules = []
    for key_code, mandatory, cp in OR_EQUAL_SYMBOLS:
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", 14)],
            "from": from_key(key_code, mandatory),
            "to": [direct(cp), reset_mode()],
        })
    return rules

def currency_rules():
    """mode 11 + ss_key1=first_letter_index + second letter → currency."""
    rules = []
    for code, cp in CURRENCIES:
        l1, l2 = code[0], code[1]
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", 11), cond("ss_key1", letter_index(l1))],
            "from": from_key(l2),
            "to": [direct(cp), reset_mode(), reset_key1()],
        })
    return rules

def fraction_rules():
    """mode 12 + ss_key1=numerator + denominator digit → fraction."""
    rules = []
    for num, den, cp in FRACTIONS:
        rules.append({
            "type": "basic",
            "conditions": [cond("ss_mode", 12), cond("ss_key1", num)],
            "from": from_key(str(den)),
            "to": [direct(cp), reset_mode(), reset_key1()],
        })
    return rules

# ── assemble ───────────────────────────────────────────────────────────────────

manipulators = [
    # Mode entry
    {"type": "basic",
     "from": {"key_code": "equal_sign",            "modifiers": {"mandatory": ["option", "control"]}},
     "to": [{"set_variable": {"name": "ss_mode", "value": 1}}]},
    {"type": "basic",
     "from": {"key_code": "hyphen",                "modifiers": {"mandatory": ["option", "control"]}},
     "to": [{"set_variable": {"name": "ss_mode", "value": 2}}]},
    {"type": "basic",
     "from": {"key_code": "backslash",             "modifiers": {"mandatory": ["option", "control"]}},
     "to": [{"set_variable": {"name": "ss_mode", "value": 3}}]},
    {"type": "basic",
     "from": {"key_code": "slash",                 "modifiers": {"mandatory": ["option", "control"]}},
     "to": [{"set_variable": {"name": "ss_mode", "value": 10}}]},
    # Escape handlers
    escape_rule(1),
    escape_rule(2),
    escape_rule(3),
    escape_rule(10),
    escape_rule(11, also_reset_key1=True),
    escape_rule(12, also_reset_key1=True),
    escape_rule(13),
    escape_rule(14),
]

manipulators += body_rules(1, "sup")
manipulators += greek_sub_rules()
manipulators += body_rules(2, "sub")
manipulators += single_key_rules()
manipulators += two_key_first_rules()
manipulators += negation_rules()
manipulators += or_equal_rules()
manipulators += currency_rules()
manipulators += fraction_rules()

out = {
    "title": "Unicode symbols",
    "rules": [{
        "description": (
            "⌥⌃= superscript  ⌥⌃- subscript  "
            "⌥⌃\\ single-key (logic/set ops, arrows, ℕℤℚℝℂ)  "
            "⌥⌃/ two-key (fractions, currencies, negation, or-equal)"
        ),
        "manipulators": manipulators,
    }],
}
print(json.dumps(out, indent=2, ensure_ascii=False))
