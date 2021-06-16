import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

#The bot was coded by _NooberrUwU#6969.
#Do not change any code line in here.
#To change the config of the bot (such as TOKEN, PREFIX,...), change them in ./data/config.json
#Any error occurs in runtime, please let me know and I will fix it ASAP 

import json
import random
import datetime

#Embed definition
def create_embed(title,color,description):
  return discord.Embed(title=title,color=int(color,16),description=description)

with open("./data/config.json","r") as data:
  data = json.load(data)
  TOKEN = data["token"]
  PREFIX = data["prefix"]

bot = commands.Bot(command_prefix=PREFIX)

bot.remove_command("help")

@bot.event
async def on_ready():
  DiscordComponents(bot)

  print("Bot is ready!")
  print("This bot was coded by _NooberrUwU#6969")
  print("Any bug in runtime will be logged in here.")
  print("If you want to turn off the bot, press CTRL + C at the same time.")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.UserNotFound):
    await ctx.send(embed=create_embed("","ff0000","**User not found! Please input a valid mention!**"))
  elif isinstance(error, commands.CommandNotFound):
    await ctx.send(embed=create_embed("","ff0000",f"**Command not found! To see the menu of commands, do: ```{PREFIX}help```**"))
  else:
    print(error)

@bot.command()
async def saveprofile(ctx):
  authorId = ctx.author.id
  authorFullUsername = f"{ctx.author.name}#{ctx.author.discriminator}"
  try:
    with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
      data = json.load(data_)
    data[str(authorId)]
    await ctx.send(embed=create_embed("","ff0000","**Your profile exists in our data file!**"))
  except:
    with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
      data = json.load(data_)
    data[str(authorId)] = {}
    source_code = data[str(authorId)]
    source_code["irl_name"] = ""
    source_code["date_of_birth"] = []
    source_code["gender"] = ""
    source_code["ig_name"] = ""
    source_code["discord"] = authorFullUsername
    source_code["gaming"] = []
    source_code["description"] = ""
    source_code["intamacy"] = {}
    source_code["intamacy"]["girl_friend"] = ""
    source_code["intamacy"]["boy_friend"] = ""
    source_code["intamacy"]["best_friend"] = []
    source_code["intamacy"]["friend"] = []
    with open("./data/profile.json","w") as data_:
      json.dump(data,data_,indent=2)

    await ctx.send(embed=create_embed("Your profile has been saved!","00ff00",f"""
    *To config the profile, do:* ```{PREFIX}configprofile (KEY) (DATA)```
    *To delete the profile, do:* ```{PREFIX}deleteprofile  *This command is on 5s cooldown!```
    """
    ))

@bot.command()
async def deleteprofile(ctx):
  authorId = ctx.author.id
  try:
    with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
      data = json.load(data_)
    data[str(authorId)]

    await ctx.send(
      embed=create_embed("You are going to execute a dangerous action!","ff0000","""
      **Warning: You can't undo this action, be carefully with your choice!
      Are you sure about that?**
      """),
      components=[[
        Button(style=ButtonStyle.green,label="Yes, delete my profile"),
        Button(style=ButtonStyle.red,label="No, undo the command")]]
    )

    res1 = await bot.wait_for("button_click",check=lambda i: True if i.component.label == "Yes, delete my profile" else False)

    if res1.channel == ctx.channel:
      data.pop(str(authorId))
      with open("./data/profile.json","w", errors='ignore',encoding='utf-8') as data_:
        json.dump(data,data_,indent=2)
      await res1.respond(embed=create_embed("","00ff00","**Your profile has been deleted! You can create one again, we'll wait you comeback!**"))
  except:
    await ctx.send(embed=create_embed("","ff0000","**You haven't create a profile, so I can't remove you from the data file!**"))

