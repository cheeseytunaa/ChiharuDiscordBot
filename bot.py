import discord
from discord.ext import commands

#The bot was coded by _NooberrUwU#7418.
#Do not change any code line in here.
#To change the config of the bot (such as TOKEN, PREFIX,...), change them in ./data/config.json
#Any error occurs in runtime, please let me know and I will fix it ASAP 

import json
import random
import datetime

with open("./data/config.json","r") as data:
    data = json.load(data)
    token = data["token"]
    prefix = data["prefix"]

bot = commands.Bot(command_prefix=prefix)

bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot is ready!")
    print("This bot was coded by _NooberrUwU#7418")
    print("Any bug in runtime will be logged in here.")
    print("If you want to turn off the bot, press CTRL + C at the same time.")

@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.UserNotFound):
            await ctx.send("😣 User not found! Please input a valid mention!")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("🤔 Command not found! To see the menu of commands, do: ```!help```")
        else:
            print(error)

@bot.command()
async def saveprofile(ctx, *args):
    authorId = ctx.author.id
    authorUsername = ctx.author.name
    authorDiscriminator = ctx.author.discriminator
    authorFullUsername = authorUsername + "#" + authorDiscriminator
    try:
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
            data = json.load(data1)
        data[str(authorId)]
        await ctx.send("🤔 Your profile exists in our data file!")
    except:
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
            data = json.load(data1)
        data[str(authorId)] = {}
        sc = data[str(authorId)]
        sc["irl_name"] = ""
        sc["date_of_birth"] = []
        sc["gender"] = ""
        sc["ig_name"] = ""
        sc["discord"] = authorFullUsername
        sc["gaming"] = []
        sc["description"] = ""
        sc["intamacy"] = {}
        sc["intamacy"]["girl_friend"] = ""
        sc["intamacy"]["boy_friend"] = ""
        sc["intamacy"]["best_friend"] = []
        sc["intamacy"]["friend"] = []
        with open("./data/profile.json","w") as data1:
            json.dump(data,data1,indent=2)

        await ctx.send("👌 Your profile has been saved!\n```To config the profile, do: !configprofile (KEY) (DATA)\nTo delete the profile, do: !deleteprofile  *This command is on 5s cooldown!```")
        # preparation: cooldown setup but i would like to set them up later

@bot.command()
async def deleteprofile(ctx, *args):
    authorId = ctx.author.id
    try:
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
            data = json.load(data1)
        data[str(authorId)]

        data.pop(str(authorId))
        with open("./data/profile.json","w", errors='ignore',encoding='utf-8') as data1:
            json.dump(data,data1,indent=2)
        await ctx.send("😥 Your profile has been deleted! You can create one again, we'll wait you comeback!")
    except:
        await ctx.send("😓 You haven't create a profile, create one!")

