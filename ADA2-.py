def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Programa principal
def main():
    while True:
        # Solicitar al usuario la cantidad de números y los números mismos
        cantidad = int(input("Ingrese la cantidad de números a ordenar: "))
        numeros = []
        for i in range(cantidad):
            numero = int(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)
        
        # Mostrar opciones de método de ordenamiento
        print("\nSeleccione el método de ordenamiento:")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix Sort")
        opcion = int(input("Ingrese el número de la opción deseada: "))

        # Ejecutar el método seleccionado
        if opcion == 1:
            print("\nUsando ShellSort...")
            resultado = shell_sort(numeros.copy())
        elif opcion == 2:
            print("\nUsando Quicksort...")
            resultado = quicksort(numeros.copy())
        elif opcion == 3:
            print("\nUsando Heapsort...")
            resultado = heapsort(numeros.copy())
        elif opcion == 4:
            print("\nUsando Radix Sort...")
            if all(num >= 0 for num in numeros): # Radix Sort solo funciona con números no negativos
                resultado = radix_sort(numeros.copy())
            else:
                print("Radix Sort solo funciona con números no negativos.")
                continue
        else:
            print("Opción no válida.")
            continue

        # Mostrar resultado
        print("Lista ordenada:", resultado)

        # Preguntar al usuario si desea volver a ejecutar el programa
        repetir = input("\n¿Desea ordenar otra lista? (s/n): ").strip().lower()
        if repetir != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()