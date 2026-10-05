import sys

def main():
    # Python lists are dynamic arrays of object references on the heap
    elements = [10, 20, 30, 40, 50]
    
    print(f"List length: {len(elements)}")
    print(f"Base container memory overhead: {sys.getsizeof(elements)} bytes")
    print(f"Elements retain length metadata when passed to functions: len = {len(elements)}")

if __name__ == "__main__":
    main()
