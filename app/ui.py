from constants import CYAN, RESET

def banner(title):
    print(f"{CYAN}=============================================={RESET}")
    print(f"{CYAN}{title:^46}{RESET}")
    print(f"{CYAN}=============================================={RESET}")
