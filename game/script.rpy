define Elina = Character("Элина")
define Midzu = Character("Мидзу")
define Oli = Character("Оли")
define Haru = Character("Хару")
define Nura = Character("Нура")
define Abyl = Character("Абыл")
define Abuka = Character("Абука")
define Ernar = Character("Ернар")
define Dastan = Character("Дастан")
define Ilya = Character("Ильяс")
define All = Character("Все")
define M = Character("Молдир")

screen disable_Lmouse():
    key "mouseup_1" action NullAction()


label start:
    # Fade to black and back.
    define fade = Fade(1.0, 1.0, 1.0)
    define fadeE = Fade(1.5, 5.2, 0.5)
    define dissolvec = Dissolve(0.2)
    stop music
    python:
        renpy.music.set_volume(0.5, 0,'music')
        renpy.music.set_volume(0.5, 0,'sound')
    play music "audio/1.mp3"
    scene bg1 with dissolve
    pause
    "29 марта."
    "Каникулы почти закончились."
    "Все дни сидела дома и смотрела аниме."
    "Единственное, что может порадовать - мой день рождения!"
    "Я хотела устроить тусу у себя дома, но Элина настаивала и
    пригласила меня и других моих друзей себе на хату."
    "Она сказала, что переехала в новое местечко, которое больше предыдущей квартиры."
    "Оглядываясь назад, мы дружим уже 5 лет. Я даже помню нашу первую встречу словно это было вчера."
    scene bg2 with fade



    #---------------------------------------ЧАСТЬ ЭЛИНЫ----------------------------------------------------#
    stop music
    "*2015 год*"
    play music "audio/elina1.mp3"
    M "'ЕБАТЬ МАЛИКА!!!'"
    "'хм?'"
label menu1:
    menu:
        "ЭЛИНА - МОДЕЛЬ!!!":
            jump option1e
        "ЭЛИНА - НЕ ДЕВСТВЕНИЦА!!!":
            jump option2e
        "ЭЛИНА - АНИМЕШНИЦА!!!":
            jump option3e
label option1e:
    "Шалбан"
    jump menu1
label option2e:
    "Шалбан"
    jump menu1
label option3e:
    "'ЧТОООООО??????'"
    show elina scared with dissolvec
    Elina "..."
    "'ТЫ ПРАВДА АНИМЕШНИЦА????'"
    show elina scaredSpeaking
    Elina "'да, но я-'"
    show elina scaredSweat
    "'БОЖЕ МОЙ А ТЫ СМОТРЕЛА ТЕМНОГО ДВОРЕЦКОГО???????'"
    show elina scaredSpeaking
    Elina "'ну я его недавно нач-'"
    show elina scared
    "'О МАЙ ГАД КАКОЙ ЖЕ ТАМ СЕБАСТЬЯН МИЛАШКА'"
    show elina scaredSpeaking
    Elina "'а?'"
    show elina scared
    "'БОЖЕ МОЙ МНЕ ТАК НРАВИТСЯ КАК В КОНЦЕ СЕЗОНА ОНИ (спойлеры)'"
    show elina depressed
    Elina "'но я еще не дошла до 5 се-'"
    show elina scared
    "'А ЧТО ДУМАЕШЬ ПРО ГЕЕВ? ТЕБЕ ОНИ НРАВЯТСЯ?'"
    show elina scaredSpeaking
    Elina "'ну да...'"
    show elina scared
    "'АААААААААААААА'"
    "'ГОСПОДИ А ХВОСТ ФЕИ? ХВОСТ ФЕИ СМОТРЕЛА? КРУТОЙ АНИМЕ ПРАВДА?'"
    show elina depressed
    Elina "'несколько серии...'"
    show elina scared
    "'ГОСПОДИ ДОСМОТРИ, ТАМ ТАКОЙ АХУЕННЫЙ БОЙ БУДЕТ В КОНЦЕ'"
    "О БОЖЕ КАК ЖЕ ОБОЖАЮ, КОГДА..."
    #----------------------------------------ЧАСТЬ ЭЛИНЫ----------------------------------------------------#





    stop music
    play music "audio/1.mp3"
    scene bg1 with fade
    "Да..."
    "Тогда я погоричилась..."
    "Но зато без нее я не познакомилась бы с Мидзу и Нурой."
    "Правда было это..."





    #----------------------------------------ЧАСТЬ МИДЗУ----------------------------------------------------#
    scene bg3 with fade
    stop music
    play music "audio/midzu1.mp3"
    show elina happy with dissolvec:
        xalign 0.8
    show midzu idle with dissolvec:
        xalign 0.2
    Elina "Малика, познакомься с моей подругой – Мидзу."
    hide elina with dissolvec
    show midzu idle with dissolvec:
        xalign 0.5
    "Получатся с этой мальявкой я должна буду делить мою любимую Элину!?"
    "Мы с Элиной должны были проводить курсы японского только и только вместе."
    "Ну чтож, раз уж она подруга Элины давай знакомится."
    "'Привет. Меня зовут Малика. Приятно познакомится!'"
    "Я протянула правую руку, но это мелкое чудо протянуло СВОЮ ПРАВУЮ РУКУ, и наши руки ударились друг о друга тыльными сторонами ладони."
    "На рукопожатие это было мало похоже."
    stop music
    show midzu scared
    Midzu "..."
    "..."
    "'Что?'"
    show midzu crying
    play music "audio/midzu2.mp3"
    Midzu "ПРОСТИ!!! Я ТУПАЯЯЯЯЯ."
    "..."
    "'Элина, отойдем поговорить.'"
    hide midzu with dissolvec
