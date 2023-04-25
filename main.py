import sys
import subprocess

# TODO: learn what yaml is.
# TODO: learn what Jinja is.
# TODO: Put this on github.





def TxtToMd(inputFile: str = 'test.txt'):
    if len(sys.argv) < 2:
        Title = input('Enter the title of the article: ')
        Date = input('Enter the date of the article (2010-12-03 10:20): ')
        Category = input('Enter the catagory of the article:  ')
    else:
        Title = sys.argv[1]
        Date = sys.argv[2]
        Category = sys.argv[3]

    with open(inputFile, 'r') as f:
        with open(f'Article{Title}.md', 'w') as f2:
            f2.write(f"Title: {Title}\n")
            f2.write(f"Date: {Date}\n")
            f2.write(f"Category: {Category}\n")
            for line in f:
                f2.write(line)


def pelicanGen():
    pass


def BashInPython():
    result = subprocess.run(['bash', '-c', 'ls'], capture_output=True, text=True)
    test = subprocess.run(['bash', '-c', 'touch ditIsEenTest.txt'])
    print(result.stdout)


def Main():
    BashInPython()

    # inputFileName = input('Enter the name of the file to convert: ')
    # TxtToMd(inputFileName)


if __name__ == '__main__':
    Main()