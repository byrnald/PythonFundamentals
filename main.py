# My own Math Utilities Library

def main():
    print(fibonacci(10))


def average(*numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return 0

def clamp(value, min_value=0, max_value=100):
    if value >= min_value and value <= max_value:
        return value
    elif value < min_value: 
        value = min_value
        return value
    else:
        value = max_value
        return value

def celsius_to_fahrenheit(cf):
    return (cf *1.8) + 32

def fahrenheit_to_celcius(fc):
    return (fc - 32) / 1.8 

def is_prime(number):
    is_prime = False
    if number <= 1:
        return is_prime
    for num in range(2,number):
        if number % num == 0:
            return is_prime
    is_prime = True
    return is_prime

def fibonacci(number):
    sequence = []
    bucket_a = 0
    bucket_b = 1
    sequence.append(bucket_a)
    sequence.append(bucket_b)
    for i in range(2, number):
        new_num = (bucket_a) + (bucket_b)  # 0 + 1 = 1, 2, 3
        bucket_a = bucket_b # 1, 1, 2
        bucket_b = new_num # 1, 2, 3
        sequence.append(new_num)
    return sequence


if __name__ == "__main__":
    main()