@bot.command()
async def configprofile(ctx, *args):
    authorId = ctx.author.id
    availableKeyObject = ["irl_name","date_of_birth","gender","ig_name","gaming","description","girl_friend","boy_friend","best_friend","friend"]
    specialKeyObject_1 = ["date_of_birth","gender"]
    specialKeyObject_2 = ["gaming"]
    specialKeyObject_3 = ["boy_friend","girl_friend"]
    specialKeyObject_4 = ["best_friend","friend"]

    if len(args) == 0:
        await ctx.send("__**Profile configurations command: !configprofile (KEY) (DATA)**__\nThe key here is the property which you want to config.\n```irl_name (string): In-real-life name\n\ndate_of_birth (list): Birthday\n!configprofile date_of_birth (DAY) (MONTH) (YEAR)\n\ngender (string): Gender\n!configprofile gender (1, 2, 3, 4)\n1 or Male: Male\n2 or Female: Female\n3: LGBT\n4: Don't want to say\n\ngaming (list): Your favourite game list\n\ndescription (string): Describe about yourself\n\n*Intamacy:\nboy_friend / girl_friend (string): You epic husband/wife\nbest_friend (list): A list contains all your best-friends, whom always help you\nfriend (list): Normal friend```")
    elif len(args) >= 2:
        try:
            with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
                data = json.load(data1)
            data[str(authorId)]

            key_object = args[0]

            if key_object in availableKeyObject and key_object not in specialKeyObject_1:
                if len(args) == 2:
                    input_data = args[1].replace("\'","\\\'")
                elif len(args) > 2:
                    input_data = args[1:len(args)]
                    input_data = " ".join(input_data).replace("\'","\\\'")
            elif key_object in availableKeyObject and key_object == "date_of_birth":
                if len(args) == 4:
                    try:
                        day = int(args[1])
                        month = int(args[2])
                        year = int(args[3])
                        input_data = [str(day),str(month),str(year)]
                    except:
                        await ctx.send("⚠ The day, month, year must be in INTEGER type!")
                        return
                else:
                    await ctx.send("🤔 Seems you wanted to set your date of birth, but you have done it with incorrect syntax! Please use: ```!configprofile date_of_birth (DAY) (MONTH) (YEAR)```\n***__Developer note:__** You must input the date in INTEGER value! Our algorithm will calculate your age. (It can even minus the age by 1 if you haven't passed the birthday in that current year)")
                    return
            elif key_object in availableKeyObject and key_object == "gender":
                input_data = args[1]
                if input_data.lower() in ["male","1"]:
                    input_data = "Male"
                elif input_data.lower() in ["female","2"]:
                    input_data = "Female"
                elif input_data == "3":
                    input_data = "I'm from LGBT Community 🏳‍🌈"
                elif input_data == "4":
                    input_data = "I don't want to say my gender."
                else:
                    await ctx.send("😫 Sorry, \"{}\" is not a valid gender type!".format(args[1]))
                    return
            else:
                await ctx.send("😢 Sorry, we haven't supported \"{}\" as an available information! You can use everything in our available information list: ```{}```".format(args[0],", ".join(availableKeyObject)))
                return

            with open("./data/profile.json","r", errors="ignore", encoding="utf-8") as data1:
                data = json.load(data1)

            if key_object in specialKeyObject_2:
                data[str(authorId)][key_object].append(input_data)
            elif key_object in specialKeyObject_3:
                data[str(authorId)]["intamacy"][key_object] = input_data
            elif key_object in specialKeyObject_4:
                data[str(authorId)]["intamacy"][key_object].append(input_data)
            else:
                data[str(authorId)][key_object] = input_data

            with open("./data/profile.json","w", errors="ignore", encoding="utf-8") as data1:
                json.dump(data,data1,indent=2)

            await ctx.send("👍 Data saved:\n**Property:** {}\n**Data**: {}".format(key_object,input_data))
        except:
            await ctx.send("😓 You haven't create a profile, create one!")
    else:
        await ctx.send("☹ Incorrect syntax! To see the guide to use this command, type this command without any argument: ```!configprofile```")

@bot.command()
async def resetproperty(ctx, *args):
    authorId = ctx.author.id
    if len(args) == 1:
        key = args[0]
        clearableKeyObject = ["gaming","best_friend","friend"]
        if key in clearableKeyObject and key == "gaming":
            try:
                with open("./data/profile.json","r") as data1:
                    data = json.load(data1)
                data[str(authorId)][key] = []
                with open("./data/profile.json","w") as data1:
                    json.dump(data,data1,indent=2)
                await ctx.send("👍 Your \"{}\" property in our data file has been reset!".format(key))
            except:
                await ctx.send("😓 You haven't create a profile, create one!")
        elif key in clearableKeyObject and key != "gaming":
            try:
                with open("./data/profile.json","r") as data1:
                    data = json.load(data1)
                data[str(authorId)]["intamacy"][key] = []
                with open("./data/profile.json","w") as data1:
                    json.dump(data,data1,indent=2)
                await ctx.send("👍 Your \"{}\" property in our data file has been reset!".format(key))
            except:
                await ctx.send("😓 You haven't create a profile, create one!")
        else:
            await ctx.send("🤨 \"{}\" is not one of the clearable keys!".format(key))
    else:
        await ctx.send("⚠ Missing arguments!")