label menu2:
    menu:
        "'Почему она такая странная!?'":
            jump option1m
        "'Это что было сейчас?'":
            jump option2m
        "'bruh'":
            jump option3m
label option3m:
    "Шалбан"
    jump menu2
label option2m:
    "Шалбан"
    jump menu2
label option1m:
    show elina scaredSpeaking with dissolvec:
        xalign 0.5
    show midzu crying with dissolvec:
        xalign 0.02
    Elina "'Эээ...'"
    Elina "'Она немного перенервничала.'"
    Elina "'Наверное...'"
#----------------------------------------ЧАСТЬ МИДЗУ----------------------------------------------------#





#-----------------------------------------ЧАСТЬ НУРА----------------------------------------------------#
    stop music
    scene fade with fade
    "2017 год"
    "Зима"
    scene bg3 with fade
    play music "audio/nura1.mp3"
    Haru "'Итак класс, сегодня у нас новый ученик...'"
    show nura idle with dissolvec:
        xalign 0.5
    Haru "'Нурмуханбет!!!'"
    play sound "audio/audience.mp3"
    "И перед классом встал тихий пацан в толстовке и рыжими волосами."
    "О! Это же мой одноклассник!"
    Haru "'Сейчас поделимся на 2 группы и будем спорить на тему...'"
    hide nura with dissolvec
label menu4:
    menu:
        "Бедный отец или богатый отец":
            jump option1n
        "Лучше хорошие, но бедные или бедные, но хорошие люди":
            jump option2n
        "Лето или зима":
            jump option3n
label option2n:
    "Шалбан"
    jump menu4
label option3n:
    "Шалбан"
    jump menu4
label option1n:
    show nura idle with dissolvec:
        xalign 0.5
    "Хорошо что мне попался бедный отец, ведь все богатые отцы мудаки!"
    Haru "'Раз уж все поделились на 2 группы то давайте начнём через 5 минут.'"
    stop music
    scene fade with fade
    "Спустя 5 минут"
    scene bg3 with fade
    Haru "'Начнём с группы богатых отцов! Начинает Нурик!'"
    show nura speaking with dissolvec:
        xalign 0.5
    Nura "'Богатый отец лучше бедного, так как....'"
    show nura idle with dissolvec:
        xalign 0.5
    play sound "audio/hit.mp3"
    with vpunch
    play music "audio/nura2.mp3" fadein 1.0
    "'Протестую!! Ведь богатые отцы все плохие!!!'"
    show nura yelling with dissolvec:
        xalign 0.5
    Nura "'Это клише из фильмов!!!'"
    "'НЕТ!!!!!'"
    Nura "'ДА!!!!'"
    "И так продолжались дебаты 30 мин..."
