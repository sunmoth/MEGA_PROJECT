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
