RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

THEMES = {
    "1": ("Catppuccin Mocha", "themes/catppuccin-mocha.properties"),
    "2": ("Dracula", "themes/dracula.properties"),
    "3": ("Nord", "themes/nord.properties")
}

PACKAGES = {
    "1": ("Fastfetch", "fastfetch"),
    "2": ("ZSH", "zsh"),
    "3": ("Starship", "starship"),
    "4": ("Neovim", "neovim"),
    "5": ("Vim", "vim"),
}

EXCLUSIVE_GROUPS = [
    {"vim", "neovim"}
]