@bot.command()
async def profile(ctx, *users : discord.User):
    if len(users) == 0:
        author = ctx.author
    elif len(users) == 1:
        author = users[0]

    try:
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
            data = json.load(data1)
        data[str(author.id)]
    except:
        await ctx.send("🥶 " + author.name + " hasn't set up a profile, create one!")
        raise

    authorId = author.id
    authorAvatar = author.avatar_url

    key_1 = ["irl_name","date_of_birth","gender","ig_name","discord","gaming","description"]
    r1 = []

    key_2 = ["girl_friend","boy_friend","best_friend","friend"]
    r2 = []

    def check_key_1(key):
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
            data = json.load(data1)
        result_key = data[str(authorId)][key]
        if result_key:
            return True
        else:
            return False

    def get_key_1(key):
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
            data = json.load(data1)
        return data[str(authorId)][key]

    def check_key_2(key):
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
            data = json.load(data1)
        result_key = data[str(authorId)]["intamacy"][key]
        if result_key:
            return True
        else:
            return False

    def get_key_2(key):
        with open("./data/profile.json","r", errors='ignore',encoding='utf-8') as data1:
            data = json.load(data1)
        return data[str(authorId)]["intamacy"][key]

    for x in key_1:
        if check_key_1(x) == True:
            r1.append(get_key_1(x))
        elif check_key_1(x) == False:
            r1.append("No information.")

    for x in key_2:
        if check_key_2(x) == True:
            r2.append(get_key_2(x))
        elif check_key_2(x) == False:
            r2.append("No information.")

    if get_key_1("date_of_birth"):
        current_year = datetime.datetime.now().year
        current_day = datetime.datetime.now().day
        current_month = datetime.datetime.now().month
        day = r1[1][0]
        month = r1[1][1]
        year = r1[1][2]

        if day in ["1","2","3","4","5","6","7","8","9"]:
            day = "0" + day
        if month in ["1","2","3","4","5","6","7","8","9"]:
            month = "0" + month

        dof = day + "/" + month + "/" + year

        if int(month) > current_month:
            age = current_year - int(year) - 1
        elif int(month) == current_month and int(day) < current_day:
            age = current_year - int(year) - 1
        else:
            age = current_year - int(year)
    else:
        dof = "No information."
        age = "No information."

    if get_key_1("gaming"):
        gaming = ', '.join(r1[5])
    else:
        gaming = "No information."

    if get_key_2("best_friend"):
        best_friend = ', '.join(r2[2])
    else:
        best_friend = "No information."

    if get_key_2("friend"):
        friend = ', '.join(r2[3])
    else:
        friend = "No information."

    title = data[str(authorId)]["discord"] + "'s profile:"
    desc = "*{}*\n\nReal name: **{}**\nDate of birth: **{}**\nAge: **{}**\nGender: **{}**\nIn-game name: **{}**\nDiscord username: **{}**\nGames: **{}**\n\n__**Intamacy information:**__ \n\t+) Girlfriend: **{}** \n+) Boyfriend: **{}** \n+) Best friend: **{}** \n+) Friend: **{}**".format(r1[6],r1[0],dof,age,r1[2],r1[3],r1[4],gaming,r2[0],r2[1],best_friend,friend)

    EmbedContent = discord.Embed(url="https://youtu.be/dQw4w9WgXcQ",title=title,description=desc,color=int("128def",16))
    EmbedContent.set_thumbnail(url=authorAvatar)
    EmbedContent.set_footer(text="Coded by _NooberrUwU#7418",icon_url="https://cdn.discordapp.com/avatars/472596894464344077/ff9b34721caf6d7da435cf2885156b5d.webp")
    await ctx.send(embed=EmbedContent)

bot.run(token)