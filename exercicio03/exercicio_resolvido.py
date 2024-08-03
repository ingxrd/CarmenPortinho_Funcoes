'''
3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta.

'''
#Function to convert Fahrenheit to Celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#Function to convert Celsius to Fahrenheit
def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Display the menu and call the function to convert
def menu():
    print("Choose the option you want to convert:")
    print("1. To convert Fahrenheit to Celsius")
    print("2. To convert Celsius to Fahrenheit")

    option = input("Choose one option ")

    if option == '1':
        fahrenheit = float(input("Enter the temperatura in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_celsius(fahrenheit)}°C")
    elif option == '2':
        celsius = float(input("Enter the temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_fahrenheit(celsius)}°F")
    else:
        print("Invalid option.")

menu()
