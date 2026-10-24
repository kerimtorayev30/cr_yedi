#!/usr/bin/env python3
"""Audited additions to the legacy 192-entry Advanced Plus pack.

Each row keeps learner-facing fields plus its printed Student's Book page and
source classification. The generator injects books[] and the app metadata.
"""
TG_PAGE = {
    '1A': 188, '1B': 189, '2A': 190, '2B': 191, '3B': 192,
    '4A': 193, '4B': 194, '5A': 195, '6A': 196, '6B': 197,
    '7A': 198, '8A': 199,
}
LESSON_VOCAB = {'3A', '5B', '7B', '8B'}


def group(lesson, page, items, section=None, tg_pdf_page=None,
          evidence=None, page_role='exact_student_book_page', source_note=''):
    """Expand concise source rows into audited Advanced Plus addition records."""
    if section is None:
        section = 'vocabulary' if lesson in LESSON_VOCAB else 'vocabulary_bank'
    if evidence is None:
        evidence = ('student_book_vocabulary_box' if section == 'vocabulary'
                    else 'student_book_vocabulary_bank')
    if tg_pdf_page is None and section == 'vocabulary_bank':
        tg_pdf_page = TG_PAGE.get(lesson)
    out = []
    for row in items:
        if len(row) not in (9, 10):
            raise ValueError(f'bad addition row for {lesson}: {row!r}')
        en, ipa, pos, tm, ru, definition, ex, ex_tm, cefr = row[:9]
        out.append({
            'en': en, 'ipa': ipa, 'pos': pos, 'tm': tm, 'ru': ru,
            'def': definition, 'ex': ex, 'exTm': ex_tm, 'cefr': cefr,
            'coll': row[9] if len(row) == 10 else '—',
            'lesson': lesson, 'page': page, 'section': section,
            'evidence': evidence, 'page_role': page_role,
            'tg_pdf_page': tg_pdf_page,
            'tg_evidence': ('Teacher’s Guide vocabulary worksheet' if tg_pdf_page else ''),
            'source_note': source_note,
        })
    return out


ADDITIONS = []

# 1A — Student's Book Vocabulary Bank, printed p.140; TG PDF p.188 cross-check.
ADDITIONS += group('1A', 140, [
    ('bit', '/bɪt/', 'N', 'azajyk', 'немного', 'a small amount or a short period of time', 'Wait a bit and I will be ready.', 'Azajyk garaş, men taýýar bolaryn.', 'B1', 'a bit of time'),
    ('thing', '/θɪŋ/', 'N', 'zat; ýagdaý', 'вещь; дело', 'a vague word for an object, fact, or situation', 'There is one thing I need to tell you.', 'Saňa aýtmaly bir zadym bar.', 'A2'),
    ('at least', '/ət ˈliːst/', 'PHR', 'azyndan', 'по меньшей мере', 'not less than a particular amount', 'At least thirty people came to the meeting.', 'Duşuşyga azyndan otuz adam geldi.', 'B1'),
    ('at most', '/ət ˈməʊst/', 'PHR', 'iň köp', 'не более чем', 'not more than a particular amount', 'The journey takes an hour at most.', 'Ýol iň köp bir sagat alýar.', 'B2'),
    ('around', '/əˈraʊnd/', 'ADV', 'takmynan', 'примерно', 'approximately, but not exactly', 'There were around five hundred people there.', 'Ol ýerde takmynan bäş ýüz adam bardy.', 'B1'),
    ('odd', '/ɒd/', 'ADJ', 'töweregi; takmynan', 'с лишним; около', 'used after a number to mean a little more than it', 'The town is twenty-odd miles away.', 'Şäher ýigrimi mil töweregi uzaklykda.', 'C1', 'twenty-odd'),
    ('-ish', '/ɪʃ/', 'PHR', 'takmynan; biraz', 'суффикс приблизительности', 'a suffix meaning approximately or somewhat', 'Let’s meet at seven-ish.', 'Takmynan sagat ýedide duşuşaly.', 'B2'),
    ('whatever', '/wɒtˈevə/', 'PRON', 'näme bolsa-da', 'что бы ни; всё равно', 'anything at all, or a vague response showing indifference', 'Choose whatever you like.', 'Islän zadyňy saýla.', 'B2'),
    ('whenever', '/wenˈevə/', 'CONJ', 'haçan bolsa-da', 'когда бы ни', 'at any time that; no matter when', 'Call me whenever you need help.', 'Kömek gerek bolanda maňa jaň et.', 'B2'),
    ('wherever', '/weərˈevə/', 'ADV', 'nirede bolsa-da', 'где бы ни', 'in or to any place that', 'Wherever she goes, she makes friends.', 'Ol nirä gitse-de dost tapýar.', 'B2'),
    ('whoever', '/huːˈevə/', 'PRON', 'kim bolsa-da', 'кто бы ни', 'any person who; it does not matter who', 'Whoever finishes first can leave.', 'Kim birinji tamamlasa, gidip biler.', 'B2'),
    ('whichever', '/wɪtʃˈevə/', 'DET', 'haýsy bolsa-da', 'какой бы ни', 'any one of a limited set of choices', 'Take whichever seat you prefer.', 'Islän oturgyjyňda otur.', 'B2'),
    ('however', '/haʊˈevə/', 'ADV', 'nähili bolsa-da', 'как бы ни', 'in whatever way; to any degree', 'However hard you try, the answer is the same.', 'Nähili köp synansaň-da, jogap şol bir zat.', 'B2'),
])

# 1B — Vocabulary Bank printed pp.141–142; TG PDF p.189 crossword corroborates.
ADDITIONS += group('1B', 141, [
    ('outlook', '/ˈaʊtlʊk/', 'N', 'garaýyş; geljekki ýagdaý', 'перспектива; прогноз', 'the likely future situation or a person’s way of thinking', 'The economic outlook is improving.', 'Ykdysady ýagdaýyň geljegi gowulanýar.', 'B2', 'economic outlook'),
    ('update', '/ˈʌpdeɪt/', 'N', 'täzelenme; täze maglumat', 'обновление; новые сведения', 'the latest information about a changing situation', 'Can you give me an update on the project?', 'Taslama barada täze maglumat berip bilersiňmi?', 'B1'),
    ('aftershock', '/ˈɑːftəʃɒk/', 'N', 'gaýtalanýan ýer titremesi', 'повторный толчок', 'a smaller earthquake that follows a larger one', 'Several aftershocks followed the earthquake.', 'Ýer titremesinden soň birnäçe gaýtalanýan sarsgyn boldy.', 'C1'),
    ('outbreak', '/ˈaʊtbreɪk/', 'N', 'başlanma; duýdansyz ýaýramak', 'вспышка; начало', 'the sudden start of something unpleasant, especially disease or violence', 'The outbreak was brought under control.', 'Keseliň ýaýramagy gözegçilik astyna alyndy.', 'C1'),
    ('take-up', '/ˈteɪk ʌp/', 'N', 'kabul ediliş; ulanylyş', 'принятие; использование', 'the number of people who accept or use something', 'There was a high take-up of the free courses.', 'Mugt okuwlary saýlap alanlaryň sany köp boldy.', 'C1'),
    ('downturn', '/ˈdaʊntɜːn/', 'N', 'peselme; yza gaýdyş', 'спад', 'a period when business or economic activity becomes weaker', 'The downturn forced several shops to close.', 'Ykdysady peselme birnäçe dükanyň ýapylmagyna sebäp boldy.', 'C1'),
    ('upkeep', '/ˈʌpkiːp/', 'N', 'saklamak üçin çykdajy', 'содержание; обслуживание', 'the cost or work of keeping something in good condition', 'The upkeep of the old house is expensive.', 'Köne jaýy saklamak gymmada düşýär.', 'C1'),
    ('rip-off', '/ˈrɪp ɒf/', 'N', 'aldaw; aşa gymmat haryt', 'обман; завышенная цена', 'something that costs far too much or is dishonest', 'That souvenir was a complete rip-off.', 'Şol ýadygärlik harydy doly aldawdy.', 'C1'),
    ('climb-down', '/ˈklaɪm daʊn/', 'N', 'yza çekilmek; eglişik', 'отступление; уступка', 'an admission that you were wrong or a decision to change your position', 'The minister’s climb-down ended the dispute.', 'Ministriň yza çekilmegi jedeli tamamlady.', 'C2'),
    ('comeback', '/ˈkʌmbæk/', 'N', 'gaýdyp gelmek; täzeden üstünlik gazanmak', 'возвращение', 'a return to success or popularity after a period away', 'The singer made a successful comeback.', 'Aýdymçy üstünlikli gaýdyp geldi.', 'B2'),
    ('breakthrough', '/ˈbreɪkθruː/', 'N', 'uly açyş; öňegidişlik', 'прорыв', 'an important new discovery or development', 'Researchers announced a medical breakthrough.', 'Alymlar lukmançylykda uly açyşy yglan etdiler.', 'B2'),
    ('break-up', '/ˈbreɪk ʌp/', 'N', 'aýrylyşma; dargama', 'расставание; распад', 'the ending of a relationship or organization', 'The break-up affected the whole family.', 'Aýrylyşma tutuş maşgala täsir etdi.', 'B2'),
    ('mix-up', '/ˈmɪks ʌp/', 'N', 'bulaşyklyk; çalşyrylyş', 'путаница', 'a mistake in which people or things are confused with each other', 'There was a mix-up with the hotel booking.', 'Myhmanhana bronunda bulaşyklyk boldy.', 'B2'),
    ('set-up', '/ˈset ʌp/', 'N', 'guramaçylyk; düzüliş', 'организация; устройство', 'the way something is arranged or organized', 'I am still learning the set-up in my new office.', 'Täze edaramdaky iş düzülişini heniz öwrenýärin.', 'B2'),
    ('let-down', '/ˈlet daʊn/', 'N', 'göwnüň galmagy', 'разочарование', 'a disappointment or failure to do what was expected', 'The cancelled concert was a real let-down.', 'Konsertiň ýatyrylmagy uly göwnüçökgünlik boldy.', 'B2'),
    ('write-off', '/ˈraɪt ɒf/', 'N', 'ulanyşdan çykarylan zat', 'списание; не подлежащая ремонту вещь', 'a damaged vehicle or object considered not worth repairing', 'The insurer declared the car a write-off.', 'Ätiýaçlandyryjy maşyny abatlap bolmaýan diýip yglan etdi.', 'C1'),
    ('backup', '/ˈbækʌp/', 'N', 'ätiýaçlyk kömek; ätiýaçlyk nusga', 'поддержка; резервная копия', 'extra help or a copy kept in case the original is lost', 'Keep a backup of all your files.', 'Ähli faýllaryň ätiýaçlyk nusgasyny sakla.', 'B2'),
    ('giveaway', '/ˈɡɪvəweɪ/', 'N', 'aňsat tanadýan alamat; sowgat', 'выдающий признак; раздача', 'a sign that reveals something, or something given free', 'His nervous smile was a giveaway.', 'Onuň tolgunýan ýylgyryşy ony aňsat tanadýardy.', 'C1'),
    ('hold-up', '/ˈhəʊld ʌp/', 'N', 'saklanma; gijikme', 'задержка', 'a delay that prevents something from continuing', 'There was a hold-up on the motorway.', 'Awtobanda gijikme boldy.', 'B2'),
    ('turnout', '/ˈtɜːnaʊt/', 'N', 'gatnaşanlaryň sany', 'явка; число пришедших', 'the number of people who attend an event', 'The march had an impressive turnout.', 'Ýörişe köp adam gatnaşdy.', 'C1'),
    ('makeover', '/ˈmeɪkəʊvə/', 'N', 'täzeden bezeme; keşbi üýtgetme', 'преображение; ремонт', 'a complete improvement or change in appearance', 'The café had a stylish makeover.', 'Kafäniň içki keşbi döwrebaplaşdyryldy.', 'B2'),
    ('setback', '/ˈsetbæk/', 'N', 'päsgelçilik; yza gaýdyş', 'неудача; препятствие', 'a problem that delays progress', 'The injury was a setback for the team.', 'Şikes topar üçin päsgelçilik boldy.', 'B2'),
    ('breakdown', '/ˈbreɪkdaʊn/', 'N', 'bozulma; nerw dartgynlygy', 'поломка; нервный срыв', 'a failure to work, or a loss of emotional control', 'A breakdown stopped the train for an hour.', 'Bozulma otlusy bir sagat saklady.', 'B2'),
    ('write-up', '/ˈraɪt ʌp/', 'N', 'ýazmaça syn ýa-da hasabat', 'письменный отзыв; отчёт', 'a written description or review of something', 'The restaurant received a good write-up.', 'Restoran barada gowy syn ýazyldy.', 'C1'),
    ('go-ahead', '/ˈɡəʊ əhed/', 'N', 'rugsat; işe başlamak üçin karar', 'разрешение; зелёный свет', 'permission to start doing something', 'We are waiting for the go-ahead to begin.', 'Başlamak üçin rugsada garaşýarys.', 'B2'),
    ('standby', '/ˈstændbaɪ/', 'N', 'garaşma ýagdaýy; ätiýaçlyk', 'режим ожидания; резерв', 'a state of readiness to act or be used when needed', 'The team remained on standby overnight.', 'Topar gijäniň dowamynda taýýar ýagdaýda galdy.', 'C1'),
    ('meltdown', '/ˈmeltdaʊn/', 'N', 'duýgy taýdan doly çökgünlik', 'эмоциональный срыв', 'a sudden loss of control caused by extreme pressure', 'The delay caused a complete meltdown at the airport.', 'Gijikme howa menzilinde uly başagaýlyk döretdi.', 'C1'),
])
# Two extra phrasal nouns from the TG 1B crossword; retained as teacher-resource
# extensions and mapped to the corresponding Student's Book section page.
ADDITIONS += group('1B', 141, [
    ('input', '/ˈɪnpʊt/', 'N', 'goşant; girizilýän maglumat', 'вклад; входные данные', 'ideas or information put into a process or system', 'We welcome input from every member of the team.', 'Toparyň her bir agzasynyň pikirini makullaýarys.', 'B2'),
    ('output', '/ˈaʊtpʊt/', 'N', 'önüm; öndürilen mukdar', 'выпуск; результат', 'the amount produced by a person, machine, or process', 'The factory increased its output this year.', 'Zawod şu ýyl önümçiligini artdyrdy.', 'B2'),
], evidence='teacher_guide_photocopiable_vocabulary', page_role='teacher_guide_extension', source_note='TG crossword for 1B; linked to the Student’s Book Phrasal nouns section')