#-----------------------------------------ЧАСТЬ НУРА----------------------------------------------------#





    stop music
    play music "audio/1.mp3"
    scene bg1 with fade
    "Но теперь я знаю, какая Мидзу сладкая булочка с корицей, и с Нурой подружился."
    "Ой. Кстати, о еде."
    "Было забавно, когда я забрала пудинг у Оли после японского."





#----------------------------------------ЧАСТЬ ОЛИ----------------------------------------------------#
    stop music
    scene fade with fade
    "2018 год"
    "Зима февраля"
    "8 вечера"
    scene oli1 with fade
    play music "audio/oli1.mp3"
    "*Переписка*"
    Oli "'Теперь у меня дома кучу йогуртов и пудингов.'"
    "'Блин хочу.'"
    Oli "'Какой?'"
label menu3:
    menu:
        "'Карамельный пудинг'":
            jump option1o
        "'Ванильный пудинг'":
            jump option2o
        "'Шоколадный пудинг'":
            jump option3o
label option1o:
    "Шалбан"
    jump menu3
label option2o:
    "Шалбан"
    jump menu3
label option3o:
    Oli "'Есть.'"
    "'Я сейчас приеду.'"
    Oli "'Что?'"
    "'Я сейчас приеду к тебе. Вынесешь мне пудинг.'"
    Oli "'Откуда ты знаешь, где я живу?'"
    "'Меньше вопросов.'"
    stop music
    scene fade with fade
    "Спустя 20 мин"
    scene oli2 with fade
    play music "audio/oli1.mp3"
    show oli speaking with dissolvec
    Oli "'Ну привет'"
    show oli idle
    "'Привет'"
    show oli speaking
    Oli "'Держи'"
    hide oli with dissolvec
    "*Протягивает шоколадный пудинг*"
    show oli question with dissolvec
    Oli "'Я не думал, что ты действительно приедешь сюда ради пудинга.'"
    "'Все ради пудинга.'"
    stop music
    play music "audio/1.mp3"
    scene bg1 with fade
#----------------------------------------ЧАСТЬ ОЛИ----------------------------------------------------#





    "Было действительно забавно."
    "Эх..."
    "Хоть бы Абыл не забыл принести 'ее'..."
    "Мою любимую..."





#----------------------------------------ЧАСТЬ АБЫЛА----------------------------------------------------#
    stop music
    scene fade with fade
    "'Где она?'"
    Abyl "'Тут.'"
    "'Качество?'"
    Abyl "'Идеальное.'"
    "'Цена?'"
    Abyl "'+100 000 тг.'"
    "'Прекрасно.'"
    "'Показывай.'"
    play music "audio/abylai1.mp3"
    scene ps1 with dissolve
    pause
    "да.."
    "Да..."
    "ДА."
    "ДААААА"
    scene abylai1 with dissolve
    show abyl speaking with dissolvec
    Abyl "Короче, там с дисками поаккуратнее."
    Abyl "И еще, чтобы зайти в акк надо..."
    scene ps2 with dissolve
    "Наконец-то."
    "Ты моя."
    "Ты даже не представляешь, сколько любви я тебе покажу."
    "Я перепройду тебя."
    "И тебя."
    "И тебя тоже."
    "Сегодня ночью только вы и я."
    "'Малика.'"
    "Божечки, неужели мне настолько хорошо, что я слышу голоса игр."
    "'Малика.'"
    "Они меня зовут."
    "'Малика!'"
    scene abylai1 with dissolve
    stop music
    show abyl yelling with dissolvec
    Abyl "'Малика!'"
    "'А?'"
    "'Что?'"
    show abyl speaking with dissolvec
    Abyl "'Поняла?'"
label menu5:
    menu:
        "Да":
            jump option1a
        "Нет":
            jump option2a
        "Может дома обьяснишь?":
            jump option3a
label option1a:
    "Шалбан"
    jump menu5
label option2a:
    "Шалбан"
    jump menu5
label option3a:
    Abyl "'Окей'"
    stop music
    play music "audio/1.mp3"
    scene bg1 with fade
