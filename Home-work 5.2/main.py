def main():
    while True:

        num1 = float(input("Введіть перше число: "))
        operation = input("Введіть дію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        # Виконання відповідної математичної операції
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Помилка: ділення на нуль неможливе")
                continue
            result = num1 / num2
        else:
            print("Неправильна дія будь ласка введіть одну з наступних дій: +, -, *, /")
            continue


        print(f"Результат: {result}")

        continue_calculation = input("Бажаєте продовжити обчислення? (y/n): ").strip().lower()
        if continue_calculation != 'y':
            break

if __name__ == "__main__":
    main()
