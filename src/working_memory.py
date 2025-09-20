from typing import Set, List

class WorkingMemory:
    def __init__(self, initial_facts: List[str] = None):
        """
        حافظه کاری را با یک لیست اولیه از فکت‌ها ایجاد می‌کند.
        """
        self.facts: Set[str] = set(initial_facts or [])

    def add(self, fact: str) -> bool:
        """
        فکت جدید اضافه می‌کند.
        برمی‌گرداند True اگر فکت جدید بود و قبلاً وجود نداشت.
        """
        if fact not in self.facts:
            self.facts.add(fact)
            return True
        return False

    def remove(self, fact: str) -> bool:
        """
        حذف یک فکت از حافظه کاری.
        """
        if fact in self.facts:
            self.facts.remove(fact)
            return True
        return False

    def has(self, fact: str) -> bool:
        """
        بررسی می‌کند آیا فکت در حافظه کاری موجود است.
        """
        return fact in self.facts

    def all(self) -> List[str]:
        """
        تمام فکت‌های موجود در حافظه کاری را به صورت لیست بازمی‌گرداند.
        """
        return list(self.facts)