#----------------------------------------ЧАСТЬ АБЫЛА----------------------------------------------------#






    "Абыл очень щедрый и добрый."
    "И кстати о добром..."




#----------------------------------------ЧАСТЬ АБУКА----------------------------------------------------#
    stop music
    scene abukabg with fade
    play music "audio/abuka.mp3"
    show abuka speaking with dissolvec
    Abuka "'Простите, что собрал вас так рано.'"
    show abuka idle with dissolvec
    "'Да не волнуйся.'"
    Nura "'Не переживай, пошлите в магаз купим попить.'"
    Nura "'Там еще Оли сказал, чтобы 5 литровую воду взять, так как у него дома закончилось.'"
    Nura "'Еще лапшу быстрого приготовления купим.'"
    "'Пошлите.'"
    stop music
    scene fade with fade
    "Спустя некоторое время"
    scene abukabg with fade
    play music "audio/abuka.mp3"
    "'Блин как же на улице холодно, поскорее бы добраться до дома Оли.'"
    "Я увидела, как Абука носил 5 литровую воду и пакеты еды."
    "'Тебе не холодно?'"
    show abuka speaking with dissolvec
    Abuka "'Да не. Даже как то жарко.'"
    show abuka idle with dissolvec
    "'А не тяжело все это носить?'"
    show abuka happy with dissolvec
    Abuka "'Норм, не переживай.'"
    Abuka "'Малика, давай свои.'"
    show abuka idle with dissolvec
    "'Зачем?'"
    show abuka happy with dissolvec
    Abuka "'Помогу потащить.'"
    hide abuka with dissolvec
label menu6:
    menu:
        "'Да, с радостью.'":
            jump option1ab
        "'Не надо, они вообще не тяжелые.'":
            jump option2ab
        "'Лучше отдам их Нуре!'":
            jump option3ab
label option1ab:
    "Шалбан"
    jump menu6
label option3ab:
    "Шалбан"
    jump menu6
label option2ab:
    "Тем более стыдно будет отдать еще и это."
    "Он и так все это носит, да еще и без перчаток в такой мороз."
    stop music
    play music "audio/1.mp3"
    scene bg1 with fade
#----------------------------------------ЧАСТЬ АБУКА----------------------------------------------------#





    "Какой же он милый и добрый человек, готовый всегда прийти на помощь."
    "В отличии от некоторых..."




#----------------------------------------ЧАСТЬ ЕРНАР----------------------------------------------------#
    stop music
    scene fade with fade
    "Данный флешбек не рекомендуется лицам достигшие 18 лет, смотрящие аниме, девушкам в крашенных волосах, фанатам хвоста фей, и людям чьё имя начинается на М."
    "Все участвующие лица выдуманные, а сходства случайны."
    "Мы не ручаемся за насилие и проишетствия связанные с данным лицом."
    "Пожалуйста обратитесь к вашему ближайшему Ернару, если у вас возникнет недовольство."
    scene ernarbg with fade
    play music "audio/ernar.mp3"
    Ernar "'В общем она очень красивая.'"
    Ernar "'У нее улыбка прекрасная.'"
    Ernar "'Ее смех самый милый.'"
    "'Уау. А как ее зовут?'"
    "'Малика.'"
    scene ernar1 with dissolve
    play sound "audio/blush.mp3"
    "'Ой спасииииибооооо.'"
    Ernar "'Эм...'"
    stop music
    Ernar "'Я вообще-то про рыжую.'"
    "..."
    scene ernar2
    play sound "audio/bell.mp3"
    "..."
    "'Больше.'"
    "'Никогда.'"
    "'Не напоминай.'"
    "'Об этом.'"
    stop music
    play music "audio/1.mp3"
    scene bg1 with fade
#----------------------------------------ЧАСТЬ ЕРНАР----------------------------------------------------#




    "Больная тема."
    "Он всегда вытворяет странные вещи."
    "Но наверное это то, что делает его таким особенным."
    "Помню даже, как в кафе с Дастаном и Ильясом..."



