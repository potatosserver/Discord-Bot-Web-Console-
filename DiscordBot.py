from pathlib import Path
import discord

print(f"\n\n"
      f"....########.....######........########.....#######....########....\n"
      f"....##.....##...##....##.......##.....##...##.....##......##.......\n"
      f"....##.....##...##.............##.....##...##.....##......##.......\n"
      f"....##.....##...##.............########....##.....##......##.......\n"
      f"....##.....##...##.............##.....##...##.....##......##.......\n"
      f"....##.....##...##....##.......##.....##...##.....##......##.......\n"
      f"....########.....######........########.....#######.......##.......\n")

bot = discord.Bot(intents=discord.Intents.all())

for cog in [p.stem for p in Path("cog").glob("*.py")]:
    bot.load_extension(f'cog.{cog}')
    print(f'new_load {cog}.')
print('Done.')
print("\n-------------------------------------------------------------------\n")

bot.run("bot_token")