def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def rulesofengagement():
    print("Welcome")
    userinput = input("Please enter 1 if you have read and agree the statement above to use this toolkit.")
    return userinput

def main():
    prRed("""
  _______    ________                    __   __               _
 |    _  \  |        |                  |  | |  |       /\    | |
 |   / \  \ |________|                  |  | |  |  ___  \/  __| |__
 |  |   |  |   |  |    ___       ___    |  | |  | /  /  __ |__   __|
 |   \_/  /    |  |  /  _  \   /  _  \  |  | |  |/  /  |  |   | |
 |   ____/     |  | |  / \  | |  / \  | |  | |     \   |  |   | |
 |  |          |  | |  \_/  | |  \_/  | |  | |  |\  \  |  |   | |
 |__|          |__|  \_____/   \_____/  |__| |__| \__\ |__|   |_|
""")

rulesofengagement()
main()

