# # # def replace_var(item, var: str, value: str):
# # #   def replacement(original, string_1, string_2):
# # #     if isinstance(original, str):
# # #       return original.replace(string_1, string_2)
# # #     elif isinstance(original, list):
# # #       return [replacement(i, string_1, string_2) for i in original]

# # #   if isinstance(item, str):
# # #     return replacement(item, var, value)
# # #   elif isinstance(item, list):
# # #     # return [line.replace(var, value) for line in item] # This is the old way / deprecated
# # #     result = []
# # #     for item_inside in item:
# # #       result.append(replacement(item_inside, var, value))
# # #     return result


# # # test = ["{PREFIX}", ["{PREFIX}", "{PREFIX}", ["{PREFIX}", "{PREFIX}"]], [], ""]

# # # print(replace_var(test, "{PREFIX}", "aaaaa"))

# # import chiharu
# # bot.run(chiharu.get_token())


# # n=int(input())
# # for i in range((n-1) * (n-1) + 1,n*n+1):
# #     print(i)
# #     s += i
# # print(s)

# # import bot
# # print(bot.aliases_data)

# # string = """🇦
# # 🇧
# # 🇨
# # 🇩
# # 🇪
# # 🇫
# # 🇬
# # 🇭
# # 🇮
# # 🇯
# # 🇰
# # 🇱
# # 🇲
# # 🇳
# # 🇴
# # 🇵
# # 🇶
# # 🇷
# # 🇸
# # 🇹
# # 🇺
# # 🇻
# # 🇼
# # 🇽
# # 🇾
# # 🇿"""

# # abc = "abcdefghijklmnopqrstuvwxyz"

# # string = string.split("\n")
# # dict = {}

# # for i in range(len(abc)):
# #   dict[abc[i]] = string[i]
  
# # import chiharu

# # chiharu.save_data("data/unicode_regional_indicator.json", dict)
# # print(dict)


