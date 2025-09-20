import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from rule import Rule
from working_memory import WorkingMemory
from engine import InferenceEngine

def test_forward_chain_simple():
    rules = [
        Rule(id="r1", antecedents=["a"], consequent="b"),
        Rule(id="r2", antecedents=["b"], consequent="c")
    ]
    wm = WorkingMemory(["a"])
    engine = InferenceEngine(rules, wm)
    conclusions = engine.forward_chain()
    assert "b" in conclusions
    assert "c" in conclusions
    assert "b" in wm.facts
    assert "c" in wm.facts

def test_explain():
    rules = [Rule(id="r1", antecedents=["a"], consequent="b")]
    wm = WorkingMemory(["a"])
    engine = InferenceEngine(rules, wm)
    engine.forward_chain()
    explanation = engine.explain()
    assert explanation["fired_rules"] == ["r1"]
    assert "b" in explanation["facts"]