from rich.console import Console
from rich.live import Live
from rich.text import Text
import time

def animate(haystack, needle):
    console = Console()
    m, n = len(haystack), len(needle)
    
    with Live(auto_refresh=True) as live:
        for i in range(m-n+1):
            text = Text(haystack)
            text.stylize("bold red", i, i+n)
            live.update(text)
            time.sleep(0.1)
            if haystack[i:i+n] == needle:
                text.stylize("bold green", i, i+n)
                live.update(text)
                break
    return i

haystack = "the quick brown fox jumps over the lazy dog"
needle = "jumps"
animate(haystack, needle)   
