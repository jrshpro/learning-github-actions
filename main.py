import sys

def main():
    print("Hello, CI/CD world!")
    # A simple check to simulate a 'test'
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        print("Test argument found. Exiting with success.")
        sys.exit(0)

if __name__ == "__main__":
    main()
