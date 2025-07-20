
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Create a new image (e.g., 800x1200 for a readable list)
width, height = 800, 1200
image = Image.new("RGB", (width, height), color="white")
draw = ImageDraw.Draw(image)

# Load a font (use a default or install a TTF like DejaVuSans)
try:
    font = ImageFont.truetype("DejaVuSans.ttf", 16)  # Adjust path and size as needed
except:
    font = ImageFont.load_default()

# Title
title = "Lesser-Known Vim Commands"
draw.text((width // 2 - len(title) * 4, 20), title, fill="black", font=font)

# List of lesser-known or advanced Vim commands (curated selection)
commands = [
    # Square Bracket Commands
    "[:[range]co[py] {address} - Copy lines to another location",
    "[:[range]t {address} - Same as :copy, synonym",
    ":[range]m[ove] {address} - Move lines to another location",
    ":[range]d - Delete lines into register",
    ":[range]y[ank] - Yank (copy) lines into register",
    ":[range]g[lobal] /pattern/ command - Execute command on matching lines",
    ":[range]v[global] /pattern/ command - Execute command on non-matching lines",
    ":[range]s[ubstitute] /pattern/replacement/[flags] - Substitute text",
    ":[range]j[oin] - Join lines",

    # g-Prefix Commands
    "gJ - Join lines without space",
    "g~ - Swap case of characters",
    "gu - Convert to lowercase",
    "gU - Convert to uppercase",
    "gd - Go to definition of word under cursor",
    "gD - Go to first occurrence in file",
    "gf - Open file under cursor",
    "gq - Format text to textwidth",
    "gn - Select next match of last search",
    "gp - Put text and leave cursor after",

    # Window and Buffer Commands
    ":wincmd {cmd} - Window command (e.g., h, j, k, l)",
    ":tabm[ove] [N] - Move tab to position N",
    ":tabdo command - Run command on all tabs",
    ":argdo command - Run command on all args",
    ":bufdo command - Run command on all buffers",
    ":windo command - Run command on all windows",
    ":vertical split - Split window vertically",
    ":hide - Hide current buffer",

    # Quickfix and Location Lists
    ":cnext - Go to next quickfix error",
    ":cprev - Go to previous quickfix error",
    ":colder - Go to older quickfix list",
    ":cnewer - Go to newer quickfix list",
    ":lnext - Go to next location list item",
    ":lprev - Go to previous location list item",
    ":lopen - Open location list window",
    ":copen - Open quickfix window",

    # Miscellaneous Advanced Commands
    ":hardcopy - Print file",
    ":mkview - Save current view (folds, cursor)",
    ":loadview - Load saved view",
    ":scriptnames - List loaded scripts",
    ":verbose set option? - Show where option was set",
    ":map! - List insert/command mode mappings",
    ":digraphs - Show or define digraphs",
    ":registers - List all registers",
    ":oldfiles - List recently edited files",
    ":history - Show command-line history"
]

# Draw the command list with wrapping
y_text = 60
for cmd in commands:
    lines = textwrap.fill(cmd, width=50).split('\n')  # Wrap text to ~50 chars
    for line in lines:
        draw.text((50, y_text), line, fill="black", font=font)
        y_text += 20
    y_text += 10  # Extra space between commands

# Save as JPEG
image.save("vim_commands.jpg", "JPEG", quality=95)
print("Vim commands list saved as 'vim_commands.jpg'")