# 2A — Vocabulary Bank, printed p.143; TG PDF p.190 cross-checks derived forms.
ADDITIONS += group('2A', 143, [
    ('anaemic', '/əˈniːmɪk/', 'ADJ', 'gan azdykly', 'страдающий анемией', 'having too few red cells in the blood', 'The doctor said I was slightly anaemic.', 'Lukman ganymyň biraz azdygyny aýtdy.', 'C1'),
    ('contradict', '/ˌkɒntrəˈdɪkt/', 'V', 'garşy çykmak; tersini aýtmak', 'противоречить', 'to say the opposite of what someone else has said', 'The witness contradicted his earlier statement.', 'Şaýat öňki aýdanlaryna garşy çykdy.', 'B2'),
    ('controversial', '/ˌkɒntrəˈvɜːʃl/', 'ADJ', 'jedelli', 'спорный', 'causing strong disagreement among people', 'The decision remains controversial.', 'Bu karar henizem jedelli.', 'B2'),
    ('extraordinary', '/ɪkˈstrɔːdnri/', 'ADJ', 'adatdan daşary', 'необыкновенный', 'very unusual or surprising', 'She showed extraordinary courage.', 'Ol adatdan daşary edermenlik görkezdi.', 'B2'),
    ('foresee', '/fɔːˈsiː/', 'V', 'öňünden görmek; çaklamak', 'предвидеть', 'to know or guess that something will happen', 'Nobody could foresee the sudden change.', 'Duýdansyz üýtgeşmäni hiç kim öňünden çaklap bilmedi.', 'C1'),
    ('homogeneous', '/ˌhɒməˈdʒiːniəs/', 'ADJ', 'birmeňzeş düzümdäki', 'однородный', 'made up of parts or people that are all similar', 'The sample was a homogeneous mixture.', 'Nusga birmeňzeş garyndydy.', 'C2'),
    ('hyperactive', '/ˌhaɪpərˈæktɪv/', 'ADJ', 'aşa hereketjeň', 'гиперактивный', 'much more active and energetic than is usual', 'The hyperactive puppy ran around the room.', 'Aşa hereketjeň güjük otagyň içinde ylgady.', 'C1'),
    ('infrastructure', '/ˈɪnfrəstrʌktʃə/', 'N', 'infrastruktura', 'инфраструктура', 'the basic systems and services a country or organization needs', 'The region needs better transport infrastructure.', 'Sebite has gowy ulag infrastrukturasy gerek.', 'C1'),
    ('macroeconomics', '/ˌmækrəʊˌiːkəˈnɒmɪks/', 'N', 'makroykdysadyýet', 'макроэкономика', 'the study of the economy of a whole country or region', 'She is studying macroeconomics at university.', 'Ol uniwersitetde makroykdysadyýeti öwrenýär.', 'C2'),
    ('microscope', '/ˈmaɪkrəskəʊp/', 'N', 'mikroskop', 'микроскоп', 'an instrument used to see very small things', 'We examined the cells under a microscope.', 'Öýjükleri mikroskop bilen gözden geçirdik.', 'B2'),
    ('paramedic', '/ˌpærəˈmedɪk/', 'N', 'gyssagly kömek lukmany', 'фельдшер скорой помощи', 'a person trained to give emergency medical care', 'A paramedic treated the injured driver.', 'Gyssagly kömek lukmany şikes alan sürüjä kömek etdi.', 'B2'),
    ('transatlantic', '/ˌtrænzətˈlæntɪk/', 'ADJ', 'Atlantikanyň aňyrsyndaky', 'трансатлантический', 'crossing or relating to the Atlantic Ocean', 'They took a transatlantic flight to Boston.', 'Olar Boston şäherine Atlantikanyň aňyrsyndan uçdylar.', 'C1'),
    ('microcosm', '/ˈmaɪkrəʊkɒzəm/', 'N', 'kiçi nusga; kiçi dünýä', 'микрокосм; модель', 'a small example that has the same features as a larger system', 'The school is a microcosm of society.', 'Mekdep jemgyýetiň kiçi nusgasydyr.', 'C2'),
    ('paranormal', '/ˌpærəˈnɔːml/', 'ADJ', 'adaty düşündirişden daşdaky', 'паранормальный', 'that cannot be explained by ordinary scientific knowledge', 'They investigated reports of paranormal activity.', 'Olar adaty düşündirişi bolmadyk hadysalary derňediler.', 'C1'),
    ('extracurricular', '/ˌekstrəkəˈrɪkjələ/', 'ADJ', 'sapakdan daşary', 'внеучебный', 'outside the main course of study at a school or university', 'She joined several extracurricular activities.', 'Ol birnäçe sapakdan daşary çärelere gatnaşdy.', 'C1'),
    ('circumspect', '/ˈsɜːkəmˌspekt/', 'ADJ', 'seresap; oýlanyşykly', 'осмотрительный', 'careful to consider all possible risks before acting', 'Be circumspect when sharing personal information.', 'Şahsy maglumaty paýlaşanyňda seresap bol.', 'C2'),
    ('forewarned', '/fɔːˈwɔːnd/', 'ADJ', 'öňünden duýdurylan', 'заранее предупреждённый', 'given information about a possible danger in advance', 'We were forewarned about the difficult conditions.', 'Kyn şertler barada bize öňünden duýduryldy.', 'C1'),
    ('achievement', '/əˈtʃiːvmənt/', 'N', 'üstünlik; gazanylan netije', 'достижение', 'something important that someone has succeeded in doing', 'Graduating was a major achievement for her.', 'Okuwy tamamlamak onuň üçin uly üstünlik boldy.', 'B1'),
    ('censorship', '/ˈsensəʃɪp/', 'N', 'senzura', 'цензура', 'the practice of controlling what information people can see', 'The government introduced strict censorship.', 'Hökümet berk senzura girizdi.', 'C1'),
    ('fragrance', '/ˈfreɪɡrəns/', 'N', 'ýakymly ys', 'аромат', 'a pleasant smell, especially from flowers or perfume', 'The fragrance of spring flowers filled the room.', 'Bahar gülleriniň ýakymly ysy otagy doldurdy.', 'C1'),
    ('inspiration', '/ˌɪnspəˈreɪʃn/', 'N', 'ylham', 'вдохновение', 'the process of feeling encouraged to create or achieve something', 'Nature is a constant source of inspiration.', 'Tebigat hemişe ylham çeşmesidir.', 'B1'),
    ('ownership', '/ˈəʊnəʃɪp/', 'N', 'eýeçilik', 'собственность; владение', 'the state of legally owning something', 'The documents prove ownership of the land.', 'Resminamalar ýere eýeçiligi subut edýär.', 'B2'),
    ('portrayal', '/pɔːˈtreɪəl/', 'N', 'şekillendiriliş; beýan ediliş', 'изображение; трактовка', 'the way someone or something is shown in a book, film, or picture', 'The film’s portrayal of the city was realistic.', 'Filmde şäheriň şekillendirilişi hakykata ýakyndy.', 'C1'),
    ('racism', '/ˈreɪsɪzəm/', 'N', 'jynsparazlyk', 'расизм', 'unfair treatment because of someone’s race or origin', 'The campaign works to challenge racism.', 'Kampaniýa jynsparazlyga garşy göreşýär.', 'B2'),
    ('storage', '/ˈstɔːrɪdʒ/', 'N', 'saklamak; ammar ýeri', 'хранение; место для хранения', 'the act or place of keeping things for later use', 'We need more storage for our equipment.', 'Enjamlarymyz üçin has köp ammar ýeri gerek.', 'B1'),
    ('survival', '/səˈvaɪvl/', 'N', 'diri galmak; ýaşap galma', 'выживание', 'the state of continuing to live or exist', 'Clean water is essential for survival.', 'Arassa suw diri galmak üçin zerurdyr.', 'B2'),
    ('treatment', '/ˈtriːtmənt/', 'N', 'bejergi; garalýyş', 'лечение; обращение', 'medical care, or the way someone is dealt with', 'The treatment helped her recover quickly.', 'Bejergi onuň tiz sagalmagyna kömek etdi.', 'B1'),
    ('wisdom', '/ˈwɪzdəm/', 'N', 'paýhas; danalyk', 'мудрость', 'the ability to make good decisions based on experience', 'My grandfather shared his wisdom with us.', 'Atam paýhasyny biziň bilen paýlaşdy.', 'B2'),
    ('metaphorical', '/ˌmetəˈfɒrɪkl/', 'ADJ', 'göçme manyly', 'метафорический', 'using an image or comparison rather than a literal meaning', 'The phrase has a metaphorical meaning here.', 'Bu ýerde söz düzümi göçme manyda ulanylýar.', 'C1'),
    ('picturesque', '/ˌpɪktʃəˈresk/', 'ADJ', 'surat ýaly gözel', 'живописный', 'attractive in a way that looks like a picture', 'We stayed in a picturesque village.', 'Biz surat ýaly gözel obada galdyk.', 'C1'),
    ('rebellious', '/rɪˈbeljəs/', 'ADJ', 'garşy çykýan; gozgalaňçy', 'мятежный; непокорный', 'deliberately resisting rules or authority', 'He was a rebellious teenager.', 'Ol düzgünlere garşy çykýan ýetginjekdi.', 'B2'),
    ('snobbish', '/ˈsnɒbɪʃ/', 'ADJ', 'özünden pes görýän; tekepbir', 'снобистский', 'behaving as if people with less money or status are inferior', 'Her snobbish attitude annoyed her classmates.', 'Onuň tekepbir garaýşy synpdaşlaryny bizar etdi.', 'C1'),
    ('truthful', '/ˈtruːθfl/', 'ADJ', 'dogruçyl', 'правдивый', 'honest and saying what is true', 'Please give a truthful account of what happened.', 'Näme bolandygyny dogruçyl gürrüň bermegiňi haýyş edýärin.', 'B1'),
    ('lovable', '/ˈlʌvəbl/', 'ADJ', 'söýgä mynasyp; ýakymly', 'милый; достойный любви', 'easy to love because of a pleasant character', 'The lovable puppy followed us everywhere.', 'Ýakymly güjük bizi hemme ýerde yzarlady.', 'B2'),
    ('reversible', '/rɪˈvɜːsəbl/', 'ADJ', 'yzyna öwrüp bolýan', 'обратимый', 'able to be changed back to the original state', 'The chemical reaction is reversible.', 'Himiki täsiri yzyna öwrüp bolýar.', 'C1'),
    ('attentive', '/əˈtentɪv/', 'ADJ', 'ünsli; dykgatly', 'внимательный', 'listening or watching carefully', 'The audience was attentive throughout the talk.', 'Diňleýjiler çykyş boýy ünsli boldular.', 'B2'),
    ('brutal', '/ˈbruːtl/', 'ADJ', 'rehimsiz; gazaply', 'жестокий', 'extremely violent or unpleasant', 'The soldiers faced a brutal winter.', 'Esgerler gazaply gyşa duçar boldular.', 'B2'),
    ('childish', '/ˈtʃaɪldɪʃ/', 'ADJ', 'çaga ýaly; ýetişmedik', 'ребяческий', 'silly or immature in a way typical of a child', 'It was childish to blame everyone else.', 'Ähli kişini günäkärlemek ýetişmedik hereketdi.', 'B2'),
    ('catastrophic', '/ˌkætəˈstrɒfɪk/', 'ADJ', 'betbagtçylykly; weýran ediji', 'катастрофический', 'causing sudden and extremely serious damage', 'The flood had catastrophic effects.', 'Suw joşmasy weýran ediji täsir galdyrdy.', 'C1'),
    ('oppressive', '/əˈpresɪv/', 'ADJ', 'basyp ýatyrýan; eziji', 'гнетущий; угнетающий', 'unfairly controlling people or making life unpleasant', 'They lived under an oppressive regime.', 'Olar eziji düzgüniň astynda ýaşadylar.', 'C1'),
    ('soulful', '/ˈsəʊlfl/', 'ADJ', 'çuňňur duýguly', 'душевный', 'showing deep emotion or sensitivity', 'She sang the song in a soulful voice.', 'Ol aýdymy çuňňur duýgy bilen aýtdy.', 'C1'),
    ('statuesque', '/ˌstætʃuˈesk/', 'ADJ', 'heýkel ýaly syratly', 'статуарный; величественный', 'tall and attractive in an impressive way', 'The statuesque actor stood out in the crowd.', 'Syratly aktýor märekäniň içinde bada-bat saýlandy.', 'C2'),
])

# 2B — Vocabulary Bank printed pp.144–145; TG PDF p.191 uses the same target verbs.
ADDITIONS += group('2B', 144, [
    ('mooch', '/muːtʃ/', 'V', 'haýal, maksatsyz gezmek', 'бродить без дела', 'to walk slowly without a clear purpose', 'He mooched around the shops all afternoon.', 'Ol günortan boýy dükanlara haýal aýlandy.', 'C2'),
    ('amble', '/ˈæmbl/', 'V', 'haýal we rahat ýöremek', 'неторопливо прогуливаться', 'to walk at a relaxed, steady pace', 'We ambled along the river.', 'Biz derýanyň boýunda rahat gezdik.', 'C1'),
    ('dash', '/dæʃ/', 'V', 'okdurylyp ylgamak', 'мчаться', 'to run somewhere quickly', 'She dashed across the road to catch the bus.', 'Ol awtobusa ýetişmek üçin ýoldan okdurylyp geçdi.', 'B2'),
    ('rush', '/rʌʃ/', 'V', 'howlukmak; howlukmaç gitmek', 'спешить', 'to move or act very quickly', 'He rushed out without his coat.', 'Ol penjegini alman howlukmaç çykdy.', 'B1'),
    ('speed', '/spiːd/', 'V', 'örän çalt hereket etmek', 'нестись; мчаться', 'to move very quickly', 'The car sped away from the traffic lights.', 'Maşyn svetofordan örän çalt ugrady.', 'B1'),
    ('tear', '/teə/', 'V', 'okdurylyp geçmek', 'мчаться', 'to move somewhere very fast and suddenly', 'The cyclist tore down the hill.', 'Welosipedçi depeden aşak okdurylyp düşdi.', 'C1'),
    ('storm', '/stɔːm/', 'V', 'gaharly ýagdaýda çalt girip-çykmak', 'врываться; выбегать в гневе', 'to enter or leave a place angrily and quickly', 'She stormed out of the meeting.', 'Ol ýygnakdan gaharly çykyp gitdi.', 'B2'),
    ('strut', '/strʌt/', 'V', 'özüni görkezjek bolup ýöremek', 'важно вышагивать', 'to walk proudly as if you are important', 'He strutted into the room in a new suit.', 'Ol täze kostýumda otaga özüni görkezjek bolup girdi.', 'C2'),
    ('swagger', '/ˈswæɡə/', 'V', 'tekepbir ädimläp ýöremek', 'шествовать развязной походкой', 'to walk with too much confidence', 'The actor swaggered across the stage.', 'Aktýor sahnadan tekepbir ädimläp geçdi.', 'C2'),
    ('hike', '/haɪk/', 'V', 'uzak aralyga pyýada ýöremek', 'совершать пеший поход', 'to walk a long distance, especially in the countryside', 'We hiked through the forest for three hours.', 'Biz tokaýyň içinden üç sagat pyýada ýöredik.', 'B1'),
    ('limp', '/lɪmp/', 'V', 'agsap ýöremek', 'хромать', 'to walk unevenly because one leg hurts', 'He limped home after the match.', 'Ol oýundan soň agsap öýe gaýtdy.', 'B2'),
    ('scramble', '/ˈskræmbl/', 'V', 'dyrmaşyp çykmak', 'карабкаться', 'to climb quickly using your hands and feet', 'They scrambled up the steep path.', 'Olar dik ýodadan dyrmaşyp çykdylar.', 'C1'),
    ('wade', '/weɪd/', 'V', 'suwdan ýa-da palçykdan geçmek', 'брести вброд', 'to walk through water or mud', 'We waded across the shallow stream.', 'Biz ýalpak çeşmeden geçdik.', 'C1'),
], page_role='exact_student_book_page')
ADDITIONS += group('2B', 145, [
    ('creep', '/kriːp/', 'V', 'sessiz süýşüp barmak', 'красться', 'to move slowly and quietly, often to avoid being noticed', 'She crept past the sleeping dog.', 'Ol uklap ýatan itiň deňinden sessiz geçdi.', 'B2'),
    ('skulk', '/skʌlk/', 'V', 'ýaşyryn aýlanyp ýörmek', 'красться; скрываться', 'to move around secretly because you do not want to be seen', 'A stranger skulked around the alley.', 'Nätanyş biri geçelgede ýaşyryn aýlandy.', 'C2'),
    ('slip', '/slɪp/', 'V', 'bildirmän girip-çykmak', 'незаметно проскользнуть', 'to go somewhere quietly and without attracting attention', 'He slipped out before the meeting ended.', 'Ol ýygnak gutarmanka bildirmän çykdy.', 'B2'),
    ('sneak', '/sniːk/', 'V', 'gizlinlikde hereket etmek', 'пробираться тайком', 'to move somewhere secretly', 'The boy sneaked into the cinema.', 'Oglan kinoteatra gizlin girdi.', 'B2'),
    ('pad', '/pæd/', 'V', 'ýumşak ädimläp ýöremek', 'ступать мягко и бесшумно', 'to walk quietly and gently', 'The cat padded across the kitchen.', 'Pişik aşhanadan ýumşak ädimläp geçdi.', 'C2'),
    ('prowl', '/praʊl/', 'V', 'aw gözläp gezmek', 'рыскать; красться', 'to move around slowly while looking for something', 'A fox prowled around the farm at night.', 'Tilki gije fermanyň daşynda aýlandy.', 'C1'),
    ('scamper', '/ˈskæmpə/', 'V', 'çalt we ýeňil ylgamak', 'сновать; быстро бегать', 'to run quickly with short, light steps', 'The children scampered out to play.', 'Çagalar oýnamaga çalt ylgap çykdylar.', 'C2'),
    ('trot', '/trɒt/', 'V', 'kiçi çalt ädimler bilen ýöremek', 'бежать рысью', 'to run with short, quick steps', 'The pony trotted along the path.', 'Poniniň ýolda kiçi çalt ädimleri bilen gitdi.', 'B2'),
    ('waddle', '/ˈwɒdl/', 'V', 'ördege meňzäp yrgyldap ýöremek', 'переваливаться при ходьбе', 'to walk with short steps, moving from side to side', 'The penguin waddled across the ice.', 'Pingwin buzuň üstünden yrgyldap geçdi.', 'C1'),
])