# raw_data = """🇦🇨 Flag: Ascension Island
# 🇦🇩 Flag: Andorra
# 🇦🇪 Flag: United Arab Emirates
# 🇦🇫 Flag: Afghanistan
# 🇦🇬 Flag: Antigua & Barbuda
# 🇦🇮 Flag: Anguilla
# 🇦🇱 Flag: Albania
# 🇦🇲 Flag: Armenia
# 🇦🇴 Flag: Angola
# 🇦🇶 Flag: Antarctica
# 🇦🇷 Flag: Argentina
# 🇦🇸 Flag: American Samoa
# 🇦🇹 Flag: Austria
# 🇦🇺 Flag: Australia
# 🇦🇼 Flag: Aruba
# 🇦🇽 Flag: Åland Islands
# 🇦🇿 Flag: Azerbaijan
# 🇧🇦 Flag: Bosnia & Herzegovina
# 🇧🇧 Flag: Barbados
# 🇧🇩 Flag: Bangladesh
# 🇧🇪 Flag: Belgium
# 🇧🇫 Flag: Burkina Faso
# 🇧🇬 Flag: Bulgaria
# 🇧🇭 Flag: Bahrain
# 🇧🇮 Flag: Burundi
# 🇧🇯 Flag: Benin
# 🇧🇱 Flag: St. Barthélemy
# 🇧🇲 Flag: Bermuda
# 🇧🇳 Flag: Brunei
# 🇧🇴 Flag: Bolivia
# 🇧🇶 Flag: Caribbean Netherlands
# 🇧🇷 Flag: Brazil
# 🇧🇸 Flag: Bahamas
# 🇧🇹 Flag: Bhutan
# 🇧🇻 Flag: Bouvet Island
# 🇧🇼 Flag: Botswana
# 🇧🇾 Flag: Belarus
# 🇧🇿 Flag: Belize
# 🇨🇦 Flag: Canada
# 🇨🇨 Flag: Cocos (Keeling) Islands
# 🇨🇩 Flag: Congo - Kinshasa
# 🇨🇫 Flag: Central African Republic
# 🇨🇬 Flag: Congo - Brazzaville
# 🇨🇭 Flag: Switzerland
# 🇨🇮 Flag: Côte d’Ivoire
# 🇨🇰 Flag: Cook Islands
# 🇨🇱 Flag: Chile
# 🇨🇲 Flag: Cameroon
# 🇨🇳 Flag: China
# 🇨🇴 Flag: Colombia
# 🇨🇵 Flag: Clipperton Island
# 🇨🇷 Flag: Costa Rica
# 🇨🇺 Flag: Cuba
# 🇨🇻 Flag: Cape Verde
# 🇨🇼 Flag: Curaçao
# 🇨🇽 Flag: Christmas Island
# 🇨🇾 Flag: Cyprus
# 🇨🇿 Flag: Czechia
# 🇩🇪 Flag: Germany
# 🇩🇬 Flag: Diego Garcia
# 🇩🇯 Flag: Djibouti
# 🇩🇰 Flag: Denmark
# 🇩🇲 Flag: Dominica
# 🇩🇴 Flag: Dominican Republic
# 🇩🇿 Flag: Algeria
# 🇪🇦 Flag: Ceuta & Melilla
# 🇪🇨 Flag: Ecuador
# 🇪🇪 Flag: Estonia
# 🇪🇬 Flag: Egypt
# 🇪🇭 Flag: Western Sahara
# 🇪🇷 Flag: Eritrea
# 🇪🇸 Flag: Spain
# 🇪🇹 Flag: Ethiopia
# 🇪🇺 Flag: European Union
# 🇫🇮 Flag: Finland
# 🇫🇯 Flag: Fiji
# 🇫🇰 Flag: Falkland Islands
# 🇫🇲 Flag: Micronesia
# 🇫🇴 Flag: Faroe Islands
# 🇫🇷 Flag: France
# 🇬🇦 Flag: Gabon
# 🇬🇧 Flag: United Kingdom
# 🇬🇩 Flag: Grenada
# 🇬🇪 Flag: Georgia
# 🇬🇫 Flag: French Guiana
# 🇬🇬 Flag: Guernsey
# 🇬🇭 Flag: Ghana
# 🇬🇮 Flag: Gibraltar
# 🇬🇱 Flag: Greenland
# 🇬🇲 Flag: Gambia
# 🇬🇳 Flag: Guinea
# 🇬🇵 Flag: Guadeloupe
# 🇬🇶 Flag: Equatorial Guinea
# 🇬🇷 Flag: Greece
# 🇬🇸 Flag: South Georgia & South Sandwich Islands
# 🇬🇹 Flag: Guatemala
# 🇬🇺 Flag: Guam
# 🇬🇼 Flag: Guinea-Bissau
# 🇬🇾 Flag: Guyana
# 🇭🇰 Flag: Hong Kong SAR China
# 🇭🇲 Flag: Heard & McDonald Islands
# 🇭🇳 Flag: Honduras
# 🇭🇷 Flag: Croatia
# 🇭🇹 Flag: Haiti
# 🇭🇺 Flag: Hungary
# 🇮🇨 Flag: Canary Islands
# 🇮🇩 Flag: Indonesia
# 🇮🇪 Flag: Ireland
# 🇮🇱 Flag: Israel
# 🇮🇲 Flag: Isle of Man
# 🇮🇳 Flag: India
# 🇮🇴 Flag: British Indian Ocean Territory
# 🇮🇶 Flag: Iraq
# 🇮🇷 Flag: Iran
# 🇮🇸 Flag: Iceland
# 🇮🇹 Flag: Italy
# 🇯🇪 Flag: Jersey
# 🇯🇲 Flag: Jamaica
# 🇯🇴 Flag: Jordan
# 🇯🇵 Flag: Japan
# 🇰🇪 Flag: Kenya
# 🇰🇬 Flag: Kyrgyzstan
# 🇰🇭 Flag: Cambodia
# 🇰🇮 Flag: Kiribati
# 🇰🇲 Flag: Comoros
# 🇰🇳 Flag: St. Kitts & Nevis
# 🇰🇵 Flag: North Korea
# 🇰🇷 Flag: South Korea
# 🇰🇼 Flag: Kuwait
# 🇰🇾 Flag: Cayman Islands
# 🇰🇿 Flag: Kazakhstan
# 🇱🇦 Flag: Laos
# 🇱🇧 Flag: Lebanon
# 🇱🇨 Flag: St. Lucia
# 🇱🇮 Flag: Liechtenstein
# 🇱🇰 Flag: Sri Lanka
# 🇱🇷 Flag: Liberia
# 🇱🇸 Flag: Lesotho
# 🇱🇹 Flag: Lithuania
# 🇱🇺 Flag: Luxembourg
# 🇱🇻 Flag: Latvia
# 🇱🇾 Flag: Libya
# 🇲🇦 Flag: Morocco
# 🇲🇨 Flag: Monaco
# 🇲🇩 Flag: Moldova
# 🇲🇪 Flag: Montenegro
# 🇲🇫 Flag: St. Martin
# 🇲🇬 Flag: Madagascar
# 🇲🇭 Flag: Marshall Islands
# 🇲🇰 Flag: North Macedonia
# 🇲🇱 Flag: Mali
# 🇲🇲 Flag: Myanmar (Burma)
# 🇲🇳 Flag: Mongolia
# 🇲🇴 Flag: Macao Sar China
# 🇲🇵 Flag: Northern Mariana Islands
# 🇲🇶 Flag: Martinique
# 🇲🇷 Flag: Mauritania
# 🇲🇸 Flag: Montserrat
# 🇲🇹 Flag: Malta
# 🇲🇺 Flag: Mauritius
# 🇲🇻 Flag: Maldives
# 🇲🇼 Flag: Malawi
# 🇲🇽 Flag: Mexico
# 🇲🇾 Flag: Malaysia
# 🇲🇿 Flag: Mozambique
# 🇳🇦 Flag: Namibia
# 🇳🇨 Flag: New Caledonia
# 🇳🇪 Flag: Niger
# 🇳🇫 Flag: Norfolk Island
# 🇳🇬 Flag: Nigeria
# 🇳🇮 Flag: Nicaragua
# 🇳🇱 Flag: Netherlands
# 🇳🇴 Flag: Norway
# 🇳🇵 Flag: Nepal
# 🇳🇷 Flag: Nauru
# 🇳🇺 Flag: Niue
# 🇳🇿 Flag: New Zealand
# 🇴🇲 Flag: Oman
# 🇵🇦 Flag: Panama
# 🇵🇪 Flag: Peru
# 🇵🇫 Flag: French Polynesia
# 🇵🇬 Flag: Papua New Guinea
# 🇵🇭 Flag: Philippines
# 🇵🇰 Flag: Pakistan
# 🇵🇱 Flag: Poland
# 🇵🇲 Flag: St. Pierre & Miquelon
# 🇵🇳 Flag: Pitcairn Islands
# 🇵🇷 Flag: Puerto Rico
# 🇵🇸 Flag: Palestinian Territories
# 🇵🇹 Flag: Portugal
# 🇵🇼 Flag: Palau
# 🇵🇾 Flag: Paraguay
# 🇶🇦 Flag: Qatar
# 🇷🇪 Flag: Réunion
# 🇷🇴 Flag: Romania
# 🇷🇸 Flag: Serbia
# 🇷🇺 Flag: Russia
# 🇷🇼 Flag: Rwanda
# 🇸🇦 Flag: Saudi Arabia
# 🇸🇧 Flag: Solomon Islands
# 🇸🇨 Flag: Seychelles
# 🇸🇩 Flag: Sudan
# 🇸🇪 Flag: Sweden
# 🇸🇬 Flag: Singapore
# 🇸🇭 Flag: St. Helena
# 🇸🇮 Flag: Slovenia
# 🇸🇯 Flag: Svalbard & Jan Mayen
# 🇸🇰 Flag: Slovakia
# 🇸🇱 Flag: Sierra Leone
# 🇸🇲 Flag: San Marino
# 🇸🇳 Flag: Senegal
# 🇸🇴 Flag: Somalia
# 🇸🇷 Flag: Suriname
# 🇸🇸 Flag: South Sudan
# 🇸🇹 Flag: São Tomé & Príncipe
# 🇸🇻 Flag: El Salvador
# 🇸🇽 Flag: Sint Maarten
# 🇸🇾 Flag: Syria
# 🇸🇿 Flag: Eswatini
# 🇹🇦 Flag: Tristan Da Cunha
# 🇹🇨 Flag: Turks & Caicos Islands
# 🇹🇩 Flag: Chad
# 🇹🇫 Flag: French Southern Territories
# 🇹🇬 Flag: Togo
# 🇹🇭 Flag: Thailand
# 🇹🇯 Flag: Tajikistan
# 🇹🇰 Flag: Tokelau
# 🇹🇱 Flag: Timor-Leste
# 🇹🇲 Flag: Turkmenistan
# 🇹🇳 Flag: Tunisia
# 🇹🇴 Flag: Tonga
# 🇹🇷 Flag: Turkey
# 🇹🇹 Flag: Trinidad & Tobago
# 🇹🇻 Flag: Tuvalu
# 🇹🇼 Flag: Taiwan
# 🇹🇿 Flag: Tanzania
# 🇺🇦 Flag: Ukraine
# 🇺🇬 Flag: Uganda
# 🇺🇲 Flag: U.S. Outlying Islands
# 🇺🇳 Flag: United Nations
# 🇺🇸 Flag: United States
# 🇺🇾 Flag: Uruguay
# 🇺🇿 Flag: Uzbekistan
# 🇻🇦 Flag: Vatican City
# 🇻🇨 Flag: St. Vincent & Grenadines
# 🇻🇪 Flag: Venezuela
# 🇻🇬 Flag: British Virgin Islands
# 🇻🇮 Flag: U.S. Virgin Islands
# 🇻🇳 Flag: Vietnam
# 🇻🇺 Flag: Vanuatu
# 🇼🇫 Flag: Wallis & Futuna
# 🇼🇸 Flag: Samoa
# 🇽🇰 Flag: Kosovo
# 🇾🇪 Flag: Yemen
# 🇾🇹 Flag: Mayotte
# 🇿🇦 Flag: South Africa
# 🇿🇲 Flag: Zambia
# 🇿🇼 Flag: Zimbabwe"""

