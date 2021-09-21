youtube-dl -f bestaudio  ytsearch:"$*" -o - 2>/dev/null | ffplay -nodisp -autoexit -i - &>/dev/null