#----------------------------------------ЧАСТЬ ИЛЬЯСА----------------------------------------------------#
    stop music
    scene fade with fade
    "2018 год"
    "9 Сентября"
    scene cafe with fade
    play music "audio/ilya1.mp3"
    Ilya "'Скучно.'"
    Ilya "'Давайте что-нибудь поделаем.'"
    Ilya "'Например порисуем на этих бумагах.'"
    show ernar speaking with dissolvec:
        xalign 0.2
    show dastan idle with dissolvec:
        xalign 0.7
    Ernar "'Давай.'"
    show dastan speaking with dissolvec:
    Dastan "'Лучше поем.'"
    scene cafe with fade
    "'Смотрите, что нарисовала.'"
    show ernar idle with dissolvec:
        xalign 0.2
    show dastan idle with dissolvec:
        xalign 0.7
    Dastan "'Ничего себе.'"
    Ernar "'Уааау.'"
    Ilya "'Нифигово получилось.'"
    Elina "'Чего еще ожидать от нее.'"
    Midzu "'Вот именно.'"
    scene cafe with fade
    show ernar speaking with dissolvec:
        xalign 0.2
    show dastan idle with dissolvec:
        xalign 0.7
    Ernar "'Черт, все равно скучно.'"
    Ernar "..."
    stop music
    show ernar idea with dissolvec:
    Ernar "'О, приудмал!'"
    "'Что вы собрались делать?'"
    Ernar "'Угадай!'"
    hide ernar with dissolvec
    hide dastan with dissolvec
label menu7:
    menu:
        "Кричать будешь?":
            jump option1i
        "Только не отжимайся":
            jump option2i
        "Ну говори же!":
            jump option3i
label option1i:
    "Шалбан"
    jump menu7
label option3i:
    "Шалбан"
    jump menu7
label option2i:
    play music "audio/ilya2.mp3"
    show ernar idle with dissolvec:
        xalign 0.2
    show dastan idle with dissolvec:
        xalign 0.7
    Ernar "'Дастан, го отжиматься.'"
    Ernar "'Прям тут!'"
    show dastan speaking with dissolvec:
    Dastan "'А что? Звучит хайпово!'"
    hide ernar with dissolvec
    hide dastan with dissolvec
    Ernar "'Раз!'"
    Dastan "'Раз!'"
    Ernar "'Два!'"
    Dastan "'Два!'"
    Ernar "'Три!'"
    Dastan "'Три!'"
    "Все начали смеятся над их поступком"
    "'Господи убейте меня...'"
    stop music
    play music "audio/1.mp3"
    scene bg1 with fade
#----------------------------------------ЧАСТЬ ИЛЬЯСА----------------------------------------------------#




    "Эх..."
    "Как много воспоминании..."
    "Так рада, что у меня есть такие друзья."
    "Ой, я опаздываю!"
    "Она позвала на 15:00, а уже 14:50!"
    "Надо поспешить."
    scene streets with fade
    "Господи, где же этот чертов дом."
    "Она сказала, что переехала в новое местечко."
    "Говорит, что дом большой. Даже фото отправила."
    "Правда, в какой жопе находится этот дом?"