# data = raw_data.split('\n')
# data = [item.split(" Flag: ") for item in data]

# epic_dict = {}
# for item in data:
#   epic_dict[item[1]] = item[0]
  
# print(epic_dict)

# import chiharu

# chiharu.save_data("flag_code.json",epic_dict)

# class A:
#   def a(self):
#     print("a")
# class B:
#   def a(self):
#     print("b")
# class C(B,A):
#   def c(self):
#     self.a()
    
# o = C()
# o.c()

# print(__name__)

# from chiharu import *
# user_data_base = {
#   "color": COLORS["CYAN"],
#   "link": "",
#   "image": "",
#   "discord": "a",
#   "irl_name": "",
#   "friendly_name": "",
#   "address": "",
#   "phone_number": "",
#   "nationality": "",
#   "date_of_birth": "",
#   "gender": 0,
#   "ig_name": "",
#   "games": [],
#   "description": "",
#   "school": "",
#   "class": "",
#   "intimacy": {
#     "girl_friend": "",
#     "boy_friend": "",
#     "best_friends": [],
#     "friends": []
#   },
#   "hidden": []
# }
# print(list(user_data_base.keys()))

test = ""

def function_1():
  global test
  test = {"test"}
def function_2():
  function_1()
  print(test)
  
function_2()