# 3A — in-lesson Research language, printed p.26.
ADDITIONS += group('3A', 26, [
    ('rise', '/raɪz/', 'V', 'ýokarlanmak; artmak', 'расти; повышаться', 'to increase in amount, level, or number', 'The figures rose steadily over the decade.', 'Sanlar on ýylyň dowamynda yzygiderli ýokarlandy.', 'B2', 'rise steadily'),
    ('peak', '/piːk/', 'V', 'iň ýokary derejesine ýetmek', 'достигать пика', 'to reach the highest level or point', 'Sales peaked in the summer.', 'Satuw tomusda iň ýokary derejesine ýetdi.', 'B2'),
    ('decline', '/dɪˈklaɪn/', 'V', 'peselmek; azalmak', 'снижаться; уменьшаться', 'to become smaller, weaker, or less important', 'The number of smokers declined.', 'Çilim çekýänleriň sany azaldy.', 'B2'),
    ('decrease', '/dɪˈkriːs/', 'V', 'azalmak', 'уменьшаться', 'to become less in amount or number', 'The rate decreased slightly last year.', 'Dereje geçen ýyl az-kem peseldi.', 'B1'),
    ('increase', '/ɪnˈkriːs/', 'V', 'artmak; köpelmek', 'увеличиваться', 'to become greater in amount or number', 'The population increased rapidly.', 'Ilat çalt köpeldi.', 'B1'),
    ('accelerate', '/əkˈseləreɪt/', 'V', 'tizleşmek; çaltlandyrmak', 'ускоряться; ускорять', 'to happen or make something happen faster', 'The growth accelerated after 2010.', 'Ösüş 2010-njy ýyldan soň tizleşdi.', 'C1'),
    ('examine', '/ɪɡˈzæmɪn/', 'V', 'barlamak; öwrenmek', 'исследовать; изучать', 'to look at something carefully in order to understand it', 'The team examined the survey results.', 'Topar anketanyň netijelerini öwrendi.', 'B2'),
    ('analyse', '/ˈænəlaɪz/', 'V', 'seljermek', 'анализировать', 'to study information in detail', 'We analysed the data from the experiment.', 'Biz synagdan alnan maglumatlary seljerdik.', 'B2'),
    ('show', '/ʃəʊ/', 'V', 'görkezmek; subut etmek', 'показывать', 'to make a fact or result clear', 'The graph shows a clear difference.', 'Grafik aýdyň tapawudy görkezýär.', 'A2'),
    ('reveal', '/rɪˈviːl/', 'V', 'açyp görkezmek; aýan etmek', 'выявлять; раскрывать', 'to make something previously unknown known', 'The study revealed an unexpected pattern.', 'Barlag garaşylmadyk nusgany ýüze çykardy.', 'B2'),
    ('conclude', '/kənˈkluːd/', 'V', 'netije çykarmak', 'делать вывод', 'to decide something after considering the evidence', 'The researchers concluded that age mattered.', 'Alymlar ýaşyň ähmiýetiniň bardygy barada netije çykardylar.', 'B2'),
    ('prove', '/pruːv/', 'V', 'subut etmek', 'доказывать', 'to show that something is true', 'The results proved the original theory wrong.', 'Netijeler öňki nazaryýetiň ýalňyşdygyny subut etdi.', 'B1'),
    ('prioritise', '/praɪˈɒrətaɪz/', 'V', 'ileri tutmak; ileri derejede goýmak', 'расставлять приоритеты', 'to decide which things are most important', 'The team prioritised the most urgent questions.', 'Topar iň gyssagly soraglary ileri tutdy.', 'C1'),
    ('rank', '/ræŋk/', 'V', 'derejelere bölmek; orun bermek', 'ранжировать; ставить по рангу', 'to put people or things in order of importance or quality', 'Participants ranked the options from best to worst.', 'Gatnaşyjylar saýlawlary gowusyndan erbedine çenli tertipleşdirdiler.', 'B2'),
    ('claim', '/kleɪm/', 'V', 'iddia etmek', 'утверждать', 'to say that something is true, especially without proof', 'The report claims that exercise improves memory.', 'Hasabat maşk etmegiň ýady gowulandyrýandygyny öňe sürýär.', 'B2'),
    ('state', '/steɪt/', 'V', 'açyk aýtmak; beýan etmek', 'заявлять; излагать', 'to say something formally or clearly', 'The authors state their main conclusion.', 'Awtorlar esasy netijelerini aýdyň beýan edýärler.', 'B2'),
])

# 3B — Vocabulary Bank, printed pp.146–147; TG PDF p.192 supplies extra idiom practice.
ADDITIONS += group('3B', 146, [
    ('be-all and end-all', '/ˌbiː ɔːl ən ˈend ɔːl/', 'N', 'iň esasy zat', 'самое главное', 'the most important part of something', 'Money is not the be-all and end-all of life.', 'Pul durmuşdaky iň esasy zat däl.', 'C1'),
    ('one fell swoop', '/wʌn fel ˈswuːp/', 'PHR', 'bir gezekde; bir demde', 'одним махом', 'with one action that deals with several things at once', 'She finished all the shopping in one fell swoop.', 'Ol ähli söwdasyny bir gezekde tamamlady.', 'C2'),
    ('sorry sight', '/ˌsɒri ˈsaɪt/', 'N', 'betnyşan görnüş; tukat ýagdaý', 'жалкое зрелище', 'a very untidy, unpleasant, or sad thing to see', 'The garden was a sorry sight after the storm.', 'Tupan geçenden soň bagyň görnüşi tukatdy.', 'C1'),
    ('elbow room', '/ˈelbəʊ ruːm/', 'N', 'hereket üçin giňişlik', 'пространство для движения', 'enough space to move comfortably', 'There was no elbow room on the crowded train.', 'Adamdan doly otluda hereket etmäge ýer ýokdy.', 'C1'),
    ('good riddance', '/ˌɡʊd ˈrɪdns/', 'PHR', 'gidenine gowy boldy', 'скатертью дорога', 'said when you are pleased that someone or something has gone', 'He has finally left the team, and good riddance.', 'Ol ahyry topardan gitdi, gideni ýagşy.', 'C1'),
    ('flesh and blood', '/ˌfleʃ ən ˈblʌd/', 'PHR', 'öz ganyndan bolan adam', 'родная кровь', 'a close family member', 'I had to help him because he is my own flesh and blood.', 'Ol meniň öz ganymdan bolansoň kömek etmeli boldum.', 'C1'),
    ('not sleep a wink', '/nɒt sliːp ə ˈwɪŋk/', 'PHR', 'göz ýumman çykmak', 'не сомкнуть глаз', 'to be unable to sleep at all', 'I did not sleep a wink before the exam.', 'Synagyň öňüsyrasynda gözüm ilmedi.', 'B2'),
    ('vanish into thin air', '/ˌvænɪʃ ɪntə θɪn ˈeə/', 'PHR', 'yz-sorsuz ýitip gitmek', 'исчезнуть бесследно', 'to disappear in a mysterious or sudden way', 'My keys seem to have vanished into thin air.', 'Açarlarim yz-sorsuz ýitip giden ýaly.', 'C1'),
    ('eat someone out of house and home', '/iːt ˌsʌmwʌn aʊt əv ˌhaʊs ən ˈhəʊm/', 'PHR', 'biriniň azygyny köp iýmek', 'объедать кого-либо', 'to eat so much that you use up someone’s food', 'The teenagers eat us out of house and home.', 'Ýetginjekler öýdäki azygyň hemmesini iýip gutarýarlar.', 'C2'),
    ('lie low', '/ˌlaɪ ˈləʊ/', 'PHR', 'gözden uzak durmak', 'залечь на дно', 'to stay quiet and avoid attention for a while', 'He decided to lie low until the story was forgotten.', 'Ol waka ýatdan çykýança gözden uzak durmagy karar etdi.', 'C1'),
    ('send someone packing', '/ˌsend ˌsʌmwʌn ˈpækɪŋ/', 'PHR', 'birini kowmak; ugratmak', 'выставить кого-либо за дверь', 'to make someone leave a place or job', 'The manager sent the rude customer packing.', 'Ýolbaşçy gödek müşderini kowup goýberdi.', 'C1'),
    ('neither here nor there', '/ˌnaɪðə ˈhɪə nə ˈðeə/', 'PHR', 'ähmiýetsiz; bu ýerde möhüm däl', 'ни при чём; не имеет значения', 'not important to the matter being discussed', 'Your opinion is neither here nor there now.', 'Indi seniň pikiriň bu ýerde möhüm däl.', 'C1'),
    ("mum's the word", '/ˌmʌmz ðə ˈwɜːd/', 'PHR', 'hiç kime aýtma', 'никому ни слова', 'used to say that something must be kept secret', 'Mum’s the word about the surprise party.', 'Geň galdyryjy oturyşyk barada hiç kime aýtma.', 'C1'),
    ("the world's your oyster", '/ðə ˌwɜːldz jɔːr ˈɔɪstə/', 'PHR', 'isleseň ähli zada ýetip bilersiň', 'весь мир открыт перед тобой', 'you have many opportunities and can do anything you want', 'With your talent, the world’s your oyster.', 'Zehiniň bilen islän zadyňa ýetip bilersiň.', 'C1'),
    ('come what may', '/ˌkʌm wɒt ˈmeɪ/', 'PHR', 'näme bolsa-da', 'несмотря ни на что', 'whatever happens', 'I will support you, come what may.', 'Näme bolsa-da, men seni goldaryn.', 'C1'),
])

# 4A — Vocabulary Bank, printed p.148; all are listed on TG PDF p.193.
ADDITIONS += group('4A', 148, [
    ('cheap and cheerful', '/ˌtʃiːp ən ˈtʃɪəfl/', 'PHR', 'arzan we ýakymly', 'дёшево и сердито', 'simple and inexpensive but pleasant or useful', 'We found a cheap and cheerful café.', 'Biz arzan hem-de ýakymly kafäni tapdyk.', 'C1'),
    ('chicken and egg', '/ˌtʃɪkɪn ən ˈeɡ/', 'PHR', 'haýsysynyň öň gelendigini bilip bolmaýan mesele', 'проблема курицы и яйца', 'a situation in which it is hard to know which of two things caused the other', 'It is a chicken-and-egg problem.', 'Bu haýsysynyň öň gelendigini bilip bolmaýan mesele.', 'C1'),
    ('cut and dried', '/ˌkʌt ən ˈdraɪd/', 'PHR', 'öňünden anyk çözülen', 'предрешённый; ясный', 'already decided and unlikely to change', 'The arrangement is not cut and dried yet.', 'Ylalaşyk entek doly çözülmedi.', 'C1'),
    ('doom and gloom', '/ˌduːm ən ˈɡluːm/', 'PHR', 'umumy tukatlyk we umytsyzlyk', 'мрак и уныние', 'a feeling that everything is going badly', 'There is no need for all this doom and gloom.', 'Beýle umytsyzlyga hiç hili zerurlyk ýok.', 'C1'),
    ('face-to-face', '/ˌfeɪs tə ˈfeɪs/', 'PHR', 'ýüzbe-ýüz', 'лицом к лицу', 'in person, with people looking directly at each other', 'We finally discussed the problem face-to-face.', 'Biz ahyry meseläni ýüzbe-ýüz ara alyp maslahatlaşdyk.', 'B1'),
    ('far and wide', '/ˌfɑː ən ˈwaɪd/', 'PHR', 'giň töwerekde; uzak-uzak ýerlerde', 'повсюду; далеко вокруг', 'over a large area', 'The singer’s fans came from far and wide.', 'Aýdymçynyň muşdaklary uzak ýerlerden geldiler.', 'C1'),
    ('hand in hand', '/ˌhænd ɪn ˈhænd/', 'PHR', 'bilelikde; el-ele', 'рука об руку', 'together or closely connected', 'Poverty and poor health often go hand in hand.', 'Garyplyk bilen saglygyň ýaramazlygy köplenç bile bolýar.', 'B2'),
    ('heart-to-heart', '/ˌhɑːt tə ˈhɑːt/', 'N', 'açyk we çynlakaý gürrüň', 'откровенный разговор', 'an honest, personal conversation', 'We had a heart-to-heart about her worries.', 'Biz onuň aladalary barada açyk gürrüň etdik.', 'C1'),
    ('little by little', '/ˌlɪtl baɪ ˈlɪtl/', 'PHR', 'kem-kemden', 'постепенно', 'gradually, in small amounts or steps', 'Little by little, the puppy began to trust us.', 'Güjük kem-kemden bize ynanyp başlady.', 'B1'),
    ('neck and neck', '/ˌnek ən ˈnek/', 'PHR', 'deňme-deň', 'ноздря в ноздрю', 'at almost the same level in a race or competition', 'The two runners were neck and neck.', 'Iki ylgawçy deňme-deň gelýärdi.', 'C1'),
    ('out and about', '/ˌaʊt ən əˈbaʊt/', 'PHR', 'daşarda iş bilen aýlanyp ýörmek', 'выйти из дома по делам', 'going to different places and doing things', 'I have been out and about all morning.', 'Men irden bäri daşarda iş bilen aýlandym.', 'B2'),
    ('part and parcel', '/ˌpɑːt ən ˈpɑːsl/', 'PHR', 'aýrylmaz bölek', 'неотъемлемая часть', 'an essential and unavoidable part of something', 'Stress is part and parcel of this job.', 'Alada bu işiň aýrylmaz bölegidir.', 'C1'),
    ('pins and needles', '/ˌpɪnz ən ˈniːdlz/', 'PHR', 'sanjyma; çümüşme duýgusy', 'мурашки; покалывание', 'an uncomfortable tingling feeling in part of your body', 'I had pins and needles in my leg.', 'Aýagymda çümüşme duýgusy boldy.', 'B2'),
    ('rough and ready', '/ˌrʌf ən ˈredi/', 'PHR', 'ýönekeý we çalt taýýarlanan', 'грубый, но годный', 'simple and prepared quickly, but good enough', 'They made a rough and ready shelter.', 'Olar ýönekeýje gaçybatalga gurdular.', 'C1'),
    ('skin and bone', '/ˌskɪn ən ˈbəʊn/', 'PHR', 'örän hor', 'кожа да кости', 'extremely thin and weak-looking', 'After the illness, the dog was skin and bone.', 'Keselden soň it örän horlapdy.', 'B2'),
    ('step by step', '/ˌstep baɪ ˈstep/', 'PHR', 'ädimme-ädim', 'шаг за шагом', 'slowly and carefully, one stage at a time', 'Let’s solve the problem step by step.', 'Geliň, meseläni ädimme-ädim çözelň.', 'B1'),
    ('through and through', '/ˌθruː ən ˈθruː/', 'PHR', 'başdan-aýak; bütinleý', 'целиком и полностью', 'completely, in every way', 'She is a Londoner through and through.', 'Ol başdan-aýak londonly.', 'C1'),
    ('trial and error', '/ˌtraɪəl ən ˈerə/', 'PHR', 'synag we ýalňyşlyk arkaly öwrenmek', 'метод проб и ошибок', 'a way of learning by trying different methods and making mistakes', 'We found the answer by trial and error.', 'Biz jogaby synag we ýalňyşlyk arkaly tapdyk.', 'B2'),
])

