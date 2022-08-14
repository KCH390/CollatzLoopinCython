from cythoncollatzwhileloop import collatz_eval as ce

def main():
    print("*******************************|COLLATZ WIZARD|*******************************")
    print("Give me a number and I will FORCE IT TO BECOME 1 WITH THE POWER OF COLLATZ CONJECTURE MWHAHAHA")
    input_number = int(input())
    steps = ce(input_number)
    print("Wow! that took " + str(steps) + " Collatz steps to convert " + str(input_number) + " to 1!")
    print("******************************************************************************")

if __name__ == "__main__":
    main()


