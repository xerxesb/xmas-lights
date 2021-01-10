from rich.console import Console
import time
import os

console = Console()

def print_pattern():
    os.system('clear')
    console.print("\r*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *", end='', style='bold blue')
    time.sleep(0.6)

    os.system('clear')
    console.print("\r  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  ", end='', style='bold blue')
    time.sleep(0.6)

print_pattern()
print_pattern()
print_pattern()
print_pattern()
print_pattern()

print()