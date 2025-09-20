from typing import List
from rule import Rule
from working_memory import WorkingMemory

class InferenceEngine:
    def __init__(self, rules: List[Rule], wm: WorkingMemory):
        """
        rules: لیست قوانین
        wm: حافظه کاری (Working Memory)
        """
        self.rules = rules
        self.wm = wm
        self.fired_rules = []  # لیست قوانین اعمال شده (شناسه‌ها)

    def _select_applicable_rules(self) -> List[Rule]:
        """
        انتخاب قوانین قابل اعمال:
        - همه antecedents باید در WM باشند
        - consequent هنوز در WM نباشد
        - اولویت بندی: salience بیشتر و سپس تعداد antecedents بیشتر
        """
        applicable = [
            r for r in self.rules
            if r.matches(self.wm.facts) and r.consequent not in self.wm.facts
        ]
        applicable.sort(key=lambda r: (r.salience, len(r.antecedents)), reverse=True)
        return applicable

    def forward_chain(self, max_iterations: int = 100) -> List[str]:
        """
        اجرای الگوریتم forward chaining:
        - تا زمانی که قوانین قابل اعمال باقی هستند یا حداکثر تکرار رسید
        - قوانین را اعمال می‌کند و فکت‌ها را به WM اضافه می‌کند
        """
        conclusions = []
        iterations = 0

        while iterations < max_iterations:
            iterations += 1
            applicable = self._select_applicable_rules()
            if not applicable:
                break
            rule = applicable[0]  # اجرای قانون با اولویت بالا
            added = self.wm.add(rule.consequent)
            if added:
                self.fired_rules.append(rule.id)
                conclusions.append(rule.consequent)

        return conclusions

    def explain(self) -> dict:
        """
        توضیح عملکرد موتور استنتاج:
        - قوانین اعمال شده
        - فکت‌های فعلی در WM
        """
        return {
            "fired_rules": self.fired_rules,
            "facts": self.wm.all()
        }