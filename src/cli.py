import click
from rule import Rule
from working_memory import WorkingMemory
from engine import InferenceEngine

# نمونه قوانین پیش‌فرض
DEFAULT_RULES = [
    Rule(id="cold", antecedents=["سرفه", "گلودرد"], consequent="احتمال سرماخوردگی", salience=10),
    Rule(id="flu", antecedents=["تب بالا", "سردرد", "بدن درد"], consequent="احتمال آنفولانزا", salience=10),
    Rule(id="allergy", antecedents=["عطسه", "آبریزش بینی"], consequent="احتمال آلرژی", salience=5),
]

@click.group()
def cli():
    """Expert System CLI"""
    pass

@cli.command()
@click.argument('symptoms', nargs=-1)
def diagnose(symptoms):
    """
    تشخیص بیماری بر اساس علائم.
    علائم را به صورت آرگومان وارد کنید یا اگر خالی بود، حالت تعاملی باز می‌شود.
    """
    if not symptoms:
        click.echo("حالت تعاملی — علائم را با کاما وارد کنید:")
        raw = click.prompt("symptoms")
        symptoms = [s.strip() for s in raw.split(',') if s.strip()]

    wm = WorkingMemory(list(symptoms))
    engine = InferenceEngine(DEFAULT_RULES, wm)
    conclusions = engine.forward_chain()

    click.echo("\n=== نتایج ===")
    click.echo(f"علائم ورودی: {symptoms}")
    click.echo(f"حافظه کاری (WM): {wm.all()}")
    click.echo(f"تشخیص: {conclusions or ['تشخیص داده نشد']}")

if __name__ == "__main__":
    cli()