# 4B — Vocabulary Bank, printed p.149; TG PDF p.194 supports the acronym set.
ADDITIONS += group('4B', 149, [
    ('acronym', '/ˈækrənɪm/', 'N', 'baş harplardan düzülen we söz ýaly aýdylýan gysgaltma', 'акроним', 'an abbreviation made from initial letters and pronounced as a word', 'NATO is an acronym.', 'NATO söz ýaly aýdylýan gysgaltmadyr.', 'C1'),
    ('initialism', '/ɪˈnɪʃəlɪzəm/', 'N', 'baş harplary aýratyn aýdylýan gysgaltma', 'инициальная аббревиатура', 'an abbreviation whose letters are pronounced separately', 'BBC is an initialism.', 'BBC harplary aýratyn aýdylýan gysgaltmadyr.', 'C2'),
    ('AIDS', '/eɪdz/', 'N', 'AIDS keseli', 'СПИД', 'a serious disease that damages the body’s ability to fight infection', 'AIDS is caused by HIV.', 'AIDS keseline HIV wirusy sebäp bolýar.', 'B2'),
    ('AKA', '/ˌeɪ keɪ ˈeɪ/', 'PHR', 'başga ady bilen belli', 'также известный как', 'an abbreviation meaning also known as', 'The musician, AKA DJ Fox, performed last night.', 'DJ Fox ady bilen hem tanalýan sazanda düýn çykyş etdi.', 'C1'),
    ('AWOL', '/ˈeɪwɒl/', 'ADJ', 'rugsatsyz ýok', 'самовольно отсутствующий', 'absent from a place without permission', 'The soldier was reported AWOL.', 'Esgeriň rugsatsyz ýokdugy habar berildi.', 'C1'),
    ('DOB', '/ˌdiː əʊ ˈbiː/', 'N', 'doglan senesi', 'дата рождения', 'an abbreviation for date of birth', 'Please enter your DOB on the form.', 'Anketada doglan senäňi ýaz.', 'B2'),
    ('FYI', '/ˌef waɪ ˈaɪ/', 'PHR', 'maglumat üçin', 'к вашему сведению', 'an abbreviation used to introduce useful information', 'FYI, the meeting starts at nine.', 'Maglumat üçin, ýygnak sagat dokuzda başlanýar.', 'B2'),
    ('GIF', '/ɡɪf/', 'N', 'hereketli şekil faýly', 'гифка; формат GIF', 'a digital image format that can show short animation', 'She sent me a funny GIF.', 'Ol maňa gülkünç hereketli şekil iberdi.', 'B2'),
    ('GMT', '/ˌdʒiː em ˈtiː/', 'N', 'Grinwiç orta wagty', 'время по Гринвичу', 'Greenwich Mean Time, the time at the Greenwich meridian', 'The flight leaves at 18:00 GMT.', 'Uçar Grinwiç wagty bilen 18:00-da ugraýar.', 'C1'),
    ('HIV', '/ˌeɪtʃ aɪ ˈviː/', 'N', 'AIDS keseline sebäp bolup bilýän wirus', 'ВИЧ', 'the virus that can cause AIDS', 'The test checks for HIV.', 'Synag HIV wirusynyň bardygyny barlaýar.', 'B2'),
    ('MBA', '/ˌem biː ˈeɪ/', 'N', 'iş dolandyryşy boýunça magistr derejesi', 'степень магистра делового администрирования', 'a postgraduate degree in business administration', 'He completed an MBA in London.', 'Ol Londonda iş dolandyryşy boýunça magistr derejesini aldy.', 'C1'),
    ('MP', '/ˌem ˈpiː/', 'N', 'parlament agzasy', 'член парламента', 'a person elected to represent people in a parliament', 'The MP spoke to local residents.', 'Parlament agzasy ýerli ýaşaýjylar bilen gepleşdi.', 'B2'),
    ('NASA', '/ˈnæsə/', 'N', 'ABŞ-nyň kosmos agentligi', 'НАСА', 'the United States government agency for space research', 'NASA sent a probe to Mars.', 'NASA Marsa barlag enjamyny iberdi.', 'B2'),
    ('PA', '/ˌpiː ˈeɪ/', 'N', 'şahsy kömekçi', 'личный помощник', 'a personal assistant who helps someone with work', 'Her PA arranged the appointments.', 'Onuň PA duşuşyklary tertipleşdirdi.', 'B2'),
    ('POTUS', '/ˈpəʊtəs/', 'N', 'ABŞ-nyň prezidenti', 'президент США', 'an informal abbreviation for the President of the United States', 'The report was sent to POTUS.', 'Hasabat ABŞ-nyň prezidentine iberildi.', 'C1'),
    ('POW', '/ˌpiː əʊ ˈdʌbljuː/', 'N', 'söweş ýesiri', 'военнопленный', 'a prisoner captured during a war', 'The POW was released after the agreement.', 'Ylalaşykdan soň söweş ýesiri boşadyldy.', 'C1'),
    ('SUV', '/ˌes juː ˈviː/', 'N', 'uly ýolagçy awtoulagy', 'внедорожник', 'a large vehicle designed for road and rough-ground use', 'They rented an SUV for the trip.', 'Syýahat üçin uly awtoulag kireýine aldylar.', 'B2'),
    ('UFO', '/ˌjuː ef ˈəʊ/', 'N', 'näbelli uçýan jisim', 'НЛО', 'an object seen in the sky that cannot be identified', 'Several people reported seeing a UFO.', 'Birnäçe adam näbelli uçýan jisimi görendigini aýtdy.', 'B2'),
    ('USB', '/ˌjuː es ˈbiː/', 'N', 'kompýuter enjamlaryny birikdirýän ulgam', 'USB; универсальная последовательная шина', 'a standard used to connect devices to computers', 'Save the file to a USB drive.', 'Faýly USB ýat kartasyna ýaz.', 'B2'),
    ('USP', '/ˌjuː es ˈpiː/', 'N', 'harydyň özboluşly artykmaçlygy', 'уникальное торговое предложение', 'the feature that makes a product different from its competitors', 'Friendly service is the café’s USP.', 'Mylaýym hyzmat kafäniň özboluşly artykmaçlygydyr.', 'C1'),
    ('AFAIK', '/ˌeɪ ef eɪ aɪ ˈkeɪ/', 'PHR', 'bilşime görä', 'насколько мне известно', 'an abbreviation meaning as far as I know', 'AFAIK, the shop is still open.', 'Bilşime görä, dükan henizem açyk.', 'C1'),
    ('BFF', '/ˌbiː ef ˈef/', 'N', 'iň ýakyn dost', 'лучший друг навсегда', 'an informal abbreviation for best friends forever', 'She is my BFF from school.', 'Ol mekdepden bäri iň ýakyn dostum.', 'B2'),
    ('BTW', '/ˌbiː tiː ˈdʌbljuː/', 'PHR', 'aýtsak, ýeri gelende', 'кстати', 'an abbreviation meaning by the way', 'BTW, I found your keys.', 'Ýeri gelende, açarlaryňy tapdym.', 'B1'),
    ('BRB', '/ˌbiː ɑː ˈbiː/', 'PHR', 'häzir gaýdyp gelýärin', 'скоро вернусь', 'an abbreviation meaning be right back', 'BRB, I need to answer the door.', 'Häzir gaýdyp gelýärin, gapyny açmaly.', 'B2'),
    ('FOMO', '/ˈfəʊməʊ/', 'N', 'bir zady sypdyrmakdan gorky', 'страх упустить что-либо', 'anxiety that you are missing an enjoyable or important experience', 'Social media can increase FOMO.', 'Sosial ulgamlar bir zady sypdyrmak gorkusyny güýçlendirip biler.', 'C1'),
    ('IMO', '/ˌaɪ em ˈəʊ/', 'PHR', 'meniň pikirimçe', 'по моему мнению', 'an abbreviation meaning in my opinion', 'IMO, the earlier train is better.', 'Meniň pikirimçe, irki otly has gowy.', 'B2'),
    ('LOL', '/ˌel əʊ ˈel/', 'PHR', 'gaty gülýärin; gülkünç', 'громко смеюсь; смешно', 'an informal abbreviation used to show that something is funny', 'He added LOL at the end of the message.', 'Ol habaryň soňuna gülkünç diýen manyda LOL ýazdy.', 'B1'),
    ('OMG', '/ˌəʊ em ˈdʒiː/', 'PHR', 'wah; haýran galmagy bildirýär', 'о боже', 'an informal abbreviation expressing surprise', 'OMG, I did not expect that!', 'Wah, muny garaşmandym!', 'B1'),
    ('OMW', '/ˌəʊ em ˈdʌbljuː/', 'PHR', 'ýolda; häzir barýaryn', 'уже в пути', 'an abbreviation meaning on my way', 'I am OMW; see you in ten minutes.', 'Ýolda, on minutdan görüşeris.', 'B2'),
    ('TBH', '/ˌtiː biː ˈeɪtʃ/', 'PHR', 'dogrusyny aýtsam', 'честно говоря', 'an abbreviation meaning to be honest', 'TBH, I preferred the first design.', 'Dogrusyny aýtsam, birinji dizaýn maňa has ýarady.', 'B2'),
    ('PhD', '/ˌpiː eɪtʃ ˈdiː/', 'N', 'filosofiýa doktory derejesi', 'степень доктора философии', 'the highest university degree in many subjects', 'She earned a PhD in linguistics.', 'Ol dil biliminden PhD derejesini aldy.', 'B2'),
])

# 5A — Vocabulary Bank, printed pp.150–151; TG PDF p.195 corroborates emotion words.
ADDITIONS += group('5A', 150, [
    ('contented', '/kənˈtentɪd/', 'ADJ', 'kanagatly; göwni hoş', 'довольный', 'happy and satisfied with what you have', 'He felt contented with his quiet life.', 'Ol asuda durmuşyndan kanagatlydy.', 'B2'),
    ('gratified', '/ˈɡrætɪfaɪd/', 'ADJ', 'kanagatlanan; göwni hoş bolan', 'удовлетворённый', 'pleased because something you hoped for has happened', 'She felt gratified by their support.', 'Olaryň goldawy ony begendirdi.', 'C1'),
    ('upbeat', '/ˈʌpbiːt/', 'ADJ', 'şadyýan; umytly', 'жизнерадостный; оптимистичный', 'cheerful and hopeful about the future', 'The team remained upbeat after the defeat.', 'Ýeňlişden soň hem topar umytly galdy.', 'B2'),
    ('exhilarated', '/ɪɡˈzɪləreɪtɪd/', 'ADJ', 'örän şat; joşgunly', 'ликующий', 'extremely happy and excited', 'I felt exhilarated after the mountain walk.', 'Dag gezelenjinden soň özümi örän şat duýdum.', 'C1'),
    ('overjoyed', '/ˌəʊvəˈdʒɔɪd/', 'ADJ', 'örän begenýän', 'безмерно счастливый', 'extremely happy about something', 'They were overjoyed to hear the news.', 'Habar eşidip, olar örän begendiler.', 'B2'),
    ('listless', '/ˈlɪstləs/', 'ADJ', 'güýçsüz we biperwaý', 'вялый; апатичный', 'having little energy or interest', 'The heat made everyone feel listless.', 'Yssy hemmeleri güýçsüz duýdurdy.', 'C1'),
    ('wistful', '/ˈwɪstfl/', 'ADJ', 'küýseýän; gamgyn arzuwly', 'тоскливый; мечтательный', 'sad because you want something that you cannot have', 'She gave a wistful smile as she left.', 'Ol gidip barýarka küýsegli ýylgyrdy.', 'C1'),
    ('dejected', '/dɪˈdʒektɪd/', 'ADJ', 'ruhdan düşen', 'унылый; подавленный', 'unhappy and disappointed', 'The players looked dejected after the final whistle.', 'Soňky jürlewükden soň oýunçylar ruhdan düşen görünýärdi.', 'C1'),
    ('dispirited', '/dɪˈspɪrɪtɪd/', 'ADJ', 'ruhdan düşen; höwessiz', 'удручённый', 'having lost hope or enthusiasm', 'The long delay left passengers dispirited.', 'Uzak gijikme ýolagçylary ruhdan düşürdi.', 'C1'),
    ('inconsolable', '/ˌɪnkənˈsəʊləbl/', 'ADJ', 'teselli tapmaýan', 'безутешный', 'so upset that it is impossible to make you feel better', 'The child was inconsolable when the toy broke.', 'Oýnawaç döwülende çagany hiç zat bilen köşeşdirip bolmady.', 'C2'),
    ('peeved', '/piːvd/', 'ADJ', 'biraz gaharly; göwni galan', 'раздосадованный', 'slightly annoyed or offended', 'He was peeved that nobody had called.', 'Hiç kim jaň etmändigi üçin onuň göwni galdy.', 'C1'),
    ('exasperated', '/ɪɡˈzɑːspəreɪtɪd/', 'ADJ', 'gaty bizar bolan', 'раздражённый до предела', 'very annoyed because something continues to go wrong', 'She sounded exasperated by the repeated questions.', 'Gaýtalanýan soraglar ony gaty bizar eden ýaly eşidildi.', 'C1'),
    ('indignant', '/ɪnˈdɪɡnənt/', 'ADJ', 'adalatsyzlyga gaharly', 'возмущённый', 'angry because something seems unfair', 'He was indignant at the unfair accusation.', 'Ol adalatsyz aýyplama sebäpli gaharlydy.', 'C1'),
    ('incensed', '/ɪnˈsenst/', 'ADJ', 'örän gaharly', 'разгневанный', 'extremely angry', 'Local residents were incensed by the decision.', 'Ýerli ýaşaýjylar bu karara örän gaharlandylar.', 'C1'),
    ('livid', '/ˈlɪvɪd/', 'ADJ', 'gazapdan ýaňa aňk-taňk bolan', 'взбешённый', 'extremely angry', 'She was livid when she saw the damage.', 'Zyýany görende ol gazaba mündi.', 'C1'),
    ('outraged', '/ˈaʊtreɪdʒd/', 'ADJ', 'gazaplanan; çuňňur nägile', 'возмущённый', 'very angry and shocked by something unfair', 'People were outraged by the abuse of power.', 'Adamlar häkimiýetiň hyýanatçylykly ulanylmagyna gazaplandylar.', 'C1'),
    ('aghast', '/əˈɡɑːst/', 'ADJ', 'aňk-taňk bolan; gorkup haýran galan', 'поражённый; потрясённый', 'very shocked or frightened by something', 'We were aghast at the sudden cost.', 'Duýdansyz çykdajyny eşidip aňk-taňk bolduk.', 'C1'),
    ('rattled', '/ˈrætld/', 'ADJ', 'tolgunan; aljyraňňy', 'растерянный; выбитый из колеи', 'nervous and confused after something unexpected', 'The unexpected question left him rattled.', 'Garaşylmadyk sorag ony aljyratdy.', 'C1'),
    ('unnerved', '/ˌʌnˈnɜːvd/', 'ADJ', 'howatyrlanan; ynamsyz bolan', 'встревоженный', 'made nervous or less confident', 'The darkness unnerved the hikers.', 'Garaňkylyk gezelenje çykanlary howatyrlandyrdy.', 'C1'),
    ('panic-stricken', '/ˈpænɪk strɪkən/', 'ADJ', 'howsala düşen', 'охваченный паникой', 'suddenly so frightened that you cannot think clearly', 'The panic-stricken crowd ran for the exits.', 'Howsala düşen mähelle çykalgalara tarap ylgady.', 'C1'),
])
ADDITIONS += group('5A', 151, [
    ('be down in the dumps', '/biː ˌdaʊn ɪn ðə ˈdʌmps/', 'PHR', 'göwni çökgün bolmak', 'быть в унынии', 'to feel unhappy and without energy', 'He has been down in the dumps all week.', 'Ol tutuş hepde göwni çökgün boldy.', 'B2'),
    ('be in the depths of despair', '/biː ɪn ðə ˌdepθs əv dɪˈspeə/', 'PHR', 'çuňňur umytsyzlykda bolmak', 'быть в глубоком отчаянии', 'to feel extremely unhappy and hopeless', 'She was in the depths of despair after the loss.', 'Ýitgiden soň ol çuňňur umytsyzlyga düşdi.', 'C1'),
    ('be on top of the world', '/biː ɒn ˌtɒp əv ðə ˈwɜːld/', 'PHR', 'özüni örän bagtly duýmak', 'быть на седьмом небе', 'to feel extremely happy and successful', 'I was on top of the world after passing.', 'Synagdan geçenden soň özümi örän bagtly duýdum.', 'B2'),
    ('be scared to death', '/biː ˌskeəd tə ˈdeθ/', 'PHR', 'gaty gorkmak', 'умирать от страха', 'to be extremely frightened', 'The thunder scared the children to death.', 'Gök gürlemesi çagalary gaty gorkuzdy.', 'B2'),
    ('go to pieces', '/ˌɡəʊ tə ˈpiːsɪz/', 'PHR', 'özüňi ýitirip, ruhdan düşmek', 'раскиснуть; потерять самообладание', 'to become unable to control your emotions', 'He went to pieces when he heard the news.', 'Habar eşidende ol özüni ýitirdi.', 'C1'),
    ('have a sinking feeling', '/hæv ə ˌsɪŋkɪŋ ˈfiːlɪŋ/', 'PHR', 'ýüregiň bir zatdan gysmagy', 'испытывать дурное предчувствие', 'to suddenly feel that something bad is going to happen', 'I had a sinking feeling when I saw the letter.', 'Hat görnen badyna ýüregim bir zatdan gysdy.', 'C1'),
    ('jump out of your skin', '/ˌdʒʌmp aʊt əv jɔː ˈskɪn/', 'PHR', 'gaty gorkup tisginmek', 'вздрагивать от страха', 'to react with sudden and extreme fright', 'The loud bang made me jump out of my skin.', 'Gaty ses meni gorkudan tisgindirdi.', 'C1'),
    ('shake like a leaf', '/ˌʃeɪk laɪk ə ˈliːf/', 'PHR', 'ýaprak ýaly sandyrap durmak', 'дрожать как лист', 'to tremble because you are very frightened or cold', 'He was shaking like a leaf before the speech.', 'Çykyşdan öň ol ýaprak ýaly sandyraýardy.', 'B2'),
    ('throw a wobbly', '/ˌθrəʊ ə ˈwɒbli/', 'PHR', 'duýdansyz gaharlanmak', 'устроить истерику', 'to suddenly become very angry or upset', 'Dad threw a wobbly when he saw the mess.', 'Kakasy bulaşyklygy görende duýdansyz gaharlanyp başlady.', 'C2'),
    ('make your blood boil', '/ˌmeɪk jɔː blʌd ˈbɔɪl/', 'PHR', 'gaty gaharyňy getirmek', 'приводить в бешенство', 'to make you extremely angry', 'It makes my blood boil when people cheat.', 'Adamlaryň aldaw etmegi meni gaty gaharladýar.', 'C1'),
    ('make your day', '/ˌmeɪk jɔː ˈdeɪ/', 'PHR', 'günüňi şat etmek', 'сделать чей-либо день', 'to make you very happy', 'Your kind message really made my day.', 'Mähirli habaryň günümi şat etdi.', 'B2'),
])

# 5B — in-lesson nationalities box, printed p.51.
ADDITIONS += group('5B', 51, [
    ('Argentinian', '/ˌɑːdʒənˈtɪniən/', 'N', 'argentinaly; Argentina raýaty', 'аргентинец; аргентинка', 'a person from Argentina', 'An Argentinian joined our group.', 'Toparymyza argentinaly biri goşuldy.', 'B1'),
    ('Dane', '/deɪn/', 'N', 'daniýaly', 'датчанин; датчанка', 'a person from Denmark', 'The guide was a Dane who knew the coast well.', 'Gid kenary gowy tanaýan daniýalydy.', 'B2'),
    ('Finn', '/fɪn/', 'N', 'finlýandiýaly', 'финн; финка', 'a person from Finland', 'A Finn explained the local customs.', 'Finlýandiýaly biri ýerli däpleri düşündirdi.', 'B2'),
    ('Pole', '/pəʊl/', 'N', 'polýak', 'поляк; полька', 'a person from Poland', 'The team includes a Pole and a Czech.', 'Toparda polýak we çeh bar.', 'B2'),
    ('Scot', '/skɒt/', 'N', 'şotlandiýaly', 'шотландец; шотландка', 'a person from Scotland', 'He is a Scot who grew up in Glasgow.', 'Ol Glazgo şäherinde ulalan şotlandiýaly.', 'B2'),
    ('Swede', '/swiːd/', 'N', 'şwesiýaly', 'швед; шведка', 'a person from Sweden', 'The Swede spoke excellent English.', 'Şwesiýaly iňlisçe örän gowy gepleýärdi.', 'B2'),
    ('Turk', '/tɜːk/', 'N', 'türk', 'турок; турчанка', 'a person from Turkey', 'Our new neighbour is a Turk.', 'Täze goňşymyz türk.', 'B2'),
    ('Spaniard', '/ˈspænjəd/', 'N', 'ispaniýaly', 'испанец; испанка', 'a person from Spain', 'The Spaniard taught us a few phrases.', 'Ispaniýaly bize birnäçe söz düzümini öwretdi.', 'B2'),
    ('Greek', '/ɡriːk/', 'N', 'grek', 'грек; гречанка', 'a person from Greece', 'A Greek family opened the restaurant.', 'Restorany grek maşgalasy açdy.', 'B1'),
    ('Swiss', '/swɪs/', 'N', 'şweýsariýaly', 'швейцарец; швейцарка', 'a person from Switzerland', 'The Swiss are known for several traditions.', 'Şweýsariýalylar birnäçe däpleri bilen tanalýar.', 'B1'),
    ('Japanese', '/ˌdʒæpəˈniːz/', 'N', 'ýapon', 'японец; японка', 'a person from Japan', 'A Japanese student joined the class.', 'Sapaga ýapon talyby goşuldy.', 'B1'),
    ('Thai', '/taɪ/', 'N', 'taýlandly', 'таец; тайка', 'a person from Thailand', 'The Thai cook showed us how to make the dish.', 'Taýlandly aşpez nahary taýýarlamagy görkezdi.', 'B1'),
])

