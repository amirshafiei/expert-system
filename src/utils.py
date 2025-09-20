import logging

# تنظیمات اولیه logging
logger = logging.getLogger("expert_system")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# یک فانکشن کمکی برای چاپ تمیز
def print_header(title: str):
    print("\n" + "="*10 + f" {title} " + "="*10)