import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from working_memory import WorkingMemory

def test_add_fact():
    wm = WorkingMemory()
    assert wm.add("a") == True
    assert wm.add("a") == False  # تکراری

def test_remove_fact():
    wm = WorkingMemory(["a"])
    assert wm.remove("a") == True
    assert wm.remove("a") == False

def test_has_fact():
    wm = WorkingMemory(["a"])
    assert wm.has("a") == True
    assert wm.has("b") == False

def test_all_facts():
    wm = WorkingMemory(["a", "b"])
    facts = wm.all()
    assert "a" in facts and "b" in facts