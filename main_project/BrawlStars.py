from flask import Flask, request, redirect, render_template, url_for
import random
app = Flask(__name__)


players = {'Mystic_Yarik': {'coins': 0, 'brawlers': ['Shelly'], 'password': '100507', 'trophies': 0, 'tokens': 0},
           'Darryl': {'coins': 0, 'brawlers': ['Shelly'], 'password': '23402', 'trophies': 0, 'tokens': 0}}


@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    all_players = players.keys()
    if request.method == 'POST':
        nickname = request.form['nickname']
        password = request.form['password']
        for i in all_players:
            if i == nickname:
                if players[nickname]['password'] == password:
                    return redirect(url_for('lobby', nickname=nickname, password=password))
        else:
            error = 'Incorrect name or password!'
            return render_template('login.html', error=error)

    return render_template('login.html', error=error)


def random_icon():
    icon_list = ['https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS9Pri8XLiIQypnRIGfu--rz7IW5F8jvqb2RQ'
                 '&usqp=CAU',
                 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQpx-DCME3io4PL-MKRMcvbZynHRvGB_joI7A'
                 '&usqp=CAU',
                 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT20-IXEeTVjXiLyke9U22O3tOzDM35eVjIiw&'
                 'usqp=CAU',
                 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRHnYmLwYTCTdSxoBaogu2YTKT7_T2uzlzoPw'
                 '&usqp=CAU',
                 'https://www.starlist.pro/assets/brawler-bs/Nani.png?v=1',
                 'https://vignette.wikia.nocookie.net/brawlstars/images/5/59/Poco_Portrait.png/revision/latest'
                 '/window-crop/width/200/x-offset/60/y-offset/0/window-width/534/window-height/534?cb=20200513143843',
                 'https://vignette.wikia.nocookie.net/brawlstars/images/f/f0/Piper_Portrait.png/revision/latest/wind'
                 'ow-crop/width/200/x-offset/22/y-offset/0/window-width/534/window-height/534?cb=20200304182144',
                 'https://forum.rebrawl.gg/uploads/userpics/443/nYJLQDBJOB1K5.png',
                 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR2heyQG--v5FFbNWjyCxUCBWtymCzcLTVivQ&u'
                 'sqp=CAU',
                 'https://vignette.wikia.nocookie.net/brawlstars/images/4/46/Darryl_Portrait.png/revision/latest/win'
                 'dow-crop/width/200/x-offset/129/y-offset/0/window-width/534/window-height/534?cb=20200317100419'
                 ]
    icon = random.choice(icon_list)
    return icon


@app.route('/lobby/<nickname>/<password>', methods=['GET', 'POST'])
def lobby(nickname, password):
    trophies = players[nickname]['trophies']
    tokens = players[nickname]['tokens']
    # brawlers = players[nickname]['brawlers']
    # len_brawlers = len(brawlers)
    coins = players[nickname]['coins']
    icon = random_icon()
    return render_template('brawl_lobby.html', nickname=nickname, trophies=trophies, icon=icon, tokens=tokens,
                           password=password, coins=coins)


@app.route('/play/<nickname>/<password>')
def play(nickname, password):
    players[nickname]['tokens'] += 15
    return redirect(url_for('lobby', nickname=nickname, password=password))


@app.route('/your_brawlers/<nickname>/<password>')
def your_brawlers(nickname, password):
    brawlers = players[nickname]['brawlers']
    len_brawlers = len(brawlers)
    return render_template('your_brawlers.html', brawlers=brawlers, len_brawlers=len_brawlers, nickname=nickname,
                           password=password)


@app.route('/get_brawler_big_box/<nickname>/<password>')
def get_big(nickname, password):
    coins = players[nickname]['coins']
    if coins < 200:
        return redirect(url_for('lobby', nickname=nickname, password=password))
    brawler_got = get_brawlers(nickname, 'big')
    link = brawler_got[0]
    brawler_name = brawler_got[1]
    rarity = brawler_got[2]
    nothing = False
    if link == 'https://vignette.wikia.nocookie.net/brawlstars/images/f/f0/Coins.png/revision/latest/scale-to' \
               '-width-down/340?cb=20190801142451&path-prefix=pl':  # nothing
        coins = random.randint(32, 64)
        players[nickname]['coins'] -= 200
        players[nickname]['coins'] += coins
        nothing = True
        return render_template('receive_brawlers_big.html', nothing=nothing, link=link, nickname=nickname,
                               password=password, coins=coins)
    else:  # brawler got
        players[nickname]['coins'] -= 200
        return render_template('receive_brawlers_big.html', link=link, brawler=brawler_name, rarity=rarity,
                               nothing=nothing, nickname=nickname, password=password)


