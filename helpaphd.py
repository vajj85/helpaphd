import sys
import os

# throws when no argument is given
if len(sys.argv) <= 1:
        print("please input a file you would like to read as an argument")
        exit (1)

def main():
    
    filepath = sys.argv[1]

    # throws if file can not be found to read
    if not os.path.isfile(filepath):
        print ("File could not be found. Please try again")
        exit(1)

    # reads file specified by user
    with open(sys.argv[1], 'r') as problems:
        cases = int(problems.readline())
        cnt = 0
        # loop iterates through file and completes arithmetic and completes
        # on number cases specified in document
        for lines in problems:
            if cnt == cases:
                file.close(problems)
                exit(1)
            elif lines.strip('\n') == "P=NP":
                print("skipped")
            else:
                num1 = int(lines.split('+')[0])
                num2 = int(lines.split('+')[1])
                final = num1 + num2
                print final
                
            cnt += 1


if __name__ == "__main__":
    main()
