# Персонажи

define mc = Character('[mcname]', ctc="ctc_atl", ctc_position="fixed", color="#3d3327", image='mc', callback=name_callback, cb_name="mc")
define j = Character('Женя', ctc="ctc_atl", ctc_position="fixed", color="#3d3327", image='jenya', callback=name_callback, cb_name="jenya")
define t = Character('Тимур', ctc="ctc_atl", ctc_position="fixed", color="#3d3327", image='timur', callback=name_callback, cb_name="timur")
define a = Character('Саша', ctc="ctc_atl", ctc_position="fixed", color="#3d3327", image='alex', callback=name_callback, cb_name="alex")
define e = Character('Ева', color="#3d3327")
define od = Character('Ольга Дмитриевна', ctc_position="fixed", color="#3d3327", image='comenda', callback=name_callback, cb_name="comenda")
define od_un = Character('Коменда', ctc_position="fixed", color="#3d3327", image='comenda', callback=name_callback, cb_name="comenda")
define j_un = Character('???', ctc_position="fixed", color="#3d3327", image='jenya', callback=name_callback, cb_name="jenya")
define a_un = Character('???', ctc_position="fixed", color="#3d3327", image='alex', callback=name_callback, cb_name="alex")
define sh = Character('Шнурок', ctc_position="fixed", color="#3d3327", image='alex', callback=name_callback, cb_name="alex")
define un = Character('???', ctc="ctc_atl", ctc_position="fixed", color="#3d3327")
define mg = Character('Марго', ctc_position="fixed", color="#3d3327")
define u = Character('Уборщик', color="#3d3327")
define bb = Character('Алевтина Павловна', color="#3d3327")
#Теги для сообщений

