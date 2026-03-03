# main.py

import click
from colorama import init, Fore, Style
import config
import utils

init(autoreset=True)

@click.command()
@click.optionn("--a", prompt="Input first number", type=float)
@click.option("--b", prompt="Input second number", type=float)
@click.option(
	"--operation",
	prompt="Choose operation (+, -, *, /)",
	type=click.Choise(["+", "-", "*", "/"]),
)
def main(a, b, operatoion):
	click.echo(Fore.CYAN + config.APP_NAME)
	click.echo(Fore.YELLOW + config.WELCOME_MESSAGE)

	try:
		result = utils.calculate(a, b, operation)
		click.echo(Fore.GREEN + f"Result: {result}")
	except ZeroDivisionError:
		click.echo(Fore.RED + config.ERROR_DIVISION_BY_ZERO)
	except ValueError:
		click.echo(Fore.RED + config.ERROR_INVALID_OPERATION)

if __name__ == "__main__":
	main()
