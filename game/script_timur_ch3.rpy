image cj_notes_blur = im.Blur("cj/cj_notebook.jpg", 1.5)
init python:
    class Puzzle15:
        def __init__(self, image_path, size=3):
            self.size = size
            self.tile_size = 1.0/size
            self.tiles = list(range(size*size))
            self.empty_pos = size*size - 1
            self.image = Image(image_path)
            self.shuffle()

        def shuffle(self):
            for _ in range(1000):
                neighbors = self.get_neighbors(self.empty_pos)
                self.swap(random.choice(neighbors))

        def get_pos(self, index):
            return (index % self.size, index // self.size)

        def get_index(self, x, y):
            return y * self.size + x

        def get_neighbors(self, index):
            x, y = self.get_pos(index)
            neighbors = []
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    neighbors.append(self.get_index(nx, ny))
            return neighbors

        def swap(self, index):
            if index in self.get_neighbors(self.empty_pos):
                self.tiles[self.empty_pos], self.tiles[index] = self.tiles[index], self.tiles[self.empty_pos]
                self.empty_pos = index

        def is_solved(self):
            return all(i == self.tiles[i] for i in range(self.size*self.size))

    def puzzle15_action(index):
        if index in puzzle.get_neighbors(puzzle.empty_pos):
            puzzle.swap(index)
            renpy.restart_interaction()
        if puzzle.is_solved():
            renpy.hide_screen("puzzle15_screen")
            renpy.jump("puzzle_solved")

screen puzzle15_screen():
    zorder 1
    modal True

    textbutton _("Показать изображение"):
        action Show("puzzle15_full_image")
        xalign 0.5
        yalign 0.85

    textbutton _("Бросить дело"):
        action Confirm("Так не хочется клеить обои? Тимур будет зол!",
        [Hide("puzzle15_screen"), Jump("puzzle_skipped")]
    )
        xalign 0.5
        yalign 0.1

    frame:
        xalign 0.5
        yalign 0.5
        background None
        grid puzzle.size puzzle.size:
            spacing 2
            for i in range(puzzle.size * puzzle.size):
                if i == puzzle.empty_pos:
                    add Solid("#0000"):
                        size (200, 200)
                else:
                    $ tile_number = puzzle.tiles[i]
                    $ x = (tile_number % puzzle.size) * puzzle.tile_size
                    $ y = (tile_number // puzzle.size) * puzzle.tile_size

                    button:
                        add Transform(puzzle.image,
                            crop=(x, y, puzzle.tile_size, puzzle.tile_size),
                            size=(200, 200))
                        action Function(puzzle15_action, i)
                        xsize 200
                        ysize 200

screen puzzle15_full_image():
    zorder 201
    modal True
    button:
        add puzzle.image:
            size (600, 603)
            alpha 0.85
            xalign 0.505
            yalign 0.515
        action Hide("puzzle15_full_image")
        xfill True
        yfill True

#define wallpapers = ["Wallpaper1", "Wallpaper2"]

# начало главы
label timur_cp3:
    $ save_name = _("Глава 3. Тимур")
    $ quick_menu = False

    scene black with dissolve
    pause 1

    scene cj_chapter3_timur1 with dissolve

    pause 0.5

    scene cj_chapter3_timur2 with dissolve

    pause 3
    scene black with dissolve
    $ quick_menu = True
    pause 1

    scene bg_room_repair_morning with dissolve
    if helpedWithRepair == False:
        play music chill
        "Утро прошло также, как и все предыдущие: проснулся, умылся, оделся, позавтракал. Я хотел поспрашивать соседей о призраке, однако мои планы нарушил Тимур, загнав меня в магазин, чтобы докупить оставшиеся материалы и обои."

        "Очень не вовремя."

        scene bg_hardware_store with dissolve
        #нужен фоновый звук для строительного магазина
        "Тимур, будучи профессионалом, бегал от полки к полке, шустро закидывая в тележку всё необходимое. И, только когда мы подошли к отделу с обоями, процесс начал затягивать и меня."

        "Я разглядывал разноцветные рулоны, представляя, какой может стать наша комната. Взгляд упал на обои, которые, как мне казалось, подошли бы идеально. Но Тимур опередил меня и одной «левой», в прямом и переносном смысле, закинул в тележку два рулона других обоев."

        scene cj_timur_argument with dissolve
        mc "Эй, а моё мнение тебя не интересует? Мне эти обои не нравятся!"

        t "И? Ты же у меня насчёт постера не спрашивал."

        "Я почувствовал злость, буквально закипал."

        scene bg_hardware_store with dissolve

        show mc very angrya at left2 with dissolve
        mc "Тоже мне сравнил, маленький постер и обои на всю комнату."

        show timur very angrya at right2 with dissolve

        "Тимур, казалось, был готов разорваться от накатывающей злости."

        t "Забыл, из-за кого нам ремонт теперь нужно делать?"

        mc "А что я такого сделал? Это ведь ты во всём виноват!"

        "Я ждал, пока злость Тимура достигнет предела, но он молчал и смотрел на меня убийственным взглядом. Я нервничал. Всё же злой Тимур – не самое безопасное существо. В момент он выдохнул и отвел взгляд. Пронесло?"

        show timur angry winter at right2 with dissolve
        t "Ладно, давай так: обои берём мои, но клеить я их буду сам."

        show mc normal winter at left2 with dissolve
        mc "Хорошо. Ты сам это предложил."

        scene bg_street_morning_winter with dissolve
        "До общежития мы шли молча, и, эта тишина даже резала мои уши. Тимур все покупки донёс бы и сам, но боль в ноге, как мне показалось, не позволяла этого."

        scene bg_room_repair_day with dissolve
        "Стоило нам зайти в комнату, Тимур сразу же ушёл, ничего мне не сказав."
        stop music fadeout 2.0
        scene black with dissolve
        pause 1.0
        play background room

        scene bg_room_repair_dark with dissolve

        "Остаток дня я ходил по общежитию и пытался что-то выяснить насчёт призрака, однако мои старания остались безуспешны. Никто из попавшихся мне на глаза о нём не слышал."

        "Вечером вернулся Тимур и снова уткнулся в свой ноутбук. Вступать в коммуникацию не хотелось. Мой сосед просто продолжал копаться в гаджете. Мне же… Мне стало скучно, и я решил лечь спать."

        scene black with off
        stop music fadeout 2.0
        pause 2.0
    else:

        play music wholesome
        "Утро прошло также, как и все предыдущие: проснулся, умылся, оделся, позавтракал."

        "Моё тело медленно передвигалось по комнате, словно я был роботом, чьё программное обеспечение ни разу не обновляли, как вдруг в незагрузившийся мозг поступил запрос для Тимура:"

        scene bg_room_repair_morning with dissolve

        show mc normal home at left2 with dissolve
        mc "Какие планы на сегодня?"

        show timur normal home at right2 with dissolve
        t "Нужно в строительный магазин сходить."

        "Собрались мы достаточно быстро и вышли из общежития в хорошем настроении."

        scene bg_hardware_store with dissolve

        "В магазине я шёл рядом с Тимуром, слушая его рассказы о его семье. За забавными рассказами о сёстрах моего соседа я и не заметил, как тележка заполнялась необходимыми товарами. Оставались только обои."

        "Я рассмотрел стеллажи с рулонами и нашёл, как мне казалось, самый лучший вариант. Я хотел окликнуть Тимура, но заметил, что в тележке уже лежат рулоны других обоев."

        show mc surprise winter at left2 with dissolve
        mc "Тимур, что это?"

        show timur normal winter at right2 with dissolve
        t "Обои."

        mc "Я вижу, но почему ты меня даже не спросил?"

        t "Так мы же вроде вчера решили, какие будем брать."

        mc "Ты серьезно взял обои под цвет карточек?!"

        t "Ну да."

        show mc normal wintera at left2 with dissolve

        "И он замолчал, видимо поняв, что наши вчерашние приколы сегодня уже неактуальны. Кажется он немного смутился."

        show timur sad wintera at right2 with dissolve

        t "М-да… Неловко вышло. А ты какие хотел?"

        "Я указал на те, что мне понравились."
        show timur angry wintersa at right2 with dissolve

        t "Эти обои не подходят. У них качество не очень. Я хорошие выбрал… Ну, по качеству."

        show mc normal wintera at left2 with dissolve

        mc "Но мне они не нравятся!"

        "Тимур, кажется, начал заводиться, а потом посмотрел на ярко-красные обои в тележке и спокойно выдохнул:"

        show timur normal winter at right2 with dissolve

        t "Ладно, давай так. Мы подберём обои, которые устроят нас обоих. Ты выбираешь цвет, а я отвечаю за качество. По рукам?"

        show mc smile wintera at left2 with dissolve

        mc "По рукам."

        show timur smile wintera at right2 with dissolve

        t "Отлично."

        scene bg_hardware_store with dissolve
        "В конечном итоге, обои мы всё же выбрали. Вроде бы и хорошего качества, и приятного цвета. Да, они были не тем, чего мы оба изначально хотели, но это был компромисс, который говорил о том, что нам с Тимуром станет легче жить друг с другом."

        "Всё же договариваться без скандала мы уже научились."

        scene bg_street_morning_winter with dissolve
        "Выйдя из магазина, мы направились в сторону общежития. Тимур хотел нести всё сам, но я не мог ему это позволить. А он, собственно, и не возражал."

        scene bg_room_repair_day with dissolve
        "Зайдя в комнату, мой сосед тут же начал собираться, чтобы снова уйти."

        show timur normal winter at right2 with dissolve
        t "Слушай, мне уже бежать пора. Обои завтра поклею."

        show mc smile winter at left2 with dissolve
        mc "Хорошо. Удачи!"

        hide timur normal winter with dissolve
        hide mc normal winter with dissolve
        "Тимур улыбнулся мне в ответ и ушёл. А я остался один."

        scene black with dissolve
        pause 1.0
        scene bg_room_repair_night with dissolve
        stop music fadeout 2.0
        play background room
        "Весь оставшийся день прошёл как в тумане. Я прошёлся по общаге. На кухне меня угостила печеньем милая рыжая девушка, которую, кажется, звали Женя."

        "Вечером мой сосед вернулся, и мы снова вместе пили чай и болтали, решив сделать это обязательным вечерним ритуалом. Однако он показался мне грустным и даже задумчивым."

        "Я не сдержался и спросил:"
        #show mc normal home at left2 with dissolve
        scene cj_teatalking with dissolve #здесь будет цг с диска - из папки с цг для ветки Тимура, где гг и Тимур пьют чай в комнате без обоев и обсуждаются - спрайты в таком случае убираем


        mc "Что-то случилось?"
        play music sadness fadein 1.0

        #show timur normal home at right2 with dissolve
        t "Да вроде нет. За пару часов, что меня не было, ничего особо не поменялось."

        mc "Просто, мне кажется, у тебя в жизни что-то не ладится."

        t "У всех студентов жизнь не ладится."

        mc "Да, но…"

        t "Прости, я не намерен обсуждать свои проблемы."

        mc "Знаешь, иногда, чтобы стало легче, нужно выговориться."

        #show timur sad homea at right2 with dissolve

        "Тимур замолчал и, кажется, глубоко задумался."

        mc "Необязательно мне. Можно сходить к психологу… как вариант."

        "Тимур снова промолчал."

        mc "Я могу сходить с тобой для моральной поддержки."

        t "Я подумаю."

        #тут цг убираем уже - просто фон комнаты без обоев вечером (дальше спрайты оставляем)
        scene bg_room_repair_night with dissolve

        "Кажется, я помог ему встать на путь решения его ментальных проблем."

        mc "Давай спать. Кажется, завтра у нас трудный день."

        show timur smile homea at right2 with dissolve
        t "Да, по койкам!"
        hide timur smile homea at right2 with dissolve
        hide mc smile homea at left2 with dissolve
        scene bg_room_repair_dark with dissolve
        pause 1.0

        "Пожелав друг другу спокойной ночи, мы уложились в кровати, и я погрузился в сон."

        scene black with off
        stop music fadeout 2.0
        pause 2.0
        scene bg_room_repair_morning with dissolve

    if relate_timur < 20:
        scene bg_room_repair_morning with dissolve
        "Утром, открыв глаза, я не обнаружил своего соседа в комнате, но заметил записку, лежавшую на столе. "

        scene cj_timur_note with dissolve

        "То есть, как это я должен обои сам? И куда Тимур вообще мог уехать?"

        "Моему возмущению не было предела. Мало того, что мы купили эти ужасные обои, так ещё и сосед наверняка меня обманул. Вдруг он гуляет с кем-то, а мне ещё с этими полотнищами мучаться."

        scene bg_room_repair_morning with dissolve

        "Ну уж нет… У меня есть свои планы. Нужно продолжить расследование про призрака."

        "Похожу по общаге – кто-то же точно должен знать о нём. Раз уж призрак общажный, значит, он студент."

        "Я хотел было взять свой рюкзак, который нигде не мог найти, как вдруг заметил его в куче с вещами Тимура. Видимо, он случайно положил рюкзак к себе, когда убирался."

        "Разгребая вещи моего соседа, я обнаружил завёрнутый листок. Любопытство взяло верх. Развернув бумажку, я понял, что это фотография."

        play sound bumaga
        show cj_photo with dissolve

        play music mystery fadein 1.0

        "На ней был Тимур и ещё несколько человек, а на фоне красовалось слово «Посвят» и год «2023». Я хотел было отложить фото, но тут вгляделся в силуэт девушки рядом с Тимуром."

        "Это же она! Это тот призрак!"
        hide cj_photo with dissolve

        "Я был в шоке. Оказалось, что человек с ответами был прямо под моим носом. Осталось только дождаться Тимура, если он вообще захочет говорить со мной…"
        
        "Но сейчас всё-таки нужно поклеить обои."

        # ПЯТНАШКИ
        $ puzzle = Puzzle15(f"images/game/Wallpaper2.png", size=3)
        call screen puzzle15_screen
    else:
        play background room fadein 1.0
        play music home fadein 1.0
        "Утром, открыв глаза, я не обнаружил своего соседа в комнате, но, включив телефон я увидел сообщение от Тимура."
        nvl_narrator "{size=+8}{color=#000000}Тимур"

        t_nvl "Привет. Извини, мне срочно нужно уйти. Поклей обои без меня, а то скоро дисциплинарка."
        mc_nvl "Хорошо"

        nvl clear

        play background room fadein 1.0

        "Я испуганно осмотрел стены: как же мне справиться без Тимура? Но, взяв себя в руки, я решил начать."

        "Я достал из пакетов обои и остальные материалы, чтобы приступить к работе."
        scene cj_notebook with dissolve

        "Однако мой взгляд упал на кровать Тимура. На ней лежал его раскрытый блокнот. Глаз случайно упал на написанное на бумаге."

        scene cj_notes_blur with dissolve
        show cj_schedule with dissolve

        "Расписание Тимура…"
        #на диске в папке у Тимура есть цг, в которой список дел Тимура показан подробно - можно вывести его ненадолго перед мини-игрой

        "Я понял, что Тимур был на работе, как и в многие другие дни, когда он исчезал и возвращался только вечером. Мне стало его жаль, и я решительно настроился на поклейку обоев."

        scene black with dissolve
        pause 2.0
        scene bg_room_repair_day with dissolve
        # ПЯТНАШКИ
        $ puzzle = Puzzle15(f"images/game/Wallpaper1.png", size=3)
        call screen puzzle15_screen

label puzzle_solved:
    $ relate_timur += 5
    "Дело сделано!"
    if relate_timur >= 20:
        jump timur_good_end
    else:
        jump timur_bad_end

label puzzle_skipped:
    $ relate_timur -= 5
    if relate_timur >= 20:
        jump timur_good_end
    else:
        jump timur_bad_end