@bot.command()
async def configprofile(ctx, *args):
  authorId = ctx.author.id
  availableKeyObject = ["irl_name","date_of_birth","gender","ig_name","gaming","description","girl_friend","boy_friend","best_friend","friend"]
  specialKeyObject_1 = ["date_of_birth","gender"]
  specialKeyObject_2 = ["boy_friend","girl_friend"]
  specialKeyObject_3 = ["best_friend","friend"]

  if len(args) == 0:
    title = "PROFILE CONFIGURATION COMMAND:"
    description = f"""
    *\*Do the command without any argument will display this guide.*
    
    **Available keys:** {", ".join(availableKeyObject)}
    --------------------------------
    **Normal-input keys:**
     ```Syntax: {PREFIX}configprofile (KEY) (DATA)```
    **- irl_name** (String): In-real-life name.
    **- ig_name** (String): In-game name.
    **- gaming** (Append to a list): Your list which consists of favourite games.
    **- description** (String): The text describes about yourself.
    **- girl_friend / boy_friend** (String): Your partner.
    **- best_friend / friend** (Append to a list): The list full of your **best friends** / **friends**. 
    
    *\*Besides, the **"discord"** property displays your discord username, which is automatically filled.*
    --------------------------------
    **Special-input keys:**
      **- date_of_birth**: Display your birthdate.
      ```Syntax: {PREFIX}configdata date_of_birth (DAY) (MONTH) (YEAR)```
      **\*Notes:**
      \t+ The form of time is from Vietnam, so it can be strange for someone who comes from overseas.
      \t+ By the way, that three arguments must be in INTEGER type.
      
      **- gender**: Display your sex (gender).
      ```Syntax: {PREFIX}configdata gender (ARGUMENT)```
      **\*Notes:** The ARGUMENT could be:
      \t+ 1 or MALE: A boy.
      \t+ 2 or FEMALE: A girl.
      \t+ 3: Lesbian Gay Bisexual Transgender.
      \t+ 4: I have no idea.
    """
    await ctx.send(embed=create_embed(title,"00ff00",description))

  else:
    if len(args) > 1:
      try:
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
          data = json.load(data_)
        data[str(authorId)]
        key_object = args[0]
        if key_object in availableKeyObject:
          if key_object not in specialKeyObject_1:
            input_data = " ".join(args[1:len(args)])
          else:
            if key_object == "date_of_birth":
              if len(args) == 4:
                try:
                  day, month, year = int(args[1]),int(args[2]),int(args[3])
                  input_data = [str(day),str(month),str(year)]
                except:
                  await ctx.send(embed=create_embed("","ff0000","**Day, Month, Year must be in integer type!**"))
                  return
              else:
                await ctx.send(embed=create_embed("","ff0000","""
                **Incorrect syntax! Please use:**
                ```!configprofile date_of_birth (DAY) (MONTH) (YEAR)```
                ***__Developer note:__** You must input the date in INTEGER value! Our algorithm will calculate your age.
                (It can even minus the age by 1 if you haven't passed the birthday in the current year)
                """))
                return
            elif key_object == "gender":
              if args[1].lower() in ["male","1"]:
                input_data = "Male"
              elif args[1].lower() in ["female","2"]:
                input_data = "Female"
              elif args[1] == "3":
                input_data = "I'm from LGBT Community 🏳‍🌈"
              elif args[1] == "4":
                input_data = "I don't want to say my gender."
              else:
                await ctx.send(embed=create_embed("","ff0000",f"**\"{args[1]}\" is not a valid gender type!**"))
                return

          if key_object == "gaming":
            data[str(authorId)][key_object].append(input_data)
          elif key_object in specialKeyObject_2:
            data[str(authorId)]["intamacy"][key_object] = input_data
          elif key_object in specialKeyObject_3:
            data[str(authorId)]["intamacy"][key_object].append(input_data)
          else:
            data[str(authorId)][key_object] = input_data

          with open("./data/profile.json","w", errors="ignore", encoding="utf-8") as data_:
            json.dump(data,data_,indent=2)
          await ctx.send(embed=create_embed("","00ff00",f"Data saved!\n**Property:** {key_object}\n**Data**: {input_data}"))

        else:
          await ctx.send(embed=create_embed("","ff0000",f"""
          Sorry, we haven't supported \"{args[0]}\" as an available information!
          You can use everything in our available information list:
          ```{", ".join(availableKeyObject)}```
          """))
      except:
        await ctx.send(embed=create_embed("","ff0000","**You haven't create a profile, create one!**"))
    else:
      await ctx.send(embed=create_embed("","ff0000",f"**Incorrect syntax, for more information, do: ```{PREFIX}configprofile```**"))

