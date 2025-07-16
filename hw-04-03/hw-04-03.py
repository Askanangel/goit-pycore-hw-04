import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_dir_tree(path: Path, prefix: str = ""):
    """Рекурсивно виводить структуру директорії з кольоровим форматуванням."""
    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    for idx, item in enumerate(items):
        connector = "┗━ " if idx == len(items) - 1 else "┣━ "
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{connector}{item.name}{Style.RESET_ALL}")
            print_dir_tree(item, prefix + ("   " if idx == len(items) - 1 else "┃  "))
        else:
            print(f"{prefix}{Fore.GREEN}{connector}{item.name}{Style.RESET_ALL}")

def main():
    init(autoreset=True)
    if len(sys.argv) != 2:
        print("Використання: python hw03.py <шлях_до_директорії>")
        sys.exit(1)
    dir_path = Path(sys.argv[1])
    if not dir_path.exists():
        print(f"Помилка: шлях '{dir_path}' не існує.")
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"Помилка: шлях '{dir_path}' не є директорією.")
        sys.exit(1)
    print(f"{Fore.BLUE}{dir_path.name}{Style.RESET_ALL}")
    print_dir_tree(dir_path)

if __name__ == "__main__":
    main()