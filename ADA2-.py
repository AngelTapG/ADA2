def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        print(f"\nGap: {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                print(f"Intercambiando posiciones: {arr}")
            arr[j] = temp
            print(f"Estado actual de la lista: {arr}")
        gap //= 2
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print(f"\nPivote seleccionado: {pivot}")
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"Sublista izquierda: {left}, Pivote(s): {middle}, Sublista derecha: {right}")
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
        print(f"Heapify: intercambiando {arr[i]} con {arr[largest]}")
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"Construyendo heap: {arr}")
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Intercambiando {arr[i]} con {arr[0]}: {arr}")
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
    print(f"Después de Counting Sort en el dígito de exp {exp}: {arr}")

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        print(f"\nOrdenando por el dígito en la posición {exp}")
        counting_sort(arr, exp)
        exp *= 10
    return arr

def main():
    while True:

        cantidad = int(input("Ingrese la cantidad de números a ordenar: "))
        numeros = []
        for i in range(cantidad):
            numero = int(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)
        
        print("\nSeleccione el método de ordenamiento:")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix Sort")
        opcion = int(input("Ingrese el número de la opción deseada: "))

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
            if all(num >= 0 for num in numeros):  
                resultado = radix_sort(numeros.copy())
            else:
                print("Radix Sort solo funciona con números no negativos.")
                continue
        else:
            print("Opción no válida.")
            continue

        print("\nLista ordenada:", resultado)

        repetir = input("\n¿Desea ordenar otra lista? (s/n): ").strip().lower()
        if repetir != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()