@bot.command()
async def resetproperty(ctx, *args):
  authorId = ctx.author.id

  if len(args) == 1:
    key = args[0]
    if key in ["irl_name","date_of_birth","gender","ig_name","gaming","description"]:
      with open("./data/profile.json",errors="ignore",encoding="utf-8") as data_:
        data = json.load(data_)
    else:
      with open("./data/profile.json",errors="ignore",encoding="utf-8") as data_:
        data = json.load(data_)
    if key in ["irl_name","gender","ig_name","description"]:
      data[str(authorId)][key] = ""
    elif key in ["date_of_birth","gaming"]:
      data[str(authorId)][key] = []
    elif key in ["boy_friend","girl_friend"]:
      data[str(authorId)]["intamacy"][key] = ""
    elif key in ["best_friend","friend"]:
      data[str(authorId)]["intamacy"][key] = []
    else:
      await ctx.send(embed=create_embed("","ff0000",f"**\"{key}\" is not one of the clearable keys!**"))
      return
    with open("./data/profile.json","w",errors="ignore",encoding="utf-8") as data_:
      json.dump(data,data_,indent=2)
    await ctx.send(embed=create_embed("","00ff00",f"**Your \"{key}\" property in our data file has been reset!**"))
  else:
    await ctx.send(embed=create_embed("","ff0000",f"**Do: ```{PREFIX}resetproperty (KEY)```**"))

@bot.command()
async def profile(ctx):
  mentions = ctx.message.mentions
  if len(mentions) == 0:
    author = ctx.author
  elif len(mentions) == 1:
    author = mentions[0]

  try:
    with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
      data = json.load(data_)
    data[str(author.id)]
  except:
    await ctx.send(embed=create_embed("","00ffff",f"**{author.name} hasn't set up a profile, create one!**"))
    return

  authorId = author.id
  authorAvatar = author.avatar_url

  key_1 = ["irl_name","date_of_birth","gender","ig_name","discord","gaming","description"]
  result_1 = []

  key_2 = ["girl_friend","boy_friend","best_friend","friend"]
  result_2 = []

  def check_key_1(key):
    with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
      data = json.load(data_)
    result_key = data[str(authorId)][key]
    if result_key:
      return True
    else:
      return False

  def get_key_1(key):
    with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
      data = json.load(data_)
      return data[str(authorId)][key]

  def check_key_2(key):
    with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
      data = json.load(data_)
    result_key = data[str(authorId)]["intamacy"][key]
    if result_key:
      return True
    else:
      return False

  def get_key_2(key):
    with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data_:
      data = json.load(data_)
    return data[str(authorId)]["intamacy"][key]

  for x in key_1:
    if check_key_1(x) == True:
      result_1.append(get_key_1(x))
    else:
      result_1.append("No information.")

  for x in key_2:
    if check_key_2(x) == True:
      result_2.append(get_key_2(x))
    else:
      result_2.append("No information.")

  if get_key_1("date_of_birth"):
    current_year = datetime.datetime.now().year
    current_day = datetime.datetime.now().day
    current_month = datetime.datetime.now().month
    day = result_1[1][0].zfill(2)
    month = result_1[1][1].zfill(2)
    year = result_1[1][2]

    dob = day + "/" + month + "/" + year

    if int(month) > current_month:
      age = current_year - int(year) - 1
    elif int(month) == current_month and int(day) < current_day:
      age = current_year - int(year) - 1
    else:
      age = current_year - int(year)
  else:
    dob = "No information."
    age = "No information."

  if get_key_1("gaming"):
    gaming = ', '.join(result_1[5])
  else:
    gaming = "No information."

  if get_key_2("best_friend"):
    best_friend = ', '.join(result_2[2])
  else:
    best_friend = "No information."

  if get_key_2("friend"):
    friend = ', '.join(result_2[3])
  else:
    friend = "No information."

  title = data[str(authorId)]["discord"] + "'s profile:"
  description = f"""
  *{result_1[6]}*
  
  Real name: **{result_1[0]}**
  Date of birth: **{dob}**
  Age: **{age}**\nGender: **{result_1[2]}**
  In-game name: **{result_1[3]}**
  Discord username: **{result_1[4]}**
  Games: **{gaming}**\n\n__**Intamacy information:**__ 
    +) Girlfriend: **{result_2[0]}** 
    +) Boyfriend: **{result_2[1]}** 
    +) Best friend: **{best_friend}** 
    +) Friend: **{friend}**"""

  EmbedContent = discord.Embed(url="https://youtu.be/dQw4w9WgXcQ",title=title,description=description,color=int("128def",16))
  EmbedContent.set_thumbnail(url=authorAvatar)
  EmbedContent.set_footer(text="Coded by _NooberrUwU#6969",icon_url="https://cdn.discordapp.com/attachments/806189408855785563/854659050862936065/a_4299cc49037979608001d0a8b04f5eb2.gif")
  await ctx.send(embed=EmbedContent)

bot.run(TOKEN)