# Chiharu Discord Bot Framework

## Introduction
**(The old documentation was removed! We will support and publish a new one as soon as possible)**

With the publish of **[discord.py](https://discordpy.readthedocs.io/en/latest/) v2.0 (Beta - Early access)**, we are developing the new version of **Chiharu Discord Bot v3.0** *(used to be known as HomophobicDiscordBot)* with a special **framework** which works perfectly with the new version of  **[discord.py](https://discordpy.readthedocs.io/en/latest/)** library!

## How to install?
***NOTE**: Please install **Python v3.7 (3.8) or upper versions** *(we do recommend you installing the latest version of Python, which is v3.10 for the smoothest experience)*
Since we're going to use the new beta-version of **[discord.py](https://discordpy.readthedocs.io/en/latest/)**, which is not published to **[pypi.org](https://pypi.org)**, because of that we have to install the library in another way, use this command:
```
In CMD (Windows) / Terminal (MacOS):
	pip install -U git+https://github.com/Rapptz/discord.py
```
Then you can clone or download my repository *(delete unnecessary files if you want to)*, copy the **BOT Token** and put it into your **.env** file:
```
In .env file:
	TOKEN=gbvhdusfh_jjrghuvfjffvrnjd_69420_lmao_shitty_ahhhahahha (or something like that)
```
Run the bot by executing the `bot.py` file in command terminal:
```
In CMD (Windows) / Terminal (MacOS):
	python3 bot.py
	py bot.py (for short, only on Windows)
```
Any error in runtime or you're struggling in turning on the bot? Feel free to message me or create an issue on Github, I'll really appreciate that! *(of course I'll review and fix the bug as soon as possible :D)*

## Developers' zone
Our ***Beta-version*** of **Chiharu Discord Bot v3.0** supports a large number of epic features that developers can modify them! Moreover, we did created a *framework* that not only for our bot, even for your own bots! So let's head into da koding!

*(Since this is the beta-stage, we won't show every feature that the source code contains, but you can find out them by yourself! We will provide you guys a full documentation in near future)*

**1. Language System**
- Yes you did heard right! You can modify our language file, or even create one for yourself!
- Currently in our default language folder, we only support `American English` and `Vietnamese`, but don't worry, you can create a pull request to have a chance for your language to be in our default folder!
- This is how to create a new language file:
	- Step 1: Copy an existed language file and name it as your language code. *(don't have to be English, just any file that you can understand to translate)*
		- `Language code`: A code that contains the name of the language and the dialect which the language uses.
		- Case in point of `Language code`: `en_us` (which means American English), `vi_vi` (which means Vietnamese), etc...
	- Step 2: Edit the language configurations:
		- At the top of the language file, you have to change the property/value of that dictionary:
			```
			"language_configurations": {
				"language": "English",
				"language_name": "American English",
				"country_id": "US",
				"language_id": "en",
				"language_code": "en-US",
				"language_file": "en_us",
				"flag_code": "us",
				"flag_emoji": ":flag_us:"
			}
			```
		- Especially, the `flag_code` property, which supports the flag emoji in `language` command, you can find the codes in `./data/flag_code.json`, the file in which contains country names and their flag codes.
	- Step 3: Now you can translate everything in the file into your language! You don't have to reload the bot, just reload the language with `language` *(change to another language then change it back, sorry for the inconvenience, we'll support a command to reload the language data soon)*
- That's it. You don't have to do anything more than those. The action that you create a new language file, the bot will automatically register that language file in to the source-code, you don't have to worry about the installations, that badboi will do everything left for you!
- **IMPORTANT NOTE**: Somewhere, the data will contain some values which are in a pair of brackets, for example:
```
"info": [
	"There are currently {NUMBER} available languages!",
	"GREEN",
	[
		"They are: **{LANGUAGES}**.",
		"Currently using: **{CURRENT_LANGUAGE}**.",
		"",
		"To change language, click the green button.",
		"For more information about localizations, click the gray button."
	]
]
```
You must keep those bracket *(actually you can remove them but it'll miss the data that we provide)*, you can put those brackets anywhere you want in the string, but please keep them, don't remove those!
- By the way, we also support `Unicode UTF-8` characters, so don't worry about the fact that your language contains non-latin characters :D
For example: `Vietnamese: ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ`

*These are things that we have done the development, but still remains some bugs and unstable statuses, also we're too lazy to write those documentations, so see ya in a later date.*
**2. (Coming soon) Custom property in user profile**
**3. (Coming soon) Support slash commands, custom commands**
**4. (Coming soon) Custom constants, functions and classes in Chiharu Framework**
**5. (Coming soon) Support databases**
**6. (Coming soon) Website, API, change user profile on website**
**7. (Coming soon) Music and Entertainments, Server-moderations**

The `beta-1.0` of `Chiharu Discord Bot v3.0` will be released on `06/18/2022` for developers.
