import sys

def calc_month(leContenu):
    if (leContenu % 2 == 0):
        leContenu = leContenu / 2
        return leContenu
    elif (leContenu % 3 == 0):
        leContenu = leContenu / 3
        return leContenu
    else:
        leContenu = leContenu - 1
        return leContenu


def main():
    contenu = eval(sys.stdin.read())
    count = 0

    while (count != 4):
        contenu = calc_month(contenu)
        count += 1

    print(int(contenu))

if __name__ == "__main__":
    exit(main())