# 6A — p.58 making-things box and Vocabulary Bank pp.152–153; TG PDF p.196 supports collocations.
ADDITIONS += group('6A', 58, [
    ('bend', '/bend/', 'V', 'egmek; bükmek', 'сгибать', 'to make something straight become curved', 'Bend the wire into a circle.', 'Simy tegelek edip egiň.', 'B1'),
    ('clip', '/klɪp/', 'V', 'gysgyç bilen berkitmek', 'скреплять зажимом', 'to fasten something with a clip', 'Clip the two pieces together.', 'Iki bölegi gysgyç bilen birleşdiriň.', 'B2'),
    ('fan', '/fæn/', 'V', 'ýelejiretmek; ýel bermek', 'обдувать; раздувать', 'to make air move over something', 'Fan the paint so it dries faster.', 'Boýag tiz guraýança oňa ýel beriň.', 'B2'),
    ('hole', '/həʊl/', 'V', 'deşik deşmek', 'проделывать отверстие', 'to make a hole in something', 'Hole the card before you thread the string.', 'Ýüpi geçirmekden öň kartonda deşik deşiň.', 'B2'),
    ('loosen', '/ˈluːsn/', 'V', 'gowşatmak', 'ослаблять', 'to make something less tight', 'Loosen the screw with a small tool.', 'Burç nurbaty kiçi gural bilen gowşadyň.', 'B1'),
    ('nail', '/neɪl/', 'V', 'dyrnak bilen berkitmek', 'прибивать гвоздём', 'to fasten something using a nail', 'Nail the shelf to the wall.', 'Tekjäni diwara dyrnak bilen berkidiň.', 'B1'),
    ('saw', '/sɔː/', 'V', 'byçgy bilen kesmek', 'пилить', 'to cut something using a saw', 'He sawed the plank in half.', 'Ol tagtany byçgy bilen ikä böldi.', 'B1'),
    ('tighten', '/ˈtaɪtn/', 'V', 'berkitmek; çekmek', 'затягивать', 'to make something tighter or more firmly fixed', 'Tighten the lid before you carry the jar.', 'Bankany götermezden öň gapagyny berkidiň.', 'B1'),
    ('unscrew', '/ʌnˈskruː/', 'V', 'nurbaty aýyrmak', 'отвинчивать', 'to remove something by turning it', 'Unscrew the cover carefully.', 'Gapagy seresaplyk bilen aýryň.', 'B2'),
    ('wire', '/ˈwaɪə/', 'V', 'sim bilen birikdirmek', 'соединять проводом', 'to connect something using electrical wire', 'An electrician wired the new lights.', 'Elektrikçi täze çyralary sim bilen birikdirdi.', 'B2'),
], section='vocabulary', tg_pdf_page=None)
ADDITIONS += group('6A', 152, [
    ('badly', '/ˈbædli/', 'ADV', 'örän; ýaramaz derejede', 'сильно; плохо', 'to a great or serious degree, or in a poor way', 'The town was badly damaged in the storm.', 'Tupan şäheri örän zaýalady.', 'A2', 'badly damaged'),
    ('blissfully', '/ˈblɪsfəli/', 'ADV', 'örän bagtly ýagdaýda', 'блаженно', 'in a way that shows complete happiness', 'They were blissfully unaware of the delay.', 'Olar gijikmeden bihabar, rahat ýagdaýdadylar.', 'C1', 'blissfully unaware'),
    ('fiercely', '/ˈfɪəsli/', 'ADV', 'gazaply; güýçli ýagdaýda', 'яростно; ожесточённо', 'in a strong, angry, or determined way', 'The rivals competed fiercely.', 'Garşydaşlar gazaply bäsleşdiler.', 'C1', 'compete fiercely'),
    ('firmly', '/ˈfɜːmli/', 'ADV', 'berk; ynamly ýagdaýda', 'твёрдо; решительно', 'in a strong or definite way', 'She firmly rejected the offer.', 'Ol teklibi berk ret etdi.', 'B2', 'firmly reject'),
    ('fully', '/ˈfʊli/', 'ADV', 'doly; bütinleý', 'полностью', 'completely or to the greatest possible degree', 'The building is fully accessible.', 'Bina doly elýeterlidir.', 'B1', 'fully aware'),
    ('happily', '/ˈhæpɪli/', 'ADV', 'bagtly ýagdaýda', 'счастливо', 'in a happy way', 'They lived happily together for years.', 'Olar ýyllar boýy bile bagtly ýaşadylar.', 'A2'),
    ('painfully', '/ˈpeɪnfəli/', 'ADV', 'örän; agyryly ýagdaýda', 'болезненно; мучительно', 'in a way that causes physical or emotional pain', 'The truth was painfully obvious.', 'Hakykat örän aýdyňdy.', 'C1', 'painfully obvious'),
    ('prohibitively', '/prəˈhɪbɪtɪvli/', 'ADV', 'aşa ýokary derejede', 'непомерно', 'to a degree that prevents something because it is too costly', 'The tickets were prohibitively expensive.', 'Petekler aşa gymmatdy.', 'C2', 'prohibitively expensive'),
    ('quietly', '/ˈkwaɪətli/', 'ADV', 'ýuwaşlyk bilen', 'тихо; спокойно', 'in a quiet or unobtrusive way', 'The company quietly changed its policy.', 'Kompaniýa syýasatyny sessiz-üýnsüz üýtgetdi.', 'B1'),
    ('reasonably', '/ˈriːznəbli/', 'ADV', 'ýeterlik derejede; ýerlikli', 'достаточно; разумно', 'to a fair or acceptable degree', 'The hotel is reasonably priced.', 'Myhmanhananyň bahasy ýerlikli.', 'B2', 'reasonably priced'),
    ('ridiculously', '/rɪˈdɪkjələsli/', 'ADV', 'aşa; gülkünç derejede', 'смехотворно; чрезвычайно', 'to an unreasonable or surprisingly great degree', 'The shoes were ridiculously expensive.', 'Aýakgaplar aşa gymmatdy.', 'B2', 'ridiculously expensive'),
    ('flatly', '/ˈflætli/', 'ADV', 'kesgitli ýagdaýda; göni', 'категорически', 'in a definite way that leaves no doubt', 'He flatly denied the accusation.', 'Ol aýyplamany kesgitli inkär etdi.', 'C1', 'flatly deny'),
    ('freely', '/ˈfriːli/', 'ADV', 'erkin ýagdaýda; päsgelçiliksiz', 'свободно', 'without restriction or difficulty', 'The ideas flowed freely during the discussion.', 'Ara alyp maslahatlaşylanda pikirler erkin aýdyldy.', 'B2'),
    ('greatly', '/ˈɡreɪtli/', 'ADV', 'ep-esli; örän', 'значительно', 'to a large degree', 'The new system greatly improved safety.', 'Täze ulgam howpsuzlygy ep-esli ýokarlandyrdy.', 'B2'),
    ('violently', '/ˈvaɪələntli/', 'ADV', 'zorluk bilen; gazaply', 'яростно; насильственно', 'with great force or strong emotion', 'The door shook violently in the wind.', 'Şemalda gapy güýçli sandyrady.', 'B2'),
    ('categorically', '/ˌkætəˈɡɒrɪkli/', 'ADV', 'kesgitli we gürrüňsiz ýagdaýda', 'категорически', 'in a clear and definite way', 'The spokesperson categorically denied the claim.', 'Metbugat wekili bu pikiri kesgitli inkär etdi.', 'C2', 'categorically deny'),
    ('warmly', '/ˈwɔːmli/', 'ADV', 'mähirli ýagdaýda', 'тепло; сердечно', 'in a friendly and kind way', 'The hosts welcomed us warmly.', 'Öý eýeleri bizi mähirli garşyladylar.', 'B1'),
])

# 6B — Vocabulary Bank: mathematical language printed p.154; measures p.155.
ADDITIONS += group('6B', 154, [
    ('plus', '/plʌs/', 'PREP', 'goşmak; üstüne', 'плюс', 'used to show that one number is added to another', 'Three plus four equals seven.', 'Üç goşmak dört deňdir ýedi.', 'A2'),
    ('minus', '/ˈmaɪnəs/', 'PREP', 'aýyrmak; minus', 'минус', 'used to show that one number is taken away from another', 'Ten minus six is four.', 'Ondan altyny aýyrsaň dört galýar.', 'A2'),
    ('times', '/taɪmz/', 'PREP', 'köpeltmek', 'умножить на', 'used to show that one number is multiplied by another', 'Five times three is fifteen.', 'Bäş gezek üç on bäş bolýar.', 'A2'),
    ('divided by', '/dɪˌvaɪdɪd ˈbaɪ/', 'PHR', 'bölünen', 'разделить на', 'used to show that one number is divided by another', 'Twenty divided by five is four.', 'Ýigrimi bäşe bölünende dört bolýar.', 'B1'),
    ('equals', '/ˈiːkwəlz/', 'V', 'deňdir', 'равняется', 'has the same value as', 'Eight plus two equals ten.', 'Sekiz goşmak iki on bolýar.', 'A2'),
    ('square root', '/ˌskweə ˈruːt/', 'N', 'kwadrat kök', 'квадратный корень', 'a number that is multiplied by itself to make another number', 'The square root of nine is three.', 'Dokuzdan alnan kwadrat kök üçdür.', 'B2'),
    ('odd number', '/ˌɒd ˈnʌmbə/', 'N', 'täklik san', 'нечётное число', 'a whole number that cannot be divided exactly by two', 'Seven is an odd number.', 'Ýedi täklik sandyr.', 'B1'),
    ('even number', '/ˌiːvn ˈnʌmbə/', 'N', 'jübüt san', 'чётное число', 'a whole number that can be divided exactly by two', 'Twelve is an even number.', 'On iki jübüt sandyr.', 'B1'),
    ('nought', '/nɔːt/', 'N', 'nol', 'ноль', 'the number zero', 'The temperature fell to nought overnight.', 'Gijäniň dowamynda temperatura nola düşdi.', 'B2'),
    ('pi', '/paɪ/', 'N', 'pi sany', 'число пи', 'the mathematical number approximately equal to 3.14', 'We used pi to calculate the circle’s area.', 'Tegelegiň meýdanyny hasaplamak üçin pi sanyny ulandyk.', 'B2'),
    ('radius', '/ˈreɪdiəs/', 'N', 'radius', 'радиус', 'a straight line from the centre of a circle to its edge', 'The circle has a radius of five centimetres.', 'Tegelegiň radiusy bäş santimetr.', 'B2'),
    ('diameter', '/daɪˈæmɪtə/', 'N', 'diametr', 'диаметр', 'a straight line across a circle through its centre', 'Measure the diameter of the wheel.', 'Tigiriň diametrini ölçäň.', 'B2'),
    ('right angle', '/ˌraɪt ˈæŋɡl/', 'N', 'göni burç', 'прямой угол', 'an angle of 90 degrees', 'The two lines meet at a right angle.', 'Iki çyzyk göni burç bilen kesişýär.', 'B1'),
    ('cubic centimetre', '/ˌkjuːbɪk ˈsentɪmiːtə/', 'N', 'kub santimetr', 'кубический сантиметр', 'a unit for measuring volume equal to a cube one centimetre on each side', 'The bottle holds 250 cubic centimetres.', 'Çüýşe 250 kub santimetr suw sygdyryar.', 'C1'),
    ('line graph', '/ˈlaɪn ɡrɑːf/', 'N', 'çyzykly grafik', 'линейный график', 'a graph that shows information using points joined by lines', 'The line graph shows sales rising.', 'Çyzykly grafik satuwyň artýandygyny görkezýär.', 'B1'),
    ('pie chart', '/ˈpaɪ tʃɑːt/', 'N', 'tegelek diagramma', 'круговая диаграмма', 'a circular chart divided into sections to show proportions', 'The pie chart compares household spending.', 'Tegelek diagramma öý hojalygynyň çykdajylaryny deňeşdirýär.', 'B1'),
    ('bar chart', '/ˈbɑː tʃɑːt/', 'N', 'sütünli diagramma', 'столбчатая диаграмма', 'a chart that uses rectangular bars to compare values', 'The bar chart compares the three regions.', 'Sütünli diagramma üç sebiti deňeşdirýär.', 'B1'),
    ('Venn diagram', '/ˈven ˌdaɪəɡræm/', 'N', 'Wenn diagrammasy', 'диаграмма Венна', 'a diagram of overlapping circles used to compare groups', 'Use a Venn diagram to show the similarities.', 'Meňzeşlikleri görkezmek üçin Wenn diagrammasyny ulanyň.', 'C1'),
])
ADDITIONS += group('6B', 155, [
    ('inch', '/ɪntʃ/', 'N', 'dýuým', 'дюйм', 'a unit of length equal to 2.54 centimetres', 'The screen is twelve inches wide.', 'Ekranyň ini on iki dýuým.', 'B1'),
    ('gallon', '/ˈɡælən/', 'N', 'gallon', 'галлон', 'a unit for measuring liquid volume', 'The tank holds five gallons of water.', 'Gap bäş gallon suw sygdyryar.', 'B2'),
    ('pint', '/paɪnt/', 'N', 'pinta', 'пинта', 'a unit for measuring liquid, equal to about half a litre in the UK', 'He ordered a pint of milk.', 'Ol bir pinta süýt sargyt etdi.', 'B2'),
    ('pound', '/paʊnd/', 'N', 'funt', 'фунт', 'a unit of weight equal to 16 ounces', 'The parcel weighs two pounds.', 'Bukjanyň agramy iki funt.', 'B1'),
    ('yard', '/jɑːd/', 'N', 'ýard', 'ярд', 'a unit of length equal to three feet', 'The garden is about twenty yards long.', 'Bagyň uzynlygy ýigrimi ýard töweregi.', 'B2'),
    ('a ton of bricks', '/ə ˌtʌn əv ˈbrɪks/', 'PHR', 'örän agyr zarba ýaly täsir', 'как тонна кирпичей', 'used to describe something that feels extremely heavy or upsetting', 'The news hit him like a ton of bricks.', 'Habar oňa örän agyr zarba ýaly täsir etdi.', 'C1'),
    ('give someone an inch', '/ˌɡɪv ˌsʌmwʌn ən ˈɪntʃ/', 'PHR', 'azajyk eglişik etmek', 'уступить кому-либо немного', 'to allow someone a small advantage, often leading them to demand more', 'If you give him an inch, he will take a mile.', 'Oňa azajyk eglişik etseň, ol has köpüsini islär.', 'C1'),
])