@app.route('/get_brawler/<nickname>/<password>')
def get_brawler(nickname, password):
    nothing = False
    tokens = players[nickname]['tokens']
    if tokens < 20:
        return redirect(url_for('lobby', nickname=nickname, password=password))
    brawler_got = get_brawlers(nickname, 'small')
    link = brawler_got[0]
    brawler_name = brawler_got[1]
    rarity = brawler_got[2]
    if link == 'https://vignette.wikia.nocookie.net/brawlstars/images/f/f0/Coins.png/revision/latest/scale-to-wid' \
               'th-down/340?cb=20190801142451&path-prefix=pl':  # nothing
        coins = random.randint(14, 32)
        nothing = True
        players[nickname]['tokens'] -= 20
        players[nickname]['coins'] += coins
        return render_template('receive_brawlers.html', link=link, nothing=nothing, nickname=nickname,
                               password=password, coins=coins)
    else:  # brawler got
        players[nickname]['tokens'] -= 20
        print('hfehffefefrf')
        return render_template('receive_brawlers.html', link=link, brawler=brawler_name, rarity=rarity,
                               nothing=nothing, nickname=nickname, password=password)


def brawlers_names():
    brawlers_rare = {'Poco': 'https://vignette.wikia.nocookie.net/brawlstars/images/2/24/Poco_Skin-Default.png/revision'
                             '/latest?cb=20190514144055',
                     'El Primo': 'https://vignette.wikia.nocookie.net/brawlstars/images/c/c0/Эль_Примо_Skin-Default.png'
                                 '/revision/latest/top-crop/width/360/height/450?cb=20190918174056&path-prefix=ru',
                     'Barley': 'https://vignette.wikia.nocookie.net/brawlstars/images/5/5a/Барли_Skin-Default.png/revi'
                               'sion/latest?cb=20190105103536&path-prefix=ru',
                     'Rosa': 'https://vignette.wikia.nocookie.net/brawlstars/images/3/34/Rosa_Skin-Default.png/revisi'
                             'on/latest?cb=20200314001007'}
    brawlers_super_rare = {'Carl': 'https://vignette.wikia.nocookie.net/brawlstars/images/4/46/Carl_Skin-Default.png'
                                   '/revision/latest?cb=20200315100242',
                           'Penny': 'https://vignette.wikia.nocookie.net/brawlstars/images/d/d6/Penny_Skin-Default.png'
                                    '/revision/latest?cb=20200225133743',
                           'Darryl': 'https://vignette.wikia.nocookie.net/super-epic-adventure-wiki/images/3/3f/Darry'
                                     'l.png/revision/latest/scale-to-width-down/340?cb=20200416222603',
                           'Jacky': 'https://static.wikia.nocookie.net/3706581b-065f-46e7-9b4b-fc31c31955e3',
                           'Rico': 'https://vignette.wikia.nocookie.net/brawlstars/images/7/71/Rico_Skin-Default.png'
                                   '/revision/latest?cb=20200303150025'}
    brawlers_epic = {'Pam': 'https://vignette.wikia.nocookie.net/brawlstars/images/2/2e/Пэм_Skin-Default.png/revision/'
                            'latest/top-crop/width/360/height/450?cb=20200512141128&path-prefix=ru',
                     'Bibi': 'https://vignette.wikia.nocookie.net/brawlstars/images/a/aa/Биби_Skin-Default.png/'
                             'revision/latest/top-crop/width/360/height/450?cb=20190521173225&path-prefix=ru',
                     'Frank': 'https://vignette.wikia.nocookie.net/brawlstars/images/5/55/Frank_Skin-Default.png/revisi'
                              'on/latest?cb=20191023114801',
                     'Bea': 'https://vignette.wikia.nocookie.net/brawlstars/images/7/73/Bea_Skin-Default.png/revision'
                            '/latest?cb=20200607124917',
                     'Nani': 'https://vignette.wikia.nocookie.net/brawlstars/images/2/20/Nani_Skin-Default.png/revision'
                             '/latest?cb=20200530181043',
                     'Piper': 'https://vignette.wikia.nocookie.net/brawlstars/images/5/5d/Piper_Skin-Default.png/revisi'
                              'on/latest?cb=20200225201844'}
    brawlers_mythic = {'Mortis': 'https://vignette.wikia.nocookie.net/brawlstars/images/b/b2/Mortis_Skin-Default.png/r'
                                 'evision/latest?cb=20200520104613',
                       'Sprout': 'https://vignette.wikia.nocookie.net/brawlstars/images/e/ec/Sprout_Skin-Default.png/'
                                 'revision/latest?cb=20200522051055',
                       'Gene': 'https://cdn140.picsart.com/310924459281211.png?type=webp&to=min&r=640',
                       'Tara': 'https://vignette.wikia.nocookie.net/brawlstars/images/a/a7/Tara_Skin-Default.png/r'
                               'evision/latest?cb=20200713183458',
                       'Mr.P': 'https://vignette.wikia.nocookie.net/brawlstars/images/a/a4/Mr._P_Skin-Default.png/r'
                               'evision/latest?cb=20200517073422',
                       'Max': 'https://vignette.wikia.nocookie.net/brawlstars/images/3/33/Max_Skin-Default.png/r'
                              'evision/latest?cb=20200225145047'}
    brawlers_legendary = {'Crow': 'https://i.pinimg.com/originals/55/4a/ed/554aed6000d74ae8db4e6cad6503158b.png',
                          'Leon': 'https://vignette.wikia.nocookie.net/brawlstars/images/6/62/Леон_Skin-Default.png/r'
                                  'evision/latest?cb=20200510055059&path-prefix=ru',
                          'Spike': 'https://vignette.wikia.nocookie.net/brawlstars/images/8/8e/Spike_Skin-Default.png/r'
                                   'evision/latest?cb=20200712190313',
                          'Sandy': 'https://vignette.wikia.nocookie.net/brawlstars/images/8/80/Sandy_Skin-Default.png/'
                                   'revision/latest?cb=20200226195634'}
    brawlers_chromatic = {'Surge': 'https://static.wikia.nocookie.net/f25ec87f-92e1-4775-a30a-72fbc1ee2866',
                          'Gale': 'https://vignette.wikia.nocookie.net/brawlstars/images/1/1e/Gale_Skin-Default.png'
                                  '/revision/latest?cb=20200517073852'}
    nothing = {'link': 'https://vignette.wikia.nocookie.net/brawlstars/images/f/f0/Coins.png/revision/latest/scale-to-'
                       'width-down/340?cb=20190801142451&path-prefix=pl'}
    brawler_names = {'rare': brawlers_rare, 'super_rare': brawlers_super_rare, 'epic': brawlers_epic,
                     'mythic': brawlers_mythic, 'legendary': brawlers_legendary, 'chroma': brawlers_chromatic,
                     'nothing': nothing}
    return brawler_names


