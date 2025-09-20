from dataclasses import dataclass
from typing import List

@dataclass
class Rule:
    id: str                    # شناسه منحصر به فرد قانون
    antecedents: List[str]     # شرایط (if)
    consequent: str            # نتیجه (then)
    salience: int = 0          # اولویت قانون برای حل تعارض

    def matches(self, facts: set) -> bool:
        """
        بررسی می‌کند که آیا تمام antecedents در حافظه کاری موجود هستند.
        facts: مجموعه factهای موجود در WM
        return: True اگر همه antecedents موجود باشند
        """
        return all(a in facts for a in self.antecedents)