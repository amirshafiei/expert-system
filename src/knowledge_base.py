import yaml
from rule import Rule
from typing import List

def load_rules_from_yaml(path: str) -> List[Rule]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    rules = []
    for item in data.get("rules", []):
        r = Rule(
            id=item.get("id"),
            antecedents=item.get("if", []),
            consequent=item.get("then"),
            salience=item.get("salience", 0)
        )
        rules.append(r)
    return rules