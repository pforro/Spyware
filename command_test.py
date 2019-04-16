from subprocess import check_output


def main():
    output = check_output('cd c:\\ && tree',shell=True, encoding='437')
    print(output)



if __name__ == "__main__":
    main()
