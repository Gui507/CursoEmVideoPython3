from time import sleep
import emoji
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[1m FELIZ ANO NOVO :tada: :tada:', use_aliases=True))