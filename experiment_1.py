try:
    with open("/content/drive/MyDrive/single_inputs.txt", "r") as file:
        line = file.readline().strip()  
        a, b, c, x = map(float, line.split()) 
    y = a * x**2 + b * x + c
    print(f"The computed weather output (y) is: {y}")
except FileNotFoundError:
    print("Error: Input file 'weather_input.txt' not found.")
except ValueError:
    print("Error: Invalid data format in the input file.")

Output:
The computed weather output (y) is: 23.92
