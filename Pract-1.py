from collections import Counter
import statistics

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_mode(data):
    data_counter = Counter(data)
    modes = [key for key, value in data_counter.items() if value == max(data_counter.values())]
    return modes

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    return median

def main():
    data = [4, 1, 2, 2, 3, 5, 4, 4]
    
    print(f"Data: {data}")
    
    mean = calculate_mean(data)
    print(f"Mean: {mean}")
    
    mode = calculate_mode(data)
    print(f"Mode: {mode}")
    
    median = calculate_median(data)
    print(f"Median: {median}")

if __name__ == "__main__":
    main()
