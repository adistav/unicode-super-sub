import json

BINARY = "/Users/adistav/.local/bin/type-unicode"

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
# Mnemonics: s=ß≈β, g=gamma, r=rho, f=phi(ph→f), x=chi(conventional)
GREEK_SUBS = [
    ("s", 0x03B2),  # ᵦ
    ("g", 0x03B3),  # ᵧ
    ("r", 0x03C1),  # ᵨ
    ("f", 0x03C6),  # ᵩ
    ("x", 0x03C7),  # ᵪ
]

def greek_sub_rules():
    rules = []
    for key_code, cp in GREEK_SUBS:
        rules.append({
            "type": "basic",
            "conditions": [{"type": "variable_if", "name": "ss_mode", "value": 2}],
            "from": {"key_code": key_code, "modifiers": {"mandatory": ["option"], "optional": ["any"]}},
            "to": [
                {"shell_command": f"{BINARY} sub {cp}"},
                {"set_variable": {"name": "ss_mode", "value": 0}}
            ]
        })
    return rules

def body_rules(mode_val, mode_str):
    rules = []
    for key_code, mandatory, cp in CHARS:
        mods = {"optional": ["any"]}
        if mandatory:
            mods["mandatory"] = mandatory
        rules.append({
            "type": "basic",
            "conditions": [{"type": "variable_if", "name": "ss_mode", "value": mode_val}],
            "from": {"key_code": key_code, "modifiers": mods},
            "to": [
                {"shell_command": f"{BINARY} {mode_str} {cp}"},
                {"set_variable": {"name": "ss_mode", "value": 0}}
            ]
        })
    return rules

manipulators = [
    {"type": "basic",
     "from": {"key_code": "equal_sign", "modifiers": {"mandatory": ["option", "control"]}},
     "to": [{"set_variable": {"name": "ss_mode", "value": 1}}]},
    {"type": "basic",
     "from": {"key_code": "hyphen", "modifiers": {"mandatory": ["option", "control"]}},
     "to": [{"set_variable": {"name": "ss_mode", "value": 2}}]},
    {"type": "basic",
     "conditions": [{"type": "variable_if", "name": "ss_mode", "value": 1}],
     "from": {"key_code": "escape", "modifiers": {"optional": ["any"]}},
     "to": [{"key_code": "escape"}, {"set_variable": {"name": "ss_mode", "value": 0}}]},
    {"type": "basic",
     "conditions": [{"type": "variable_if", "name": "ss_mode", "value": 2}],
     "from": {"key_code": "escape", "modifiers": {"optional": ["any"]}},
     "to": [{"key_code": "escape"}, {"set_variable": {"name": "ss_mode", "value": 0}}]},
]
manipulators += body_rules(1, "sup")
manipulators += greek_sub_rules()
manipulators += body_rules(2, "sub")

out = {
    "title": "Superscript and Subscript",
    "rules": [{"description": "⌥⌃= then char → superscript; ⌥⌃- then char → subscript",
               "manipulators": manipulators}]
}
print(json.dumps(out, indent=2, ensure_ascii=False))