#----------------------------------------КОНЦОВКА----------------------------------------------------#
    scene house with fade
    "Ничего себе!"
    "Это ее дом?"
    "В жизни выглядит больше, чем на фото."
    "Ворота почему-то открыты."
    "Надеюсь она не против, если я зайду."
    stop music fadeout 2.0
    "Наконец-то я тут."
    "Пора звонить."
    play sound "audio/doorbell.mp3"
    scene ending with fadeE
    play music "audio/ending.mp3"
    play sound "audio/horn.mp3"
    $ _skipping = False
    All "'С днем рождения!'"
    Dastan "'Не сосчитать тех достоинств, которые у тебя есть. Я искренне надеюсь, что ты достигнешь колоссальных высот во всех сферах своей жизни!'"
    Dastan "'Поздравляю тебя с этим замечательным праздником и желаю как можно больше счастливых, запоминающихся моментов :)'"
    Ilya "'И так, Малика которой исполнилось 18 лет желаю я тебе, 'Желание', три. Мои слова не должны сделать тебе приятно, они должны сделать тебя лучше'"
    Ilya "'Что бы ты достигла всего, чего желаешь, а чего ты желаешь я не могу знать, желаю тебе, что бы у тебя все получилось, и всего достигла в твоих странствиях по этому удивительному миру, и по планете Земля.'"
    Oli "'За все 4 года нашей дружбы ты стала для меня словно родной сестрой. Я хочу сказать, чтобы ты не огорчалась насчет своего дня рождения, ведь в конце концов твои друзья всегда рядом с тобой.'" 
    Oli "'Желаю тебе сил и терпения во взрослой жизни, беспрерывного прогресса в своих делах и хобби, чтобы каждый новый день ты становилась на 1 процент лучше и не забывать, что мы все тебя любим.'"
    Abuka "'Дорогая доча, поздравляю тебя с днем рождения, что бы у тебя всегда было хорошое настроение и здоровье становись с каждым днем все лучше и лучше.'"
    Abyl "'C др малика, желаю тебе плойку, этого достаточно для счастья'"
    Nura "'Малике, мой самый любимый трап! Поздравляю тебя с этим чудесным праздником! И желаю тебе продолжать быть таким наивным и хорошим человеком! Всего хорошего и ничего плохого'"
    Ernar "'Хей, йоу, ватсапп бро. С днем рождения тебя. Здоровье, счастье и бла-бла-бла... БАНАЛЬНО!'"
    Ernar "'Желаю тебе когда нибудь в твоей жизни перейти от днобука на норм ноут. И пожалуй, чтоб твои роды были не такими болезненными. Аминь. Удачи тебе в твое 18 летие. Надеюсь этот возраст не будет твоим последним'"
    Midzu "'Вот и настало твое 18-тилетие. Желаю тебе всего самого наилучшего и хорошего на новом этапе твоей жизни. Ты всего добьешься, всего достигнешь, ты очень талантливая девочка и я верю, что ты станешь успешным человеком.'"
    Midzu "'Я всегда буду поддерживать тебя! Меньше болей, больше улыбайся и смейся. Желаю тебе побольше счастливых моментов с твоими любимыми людьми. Люблю тебя!'"
    Elina "'Малика, с др короче! ;P'"
    
    jump credits
    return

label credits:
    scene fade #replace this with a fancy background
    with dissolve

    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3,hard=True)
    hide theend

    show directed:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3,hard=True)
    hide directed

    show screenwriter:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3,hard=True)
    hide screenwriter

    show designer1:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3,hard=True)
    hide designer1

    show designer2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3,hard=True)
    hide designer2

    show musics:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3,hard=True)
    hide musics

    show progrmmer:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3,hard=True)
    hide progrmmer

    show love:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4,hard=True)
    hide love

    show birthday:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4,hard=True)
    hide birthday
    return

init:
    image directed = Text("Directed by"+"\n"+ "{size=60}{color=#fff}Hideo Kodjima{/color}", text_align=0.5)
    image screenwriter = Text("{size=40}Сценари"+"\n"+ "{size=60}{color=#fff}Нура и Оли{/color}", text_align=0.5)
    image designer1 = Text("{size=40}Главный дизайнер"+"\n"+ "{size=60}{color=#fff}Мидзу{/color}", text_align=0.5)
    image designer2 = Text("{size=40}Главный дизайнер концовки"+"\n"+ "{size=60}{color=#fff}Элина{/color}", text_align=0.5)
    image musics = Text("{size=40}Музыка"+"\n"+ "{size=60}{color=#fff}Нура и Оли{/color}", text_align=0.5)
    image progrmmer = Text("{size=40}Программист"+"\n"+ "{size=60}{color=#fff}Оли{/color}", text_align=0.5)
    image theend = Text("{size=80}{color=#fff}Конец{/color}", text_align=0.5)
    image thanks = Text("{size=80}{color=#fff}Спасибо за игру!{/color}", text_align=0.5)
    image birthday = Text("{size=80}{color=#fff}C днем рождения!{/color}", text_align=0.5)
    image love = Text("{size=40}Любят"+"\n"+ "{size=60}{color=#fff}Все{/color}", text_align=0.5)

return