# 7A — Vocabulary Bank, printed pp.156–157; TG PDF p.198 corroborates legal terms.
ADDITIONS += group('7A', 156, [
    ('appeal', '/əˈpiːl/', 'N', 'şikaýat; höküme garşy ýüz tutma', 'апелляция', 'a formal request for a court to change a decision', 'The defendant plans to make an appeal.', 'Aýyplanýan höküme garşy şikaýat etmegi meýilleşdirýär.', 'B2'),
    ('death penalty', '/ˈdeθ ˌpenəlti/', 'N', 'ölüm jezasy', 'смертная казнь', 'the punishment of being killed for a serious crime', 'The country abolished the death penalty.', 'Ýurt ölüm jezasyny ýatyrdy.', 'B2'),
    ('electric chair', '/ɪˈlektrɪk ˌtʃeə/', 'N', 'elektrik oturgyjy', 'электрический стул', 'a chair used to execute a prisoner by electricity', 'The electric chair was once used for executions.', 'Bir wagtlar ölüm jezasy üçin elektrik oturgyjy ulanylýardy.', 'C1'),
    ('diminished responsibility', '/dɪˌmɪnɪʃt rɪˌspɒnsəˈbɪləti/', 'N', 'jogapkärçiligiň peselmegi', 'ограниченная вменяемость', 'a legal condition in which a person’s ability to understand an act was reduced', 'The court considered diminished responsibility.', 'Kazyýet jogapkärçiligiň peselendigini göz öňünde tutdy.', 'C2'),
    ('war crime', '/ˈwɔː kraɪm/', 'N', 'uruş jenaýaty', 'военное преступление', 'an extremely serious crime committed during a war', 'The tribunal investigated the alleged war crime.', 'Kazyýet uruş jenaýaty baradaky aýyplamany derňedi.', 'C1'),
    ('serial offender', '/ˌsɪəriəl əˈfendə/', 'N', 'gaýtalap jenaýat edýän adam', 'рецидивист', 'a person who repeatedly commits crimes', 'The serial offender received a longer sentence.', 'Gaýtalap jenaýat eden adama has uzak möhlet berildi.', 'C1'),
    ('defendant', '/dɪˈfendənt/', 'N', 'aýyplanýan; jogap beriji', 'обвиняемый; ответчик', 'a person accused of a crime in court', 'The defendant denied the charge.', 'Aýyplanýan aýyplamany inkär etdi.', 'B2'),
    ('hanging', '/ˈhæŋɪŋ/', 'N', 'asma jezasy', 'повешение', 'a method of execution in which a person is killed by hanging', 'Hanging was abolished in many countries.', 'Köp ýurtlarda asma jezasy ýatyryldy.', 'C1'),
    ('death row', '/ˈdeθ rəʊ/', 'N', 'ölüm jezasyna garaşýanlaryň kamerasy', 'камера смертников', 'the part of a prison for people sentenced to death', 'He spent years on death row.', 'Ol ölüm jezasyna garaşýanlaryň kamerasynda ençeme ýyl geçirdi.', 'C1'),
    ('inmate', '/ˈɪnmeɪt/', 'N', 'tussag; türme sakçysy', 'заключённый', 'a person kept in a prison or other institution', 'The inmates attended an education programme.', 'Tussaglar okuw maksatnamasyna gatnaşdylar.', 'C1'),
    ('lethal injection', '/ˌliːθl ɪnˈdʒekʃn/', 'N', 'öldüriji sanjym', 'смертельная инъекция', 'a method of execution using drugs injected into the body', 'The sentence was carried out by lethal injection.', 'Jeza öldüriji sanjym arkaly ýerine ýetirildi.', 'C1'),
    ('maximum security', '/ˌmæksɪməm sɪˈkjʊərəti/', 'N', 'iň ýokary howpsuzlyk düzgüni', 'максимальный уровень безопасности', 'the strictest level of security in a prison', 'He was transferred to a maximum-security prison.', 'Ol iň ýokary howpsuzlykly türmä geçirildi.', 'C1'),
    ('mitigating circumstances', '/ˌmɪtɪɡeɪtɪŋ ˈsɜːkəmstænsɪz/', 'N', 'jezany ýeňilleşdirýän ýagdaýlar', 'смягчающие обстоятельства', 'facts that make a crime seem less serious and may reduce a sentence', 'The judge took the mitigating circumstances into account.', 'Kazy jezany ýeňilleşdirýän ýagdaýlary hasaba aldy.', 'C2'),
    ('non-custodial sentence', '/ˌnɒn kəˈstəʊdiəl ˈsentəns/', 'N', 'türme tussaglygy bolmadyk jeza', 'наказание без лишения свободы', 'a punishment that does not involve sending someone to prison', 'She received a non-custodial sentence.', 'Oňa türme tussaglygy bolmadyk jeza berildi.', 'C1'),
    ('open prison', '/ˌəʊpən ˈprɪzn/', 'N', 'açyk görnüşli türme', 'тюрьма открытого типа', 'a prison with less strict security for selected prisoners', 'He was moved to an open prison near the city.', 'Ol şäheriň golaýyndaky açyk görnüşli türmä geçirildi.', 'C1'),
    ('quash', '/kwɒʃ/', 'V', 'karary ýatyrmak', 'отменять; аннулировать', 'to officially state that a legal decision is no longer valid', 'The appeal court quashed the conviction.', 'Şikaýat kazyýeti günä hökümini ýatyrdy.', 'C1'),
    ('rehabilitation', '/ˌriːhəˌbɪlɪˈteɪʃn/', 'N', 'täzeden jemgyýete uýgunlaşdyrma', 'реабилитация', 'the process of helping someone return to a healthy or useful life', 'Education can support the rehabilitation of offenders.', 'Bilim jenaýatçylaryň jemgyýete gaýdyp gelmegine kömek edip biler.', 'C1'),
    ('reoffend', '/ˌriːəˈfend/', 'V', 'gaýtadan jenaýat etmek', 'совершить преступление повторно', 'to commit another crime after being punished', 'Support can reduce the chance that a person will reoffend.', 'Goldaw adamyň gaýtadan jenaýat etmek ähtimallygyny azaldyp biler.', 'C1'),
    ('retrial', '/ˈriːtraɪəl/', 'N', 'gaýtadan kazyýet işi', 'повторное судебное разбирательство', 'a new trial after an earlier one was judged unfair or incorrect', 'The court ordered a retrial.', 'Kazyýet işi gaýtadan geçirmegi buýurdy.', 'C1'),
    ('solitary confinement', '/ˌsɒlətri kənˈfaɪnmənt/', 'N', 'ýekelikde tussag etmek', 'одиночное заключение', 'the punishment of keeping a prisoner alone', 'Solitary confinement can have serious effects.', 'Ýekelikde tussag etmek agyr täsir ýetirip biler.', 'C1'),
    ('electronic tag', '/ɪˌlekˈtrɒnɪk ˈtæɡ/', 'N', 'elektron gözegçilik enjamy', 'электронный браслет', 'a device worn to monitor a person’s location', 'He was released with an electronic tag.', 'Ol elektron gözegçilik enjamy bilen boşadyldy.', 'C1'),
    ('exercise yard', '/ˈeksəsaɪz jɑːd/', 'N', 'türme gezelenç meýdançasy', 'тюремный прогулочный двор', 'an outdoor area where prisoners can exercise', 'Prisoners use the exercise yard each morning.', 'Tussaglar her gün irden gezelenç meýdançasyna çykýarlar.', 'C1'),
    ('prison officer', '/ˈprɪzn ˌɒfɪsə/', 'N', 'türme işgäri', 'сотрудник тюрьмы', 'a person whose job is to supervise prisoners', 'A prison officer escorted him to the room.', 'Türme işgäri ony otaga alyp gitdi.', 'B2'),
])

# 7B — in-lesson connotation pairs, printed p.70.
ADDITIONS += group('7B', 70, [
    ('alone', '/əˈləʊn/', 'ADJ', 'ýeke; ýanynda hiç kim ýok', 'один; в одиночестве', 'without other people', 'She was alone in the house.', 'Ol öýde ýeke galypdy.', 'A2'),
    ('lonely', '/ˈləʊnli/', 'ADJ', 'özüňi ýalňyz duýýan', 'одинокий', 'unhappy because you are without company', 'He felt lonely in the new city.', 'Täze şäherde ol özüni ýalňyz duýdy.', 'B1'),
    ('solitary', '/ˈsɒlətri/', 'ADJ', 'ýeke ýaşaýan ýa-da edilýän', 'одинокий; уединённый', 'done or experienced alone', 'They took a solitary walk along the coast.', 'Olar kenar boýunda ýeke gezdiler.', 'C1'),
    ('interested', '/ˈɪntrəstɪd/', 'ADJ', 'gyzyklanýan', 'заинтересованный', 'wanting to know more about something', 'She is interested in local history.', 'Ol ýerli taryh bilen gyzyklanýar.', 'A2'),
    ('second-hand', '/ˌsekənd ˈhænd/', 'ADJ', 'ulanylan; ikinji el', 'подержанный', 'owned by someone else before you', 'He bought a second-hand bicycle.', 'Ol ulanylan welosiped satyn aldy.', 'B1'),
    ('vintage', '/ˈvɪntɪdʒ/', 'ADJ', 'köne, ýöne gymmatly we döwrebap', 'винтажный', 'old but high-quality or fashionable', 'She wore a vintage jacket.', 'Ol köne döwrebap penjek geýdi.', 'C1'),
    ('youthful', '/ˈjuːθfl/', 'ADJ', 'ýaşlara mahsus; ýaş görünýän', 'молодой; юный', 'looking or seeming young', 'He has a youthful appearance.', 'Ol ýaş görünýär.', 'B2'),
    ('original', '/əˈrɪdʒənl/', 'ADJ', 'özboluşly; täze pikirli', 'оригинальный', 'new and different from what is usual', 'Her original idea impressed the judges.', 'Onuň özboluşly pikiri eminleri haýran galdyrdy.', 'B2'),
    ('weird', '/wɪəd/', 'ADJ', 'geň; adaty däl', 'странный', 'very strange and unusual', 'We heard a weird noise outside.', 'Daşardan geň ses eşitdik.', 'B1'),
    ('affordable', '/əˈfɔːdəbl/', 'ADJ', 'satyn almaga güýjüň ýetýän', 'доступный по цене', 'not too expensive for most people', 'The shop sells affordable furniture.', 'Dükanda bahasy elýeterli mebel satylýar.', 'B2'),
    ('smarmy', '/ˈsmɑːmi/', 'ADJ', 'ýapyşganak ýakymly görünjek bolýan', 'слащавый', 'too polite or friendly in a way that seems insincere', 'His smarmy manner made people suspicious.', 'Onuň ýasamalyk bilen mylaýym bolmagy adamlary şübhelendirdi.', 'C2'),
    ('assertive', '/əˈsɜːtɪv/', 'ADJ', 'öz pikirini ynamly aýdýan', 'уверенный в себе; напористый', 'confidently expressing your opinions without being aggressive', 'Try to be assertive but polite.', 'Öz pikiriňi ynamly, ýöne mylaýym aýtmaga çalyş.', 'C1'),
])

# 8A — eating vocabulary printed p.158 and idioms on p.159, cross-referenced from lesson 8A.
ADDITIONS += group('8A', 158, [
    ('chew', '/tʃuː/', 'V', 'çeýnemek', 'жевать', 'to crush food with your teeth before swallowing', 'Chew your food slowly.', 'Iýmiti haýal çeýne.', 'A2'),
    ('guzzle', '/ˈɡʌzl/', 'V', 'suwaý ýaly çalt içmek', 'жадно пить', 'to drink something quickly and noisily', 'He guzzled a bottle of water after the run.', 'Ylgandan soň ol bir çüýşe suwy suwaý ýaly içdi.', 'C1'),
    ('lick', '/lɪk/', 'V', 'ýalamak', 'лизать', 'to move your tongue over something', 'The child licked the spoon clean.', 'Çaga çemçäni ýalap arassalady.', 'A2'),
    ('scoff', '/skɒf/', 'V', 'işdämenlik bilen çalt iýmek', 'жадно уплетать', 'to eat something quickly and eagerly', 'They scoffed the sandwiches before the train arrived.', 'Olar otly gelmänkä sendwiçleri işdämenlik bilen iýdiler.', 'C1'),
    ('slurp', '/slɜːp/', 'V', 'ses edip içmek ýa-da iýmek', 'хлебать; чавкать', 'to eat or drink noisily', 'He slurped his soup.', 'Ol çorbasyny ses edip içdi.', 'C1'),
    ('suck', '/sʌk/', 'V', 'sormak', 'сосать', 'to draw liquid or flavour into your mouth', 'She sucked a mint sweet.', 'Ol narpyzly süýjini sorup iýdi.', 'B1'),
    ('dig in', '/ˌdɪɡ ˈɪn/', 'PHR', 'nahara işdämenlik bilen başlamak', 'приступать к еде', 'to start eating eagerly', 'The food is ready, so dig in.', 'Nahar taýýar, başlaň.', 'B2'),
    ('eat up', '/ˌiːt ˈʌp/', 'PHR', 'hemmesini iýip gutarmak', 'доедать', 'to eat all of something', 'Eat up your vegetables before dessert.', 'Şirinligiň öňünden gök önümleriňi iýip gutar.', 'B1'),
    ('pick at', '/ˌpɪk ˈæt/', 'PHR', 'nahary işdäsiz çüňkemek', 'ковырять еду', 'to eat only small amounts without interest', 'She only picked at her lunch.', 'Ol günortanlyk naharyny işdäsiz çüňkedi.', 'B2'),
    ('polish off', '/ˌpɒlɪʃ ˈɒf/', 'PHR', 'iýip ýa-da içip gutarmak', 'быстро прикончить', 'to finish all of a meal or drink', 'We polished off the last piece of cake.', 'Biz tortuň soňky bölegini iýip gutardyk.', 'C1'),
    ('put away', '/ˌpʊt əˈweɪ/', 'PHR', 'köp iýip-içmek', 'уплетать; поглощать', 'to eat or drink a large amount', 'He can put away three plates of pasta.', 'Ol üç tabak makaron iýip bilýär.', 'C1'),
    ('toy with', '/ˌtɔɪ ˈwɪð/', 'PHR', 'nahary oýnap çüňkemek', 'ковырять еду', 'to move food around without seriously eating it', 'The nervous student toyed with her salad.', 'Tolgunýan okuwçy salatyny çüňkedi.', 'C1'),
])
ADDITIONS += group('8A', 159, [
    ('sour grapes', '/ˌsaʊə ˈɡreɪps/', 'PHR', 'ýetip bilmedik zadyňy peseltmek', 'кислый виноград', 'pretending you do not want something because you cannot have it', 'Calling the prize useless sounded like sour grapes.', 'Baýragy peýdasyz diýmek ýetip bilmedik zadyňy peseltmek ýalydy.', 'C1'),
    ('piece of cake', '/ˌpiːs əv ˈkeɪk/', 'PHR', 'örän aňsat zat', 'проще простого', 'something that is very easy to do', 'The test was a piece of cake.', 'Synag örän aňsat boldy.', 'B1'),
    ('a lot on your plate', '/ə ˌlɒt ɒn jɔː ˈpleɪt/', 'PHR', 'köp iş-aladaň bolmak', 'много дел на руках', 'to have many things to do or worry about', 'She has a lot on her plate this week.', 'Bu hepde onuň işi we aladasy köp.', 'C1'),
    ('spill the beans', '/ˌspɪl ðə ˈbiːnz/', 'PHR', 'syry açmak', 'выдать секрет', 'to reveal secret information', 'Who spilled the beans about the party?', 'Oturyşyk baradaky syry kim açdy?', 'B2'),
    ('not my cup of tea', '/nɒt maɪ ˌkʌp əv ˈtiː/', 'PHR', 'meniň göwnüme ýaramaýar', 'не в моём вкусе', 'not something that you like or enjoy', 'Horror films are not my cup of tea.', 'Gorkunç filmler meniň göwnüme ýaramaýar.', 'B2'),
    ('the icing on the cake', '/ði ˌaɪsɪŋ ɒn ðə ˈkeɪk/', 'PHR', 'üstesine gelen ýakymly zat', 'вишенка на торте', 'an extra good thing that makes a good situation even better', 'The sunny weather was the icing on the cake.', 'Güneşli howa eýýäm gowy bolan güni has-da gözel etdi.', 'C1'),
    ('pie in the sky', '/ˌpaɪ ɪn ðə ˈskaɪ/', 'PHR', 'amala aşmagy kyn arzuw', 'несбыточная мечта', 'a plan or hope that is unlikely to happen', 'Without funding, the project is pie in the sky.', 'Maliýeleşdirme bolmasa, taslama amala aşmajak arzuw bolup galar.', 'C1'),
    ('have your cake and eat it', '/hæv jɔː ˌkeɪk ən ˈiːt ɪt/', 'PHR', 'iki taraplaýyn artykmaçlyk islemek', 'и рыбку съесть, и в воду не лезть', 'to want two advantages that cannot normally be enjoyed together', 'You cannot have your cake and eat it.', 'Iki tarapyň hem peýdasyny bir wagtda alyp bolmaz.', 'C1'),
    ('take something with a pinch of salt', '/teɪk ˌsʌmθɪŋ wɪð ə ˌpɪntʃ əv ˈsɔːlt/', 'PHR', 'habara doly ynanmazlyk', 'относиться к чему-либо с недоверием', 'to doubt that information is completely true', 'Take online rumours with a pinch of salt.', 'Internetdäki myş-myşlara doly ynanma.', 'C1'),
    ('put it in a nutshell', '/ˌpʊt ɪt ɪn ə ˈnʌtʃel/', 'PHR', 'gysgaça aýdanyňda', 'короче говоря', 'to express the main facts in a very short way', 'To put it in a nutshell, we need more time.', 'Gysgaça aýdanyňda, bize has köp wagt gerek.', 'C1'),
])

# 8B — in-lesson Seeing vocabulary, printed p.80.
ADDITIONS += group('8B', 80, [
    ('spot', '/spɒt/', 'V', 'görüp saýgarmak; tapmak', 'заметить; разглядеть', 'to see or notice someone or something, especially from a distance', 'I spotted a familiar face in the crowd.', 'Mähelläniň içinde tanyş ýüzi saýgardym.', 'B1'),
    ('blank look', '/ˌblæŋk ˈlʊk/', 'N', 'düşünmeýän ýa-da hiç zat aňlatmaýan nazar', 'пустой взгляд', 'an expression showing that someone does not understand', 'He gave me a blank look when I asked.', 'Sorag beremde ol maňa düşünmeýän nazar bilen seretdi.', 'B2'),
], section='vocabulary', tg_pdf_page=None)

