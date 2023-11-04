def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")
        
def print_row(width):
    print("?" * width)
    
def print_square(size):
    for linhas in range(size):
        print_row_square(size)

def print_row_square(size):
    print("#" * size)
main()