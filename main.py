import requests
import os
from dotenv import load_dotenv
import argparse


def convert_amount(token, target, amount, base):
    try:
        url =f"https://v6.exchangerate-api.com/v6/{token}/pair/{base}/{target}/{amount}"
        response = requests.get(url)
        response.raise_for_status()
        conversion_result = response.json()['conversion_result']
        return conversion_result
    except KeyError:
        print(f"Ошибка: Валюта {target} не найдена в данных курсов обмена")
        return None
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")
        return None


def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    parser = argparse.ArgumentParser(description="Конвертер валют")
    parser.add_argument("base", nargs="?", default="RUB", help="Базовая валюта (по умолчанию: RUB)")
    parser.add_argument("target", nargs="?", default="USD", help="Целевая валюта (по умолчанию: USD)")
    parser.add_argument("amount", nargs="?", type=float, default=10000, help="Сумма для конвертации (по умолчанию: 10000)")
    args = parser.parse_args()
    base = args.base.upper()
    target = args.target.upper()
    amount = args.amount
    print(f"Конвертация {amount} {base} в {target}...")

    conversion_result = convert_amount(token, target, amount, base)
    if conversion_result is not None:
         print(f"\n{amount} {base} = {conversion_result:.2f} {target}")


if __name__ == "__main__":
    main()
