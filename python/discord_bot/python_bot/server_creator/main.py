from requests import get
import discord
import urllib

url = "http://localhost/password.txt"
file = urllib.request.urlopen(url)

for line in file:
    decoded_line = line.decode("utf-8")
    
TOKEN = decoded_line
##############################################
client = discord.Client()


@client.event
async def on_message(message):
    if message.content.startswith('-begin'):
        channel1 = message.channel #define the channel from which the begin message was sent
        await channel1.send('I need to know the password first.') #send password request to the user
        def check(m):
            return m.content == "Uwe@u$nL9h_YrzUKHrmkh326zX@gbg-5P4&PVa?eT!ES9gR!pu357EGC6aeM#p4M2jfAha$7nThs684mB5_Wrj&ub3X3dZ?zChu_vdvv4=*W#A^k2N3cKbJkhmxNX8p5qS2eJTv4auX^AjakcxXFV9L$xD%!WyjP7g^f!74TzYEVX+J5!Q3!U68xj?^HfrUb9G!8E9%S266dDW!gDV9$E^!@5-DyyEQAuM%BKrkH29sUaa%mZZ&xDvAh^EF$" and m.channel == channel1 #define password
        msg = await client.wait_for('message', check=check) #if password is said then continue
        await channel1.send('It begins.') 
        embedVar = discord.Embed(title="Heisenberg Bot", description="", color=0x058bff) #create embed and other fields
        embedVar.add_field(name="Announcement", value="This server is now beginning automatic maintenance by the Heisenberg Bot. Thank you for using this server.", inline=False)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/838114727816462356/549cd61912d8c2fd3f7d912d84e8ffb3.webp?size=2048")
        embedVar.set_author(name="Created by skee#0855", icon_url="https://cdn.discordapp.com/avatars/250019320875188224/e2880238f7650b9564e86b8b6b8593b5.webp?size=128")
        channel2 = client.get_channel(825209843106840621) #get channel from bot and define it
        await channel2.send(embed=embedVar) #send embed

    if message.content.startswith('-startroles'):
        guild = message.guild

        #create roles
        await guild.create_role(name="Drug Lord", color=discord.Color(0x058bff), hoist=1, permissions=discord.Permissions(permissions=8))
        await guild.create_role(name="Chairman", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=8))
        await guild.create_role(name="Chief Executive Officer", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=8))
        await guild.create_role(name="Chief Financial Officer", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Corporate President", color=discord.Color(0x15992a), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Vice President", color=discord.Color(0x012c7c), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Board of Directors", color=discord.Color(0x95a5a6), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Director", color=discord.Color(0x0f1233), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Independent Director", color=discord.Color(0xff00f4), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Real Estate Agent", color=discord.Color(0x0065c4), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Investor", color=discord.Color(0xfcd42e), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        


    if message.content.startswith('-startchannels'):
        guild = message.guild
        
        #define major roles
        Chairman=discord.utils.get(guild.roles, name="Chairman")
        DrugLord=discord.utils.get(guild.roles, name="Drug Lord")
        Director=discord.utils.get(guild.roles, name="Director")

        #define normal roles
        IndependentDirector=discord.utils.get(guild.roles, name="Independent Director")
        CorporatePresident=discord.utils.get(guild.roles, name="Corporate President")
        VicePresident=discord.utils.get(guild.roles, name="Vice President")
        BoardofDirectors=discord.utils.get(guild.roles, name="Board of Directors")
        RealEstateAgent=discord.utils.get(guild.roles, name="Real Estate Agent")
        Investor=discord.utils.get(guild.roles, name="Investor")
        ChiefFinancialOfficer=discord.utils.get(guild.roles, name="Chief Financial Officer")

        #create overwritten perms for director, owner and bot roles
        owner_overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=True),
            DrugLord: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            Chairman: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        #create overwrites for normal users.
        normal_user_overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            ChiefFinancialOfficer: discord.PermissionOverwrite(view_channel=False),
            IndependentDirector: discord.PermissionOverwrite(view_channel=True, read_messages=True),
            CorporatePresident: discord.PermissionOverwrite(view_channel=True, read_messages=True),
            VicePresident: discord.PermissionOverwrite(view_channel=True, read_messages=True),
            BoardofDirectors: discord.PermissionOverwrite(view_channel=True, read_messages=True),
            RealEstateAgent: discord.PermissionOverwrite(view_channel=True, read_messages=True),
            Investor: discord.PermissionOverwrite(view_channel=True, read_messages=True)
        }

        #welcome channel overwrites
        welcome_overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False),
            ChiefFinancialOfficer: discord.PermissionOverwrite(view_channel=False),
            IndependentDirector: discord.PermissionOverwrite(view_channel=False),
            CorporatePresident: discord.PermissionOverwrite(view_channel=False),
            VicePresident: discord.PermissionOverwrite(view_channel=False),
            BoardofDirectors: discord.PermissionOverwrite(view_channel=False),
            RealEstateAgent: discord.PermissionOverwrite(view_channel=False),
            Investor: discord.PermissionOverwrite(view_channel=False)
        }

        #set announcement permissions
        important_overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False),
            Director: discord.PermissionOverwrite(view_channel=True, send_messages=True),
            DrugLord: discord.PermissionOverwrite(view_channel=True, send_messages=True),
            Chairman: discord.PermissionOverwrite(view_channel=True, send_messages=True)
        }

        #create categories in order
        await guild.create_category_channel(name="Important", overwrites=important_overwrites)
        important_category=discord.utils.get(guild.categories, name="Important")
        await guild.create_category_channel(name="Office", overwrites=normal_user_overwrites)
        text_category=discord.utils.get(guild.categories, name="Office")
        await guild.create_category_channel(name="Director+", overwrites=important_overwrites)
        staff_category=discord.utils.get(guild.categories, name="Director+")



        await guild.create_text_channel(name="welcome", overwrites=welcome_overwrites)
        await guild.create_text_channel(name="senior-bot-commands", category=staff_category, overwrites=important_overwrites)
        await guild.create_text_channel(name="important-memorandums", category=important_category, overwrites=important_overwrites)
        await guild.create_text_channel(name="role-explanation", category=important_category, overwrites=owner_overwrites)
        await guild.create_text_channel(name="general", category=text_category, overwrites=normal_user_overwrites)
        await guild.create_text_channel(name="out-of-context", category=text_category, overwrites=normal_user_overwrites)

    if message.content.startswith('-startannouncements'):

        embedVar = discord.Embed(title="Role Explanation", description="This channel will explain to you the different roles of the company.", color=0x058bff) #create embed and other fields
        embedVar.add_field(name="Director", value="Primary member of the Board of Directors.", inline=False)
        embedVar.add_field(name="Independent Director", value="Director not associated with the company. Can still be on the board (AKA Senior Associate). Assigned to partners that do not belong to the business.", inline=False)
        embedVar.add_field(name="Logistics", value="People who create & develop the functionings of a business.", inline=False)
        embedVar.add_field(name="Manufacturing", value="Producers of goods of any type.", inline=False)
        embedVar.add_field(name="Real Estate", value="Business that sell land, houses, and other type of property.", inline=False)
        embedVar.add_field(name="Food and Beverage", value="Businesses responsible for the sale of consumable items.", inline=False)
        embedVar.add_field(name="Wholesale", value="Businesses responsible for the sale of merchandise to retailers", inline=False)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/838114727816462356/549cd61912d8c2fd3f7d912d84e8ffb3.webp?size=2048")
        embedVar.set_author(name="Created by skee#0855", icon_url="https://cdn.discordapp.com/avatars/250019320875188224/e2880238f7650b9564e86b8b6b8593b5.webp?size=128")
        channel = client.get_channel(848711421743464448) #get channel from bot and define it
        await channel.send(embed=embedVar) #send embed

        embedVar = discord.Embed(title="Heisenberg Bot", description="", color=0x058bff) #create embed and other fields
        embedVar.add_field(name="Announcement", value="Maintenance is now finished. Thank you for your patience.", inline=False)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/838114727816462356/549cd61912d8c2fd3f7d912d84e8ffb3.webp?size=2048")
        embedVar.set_author(name="Created by skee#0855", icon_url="https://cdn.discordapp.com/avatars/250019320875188224/e2880238f7650b9564e86b8b6b8593b5.webp?size=128")
        channel = client.get_channel(848711421017063464) #get channel from bot and define it
        await channel.send(embed=embedVar) #send embed


        embedVar = discord.Embed(title="Heisenberg Bot", description="", color=0x058bff) #create embed and other fields
        embedVar.add_field(name="Welcome!", value="Hello and welcome to Skeeshaw's Corporation. Here, the role structure follows what you would usually see in a company. Whether you are an invited guest or a new member I hope you enjoy your stay!", inline=False)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/838114727816462356/549cd61912d8c2fd3f7d912d84e8ffb3.webp?size=2048")
        embedVar.set_author(name="Created by skee#0855", icon_url="https://cdn.discordapp.com/avatars/250019320875188224/e2880238f7650b9564e86b8b6b8593b5.webp?size=128")
        channel = client.get_channel(848711419448262706) #get channel from bot and define it
        await channel.send(embed=embedVar) #send embed


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)