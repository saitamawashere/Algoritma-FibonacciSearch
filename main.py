def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def fbs_optimization(target_value):
    fib_sequence = fibonacci(10)  # Menggunakan 10 angka Fibonacci sebagai basis pencarian
    best_value = float('inf')
    best_solution = None

    for i in range(len(fib_sequence)):
        x = fib_sequence[i]
        y = target_value - x
        
        # Lakukan perhitungan atau optimisasi berdasarkan nilai x dan y
        
        # Misalnya, hitung nilai f(x) dan f(y) serta cari solusi terbaik
        fx = x**2
        fy = y**2
        
        if fx + fy < best_value:
            best_value = fx + fy
            best_solution = (x, y)
    
    return best_solution

# Main program
if __name__ == '__main__':
    target_value = int(input("Masukkan nilai target: "))
    solution = fbs_optimization(target_value)
    print("Solusi terbaik:", solution)