# Remaining explicit targets from the suffix, emotion, nationality, and maths lists.
ADDITIONS += group('2A', 143, [
    ('adversity', '/ədˈvɜːsəti/', 'N', 'kynçylyk; şowsuzlyk', 'трудности; невзгоды', 'a difficult or unpleasant situation that must be dealt with', 'She overcame great adversity.', 'Ol uly kynçylyklary ýeňip geçdi.', 'C1'),
    ('boredom', '/ˈbɔːdəm/', 'N', 'içgysgynçlyk', 'скука', 'the feeling of being uninterested because nothing is happening', 'The long wait filled us with boredom.', 'Uzak garaşmak bizi içgysgynçlyga saldy.', 'B1'),
    ('competence', '/ˈkɒmpɪtəns/', 'N', 'başarnyk; ukyp', 'компетентность', 'the ability to do something well or effectively', 'The job requires technical competence.', 'Bu iş tehniki başarnygy talap edýär.', 'C1'),
    ('idealism', '/aɪˈdɪəlɪzəm/', 'N', 'idealistlik; belent maksatlara ynam', 'идеализм', 'the belief that perfect principles should guide life and society', 'Her idealism inspired the group.', 'Onuň idealistligi topary ruhlandyrdy.', 'C1'),
    ('invasion', '/ɪnˈveɪʒn/', 'N', 'basybalyjylyk; çozuş', 'вторжение', 'the act of entering a country by force', 'The invasion began at dawn.', 'Basybalyjylyk daň bilen başlandy.', 'B2'),
    ('marriage', '/ˈmærɪdʒ/', 'N', 'nika; maşgala durmuşy', 'брак', 'the legal relationship between two people who are married', 'Their marriage lasted for decades.', 'Olaryň nikasy onlarça ýyl dowam etdi.', 'B1'),
    ('purity', '/ˈpjʊərəti/', 'N', 'arassalyk; päklik', 'чистота', 'the state of being clean or not mixed with anything else', 'The purity of the water was tested.', 'Suwuň arassalygy barlandy.', 'C1'),
    ('stiffness', '/ˈstɪfnəs/', 'N', 'gatylyk; hereketiň kynlygy', 'жёсткость; скованность', 'the state of being difficult to bend or move', 'The cold caused stiffness in my fingers.', 'Sowuk barmaklarymyň hereketini kynlaşdyrdy.', 'C1'),
    ('unpleasantness', '/ʌnˈplezntnəs/', 'N', 'ýakymsyzlyk', 'неприятность', 'the quality of being uncomfortable or not enjoyable', 'There was some unpleasantness during the meeting.', 'Duşuşykda biraz ýakymsyzlyk boldy.', 'C1'),
    ('bloody', '/ˈblʌdi/', 'ADJ', 'ganly; gazaply', 'кровавый', 'covered in blood, or involving a lot of violence', 'The battle was long and bloody.', 'Söweş uzak we ganly boldy.', 'B2'),
    ('instrumental', '/ˌɪnstrəˈmentl/', 'ADJ', 'möhüm goşant goşýan', 'играющий важную роль', 'important in making something happen or succeed', 'Her advice was instrumental in our success.', 'Onuň maslahaty üstünligimizde möhüm rol oýnady.', 'C1'),
    ('cosmic', '/ˈkɒzmɪk/', 'ADJ', 'kosmosa degişli; ägirt uly', 'космический; огромный', 'relating to the universe or outer space', 'The observatory studies cosmic radiation.', 'Synlaýyş merkezi kosmiki şöhlelenmäni öwrenýär.', 'C1'),
])
# These five headwords were corroborated on the TG worksheet, rather than
# read directly in the SB bank text; page 143 is only their linked lesson section.
_TG_AFFIX_EXTENSIONS = {'microcosm', 'paranormal', 'extracurricular', 'circumspect', 'forewarned'}
for _item in ADDITIONS:
    if _item['lesson'] == '2A' and _item['en'] in _TG_AFFIX_EXTENSIONS:
        _item.update({
            'evidence': 'teacher_guide_photocopiable_vocabulary',
            'page_role': 'teacher_guide_extension',
            'source_note': 'TG affixes worksheet, physical PDF p.190; mapped to SB 2A section p.143',
        })
ADDITIONS += group('3B', 147, [
    ('in your heart of hearts', '/ɪn jɔː ˌhɑːt əv ˈhɑːts/', 'PHR', 'çuňňur içiňden; kalbyňda', 'в глубине души', 'when you know what you really think or feel', 'In your heart of hearts, you know the answer.', 'Kalbyňda jogaby bilýärsiň.', 'C1'),
])
ADDITIONS += group('5A', 150, [
    ('pleased', '/pliːzd/', 'ADJ', 'begenýän; hoşal', 'довольный', 'feeling happy about something that has happened', 'She was pleased with the result.', 'Ol netijä begendi.', 'B1'),
    ('cheerful', '/ˈtʃɪəfl/', 'ADJ', 'şadyýan', 'весёлый; жизнерадостный', 'happy and positive in mood', 'He is always cheerful in the morning.', 'Ol irden hemişe şadyýan bolýar.', 'B1'),
    ('glad', '/ɡlæd/', 'ADJ', 'begenýän; hoşal', 'радостный; довольный', 'happy that something has happened', 'I am glad you came.', 'Geleniňe begenýärin.', 'A2'),
    ('satisfied', '/ˈsætɪsfaɪd/', 'ADJ', 'kanagatlanan', 'удовлетворённый', 'pleased because something is as good as you wanted', 'The customers were satisfied with the service.', 'Müşderiler hyzmatdan kanagatlandylar.', 'B1'),
    ('low', '/ləʊ/', 'ADJ', 'göwni çökgün', 'подавленный', 'unhappy and lacking energy', 'She felt low after the long winter.', 'Uzak gyşdan soň onuň göwni çökgündi.', 'B1'),
    ('upset', '/ʌpˈset/', 'ADJ', 'gynanan; göwni galan', 'расстроенный', 'unhappy or worried because of something unpleasant', 'He was upset by the rude comment.', 'Gödek söz ony gynandyrdy.', 'B1'),
    ('discouraged', '/dɪsˈkʌrɪdʒd/', 'ADJ', 'ruhdan düşen; höwesi gaçan', 'обескураженный', 'having lost confidence or hope', 'Do not feel discouraged by one mistake.', 'Bir ýalňyşlyk sebäpli ruhdan düşme.', 'B2'),
    ('gloomy', '/ˈɡluːmi/', 'ADJ', 'gamgyn; tukat', 'мрачный; унылый', 'sad and without hope', 'The news made everyone gloomy.', 'Habar hemmeleri gamgyn etdi.', 'B2'),
    ('miserable', '/ˈmɪzrəbl/', 'ADJ', 'örän betbagt; gamgyn', 'несчастный; подавленный', 'extremely unhappy or uncomfortable', 'He felt miserable after the argument.', 'Jedelden soň ol özüni betbagt duýdy.', 'B2'),
    ('cross', '/krɒs/', 'ADJ', 'gaharly; öýkeli', 'сердитый', 'slightly angry or annoyed', 'Dad was cross about the broken window.', 'Kakasy döwlen penjire üçin gaharlydy.', 'B1'),
    ('displeased', '/dɪsˈpliːzd/', 'ADJ', 'nägile; göwni hoş däl', 'недовольный', 'annoyed because something is not acceptable', 'The manager was displeased with the delay.', 'Ýolbaşçy gijikmä nägiledi.', 'C1'),
    ('frustrated', '/frʌˈstreɪtɪd/', 'ADJ', 'gahary gelen; göwni geçen', 'раздосадованный', 'annoyed because you cannot do or achieve something', 'She felt frustrated by the slow progress.', 'Haýal öňegidişlikden ol lapykeç boldy.', 'B2'),
    ('irate', '/aɪˈreɪt/', 'ADJ', 'örän gaharly', 'разгневанный', 'extremely angry', 'An irate customer demanded a refund.', 'Örän gaharly müşderi puluny yzyna talap etdi.', 'C1'),
    ('disconcerted', '/ˌdɪskənˈsɜːtɪd/', 'ADJ', 'aljyran; ynjalygy bozulan', 'смущённый; сбитый с толку', 'worried or confused by something unexpected', 'He looked disconcerted by the question.', 'Ol soragdan aljyran ýaly boldy.', 'C1'),
    ('uneasy', '/ʌnˈiːzi/', 'ADJ', 'aladaçyl; ynjalyksyz', 'тревожный; беспокойный', 'worried because you feel something may be wrong', 'I felt uneasy walking home alone.', 'Öýüme ýeke gaýdyp barýarkam howatyrlandym.', 'B2'),
    ('wary', '/ˈweəri/', 'ADJ', 'seresap; şübheli', 'настороженный', 'careful because you do not completely trust someone or something', 'She was wary of making a quick decision.', 'Ol howlukmaç karar bermekden saklandy.', 'C1'),
    ('scared', '/skeəd/', 'ADJ', 'gorkan', 'испуганный', 'frightened or worried', 'The child was scared of the dark.', 'Çaga garaňkylykdan gorkýardy.', 'B1'),
    ('filled with dread', '/fɪld wɪð ˈdred/', 'PHR', 'güýçli gorky we howatyr bilen doly', 'охваченный тревогой', 'feeling extremely worried about what may happen', 'She was filled with dread before the call.', 'Jaňdan öň ol güýçli howatyra düşdi.', 'C1'),
])
ADDITIONS += group('6B', 154, [
    ('brackets', '/ˈbrækɪts/', 'N', 'ýaýlar', 'скобки', 'symbols used to separate extra information in writing or maths', 'Put the answer in brackets.', 'Jogaby ýaýyň içine ýazyň.', 'B1'),
    ('ordinal number', '/ˌɔːdɪnl ˈnʌmbə/', 'N', 'tertipleýji san', 'порядковое числительное', 'a number that shows the position of something in a series', 'Fourth is an ordinal number.', 'Dördünji tertipleýji sandyr.', 'B2'),
    ('squared', '/skweəd/', 'ADJ', 'kwadrata göterilen', 'в квадрате', 'multiplied by itself', 'Four squared is sixteen.', 'Dört kwadrata göterilende on alty bolýar.', 'B1'),
    ('percentage', '/pəˈsentɪdʒ/', 'N', 'göterim; paý', 'процентное соотношение', 'a proportion expressed as a number out of one hundred', 'What percentage of the class passed?', 'Synpyň näçe göterimi synagdan geçdi?', 'B1'),
    ('table', '/ˈteɪbl/', 'N', 'tablisa', 'таблица', 'information arranged in rows and columns', 'The table shows the results by age.', 'Tablisa netijeleri ýaş boýunça görkezýär.', 'A2'),
    ('fish out of water', '/ˌfɪʃ aʊt əv ˈwɔːtə/', 'PHR', 'öz ýerinde däl ýaly duýýan adam', 'не в своей тарелке', 'a person who feels uncomfortable in an unfamiliar situation', 'I felt like a fish out of water at the formal dinner.', 'Resmi agşamlyk naharynda özümi ýat ýerde ýaly duýdum.', 'C1'),
])

# Nationality forms explicitly requested or modelled on the p.51 box and chart.
ADDITIONS += group('5B', 51, [
    ('Norwegian', '/nɔːˈwiːdʒən/', 'N', 'norwegiýaly', 'норвежец; норвежка', 'a person from Norway', 'A Norwegian family moved next door.', 'Goňşy jaýa norwegiýaly maşgala göçüp geldi.', 'B1'),
    ('Belgian', '/ˈbeldʒən/', 'N', 'belgiýaly', 'бельгиец; бельгийка', 'a person from Belgium', 'The Belgian spoke three languages.', 'Belgiýaly üç dilde gepleýärdi.', 'B1'),
    ('Pakistani', '/ˌpɑːkɪˈstɑːni/', 'N', 'päkistanly', 'пакистанец; пакистанка', 'a person from Pakistan', 'A Pakistani student joined the class.', 'Sapaga päkistanly talyp goşuldy.', 'B1'),
    ('Vietnamese', '/ˌvjetnəˈmiːz/', 'N', 'wýetnamly', 'вьетнамец; вьетнамка', 'a person from Vietnam, or relating to Vietnam', 'The Vietnamese community celebrates the festival.', 'Wýetnamly jemgyýet baýramçylygy belleýär.', 'B1'),
    ('Afghan', '/ˈæfɡæn/', 'N', 'owgan', 'афганец; афганка', 'a person from Afghanistan', 'An Afghan family settled in the area.', 'Sebitde owgan maşgalasy ýerleşdi.', 'B1'),
    ('Lebanese', '/ˌlebəˈniːz/', 'ADJ', 'liwanly; Liwana degişli', 'ливанский; ливанец', 'from Lebanon or relating to its people and culture', 'They serve Lebanese food here.', 'Bu ýerde liwan naharlary berilýär.', 'B1'),
    ('Peruvian', '/pəˈruːviən/', 'N', 'peruly', 'перуанец; перуанка', 'a person from Peru', 'The Peruvian described life in Lima.', 'Peruly Lima şäherindäki durmuş barada gürrüň berdi.', 'B1'),
    ('Welsh', '/welʃ/', 'ADJ', 'uelsli; Uels bilen bagly', 'валлийский; валлиец', 'from Wales or relating to its people and language', 'She is learning Welsh.', 'Ol uels dilini öwrenýär.', 'B1'),
    ('Iraqi', '/ɪˈrɑːki/', 'N', 'yrakly', 'иракец; иракка', 'a person from Iraq', 'An Iraqi artist spoke at the event.', 'Çärede yrakly suratkeş çykyş etdi.', 'B1'),
    ('Dutch', '/dʌtʃ/', 'ADJ', 'niderlandly; niderland diline degişli', 'нидерландский; голландец', 'from the Netherlands or relating to its people and language', 'Dutch is spoken in the Netherlands.', 'Niderland dilinde Niderlandlarda gepleşilýär.', 'B1'),
    ('Danish', '/ˈdeɪnɪʃ/', 'ADJ', 'daniýaly; Daniýa degişli', 'датский', 'from Denmark or relating to its people and language', 'We tried a Danish pastry.', 'Biz daniýa süýjüligini dadyp gördük.', 'B1'),
    ('Finnish', '/ˈfɪnɪʃ/', 'ADJ', 'finlýandiýaly; fin diline degişli', 'финский', 'from Finland or relating to its people and language', 'She is taking a Finnish language course.', 'Ol fin dili kursuna gatnaşýar.', 'B1'),
    ('Polish', '/ˈpəʊlɪʃ/', 'ADJ', 'polýak; Polşa degişli', 'польский', 'from Poland or relating to its people and language', 'He reads Polish newspapers.', 'Ol polýak gazetlerini okaýar.', 'B1'),
    ('Scottish', '/ˈskɒtɪʃ/', 'ADJ', 'şotlandiýaly; Şotlandiýa degişli', 'шотландский', 'from Scotland or relating to its people and culture', 'They visited a Scottish castle.', 'Olar şotlandiýa galasyna baryp gördüler.', 'B1'),
    ('Swedish', '/ˈswiːdɪʃ/', 'ADJ', 'şwesiýaly; Şwesiýa degişli', 'шведский', 'from Sweden or relating to its people and language', 'The company has a Swedish office.', 'Kompaniýanyň Şwesiýada edarasy bar.', 'B1'),
    ('Turkish', '/ˈtɜːkɪʃ/', 'ADJ', 'türk; Türkiýä degişli', 'турецкий', 'from Turkey or relating to its people and language', 'We ate Turkish food for dinner.', 'Agşamlyk naharynda türk naharyny iýdik.', 'B1'),
    ('British', '/ˈbrɪtɪʃ/', 'ADJ', 'britaniýaly; Britaniýa degişli', 'британский', 'from Britain or relating to its people and culture', 'She studies British history.', 'Ol Britaniýanyň taryhyny öwrenýär.', 'B1'),
    ('Brit', '/brɪt/', 'N', 'britaniýaly (resmi däl)', 'британец; британка', 'an informal word for a British person', 'A Brit told us about the local custom.', 'Britaniýaly biri bize ýerli däp barada gürrüň berdi.', 'B2'),
    ('Englishman', '/ˈɪŋɡlɪʃmən/', 'N', 'iňlis (erkek)', 'англичанин', 'a man from England', 'The Englishman spoke with a London accent.', 'Iňlis londonly äheňinde gepleýärdi.', 'B1'),
    ('Frenchwoman', '/ˈfrentʃwʊmən/', 'N', 'fransuz zenany', 'француженка', 'a woman from France', 'A Frenchwoman led the walking tour.', 'Gezelenje fransuz zenany ýolbaşçylyk etdi.', 'B1'),
    ('Dutchman', '/ˈdʌtʃmən/', 'N', 'niderlandly erkek', 'голландец', 'a man from the Netherlands', 'The Dutchman works in Amsterdam.', 'Niderlandly Amsterdamda işleýär.', 'B1'),
    ('Norwegians', '/nɔːˈwiːdʒənz/', 'N', 'norwegiýalylar', 'норвежцы', 'the people of Norway', 'The Norwegians are proud of their coastline.', 'Norwegiýalylar kenarýakasy bilen buýsanýarlar.', 'B1'),
    ('Peruvians', '/pəˈruːviənz/', 'N', 'perulylar', 'перуанцы', 'the people of Peru', 'Peruvians celebrate many regional festivals.', 'Perulylar köp sebit baýramlaryny belleýärler.', 'B1'),
    ('Iraqis', '/ɪˈrɑːkiz/', 'N', 'yraklylar', 'иракцы', 'the people of Iraq', 'Iraqis have a rich cultural history.', 'Yraklylaryň baý medeni taryhy bar.', 'B1'),
    ('the Spanish', '/ðə ˈspænɪʃ/', 'N', 'ispanlar', 'испанцы', 'the people of Spain considered as a group', 'The Spanish have several regional languages.', 'Ispanlaryň birnäçe sebit dili bar.', 'B1'),
], section='vocabulary', tg_pdf_page=None)
ADDITIONS += group('5B', 51, [
    ('the Danes', '/ðə ˈdeɪnz/', 'N', 'daniýalylar', 'датчане', 'the people of Denmark considered as a group', 'The Danes have a strong cycling culture.', 'Daniýalylar welosiped sürmek medeniýeti bilen tanalýarlar.', 'B1'),
    ('the Finns', '/ðə ˈfɪnz/', 'N', 'finlýandiýalylar', 'финны', 'the people of Finland considered as a group', 'The Finns value their forests and lakes.', 'Finlýandiýalylar tokaýlaryna we köllerine sarpa goýýarlar.', 'B1'),
    ('the Poles', '/ðə ˈpəʊlz/', 'N', 'polýaklar', 'поляки', 'the people of Poland considered as a group', 'The Poles have a rich musical tradition.', 'Polýaklaryň baý saz däbi bar.', 'B1'),
    ('the Scots', '/ðə ˈskɒts/', 'N', 'şotlandiýalylar', 'шотландцы', 'the people of Scotland considered as a group', 'The Scots celebrate several local festivals.', 'Şotlandiýalylar birnäçe ýerli baýramçylygy belleýärler.', 'B1'),
    ('the Swedes', '/ðə ˈswiːdz/', 'N', 'şwesiýalylar', 'шведы', 'the people of Sweden considered as a group', 'The Swedes elected a new government.', 'Şwesiýalylar täze hökümeti saýladylar.', 'B1'),
    ('the Turks', '/ðə ˈtɜːks/', 'N', 'türkler', 'турки', 'the people of Turkey considered as a group', 'The Turks welcomed us warmly.', 'Türkler bizi mähirli garşyladylar.', 'B1'),
    ('the Brits', '/ðə ˈbrɪts/', 'N', 'britaniýalylar (resmi däl)', 'британцы', 'an informal word for British people as a group', 'The Brits queued patiently for the concert.', 'Britaniýalylar konserte sabyrly nobata durdular.', 'B2'),
    ('the British', '/ðə ˈbrɪtɪʃ/', 'N', 'britaniýalylar', 'британцы', 'the people of Britain considered as a group', 'The British voted in the election.', 'Britaniýalylar saýlawda ses berdiler.', 'B1'),
    ('Afghans', '/ˈæfɡænz/', 'N', 'owganlar', 'афганцы', 'the people of Afghanistan considered as a group', 'Afghans have a long poetic tradition.', 'Owganlaryň uzak şygryýet däbi bar.', 'B1'),
], section='vocabulary', tg_pdf_page=None)

