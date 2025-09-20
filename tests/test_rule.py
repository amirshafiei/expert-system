import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from rule import Rule

def test_rule_matches():
    rule = Rule(id="r1", antecedents=["a", "b"], consequent="c")
    facts = {"a", "b", "x"}
    assert rule.matches(facts) == True

def test_rule_not_matches():
    rule = Rule(id="r2", antecedents=["a", "y"], consequent="c")
    facts = {"a", "b", "x"}
    assert rule.matches(facts) == False