def stop():
    return 'You cannot open boxes anymore, because you have all Brawlers!'


def get_random_brawler_small():
    brawler_chance = ['Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!',
                      'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!',
                      'Epic!', 'Epic!', 'Epic!',
                      'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!',
                      'Legendary!',
                      'Chromatic!']
    brawler_got = random.choice(brawler_chance)
    return brawler_got


def get_random_brawler_big():
    brawler_chance = ['Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                      'Nothing!', 'Nothing!', 
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                      'Rare!', 'Rare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                      'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!',
                      'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!',
                      'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!',
                      'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!',
                      'Mythic!', 'Mythic!', 'Mythic!',
                      'Legendary!', 'Legendary!', 'Legendary!',
                      'Chromatic!', 'Chromatic!', 'Chromatic!']
    brawler_got = random.choice(brawler_chance)
    print(brawler_chance.count('Nothing!'))
    return brawler_got


def get_brawlers(nickname, box):
    acc = players[nickname]
    brawlers = acc['brawlers']
    coins = players[nickname]['coins']
    len_brawlers = len(brawlers)
    brawler_names = brawlers_names()
    brawlers_rare = brawler_names['rare'].keys()
    brawlers_rare = list(brawlers_rare)
    brawlers_super_rare = brawler_names['super_rare'].keys()
    brawlers_super_rare = list(brawlers_super_rare)
    brawlers_epic = brawler_names['epic'].keys()
    brawlers_epic = list(brawlers_epic)
    brawlers_mythic = brawler_names['mythic'].keys()
    brawlers_mythic = list(brawlers_mythic)
    brawlers_legendary = brawler_names['legendary'].keys()
    brawlers_legendary = list(brawlers_legendary)
    brawlers_chromatic = brawler_names['chroma'].keys()
    brawlers_chromatic = list(brawlers_chromatic)
    for i in brawlers:
        if i in brawlers_rare:
            brawlers_rare.remove(i)
        if i in brawlers_super_rare:
            brawlers_super_rare.remove(i)
        if i in brawlers_epic:
            brawlers_epic.remove(i)
        if i in brawlers_mythic:
            brawlers_mythic.remove(i)
        if i in brawlers_legendary:
            brawlers_legendary.remove(i)
        if i in brawlers_chromatic:
            brawlers_chromatic.remove(i)

    brawler_got = ''
    if box == 'small':
        brawler_got = get_random_brawler_small()
    if box == 'big':
        brawler_got = get_random_brawler_big()

    if brawler_got == 'Nothing!' or len_brawlers == 28:
        print(brawlers)
        print(len_brawlers)
        print(coins)
        return brawler_names['nothing']['link'], None, None

    elif brawler_got == 'Rare!':
        if brawlers_rare == []:
            return brawler_names['nothing']['link'], None, None
        else:
            brawler_name = random.choice(brawlers_rare)
            acc['brawlers'].append(brawler_name)
            len_brawlers += 1
            link = brawler_names['rare'][brawler_name]
            return link, brawler_name, 'Rare'

    elif brawler_got == 'SuperRare!':
        if brawlers_super_rare == []:
            return brawler_names['nothing']['link'], None, None
        else:
            brawler_name = random.choice(brawlers_super_rare)
            acc['brawlers'].append(brawler_name)
            len_brawlers += 1
            link = brawler_names['super_rare'][brawler_name]
            return link, brawler_name, 'Super rare'

    elif brawler_got == 'Epic!':
        if brawlers_epic == []:
            return brawler_names['nothing']['link'], None, None
        else:
            brawler_name = random.choice(brawlers_epic)
            acc['brawlers'].append(brawler_name)
            len_brawlers += 1
            link = brawler_names['epic'][brawler_name]
            return link, brawler_name, 'Epic'

    elif brawler_got == 'Mythic!':
        if brawlers_mythic == []:
            return brawler_names['nothing']['link'], None, None
        else:
            brawler_name = random.choice(brawlers_mythic)
            acc['brawlers'].append(brawler_name)
            len_brawlers += 1
            link = brawler_names['mythic'][brawler_name]
            return link, brawler_name, 'Mythic'

    elif brawler_got == 'Legendary!':
        if brawlers_legendary == []:
            return brawler_names['nothing']['link'], None, None
        else:
            brawler_name = random.choice(brawlers_legendary)
            acc['brawlers'].append(brawler_name)
            len_brawlers += 1
            link = brawler_names['legendary'][brawler_name]
            return link, brawler_name, 'Legendary'

    elif brawler_got == 'Chromatic!':
        if brawlers_chromatic == []:
            return brawler_names['nothing']['link'], None, None
        else:
            brawler_name = random.choice(brawlers_chromatic)
            acc['brawlers'].append(brawler_name)
            len_brawlers += 1
            link = brawler_names['chroma'][brawler_name]
            return link, brawler_name, 'Chromatic'


if __name__ == '__main__':
    app.run(debug=True)
