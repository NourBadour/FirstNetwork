def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for bit in binary:
        if bit == '1':
            decimal += 2 ** power
        elif bit != '0':
            return None  # Invalid binary digit
        power -= 1
    return decimal
def main():
    binary = input("Enter a binary number: ")
    decimal = binary_to_decimal(binary)
    if decimal is not None:
        print(f"The decimal equivalent of {binary} is {decimal}.")
    else:
        print("Conversion failed. Please check the input.")
if __name__ == "__main__":
    main()