define mc_nvl = Character("Я", kind=nvl, image="mcimage", callback=Phone_SendSound)
define j_nvl = Character("Женя Лис", kind=nvl, callback=Phone_ReceiveSound)
define a_nvl = Character("Alexander", kind=nvl, callback=Phone_ReceiveSound)
define t_nvl = Character("Тимур", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#Теги для выделения спрайтов

define n = Character(callback=name_callback, cb_name=None)


image jenya normala = At('jenya normal', sprite_highlight('jenya'))
image jenya smilea = At('jenya smile', sprite_highlight('jenya'))
image jenya normal wintera = At('jenya normal winter', sprite_highlight('jenya'))
image jenya surprisea = At('jenya surprise', sprite_highlight('jenya'))
image jenya angrya = At('jenya angry', sprite_highlight('jenya'))
image jenya blusha = At('jenya blush', sprite_highlight('jenya'))
image jenya sada = At('jenya sad', sprite_highlight('jenya'))
image jenya normal smilea = At('jenya normal smile', sprite_highlight('jenya'))
image jenya angry wintera = At('jenya angry winter', sprite_highlight('jenya'))
image jenya blush wintera = At('jenya blush winter', sprite_highlight('jenya'))
image jenya grina = At('jenya grin', sprite_highlight('jenya'))
image jenya grin wintera = At('jenya grin winter', sprite_highlight('jenya'))
image jenya sad wintera = At('jenya sad winter', sprite_highlight('jenya'))
image jenya smile wintera = At('jenya smile winter', sprite_highlight('jenya'))
image jenya surprise wintera = At('jenya surprise winter', sprite_highlight('jenya'))
image jenya thoughtful wintera = At('jenya thoughtful winter', sprite_highlight('jenya'))
image jenya thoughtfula = At('jenya thoughtful', sprite_highlight('jenya'))
image jenya angry handsa = At('jenya angry hands', sprite_highlight('jenya'))
image jenya angry homea = At('jenya angry home', sprite_highlight('jenya'))
image jenya blush handsa = At('jenya blush hands', sprite_highlight('jenya'))
image jenya blush homea = At('jenya blush home', sprite_highlight('jenya'))
image jenya grin handsa = At('jenya grin hands', sprite_highlight('jenya'))
image jenya grin homea = At('jenya grin home', sprite_highlight('jenya'))
image jenya normal handsa = At('jenya normal hands', sprite_highlight('jenya'))
image jenya normal homea = At('jenya normal home', sprite_highlight('jenya'))
image jenya normal smile handsa = At('jenya normal smile hands', sprite_highlight('jenya'))
image jenya normal smile homea = At('jenya normal smile home', sprite_highlight('jenya'))
image jenya normal smile2 handsa = At('jenya normal smile2 hands', sprite_highlight('jenya'))
image jenya sad handsa = At('jenya sad hands', sprite_highlight('jenya'))
image jenya sad homea = At('jenya sad home', sprite_highlight('jenya'))
image jenya smile2 homea = At('jenya smile2 home', sprite_highlight('jenya'))
image jenya smile3 handsa = At('jenya smile3 hands', sprite_highlight('jenya'))
image jenya surprise handsa = At('jenya surprise hands', sprite_highlight('jenya'))
image jenya surprise homea = At('jenya surprise home', sprite_highlight('jenya'))
image jenya thoughtful handsa = At('jenya thoughtful hands', sprite_highlight('jenya'))
image jenya thoughtful homea = At('jenya thoughtful home', sprite_highlight('jenya'))
image jenya yawn homea = At('jenya yawn home', sprite_highlight('jenya'))
image jenya normal smile wintera = At('jenya normal smile winter', sprite_highlight('jenya'))


image mc normala = At('mc normal', sprite_highlight('mc'))
image mc smile crosseda = At('mc smile crossed', sprite_highlight('mc'))
image mc talk crosseda = At('mc talk crossed', sprite_highlight('mc'))
image mc normal wintera = At('mc normal winter', sprite_highlight('mc'))
image mc normal homea = At('mc normal home', sprite_highlight('mc'))
image mc normal handa = At('mc normal hand', sprite_highlight('mc'))
image mc angry crosseda = At('mc angry crossed', sprite_highlight('mc'))
image mc blush handa = At('mc blush hand', sprite_highlight('mc'))
image mc blush homea = At('mc blush home', sprite_highlight('mc'))
image mc blush wintera = At('mc blush winter', sprite_highlight('mc'))
image mc blusha = At('mc blush', sprite_highlight('mc'))
image mc sad crosseda = At('mc sad crossed', sprite_highlight('mc'))
image mc sad handa = At('mc sad hand', sprite_highlight('mc'))
image mc sad homea = At('mc sad home', sprite_highlight('mc'))
image mc sad wintera = At('mc sad winter', sprite_highlight('mc'))
image mc sada = At('mc sad', sprite_highlight('mc'))
image mc smile handa = At('mc smile hand', sprite_highlight('mc'))
image mc smile homea = At('mc smile home', sprite_highlight('mc'))
image mc smile wintera = At('mc smile winter', sprite_highlight('mc'))
image mc smilea = At('mc smile', sprite_highlight('mc'))
image mc surprise handa = At('mc surprise hand', sprite_highlight('mc'))
image mc surprise homea = At('mc surprise home', sprite_highlight('mc'))
image mc surprise wintera = At('mc surprise winter', sprite_highlight('mc'))
image mc surprisea = At('mc surprise', sprite_highlight('mc'))
image mc thoughtful crosseda = At('mc thoughtful crossed', sprite_highlight('mc'))
image mc normal crosseda = At('mc normal crossed', sprite_highlight('mc'))
image mc angry poster = At('mc poster mouth closed', sprite_highlight('mc'))
image mc angry poster2 = At('mc poster mouth opened', sprite_highlight('mc'))
image mc angry homea = At('mc angry home', sprite_highlight('mc'))
image mc very angrya = At('mc very angry', sprite_highlight('mc'))

image mc blush hand ca = At('mc blush hand c', sprite_highlight('mc'))
image mc blush home ca = At('mc blush home c', sprite_highlight('mc'))
image mc normal ca = At('mc normal c', sprite_highlight('mc'))
image mc normal crossed ca = At('mc normal crossed c', sprite_highlight('mc'))
image mc normal hand ca = At('mc normal hand c', sprite_highlight('mc'))
image mc normal home ca = At('mc normal home c', sprite_highlight('mc'))
image mc sad ca = At('mc sad c', sprite_highlight('mc'))
image mc sad crossed ca = At('mc sad crossed c', sprite_highlight('mc'))
image mc sad home ca = At('mc sad home c', sprite_highlight('mc'))
image mc smile ca = At('mc smile c', sprite_highlight('mc'))
image mc smile crossed ca = At('mc smile crossed c', sprite_highlight('mc'))
image mc smile hand ca = At('mc smile hand c', sprite_highlight('mc'))
image mc smile home ca = At('mc smile home c', sprite_highlight('mc'))
image mc surprise ca = At('mc surprise c', sprite_highlight('mc'))
image mc surprise hand ca = At('mc surprise hand c', sprite_highlight('mc'))
image mc surprise home ca = At('mc surprise home c', sprite_highlight('mc'))
image mc talk crossed ca = At('mc talk crossed c', sprite_highlight('mc'))
image mc thoughtful crossed ca = At('mc thoughtful crossed c', sprite_highlight('mc'))

image timur normala = At('timur normal', sprite_highlight('timur'))
image timur normal wintera = At('timur normal winter', sprite_highlight('timur'))
image timur angry wintera = At('timur angry look winter', sprite_highlight('timur'))
image timur normal smilea = At('timur normal smile', sprite_highlight('timur'))
image timur normal homea = At('timur normal home', sprite_highlight('timur'))
image timur sada = At('timur sad', sprite_highlight('timur'))
image timur sad homea = At('timur sad home', sprite_highlight('timur'))
image timur sad wintera = At('timur sad winter', sprite_highlight('timur'))
image timur smilea = At('timur smile', sprite_highlight('timur'))
image timur surprisea = At('timur surprise', sprite_highlight('timur'))
image timur thoughtfula = At('timur thoughtful', sprite_highlight('timur'))
image timur angry homea = At('timur angry home', sprite_highlight('timur'))
image timur angry postera = At('timur angry poster', sprite_highlight('timur'))
image timur harsh = At('timur_s angry home',  sprite_highlight('timur'))
image timur surprise homea = At('timur surprised home', sprite_highlight('timur'))
image timur yell wintera = At('timur yelling winter', sprite_highlight('timur'))
image timur embarrassed homea = At('timur_s smile home', sprite_highlight('timur'))
image timur smile homea = At('timur smile home', sprite_highlight('timur'))
image timur happy homea = At('timur happy home', sprite_highlight('timur'))
image timur smile wintera = At('timur smile winter', sprite_highlight('timur'))
image timur angry wintersa = At('timur angry winter', sprite_highlight('timur'))
image timur very angrya = At('timur very angry', sprite_highlight('timur'))


image alex normala = At('alex normal', sprite_highlight('alex'))
image alex smilea = At('alex smile', sprite_highlight('alex'))
image alex gloomya = At('alex gloomy', sprite_highlight('alex'))

image comenda normal = At('commandant normal', sprite_highlight('comenda'))
image comenda angry = At('commandant angry', sprite_highlight('comenda'))
image comenda smile = At('commandant winter smile', sprite_highlight('comenda'))
image comenda sad = At('commandant winter sad', sprite_highlight('comenda'))
image comenda home normala = At('commandant home', sprite_highlight('comenda'))
image comenda home angrya = At('commandant home angry', sprite_highlight('comenda'))
image comenda home scared = At('commandant home scared', sprite_highlight('comenda'))

image eve silhouette black glow = At('eva silhouette black glow', sprite_highlight('e')) #2 глава Жени
image eve silhouette grey glow = At('eva silhouette grey glow', sprite_highlight('e')) #1 глава Тимура

# звуки
define audio.snow = "audio/sounds/snowsteps.mp3"
define audio.bumaga = "audio/perelist.mp3"
define audio.clock = "audio/sounds/signal.mp3"
define audio.steps = "audio/sounds/steps.mp3"
define audio.ambulance = "audio/sounds/ambulance.mp3"
define audio.ambulance2 = "audio/sounds/ambulance2.mp3"
define audio.stuk = "audio/sounds/stuk.mp3"
define audio.screamer = "audio/sounds/screamer2.wav"
define audio.screamer_short = "audio/sounds/screamer_short.mp3"
define audio.door = "audio/sounds/door.mp3"
define audio.stamp = "audio/sounds/stamp.mp3"
define audio.bibika = "audio/sounds/bibika.mp3"
define audio.amulet = "audio/sounds/amulet_breaks.mp3"
define audio.table = "audio/sounds/hit_table.mp3"
define audio.jenyar = "audio/sounds/jenya_ringtone.mp3"
define audio.pen = "audio/sounds/pen_drop.mp3"
define audio.coffee = "audio/sounds/spill_coffee.mp3"
define audio.tire = "audio/sounds/tire.ogg"
define audio.ruining = "audio/sounds/ruin_room.mp3"
define audio.smash = "audio/sounds/smash.wav"
define auidio.trash = "audio/sounds/trash.mp3"
define audio.scotch = "audio/sounds/scotch.mp3"
define audio.stomach = "audio/sounds/stomach_groaning.mp3"

#эмбиент
define audio.city = "audio/ambient/city.mp3"
define audio.room = "audio/ambient/room.mp3"
define audio.shower = "audio/ambient/shower.mp3"
define audio.park = "audio/ambient/park.mp3"
define audio.birds = "audio/ambient/birds_out.mp3"
define audio.cooking = "audio/ambient/cooking.mp3"
define audio.people = "audio/ambient/people_around.mp3"
define audio.wind = "audio/ambient/winter_wind.mp3"
define audio.shop = "audio/ambient/shop.mp3"
define audio.repair = "audio/ambient/repair.mp3"
define audio.talk = "audio/ambient/talk.mp3"

#музыка
define audio.sincerely = "audio/music/Sincerely.mp3"
define audio.base = "audio/Morning.ogg"
define audio.evening = "audio/music/Past Sadness.mp3"
define audio.wholesome = "audio/music/Wholesome.mp3"
define audio.cozy = "audio/music/Cozy.mp3"
define audio.crossroads = "audio/music/Crossroads.mp3"
define audio.sadness = "audio/music/Happy-Sad.mp3"
define audio.chill = "audio/music/Chill.mp3"
define audio.darkrooms = "audio/music/DarkRooms.mp3"
define audio.mystery = "audio/music/EvaMemories.mp3"
define audio.funny = "audio/music/Funny.mp3"
define audio.circus = "audio/music/DailyCircus.mp3"
define audio.home = "audio/music/Home.mp3"
define audio.knowledge = "audio/music/Knowledge.mp3"
define audio.leaves = "audio/music/Leaves.mp3"
define audio.sunshine = "audio/music/Sunshine.mp3"
define audio.together = "audio/music/Together.mp3"
define audio.bright = "audio/music/PiensoViento.mp3"

# Переменные

init:
    $ right2 = Position (xalign=0.8, yalign=1.005)
    $ left2 = Position (xalign=0.2, yalign=1.005)

# Переменные отношений
default maxrelate = 100
default minrelate = 0

default relate_jenya = 0
default relate_timur = 0
default relate_alex = 0
default relate_eve = 0


#with moveoutleft\right
#with moveinleft\right
#with easeinleft
#with blinds
#with wipeleft
#with pushleft

# Код для галлереи
init 3 python:

    g = Gallery()

    g.locked_button = "images/posters/lock.png"

    g.button("poster1")
    g.condition("persistent.poster1")
    g.image("cj_mc_jenya")

    g.button("poster2")
    g.condition("persistent.poster2")
    g.image("cj_aftertalk")

    g.button("poster3")
    g.condition("persistent.poster3")
    g.image("cj_gift")

    g.button("poster4")
    g.condition("persistent.poster4")
    g.image("cj_eat_cake")

    g.button("poster5")
    g.condition("persistent.poster5")
    g.image("cj_discussion")

    g.button("poster6")
    g.condition("persistent.poster6")
    g.image("cj_renovation_dream")

    g.button("poster7")
    g.condition("persistent.poster7")
    g.image("cj_uno")

    g.button("poster8")
    g.condition("persistent.poster8")
    g.image("cj_timur_good_ending")


transform tremble:
        alpha 1.0 xoffset 0
        choice:
            block:
                linear 0.05 xoffset 10
                linear 0.05 xoffset -10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2
        choice:
            block:
                linear 0.05 xoffset -10
                linear 0.05 xoffset 10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
        linear 0.07 xoffset 0

init python:
    def set_quick_menu(value):
        global quick_menu
        quick_menu = value
        if not quick_menu:
            renpy.hide_screen("mm_tooltip")
