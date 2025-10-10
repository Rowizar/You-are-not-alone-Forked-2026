label timur_bad_end:
    stop music fadeout 2.0
    play background room

    scene bg_room_after_repair with dissolve
    "Весь день я клеил эти чёртовы обои. Где-то они отклеивались, где-то наслаивались. У меня уже не оставалось сил."
    if persistent.timur_bad != True:
        $ renpy.notify("В дневнике появилась новая запись!")
    $ persistent.timur_bad = True

    "В конечном итоге я махнул рукой и лёг спать."

    scene black with off
    pause 0.5
    stop music fadeout 2.0

    "Однако во сне призрак девушки вновь явился ко мне."

    "Она смотрела на меня самым что ни на есть суровым взглядом. Стоя в полной темноте, она погрозила мне пальцем, словно маленькому ребёнку."
    pause 2.0
    stop background fadeout 2.0

    play music mystery fadein 1.0
    #нужна фоновая музыка (возможно, этим займусь уже я, но, если вдруг есть идея по поводу музыки - вперёд!)
    scene cj_timur_bad_ending with dissolve

    "По итогам дисциплинарной комиссии мы получили выговор с занесением в личное дело. Мои тяпы-ляпы не прокатили, и один из кусков обоев свалился прямо на голову коменданта."

    "После этого Тимур съехал от меня. Он не сказал ни слова на прощание, и мне было стыдно говорить что-либо. Один раз я встретил его на кухне вместе с новым соседом, и они увлечённо обсуждали какую-то игру."

    "После переезда Тимура призрак больше ко мне не являлся."

    pause 2
    stop music fadeout 2.5
    $ persistent.ending4 = True
    $ set_quick_menu(False)

    scene black with dissolve
    play background audio.wind
    centered "{size=+24}{color=#ffffff}Давай помогу начать всё сначала."
    stop background fadeout 1.0

return