# Additional explicit list items and repeated cross-lesson source occurrences.
ADDITIONS += group('4B', 149, [
    ('a.m.', '/ˌeɪ ˈem/', 'ADV', 'günüň birinji ýarymynda', 'до полудня', 'an abbreviation meaning before noon', 'The train leaves at 9 a.m.', 'Otly irden sagat dokuzda ugraýar.', 'B1'),
    ('p.m.', '/ˌpiː ˈem/', 'ADV', 'günüň ikinji ýarymynda', 'после полудня', 'an abbreviation meaning after noon', 'The meeting starts at 2 p.m.', 'Duşuşyk günortandan soň sagat ikide başlanýar.', 'B1'),
    ('e.g.', '/ˌiː ˈdʒiː/', 'PHR', 'mysal üçin', 'например', 'an abbreviation used before one or more examples', 'Some fruits, e.g. pears, grow well here.', 'Käbir miweler, mysal üçin armyt, bu ýerde gowy ösýär.', 'B2'),
    ('etc.', '/et ˈsetərə/', 'PHR', 'we ş.m.; we başgalar', 'и так далее', 'an abbreviation meaning and other similar things', 'Bring a pen, notebook, etc.', 'Galam, depder we ş.m. getir.', 'B1'),
    ('i.e.', '/ˌaɪ ˈiː/', 'PHR', 'ýagny', 'то есть', 'an abbreviation used to explain something more clearly', 'The office is closed on weekdays, i.e. Monday to Friday.', 'Edara iş günlerinde, ýagny duşenbe-juma aralygynda ýapyk.', 'B2'),
    ('N.B.', '/ˌen ˈbiː/', 'PHR', 'üns beriň; bellik ediň', 'обратите внимание', 'an abbreviation used to draw attention to an important point', 'N.B. The final date has changed.', 'Üns beriň, soňky sene üýtgedi.', 'C1'),
    ('QED', '/ˌkjuː iː ˈdiː/', 'PHR', 'subut edildi', 'что и требовалось доказать', 'an abbreviation written at the end of a proof', 'The proof ends with QED.', 'Subutnama QED bilen tamamlanýar.', 'C2'),
    ('RIP', '/ˌɑː aɪ ˈpiː/', 'PHR', 'jaýy jennet bolsun', 'покойся с миром', 'an abbreviation written to express respect for someone who has died', 'The message ended with RIP.', 'Habaryň soňunda jaýy jennet bolsun diýilýärdi.', 'B2'),
])
ADDITIONS += group('6A', 153, [
    ('strongly', '/ˈstrɒŋli/', 'ADV', 'güýçli ýagdaýda; berk', 'настоятельно; сильно', 'to a great degree or with strong feeling', 'We strongly recommend booking early.', 'Ir bron etmegi berk maslahat berýäris.', 'B2', 'strongly recommend'),
    ('kindly', '/ˈkaɪndli/', 'ADV', 'mylaýymlyk bilen', 'любезно', 'in a kind or polite way', 'They kindly agreed to water the plants.', 'Olar ösümliklere suw bermäge mylaýymlyk bilen razy boldular.', 'B2', 'kindly agree'),
], tg_pdf_page=196)
ADDITIONS += group('6B', 155, [
    ('foot', '/fʊt/', 'N', 'fut', 'фут', 'a unit of length equal to twelve inches', 'The room is ten feet long.', 'Otagyň uzynlygy on fut.', 'B1'),
    ('mile', '/maɪl/', 'N', 'mil', 'миля', 'a unit of distance equal to about 1.6 kilometres', 'The village is two miles away.', 'Oba iki mil uzaklykda.', 'B1'),
    ('ounce', '/aʊns/', 'N', 'uns', 'унция', 'a unit of weight equal to about 28 grams', 'Add one ounce of sugar.', 'Bir uns şeker goşuň.', 'B2'),
    ('ton', '/tʌn/', 'N', 'tonna; örän köp mukdar', 'тонна', 'a unit of weight, or an informal large amount', 'The old truck weighs nearly a ton.', 'Köne ýük maşyny bir tonna golaý çekýär.', 'B1'),
    ('go the extra mile', '/ˌɡəʊ ði ˌekstrə ˈmaɪl/', 'PHR', 'goşmaça tagalla etmek', 'приложить дополнительные усилия', 'to make more effort than is expected', 'The staff went the extra mile for their guests.', 'Işgärler myhmanlar üçin goşmaça tagalla etdiler.', 'C1'),
    ('narrow escape', '/ˌnærəʊ ɪˈskeɪp/', 'N', 'zordan halas bolma', 'чудесное спасение', 'a situation in which you nearly have an accident or get hurt', 'It was a narrow escape from the falling tree.', 'Ýykylan agaçdan zordan halas bolduk.', 'B2'),
    ('weigh a ton', '/ˌweɪ ə ˈtʌn/', 'PHR', 'örän agyr bolmak', 'весить целую тонну', 'to feel extremely heavy', 'This suitcase weighs a ton.', 'Bu çemodan örän agyr.', 'B2'),
    ('come down on someone like a ton of bricks', '/kʌm ˌdaʊn ɒn ˌsʌmwʌn laɪk ə ˌtʌn əv ˈbrɪks/', 'PHR', 'birine gaty berk çäre görmek', 'обрушиться на кого-либо с суровой критикой', 'to criticize or punish someone very severely', 'The tutor came down on him like a ton of bricks.', 'Mugallym oňa örän berk käýindi.', 'C2'),
])
ADDITIONS += group('5A', 151, [
    ("break someone's heart", '/ˌbreɪk ˌsʌmwʌnz ˈhɑːt/', 'PHR', 'biriniň ýüregini agyrtmak', 'разбить кому-либо сердце', 'to make someone extremely sad', 'It broke her heart to leave the children.', 'Çagalary terk etmek onuň ýüregini agyrtdy.', 'B2'),
    ('scare the living daylights out of someone', '/ˌskeə ðə ˌlɪvɪŋ ˈdeɪlaɪts aʊt əv ˌsʌmwʌn/', 'PHR', 'birini gaty gorkuzmak', 'напугать до смерти', 'to frighten someone very badly', 'The sudden noise scared the living daylights out of me.', 'Duýdansyz ses meni gaty gorkuzdy.', 'C1'),
])
ADDITIONS += group('7B', 70, [
    ('cheap', '/tʃiːp/', 'ADJ', 'arzan; pes hilli', 'дешёвый; низкого качества', 'costing little, sometimes suggesting poor quality', 'The cheap watch stopped working.', 'Arzan sagat işlemegini bes etdi.', 'B1'),
    ('charming', '/ˈtʃɑːmɪŋ/', 'ADJ', 'ýakymly; özüne çekiji', 'обаятельный', 'pleasant and attractive in a way that makes people like you', 'The charming host welcomed everyone.', 'Ýakymly öý eýesi hemmeleri garşylady.', 'B2'),
    ('aggressive', '/əˈɡresɪv/', 'ADJ', 'gazaply; başgalara basyş edýän', 'агрессивный', 'behaving in a forceful or angry way', 'His aggressive tone stopped the discussion.', 'Onuň gazaply äheňi ara alyp maslahatlaşmany bes etdirdi.', 'B2'),
    ('childish', '/ˈtʃaɪldɪʃ/', 'ADJ', 'çaga ýaly; ýetişmedik', 'ребяческий', 'silly or immature in a way typical of a child', 'It was childish to refuse to talk.', 'Gürleşmekden ýüz öwürmek ýetişmedik hereketdi.', 'B2'),
], section='vocabulary', tg_pdf_page=None)
ADDITIONS += group('8A', 159, [
    ('know which side your bread is buttered', '/ˌnəʊ wɪtʃ ˌsaɪd jɔː bred ɪz ˈbʌtəd/', 'PHR', 'öz bähbidiň nireden gelýändigini bilmek', 'знать, откуда приходит выгода', 'to know who gives you an advantage and avoid upsetting them', 'You should know which side your bread is buttered.', 'Öz bähbidiň nireden gelýändigini bilmeli.', 'C1'),
])

# Additional punishment targets from the p.156 trial and sentencing text.
ADDITIONS += group('7A', 156, [
    ('deterrent', '/dɪˈterənt/', 'N', 'saklaýjy täsir; päsgel', 'сдерживающий фактор', 'something that makes people less likely to do something wrong', 'A fine can act as a deterrent.', 'Jerime saklaýjy täsir edip biler.', 'C1'),
    ('offence', '/əˈfens/', 'N', 'jenaýat; düzgün bozma', 'правонарушение', 'an illegal act or a breach of a rule', 'The court considered the seriousness of the offence.', 'Kazyýet jenaýatyň agyrlygyny göz öňünde tutdy.', 'B2'),
    ('criminal record', '/ˌkrɪmɪnl ˈrekɔːd/', 'N', 'jenaýat ýazgysy', 'судимость; криминальное прошлое', 'an official record of a person’s previous crimes', 'A previous criminal record may affect the sentence.', 'Öňki jenaýat ýazgysy jeza täsir edip biler.', 'B2'),
    ('offender', '/əˈfendə/', 'N', 'jenaýatçy; düzgün bozujy', 'правонарушитель', 'a person who commits a crime or breaks a rule', 'The programme helps young offenders.', 'Maksatnama ýaş jenaýatçylara kömek edýär.', 'B2'),
    ('repeat offender', '/rɪˌpiːt əˈfendə/', 'N', 'gaýtalap jenaýat edýän adam', 'рецидивист', 'a person who has committed crimes more than once', 'The judge gave the repeat offender a longer sentence.', 'Kazy gaýtalap jenaýat edene has uzak jeza berdi.', 'C1'),
    ('abolish', '/əˈbɒlɪʃ/', 'V', 'ýatyrmak; güýjüni bes etmek', 'отменить', 'to officially end a law, system, or practice', 'Several countries have abolished capital punishment.', 'Birnäçe ýurt ölüm jezasyny ýatyrdy.', 'B2'),
])
ADDITIONS += group('5A', 150, [
    ('amused', '/əˈmjuːzd/', 'ADJ', 'güldürilen; keýpi açylan', 'развеселённый', 'thinking something is funny or entertaining', 'She looked amused by his story.', 'Onuň hekaýasy oňa gülkünç görünýärdi.', 'B1'),
    ('offended', '/əˈfendɪd/', 'ADJ', 'göwni galan; kemsidilen', 'обиженный', 'upset because someone has been rude or unfair', 'He felt offended by the personal remark.', 'Şahsy bellik onuň göwnüne degdi.', 'B2'),
])

# Further explicitly listed terms from the p.157 prison and release sections.
ADDITIONS += group('7A', 157, [
    ('cell', '/sel/', 'N', 'türme kamerasy', 'камера; одиночная камера', 'a small room in a prison where a prisoner is kept', 'The inmate returned to his cell.', 'Tussag kamerasyna gaýdyp geldi.', 'B2'),
    ('be deprived of', '/biː dɪˈpraɪvd əv/', 'PHR', 'mahrum edilmek', 'быть лишённым', 'to have something important taken away from you', 'Prisoners should not be deprived of medical care.', 'Tussaglar lukmançylyk kömeginden mahrum edilmeli däl.', 'C1'),
    ('lock someone up', '/ˌlɒk ˌsʌmwʌn ˈʌp/', 'PHR', 'birini türmä basmak', 'заключить кого-либо под стражу', 'to put someone in prison or another locked place', 'They locked him up for the night.', 'Olar ony gije türmä basdylar.', 'B2'),
    ('surveillance', '/səˈveɪləns/', 'N', 'gözegçilik; gizlin yzarlama', 'наблюдение; слежка', 'the careful watching of a person or place', 'The building is under constant surveillance.', 'Bina hemişe gözegçilik astynda.', 'C1'),
    ('reintegrate', '/ˌriːˈɪntɪɡreɪt/', 'V', 'jemgyýete täzeden goşulmak', 'повторно интегрировать', 'to become part of a group or society again', 'The programme helps prisoners reintegrate into society.', 'Maksatnama tussaglaryň jemgyýete täzeden goşulmagyna kömek edýär.', 'C1'),
    ('pardon', '/ˈpɑːdn/', 'N', 'amnistiýa; bagyşlama', 'помилование', 'an official decision to forgive a crime or cancel a punishment', 'The president granted him a pardon.', 'Prezident ony günäsinden geçirdi.', 'B2'),
    ('compensation', '/ˌkɒmpenˈseɪʃn/', 'N', 'öwez tölegi', 'компенсация', 'money paid to someone for loss or harm', 'The court awarded compensation to the victim.', 'Kazyýet pidanyň öwezini dolmagy buýurdy.', 'B2'),
    ('wrongfully convicted', '/ˌrɒŋfəli kənˈvɪktɪd/', 'ADJ', 'nädogry günäli tapylan', 'неправомерно осуждённый', 'found guilty of a crime that you did not commit', 'The wrongfully convicted man was finally freed.', 'Nädogry günäli tapylan adam ahyry boşadyldy.', 'C1'),
])

# Repair page-level provenance where a bank spans facing pages.
_PAGE_142 = {
    'rip-off', 'climb-down', 'comeback', 'breakthrough', 'break-up', 'mix-up',
    'set-up', 'let-down', 'write-off', 'backup', 'giveaway', 'hold-up', 'turnout',
    'makeover', 'setback', 'breakdown', 'write-up', 'go-ahead', 'standby', 'meltdown',
}
_PAGE_145 = {'hike', 'limp', 'scramble', 'wade'}
_PAGE_147 = {
    'neither here nor there', "mum's the word", "the world's your oyster", 'come what may',
}
_PAGE_151 = {'aghast', 'rattled', 'unnerved', 'panic-stricken', 'disconcerted', 'uneasy', 'wary', 'scared', 'filled with dread'}
_PAGE_153 = {'flatly', 'freely', 'greatly', 'violently', 'categorically', 'warmly'}
_PAGE_155 = {'fish out of water'}
_PAGE_157 = {
    'inmate', 'maximum security', 'open prison', 'quash', 'rehabilitation', 'reoffend',
    'retrial', 'solitary confinement', 'electronic tag', 'exercise yard', 'prison officer',
}
for _item in ADDITIONS:
    if _item['lesson'] == '1B' and _item['en'] in _PAGE_142:
        _item['page'] = 142
    elif _item['lesson'] == '2B' and _item['en'] in _PAGE_145:
        _item['page'] = 145
    elif _item['lesson'] == '3B' and _item['en'] in _PAGE_147:
        _item['page'] = 147
    elif _item['lesson'] == '5A' and _item['en'] in _PAGE_151:
        _item['page'] = 151
    elif _item['lesson'] == '6A' and _item['en'] in _PAGE_153:
        _item['page'] = 153
    elif _item['lesson'] == '6B' and _item['en'] in _PAGE_155:
        _item['page'] = 155
    elif _item['lesson'] == '7A' and _item['en'] in _PAGE_157:
        _item['page'] = 157

# A repeated headword is allowed only when it is a different, explicitly sourced
# lesson occurrence; the pack will keep one card and attach both book references.
_seen_additions = {}
for _item in ADDITIONS:
    _key = _item['en'].casefold()
    _lessons = _seen_additions.setdefault(_key, set())
    if _item['lesson'] in _lessons:
        raise ValueError(f'duplicate addition in {_item["lesson"]}: {_item["en"]}')
    _lessons.add(_item['lesson'])
