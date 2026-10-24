#!/usr/bin/env python3
"""English File Advanced — vocabulary organised by the book's own structure.

Same generator pattern as gen_upp.py / gen_int.py. The supplied Student’s Book
was OCR’d page-by-page into content/pdf/adv-sb.txt (177 physical PDF-page markers);
the full Teacher’s Guide text is in content/pdf/adv-tg.txt (230 physical PDF-page
markers). Student’s Book printed pages begin one page earlier than their OCR
markers (e.g. physical p163 is printed p162); the `books.page` fields and candidate
`page` values use printed pages. Candidate `tg_pdf_page` values use physical PDF
markers. New bank entries were reviewed against those page-marked sources and
cross-referenced to the matching guide worksheets/lesson notes. Turkmen and Russian glosses,
definitions, and examples are draft work; proofread remains false, and IPA was
curated rather than copied from noisy OCR.

STRUCTURE (contents table and lesson/page mapping below). Advanced 4th edition
has 10 units, each with TWO lessons (A and B — no C), and five Colloquial English
episodes after units 1, 3, 5, 7 and 9:
  1A We are family · 1B A job for life? · CE1 talking about work and family
  2A Do you remember...? · 2B On the tip of my tongue
  3A A love-hate relationship · 3B Dramatic licence · CE2 talking about history
  4A An open book · 4B The sound of silence
  5A No time for anything · 5B Not for profit? · CE3 talking about stress
  6A Help, I need somebody! · 6B Can't give it up
  7A As a matter of fact... · 7B A masterpiece? · CE4 talking about illustration
  8A The best medicine? · 8B A 'must-see' attraction
  9A Pet hates · 9B How to cook, how to eat · CE5 talking about insects
  10A On your marks, set, go! · 10B No direction home

Vocabulary Bank (11 sections) -> lesson: Personality->1A, Work->1B,
Phrases with get->3A, Conflict and warfare->3B, Sounds and the human
voice->4B, Expressions with time->5A, Money->5B, Prefixes->7A,
Travel and tourism->8B, Animal matters->9A, Preparing food->9B.
The 6A compound adjectives, 6B technology/preposition boxes, the 8A guide
vocabulary notes, and 10A word-building candidates carry explicit page provenance.

Colloquial English episodes carry unit 11 in the data (units 1-10 are the
book's), and the app shows each episode right after the unit it follows.

Usage: python3 content/tools/gen_adv.py
"""
import json
import os
import re
import sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'advanced.json')

# topic -> [ (en, ipa, pos, tm, ru, def, ex, exTm, cefr[, coll]) ]
T = {}

# ---- Vocabulary Bank — Personality -> 1A ----
T['personality'] = [
    ('charming', '/ˈtʃɑːmɪŋ/', 'ADJ', 'özüne çekiji (sympatik)', 'очаровательный', 'very pleasant and likeable', 'The charming host welcomed everyone.', 'Özüne çekiji eýe hemmäni garşylady.', 'B1'),
    ('cheerful', '/ˈtʃɪəfl/', 'ADJ', 'şähdaçyk', 'жизнерадостный', 'happy and positive', 'She gave us a cheerful smile.', 'Şähdaçyk ýylgyryş berdi.', 'A2'),
    ('cruel', '/ˈkruːəl/', 'ADJ', 'rehimsiz', 'жестокий', 'causing pain without pity', 'It was cruel to laugh at him.', 'Oňa gülmek rehimsiz boldy.', 'B1'),
    ('gentle', '/ˈdʒentl/', 'ADJ', 'mulýum', 'нежный, мягкий', 'kind and careful', 'Be gentle with the kitten.', 'Pişik çagasyna mulýum bol.', 'A2'),
    ('mean', '/miːn/', 'ADJ', 'gysganç (erbet)', 'скупой, злой', 'unkind, or unwilling to share', 'It was mean of him to say that.', 'Onuň beýle aýtmagy erbet boldy.', 'A2'),
    ('moody', '/ˈmuːdi/', 'ADJ', 'keýpi üýtgeýän', 'с переменчивым настроением', 'often changing moods', 'Teenagers can be moody.', 'Ýetginjekleriň keýpi üýtgäp durýar.', 'B1'),
    ('optimistic', '/ˌɒptɪˈmɪstɪk/', 'ADJ', 'oňyn pikirlenýän', 'оптимистичный', 'expecting good things', 'She is optimistic about the future.', 'Geljege oňyn garaýar.', 'B1', 'optimistic about'),
    ('outgoing', '/ˈaʊtɡəʊɪŋ/', 'ADJ', 'açyk (jemgyýetçil)', 'общительный, открытый', 'friendly and sociable', 'His outgoing manner wins people over.', 'Açyk häsiýeti adamlary özüne çekýär.', 'B1'),
    ('patient', '/ˈpeɪʃnt/', 'ADJ', 'sabyrly', 'терпеливый', 'able to wait without complaining', 'A good teacher is patient.', 'Gowy mugallym sabyrly bolýar.', 'A2'),
    ('pessimistic', '/ˌpesɪˈmɪstɪk/', 'ADJ', 'ýaramaz pikirlenýän', 'пессимистичный', 'expecting bad things', 'Do not be so pessimistic!', 'Beýle ýaramaz pikirlenme!', 'B1'),
    ('shy', '/ʃaɪ/', 'ADJ', 'ýaýraň', 'застенчивый', 'nervous about meeting people', 'The shy boy hid behind his mother.', 'Ýaýraň oglan ejesiniň arkasynda gizlendi.', 'A2'),
    ('stubborn', '/ˈstʌbən/', 'ADJ', 'tetik (inat)', 'упрямый', 'refusing to change your mind', 'He is too stubborn to apologise.', 'Ol ötünç soramak üçin gaty inat.', 'B1'),
    ('vain', '/veɪn/', 'ADJ', 'özüni göterýän', 'тщеславный', 'too proud of your appearance', 'The vain actor admired his photo.', 'Özüni göterýän aktýor suratyna syn etdi.', 'B2'),
    ('wise', '/waɪz/', 'ADJ', 'paýhasly (dana)', 'мудрый', 'having deep understanding', 'My grandmother gave me wise advice.', 'Mamam paýhasly maslahat berdi.', 'A2'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('bright', '/braɪt/', 'ADJ', 'zehinli', 'сообразительный', 'intelligent and quick to learn', 'She is a bright student who asks good questions.', 'Ol gowy soraglary berýän zehinli talyp.', 'A2'),
    ('conscientious', '/ˌkɒnʃiˈenʃəs/', 'ADJ', 'jogapkärli, ünsli', 'добросовестный', 'careful to do your work well and properly', 'A conscientious employee checks every detail.', 'Jogapkärli işgär her jikme-jigi barlaýar.', 'B2'),
    ('determined', '/dɪˈtɜːmɪnd/', 'ADJ', 'tutanýerli, aýgytly', 'решительный', 'not willing to give up', 'She was determined to finish the course.', 'Ol okuwy tamamlamagy ýüregine düwdi.', 'B1'),
    ('resourceful', '/rɪˈzɔːsfl/', 'ADJ', 'ugurtapyjy', 'находчивый', 'good at finding quick ways to solve problems', 'The resourceful team fixed the problem quickly.', 'Ugurtapyjy topar meseläni tiz çözdi.', 'B2'),
    ('sarcastic', '/sɑːˈkæstɪk/', 'ADJ', 'kinayeli', 'саркастичный', 'using words that mean the opposite to mock someone', 'His sarcastic comment made everyone uncomfortable.', 'Onuň kinayeli sözi hemmäni oňaýsyz ýagdaýa saldy.', 'B2'),
    ('self-sufficient', '/ˌself səˈfɪʃnt/', 'ADJ', 'özbaşdak', 'самостоятельный', 'able to manage without help from others', 'The village is almost self-sufficient in food.', 'Oba azyk babatda diýen ýaly özbaşdak.', 'B2'),
    ('spontaneous', '/spɒnˈteɪniəs/', 'ADJ', 'duýdansyz, öz-özünden bolan', 'спонтанный', 'done naturally without planning', 'We made a spontaneous decision to stay another night.', 'Ýene bir gije galmak barada duýdansyz karar etdik.', 'B2'),
    ('steady', '/ˈstedi/', 'ADJ', 'durnukly, ygtybarly', 'устойчивый, надёжный', 'calm and reliable, or not changing suddenly', 'She has a steady personality and rarely panics.', 'Onuň häsiýeti durnukly, ol seýrek howsala düşýär.', 'B1'),
    ('straightforward', '/ˌstreɪtˈfɔːwəd/', 'ADJ', 'gönümel, açyk', 'прямолинейный', 'honest and direct in what you say', 'He is straightforward about his opinions.', 'Ol pikirlerini gönümel aýdýar.', 'B2'),
    ('sympathetic', '/ˌsɪmpəˈθetɪk/', 'ADJ', 'duýgudaş', 'сочувствующий', 'kind and understanding when someone has a problem', 'My manager was sympathetic when I was ill.', 'Kesellänimde ýolbaşçym maňa duýgudaşlyk bildirdi.', 'B1'),
    ('thorough', '/ˈθʌrə/', 'ADJ', 'jikme-jik, örän ünsli', 'тщательный', 'careful to include every detail', 'The inspector made a thorough check of the building.', 'Barlagçy binany jikme-jik barlady.', 'B2'),
    ('control freak', '/kənˈtrəʊl friːk/', 'N', 'hemme zady dolandyrmaga çalyşýan adam', 'человек, стремящийся всё контролировать', 'someone who insists on controlling everything', 'My sister is a bit of a control freak.', 'Uýam hemme zady dolandyrmaga biraz aşa çalyşýar.', 'B2'),
    ('too trusting', '/tuː ˈtrʌstɪŋ/', 'ADJ', 'aşa ynanjaň', 'слишком доверчивый', 'too ready to believe that people are honest', 'He is too trusting and people sometimes take advantage of him.', 'Ol aşa ynanjaň, adamlar käwagt ondan peýdalanýarlar.', 'B2'),
    ('tend to', '/tend tuː/', 'PHR', 'adatça etmek, meýilli bolmak', 'иметь склонность', 'to usually do or be something', 'I tend to avoid arguments.', 'Men adatça jedellerden gaça durýaryn.', 'B1'),
    ('come across as', '/kʌm əˈkrɒs æz/', 'PHR', '... bolup görünmek', 'производить впечатление', 'to seem to have a particular quality', 'She comes across as confident, but she is shy.', 'Ol özüne ynamly bolup görünýär, ýöne utanjaň.', 'B2'),
    ('deep down', '/ˌdiːp ˈdaʊn/', 'ADV', 'içinden, aslynda', 'в глубине души', 'when you consider someone’s real feelings', 'Deep down, he knows that she is right.', 'Ol içinden onuň mamladygyny bilýär.', 'B2'),
    ('on the surface', '/ɒn ðə ˈsɜːfɪs/', 'PHR', 'daşyndan seredeniňde', 'на первый взгляд', 'judging only by what is visible', 'On the surface, the job seems easy.', 'Daşyndan seredeniňde, iş aňsat ýaly.', 'B2'),
    ('on the whole', '/ɒn ðə həʊl/', 'ADV', 'umuman alanyňda', 'в целом', 'in general, considering everything', 'On the whole, the team worked well together.', 'Umuman alanyňda, topar bilelikde gowy işledi.', 'B1'),
    ('heart of gold', '/ˌhɑːt əv ˈɡəʊld/', 'PHR', 'altyn ýürekli', 'золотое сердце', 'a very kind and generous nature', 'My grandfather has a heart of gold.', 'Atamyň ýüregi altyn ýaly.', 'B2'),
    ('down to earth', '/ˌdaʊn tuː ˈɜːθ/', 'PHR', 'sada we durmuşa ýakyn', 'простой и практичный', 'sensible, practical, and not pretentious', 'Despite her success, she is very down to earth.', 'Üstünlik gazansa-da, ol örän sada.', 'B2'),
    ('cold fish', '/ˌkəʊld ˈfɪʃ/', 'PHR', 'sowukganly, duýgusyny görkezmeýän adam', 'холодный, замкнутый человек', 'an unfriendly person who does not show emotion', 'He seemed like a cold fish at first.', 'Ilkibaşda ol sowukganly adam ýaly göründi.', 'B2'),
    ('pain in the neck', '/ˌpeɪn ɪn ðə ˈnek/', 'PHR', 'örän bizar ediji adam ýa-da zat', 'страшно надоедливый человек или предмет', 'someone or something very annoying', 'Waiting in that queue was a real pain in the neck.', 'Şol nobata garaşmak örän bizar edijidi.', 'B2'),
    ('soft touch', '/ˌsɒft ˈtʌtʃ/', 'PHR', 'ýüregi ýumşak, aňsat razy bolýan adam', 'мягкий, уступчивый человек', 'someone who is easily persuaded to give or do something', 'Ask Dad for a loan; he is a soft touch.', 'Kakadan karz sora, ol aňsat razy bolýar.', 'B2'),
    ('quick temper', '/ˌkwɪk ˈtempə/', 'PHR', 'çalt gaharlanýan häsiýet', 'вспыльчивый характер', 'a tendency to become angry easily', 'My brother has a quick temper.', 'Doganım çalt gaharlanýar.', 'B2'),
    ('full of yourself', '/ˌfʊl əv jəˈself/', 'PHR', 'özüni aşa gowy görýän', 'самовлюблённый', 'too pleased with yourself and your importance', 'He is so full of himself that nobody enjoys his company.', 'Ol özüni şeýle gowy görýär welin, hiç kim onuň ýanynda bolasy gelenok.', 'B2'),
    ("wouldn't hurt a fly", '/ˌwʊdnt hɜːt ə ˈflaɪ/', 'PHR', 'hiç kime zyýan ýetirmez', 'мухи не обидит', 'is very gentle and harmless', 'She looks serious, but she wouldn’t hurt a fly.', 'Ol çynlakaý görünýär, ýöne hiç kime zyýan ýetirmez.', 'B2'),
    ('lift a finger', '/ˌlɪft ə ˈfɪŋɡə/', 'PHR', 'kiçijik hem kömek etmezlik', 'палец о палец не ударить', 'to make even a small effort to help', 'He never lifts a finger to help with the housework.', 'Ol öý işlerine kömek etmek üçin barmagyny-da gymyldatmaýar.', 'B2'),
    ('life and soul of the party', '/ˌlaɪf ən ˌsəʊl əv ðə ˈpɑːti/', 'PHR', 'oturyşyň şowhunly merkezi', 'душа компании', 'the person who makes a social event enjoyable', 'Mina is always the life and soul of the party.', 'Mina hemişe oturyşyň şowhunly merkezi bolýar.', 'B2'),
]

# ---- Vocabulary Bank — Work -> 1B ----
T['work2'] = [
    ('ambition', '/æmˈbɪʃn/', 'N', 'maksat (öňe saýlanma)', 'амбиция, стремление', 'a strong wish to achieve something', 'Her ambition is to become a doctor.', 'Maksady lukman bolmak.', 'B1', 'career ambition'),
    ('career', '/kəˈrɪə(r)/', 'N', 'kär (uzak möhletli iş)', 'карьера', 'a job or profession you do for years', 'He built a career in banking.', 'Bank ulgamynda kär gurdu.', 'A2', 'career path'),
    ('intern', '/ˈɪntɜːn/', 'N', 'stajýor', 'стажёр', 'a student gaining work experience', 'The intern helped with the report.', 'Stajýor hasabata kömek etdi.', 'B1'),
    ('job satisfaction', '/dʒɒb ˌsætɪsˈfækʃn/', 'N', 'işden kanagatlanma', 'удовлетворение работой', 'the pleasure you get from your job', 'Job satisfaction matters more than pay.', 'Işden kanagatlanma aýlykdan möhüm.', 'B2'),
    ('profession', '/prəˈfeʃn/', 'N', 'hünär (kär)', 'профессия', 'a job needing special training', 'Teaching is a noble profession.', 'Mugallymçylyk asylly hünär.', 'A2'),
    ('promotion', '/prəˈməʊʃn/', 'N', 'wezipe galmak', 'повышение (в должности)', 'moving to a higher job level', 'She got a promotion last year.', 'Geçen ýyl wezipesi galdy.', 'A2', 'get a promotion'),
    ('qualified', '/ˈkwɒlɪfaɪd/', 'ADJ', 'hünärli', 'квалифицированный', 'having the right training for a job', 'We need a qualified electrician.', 'Hünärli elektrik gerek.', 'A2', 'highly qualified'),
    ('retire', '/rɪˈtaɪə(r)/', 'V', 'pensiýa çykmak', 'выходить на пенсию', 'to stop working because of age', 'He plans to retire at sixty.', 'Alty ýaşynda pensiýa çykmagy meýilleşdirýär.', 'A2', 'retire from'),
    ('unemployment', '/ˌʌnɪmˈplɔɪmənt/', 'N', 'işsizlik', 'безработица', 'the state of having no job', 'Unemployment fell this year.', 'Işsizlik şu ýyl azaldy.', 'B1', 'unemployment rate'),
    ('vacancy', '/ˈveɪkənsi/', 'N', 'boş iş orny', 'вакансия', 'an unfilled job position', 'There is a vacancy in the sales team.', 'Satuw toparynda boş iş orny bar.', 'B1', 'job vacancy'),
    ('workaholic', '/ˌwɜːkəˈhɒlɪk/', 'N', 'işbaz', 'трудоголик', 'a person who works too much', 'The workaholic never takes holidays.', 'Işbaz hiç wagt dynç almaga gitmeýär.', 'B2'),
    ('workforce', '/ˈwɜːkfɔːs/', 'N', 'işçi güýji', 'рабочая сила', 'all the workers of a company', 'The workforce grew by ten per cent.', 'Işçi güýji on göterim artdy.', 'B2'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('challenging', '/ˈtʃælɪndʒɪŋ/', 'ADJ', 'kyn, synagly', 'сложный, требующий усилий', 'difficult in an interesting way', 'Teaching a large class can be challenging.', 'Uly synpa sapak bermek kyn bolup biler.', 'B1'),
    ('monotonous', '/məˈnɒtənəs/', 'ADJ', 'birmeňzeş we ýürekgysdyryjy', 'монотонный', 'boring because it never changes', 'The work became monotonous after a few months.', 'Birnäçe aýdan soň iş birmeňzeş we ýürekgysdyryjy boldy.', 'B2'),
    ('repetitive', '/rɪˈpetətɪv/', 'ADJ', 'gaýtalanýan', 'повторяющийся', 'involving the same actions again and again', 'The job is repetitive, but it is not difficult.', 'Iş gaýtalanýar, ýöne kyn däl.', 'B2'),
    ('rewarding', '/rɪˈwɔːdɪŋ/', 'ADJ', 'kanagatlandyryjy', 'приносящий удовлетворение', 'making you feel that your work is valuable', 'Working with children is very rewarding.', 'Çagalar bilen işlemek örän kanagatlandyryjy.', 'B1'),
    ('fulfilling', '/fʊlˈfɪlɪŋ/', 'ADJ', 'manyly, ruhy taýdan kanagatlandyryjy', 'приносящий удовлетворение', 'giving you a strong feeling of satisfaction', 'She finds her job as a nurse fulfilling.', 'Ol şepagat uýasy işini manyly hasaplaýar.', 'B2'),
    ('motivating', '/ˈməʊtɪveɪtɪŋ/', 'ADJ', 'höweslendiriji', 'мотивирующий', 'making you want to work or achieve more', 'A supportive manager can be very motivating.', 'Goldaýan ýolbaşçy örän höweslendiriji bolup biler.', 'B2'),
    ('demanding', '/dɪˈmɑːndɪŋ/', 'ADJ', 'köp güýç we zähmet talap edýän', 'требовательный, тяжёлый', 'needing a lot of time, energy, or skill', 'Being a surgeon is a demanding job.', 'Hirurg bolmak köp zähmet talap edýän iş.', 'B2'),
    ('tedious', '/ˈtiːdiəs/', 'ADJ', 'ýürekgysdyryjy, iriziji', 'утомительный, скучный', 'boring and continuing for too long', 'Entering all the data by hand is tedious.', 'Ähli maglumatlary el bilen girizmek ýürekgysdyryjy.', 'B2'),
    ('dead-end', '/ˌded ˈend/', 'ADJ', 'ösüş mümkinçiligi bolmadyk', 'бесперспективный', 'offering no chance of promotion or progress', 'He left his dead-end job and went back to college.', 'Ol ösüş mümkinçiligi bolmadyk işinden çykyp, kolleje dolandy.', 'B2'),
    ('high-powered', '/ˌhaɪ ˈpaʊəd/', 'ADJ', 'ýokary derejeli we jogapkärçiligi uly', 'высокопоставленный', 'important and involving a lot of responsibility', 'She has a high-powered job in finance.', 'Maliýe ulgamynda ýokary derejeli işi bar.', 'B2'),
    ('career move', '/kəˈrɪə muːv/', 'PHR', 'karýera ädimi', 'карьерный шаг', 'a decision that helps or changes your career', 'Moving abroad was a smart career move.', 'Daşary ýurda göçmek karýera üçin oňat ädim boldy.', 'B2'),
    ('job hunting', '/ˈdʒɒb ˌhʌntɪŋ/', 'N', 'iş gözlemek', 'поиск работы', 'the activity of looking for a job', 'He is job hunting after finishing university.', 'Uniwersiteti tamamlandan soň ol iş gözleýär.', 'B1'),
    ('event manager', '/ɪˈvent ˌmænɪdʒə/', 'N', 'çäreleri gurnaýjy', 'организатор мероприятий', 'a person who plans and organizes events', 'The event manager arranged the conference.', 'Çäreleri gurnaýjy maslahaty gurady.', 'B2'),
    ('qualification', '/ˌkwɒlɪfɪˈkeɪʃn/', 'N', 'hünär derejesi, şahadatnama', 'квалификация', 'an exam result or skill needed for a job', 'This position requires a teaching qualification.', 'Bu wezipe mugallymçylyk hünär derejesini talap edýär.', 'B1'),
    ('work experience', '/ˈwɜːk ɪkˌspɪəriəns/', 'N', 'iş tejribesi', 'опыт работы', 'knowledge and skills gained by doing a job', 'The advert asks for two years of work experience.', 'Bildirişde iki ýyl iş tejribesi soralýar.', 'B1'),
    ('career ladder', '/kəˈrɪə ˌlædə/', 'N', 'karýera basgançagy', 'карьерная лестница', 'the series of jobs that lead to higher positions', 'She hopes to move up the career ladder.', 'Ol karýera basgançagyndan ýokary galmagy umyt edýär.', 'B2'),
    ('civil servant', '/ˌsɪvl ˈsɜːvənt/', 'N', 'döwlet gullukçysy', 'государственный служащий', 'a person who works for a government department', 'My aunt is a civil servant in the health department.', 'Daýzam saglygy goraýyş bölüminde döwlet gullukçysy.', 'B2'),
    ('fast track', '/ˌfɑːst ˈtræk/', 'N', 'çalt öňe gidiş ýoly', 'ускоренный путь к успеху', 'a quick route to promotion or success', 'The company put its best graduates on the fast track.', 'Kompaniýa iň gowy uçurymlaryny çalt öňe gidiş ýoluna goşdy.', 'B2'),
    ('colleague', '/ˈkɒliːɡ/', 'N', 'işdeşim', 'коллега', 'a person you work with', 'One of my colleagues is moving to another office.', 'Işdeşlerimiň biri başga edara geçýär.', 'A2'),
    ('co-worker', '/ˌkəʊ ˈwɜːkə/', 'N', 'işdeşim', 'сослуживец', 'a person who works with you', 'I get on well with my co-workers.', 'Işdeşlerim bilen oňat düşünişýärin.', 'B1'),
    ('quit', '/kwɪt/', 'V', 'işden çykmak, bes etmek', 'увольняться, бросать', 'to leave a job or stop doing something', 'She decided to quit her job and travel.', 'Ol işinden çykyp, syýahat etmegi karar etdi.', 'A2'),
    ('resign', '/rɪˈzaɪn/', 'V', 'işden meýletin çykmak', 'увольняться', 'to formally leave a job', 'He resigned after ten years as director.', 'Ol on ýyl direktor bolandan soň işden çykdy.', 'B2'),
    ('staff', '/stɑːf/', 'N', 'işgärler', 'персонал', 'all the people who work for an organization', 'The hotel staff were very helpful.', 'Myhmanhananyň işgärleri örän kömek etdi.', 'A2'),
    ('lay off', '/ˌleɪ ˈɒf/', 'V', 'işgär sanyny azaltmak üçin işden çykarmak', 'увольнять из-за сокращения', 'to stop employing someone because there is not enough work', 'The factory laid off fifty workers.', 'Zawod elli işgäri işden çykardy.', 'B2'),
    ('make redundant', '/ˌmeɪk rɪˈdʌndənt/', 'PHR', 'wezipe zerur bolmansoň işden çykarmak', 'увольнять из-за сокращения штата', 'to end someone’s job because it is no longer needed', 'The company made several employees redundant.', 'Kompaniýa birnäçe işgäri wezipäniň gysgaldylmagy sebäpli çykardy.', 'B2'),
    ('out of work', '/ˌaʊt əv ˈwɜːk/', 'PHR', 'işsiz', 'без работы', 'without a job', 'He has been out of work since January.', 'Ýanwardan bäri ol işsiz.', 'B1'),
    ('off work', '/ˌɒf ˈwɜːk/', 'PHR', 'işe çykmaýan, işden rugsatly', 'не на работе', 'not at work, often because you are ill or on holiday', 'I am off work this week with a bad cold.', 'Güýçli dümew sebäpli şu hepde işe çykamok.', 'B1'),
    ('sack', '/sæk/', 'V', 'işden kowmak', 'увольнять', 'to make someone leave their job', 'The manager sacked him for repeated lateness.', 'Ýolbaşçy ony yzygiderli gijä galýandygy üçin işden kowdy.', 'B1'),
    ('fire', '/ˈfaɪə/', 'V', 'işden çykarmak', 'увольнять', 'to make someone leave a job, especially because of poor work', 'They fired the employee for breaking the rules.', 'Düzgüni bozandygy üçin işgäri işden çykardylar.', 'B1'),
    ('promote', '/prəˈməʊt/', 'V', 'wezipe galdyrmak', 'повышать в должности', 'to give someone a higher position at work', 'The company promoted her to team leader.', 'Kompaniýa ony topar ýolbaşçysy wezipesine galdyrdy.', 'B1'),
    ('pay rise', '/ˈpeɪ raɪz/', 'N', 'aýlyk ýokarlanmasy', 'повышение зарплаты', 'an increase in the money you earn', 'He asked his boss for a pay rise.', 'Ol ýolbaşçysyndan aýlygynyň ýokarlandyrylmagyny sorady.', 'B1'),
    ('skill', '/skɪl/', 'N', 'başarnyk', 'навык', 'an ability to do something well', 'Good communication skills are useful in this job.', 'Gowy aragatnaşyk başarnyklary bu işde peýdaly.', 'A2'),
    ('hire', '/ˈhaɪə/', 'V', 'işe almak', 'нанимать', 'to give someone a job', 'The company plans to hire two designers.', 'Kompaniýa iki dizaýneri işe almagy meýilleşdirýär.', 'A2'),
    ('employ', '/ɪmˈplɔɪ/', 'V', 'işe almak', 'нанимать', 'to give work to someone and pay them', 'The hotel employs over a hundred people.', 'Myhmanhana ýüzden gowrak adamy işe alýar.', 'A2'),
    ('perk', '/pɜːk/', 'N', 'goşmaça ýeňillik', 'льгота, бонус', 'an extra benefit provided by a job', 'Free lunches are one of the perks of the job.', 'Mugt günortanlyk bu işiň goşmaça ýeňillikleriniň biridir.', 'B2'),
    ('benefit', '/ˈbenɪfɪt/', 'N', 'goşmaça ýeňillik', 'льгота, преимущество', 'an extra advantage provided by an employer', 'The benefits include health insurance.', 'Goşmaça ýeňilliklere saglyk ätiýaçlandyryşy girýär.', 'B1'),
    ('freelance', '/ˈfriːlɑːns/', 'ADJ', 'erkin işleýän', 'внештатный', 'working for different companies rather than one employer', 'She does freelance translation from home.', 'Ol öýünden erkin terjime işini edýär.', 'B2'),
    ('paternity leave', '/pəˈtɜːnəti liːv/', 'N', 'atanyň çaga doglandan soňky rugsady', 'отцовский отпуск', 'time off work for a father after a baby is born', 'He took two weeks of paternity leave.', 'Ol iki hepde atalyk rugsadyny aldy.', 'B2'),
    ('permanent', '/ˈpɜːmənənt/', 'ADJ', 'hemişelik', 'постоянный', 'continuing for a long time or without an end', 'She is looking for a permanent position.', 'Ol hemişelik wezipe gözleýär.', 'B1'),
    ('sick leave', '/ˈsɪk liːv/', 'N', 'kesel sebäpli rugsat', 'больничный отпуск', 'time away from work because you are ill', 'He is on sick leave until Friday.', 'Ol anna gününe çenli kesel rugsadynda.', 'B1'),
    ('compassionate leave', '/kəmˈpæʃənət liːv/', 'N', 'maşgala ýagdaýy sebäpli berilýän rugsat', 'отпуск по семейным обстоятельствам', 'time off work after a serious family event', 'She took compassionate leave after her father died.', 'Kakasy aradan çykandan soň ol maşgala rugsadyny aldy.', 'C1'),
    ('full-time', '/ˌfʊl ˈtaɪm/', 'ADJ', 'doly iş güni', 'полный рабочий день', 'working the normal number of hours each week', 'He has a full-time job at the bank.', 'Ol bankda doly iş gününde işleýär.', 'A2'),
    ('unpaid', '/ˌʌnˈpeɪd/', 'ADJ', 'tölegsiz', 'неоплачиваемый', 'not receiving money for work or time off', 'She took a month of unpaid leave.', 'Ol bir aý tölegsiz rugsat aldy.', 'B1'),
    ('zero-hours contract', '/ˌzɪərəʊ ˈaʊəz ˌkɒntrækt/', 'N', 'iş sagady kepillendirilmeýän şertnama', 'контракт без гарантированных часов', 'a work contract with no guaranteed minimum hours', 'He works weekends on a zero-hours contract.', 'Ol dynç günleri iş sagady kepillendirilmeýän şertnama bilen işleýär.', 'C1'),
]

# ---- in-lesson 2A — abstract nouns ----
T['abstract_nouns'] = [
    ('anger', '/ˈæŋɡə(r)/', 'N', 'gahar', 'гнев', 'a strong feeling of displeasure', 'He spoke with anger in his voice.', 'Sesinde gahar bilen gürledi.', 'A2', 'feel anger'),
    ('anxiety', '/æŋˈzaɪəti/', 'N', 'alada (ynjalyksyzlyk)', 'тревога', 'a feeling of worry', 'Exams cause anxiety for students.', 'Synaglar talyplarda alada döredýär.', 'B1', 'feel anxiety'),
    ('courage', '/ˈkʌrɪdʒ/', 'N', 'edermenlik', 'мужество', 'the ability to face danger', 'The firefighter showed great courage.', 'Ýangyn söndüriji uly edermenlik görkezdi.', 'A2', 'have the courage'),
    ('curiosity', '/ˌkjʊəriˈɒsəti/', 'N', 'interik', 'любопытство', 'a wish to know things', 'Her curiosity never stops.', 'Interigi hiç wagt gutaranok.', 'A2', 'out of curiosity'),
    ('enthusiasm', '/ɪnˈθjuːziæzəm/', 'N', 'yhläs', 'энтузиазм', 'a feeling of great interest', 'She talked with real enthusiasm.', 'Hakyky yhläs bilen gürrüň berdi.', 'B1', 'show enthusiasm'),
    ('friendship', '/ˈfrendʃɪp/', 'N', 'dostluk', 'дружба', 'the relationship between friends', 'Their friendship lasted forty years.', 'Dostlugy kyrk ýyl dowam etdi.', 'A2'),
    ('happiness', '/ˈhæpinəs/', 'N', 'bagt', 'счастье', 'the feeling of being happy', 'Money does not always bring happiness.', 'Pul hemişe bagt getirmeýär.', 'A2'),
    ('honesty', '/ˈɒnəsti/', 'N', 'dogruçyllyk', 'честность', 'the quality of telling the truth', 'I appreciate your honesty.', 'Dogruçyllygyňa baha berýärin.', 'B1'),
    ('intelligence', '/ɪnˈtelɪdʒəns/', 'N', 'zeka', 'интеллект', 'the ability to learn and understand', 'The puzzle tested my intelligence.', 'Tapmaça zekamy synady.', 'A2'),
    ('kindness', '/ˈkaɪndnəs/', 'N', 'mähirlilik', 'доброта', 'the quality of being kind', 'Thank you for your kindness.', 'Mähirliligiňiz üçin sag boluň.', 'A2'),
    ('loneliness', '/ˈləʊnlinəs/', 'N', 'ýalňyzlyk', 'одиночество', 'sadness from being alone', 'Loneliness affects many old people.', 'Ýalňyzlyk köp garrylara täsir edýär.', 'B1'),
    ('patience', '/ˈpeɪʃns/', 'N', 'sabyr', 'терпение', 'the ability to wait calmly', 'Teaching requires great patience.', 'Mugallymçylyk uly sabyr talap edýär.', 'A2', 'lose patience'),
    ('pride', '/praɪd/', 'N', 'buýsanç', 'гордость', 'a feeling of pleasure in yourself', 'She spoke with pride about her son.', 'Ogly barada buýsanç bilen gürledi.', 'A2', 'take pride in'),
    ('wealth', '/welθ/', 'N', 'baýlyk', 'богатство', 'a large amount of money', 'He shared his wealth with others.', 'Baýlygyny beýlekiler bilen paýlaşdy.', 'A2'),
]

# ---- in-lesson 2B — relationships ----
T['relationships'] = [
    ('acquaintance', '/əˈkweɪntəns/', 'N', 'tanyş', 'знакомый', 'a person you know a little', 'He is an acquaintance, not a friend.', 'Ol dost däl, tanyş.', 'B1'),
    ('bond', '/bɒnd/', 'N', 'baglanyşyk (duýgy)', 'связь, узы', 'a strong feeling between people', 'The twins have a special bond.', 'Ekizleriň aýratyn baglanyşygy bar.', 'B1', 'emotional bond'),
    ('companion', '/kəmˈpæniən/', 'N', 'ýoldaş (hemra)', 'спутник, компаньон', 'a person you spend time with', 'The dog was her faithful companion.', 'It onuň wepaly ýoldaşy boldy.', 'B1'),
    ('engagement', '/ɪnˈɡeɪdʒmənt/', 'N', 'atlanysyklar', 'помолвка', 'an agreement to marry', 'They announced their engagement.', 'Atlanyşyklaryny yglan etdiler.', 'B1'),
    ('marriage', '/ˈmærɪdʒ/', 'N', 'toý (nika)', 'брак, супружество', 'the state of being married', 'Their marriage has lasted ten years.', 'Nikalary on ýyl dowam etdi.', 'A2', 'happy marriage'),
    ('mate', '/meɪt/', 'N', 'dost (ýoldaş)', 'приятель', 'a friend (informal)', 'He went fishing with his mates.', 'Dostlary bilen balyk tutmaga gitdi.', 'A2'),
    ('relatives', '/ˈrelətɪvz/', 'N', 'garyndaşlar', 'родственники', 'members of your family', 'All our relatives came to the wedding.', 'Ähli garyndaşlarymyz toýa geldi.', 'A2'),
    ('sibling', '/ˈsɪblɪŋ/', 'N', 'dogan (aga-ini/uýa)', 'брат или сестра', 'a brother or sister', 'Do you have any siblings?', 'Doganyňyz barmy?', 'B1'),
    ('spouse', '/spaʊs/', 'N', 'ýanýoldaş', 'супруг(а)', 'a husband or wife', 'You may bring your spouse to the dinner.', 'Agşamlyk nahara ýanýoldaşyňyzy alyp gelip bilersiňiz.', 'B2'),
    ('generation gap', '/ˌdʒenəˈreɪʃn ɡæp/', 'N', 'nesil tapawudy', 'разрыв поколений', 'differences between old and young', 'Music often shows the generation gap.', 'Saz köplenç nesil tapawudyny görkezýär.', 'B1'),
]

# ---- Vocabulary Bank — Phrases with get -> 3A ----
T['get_phrases'] = [
    ('get away with', '/ɡet əˈweɪ wɪð/', 'PHR', 'jezasyz gutulmak', 'сходить с рук', 'to do something wrong without punishment', 'He never gets away with lies.', 'Ýalany hiç wagt jezasyz galmaýar.', 'B1'),
    ('get by', '/ɡet baɪ/', 'PHR', 'güzeranyny dolamak', 'сводить концы с концами', 'to manage with difficulty', 'They get by on a small salary.', 'Az aýlyk bilen güzeranyny dolap gelýärler.', 'B1', 'get by on'),
    ('get down to', '/ɡet daʊn tuː/', 'PHR', 'başlamak (çynlakaý)', 'браться за', 'to start doing something seriously', 'Let us get down to work.', 'Geliň, işe girişeliň.', 'A2', 'get down to business'),
    ('get over', '/ɡet ˈəʊvə(r)/', 'PHR', 'gutulmak (keselden)', 'оправиться от', 'to recover from something bad', 'She finally got over the flu.', 'Ahyry dümewden gutuldy.', 'A2', 'get over an illness'),
    ('get together', '/ɡet təˈɡeðə(r)/', 'PHR', 'ýygnanmak', 'собираться вместе', 'to meet and spend time', 'We get together every Sunday.', 'Her ýekşenbe ýygnanýarys.', 'A2'),
    ('get used to', '/ɡet ˈjuːzd tuː/', 'PHR', 'öwrenişmek', 'привыкать', 'to become familiar with something', 'I got used to the cold weather.', 'Sowuk howa öwrenişdim.', 'A2', 'get used to doing'),
    ('get away', '/ɡet əˈweɪ/', 'PHR', 'gaçyp gutulmak', 'сбежать, вырваться', 'to escape, or go on holiday', 'The thieves got away in a car.', 'Ogrular maşyn bilen gaçyp gutuldy.', 'A2'),
    ('get round to', '/ɡet ˈraʊnd tuː/', 'PHR', 'wagt tapyp etmek', 'собираться сделать', 'to finally do something delayed', 'I never got round to calling him.', 'Oňa jaň etmäge wagt tapmadym.', 'B2'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('get the chance', '/ˌɡet ðə ˈtʃɑːns/', 'PHR', 'mümkinçilik gazanmak', 'получить возможность', 'to have an opportunity to do something', 'We got the chance to meet the author.', 'Awtory bilen duşuşmaga mümkinçilik gazandyk.', 'B1'),
    ('get the impression', '/ˌɡet ði ɪmˈpreʃn/', 'PHR', 'täsir almak, pikir döremek', 'создаётся впечатление', 'to begin to think that something is true', 'I get the impression that he is worried.', 'Ol aladaly ýaly bolup görünýär.', 'B2'),
    ('get the wrong end of the stick', '/ˌɡet ðə ˌrɒŋ end əv ðə ˈstɪk/', 'PHR', 'nädogry düşünmek', 'неправильно понять', 'to misunderstand a situation', 'I think you got the wrong end of the stick.', 'Meniňçe, sen ýagdaýy nädogry düşündiň.', 'C1'),
    ('get the joke', '/ˌɡet ðə ˈdʒəʊk/', 'PHR', 'degişmä düşünmek', 'понять шутку', 'to understand why something is funny', 'Nobody got the joke about the old computer.', 'Köne kompýuter baradaky degişmä hiç kim düşünmedi.', 'B1'),
    ('get to know', '/ˌɡet tə ˈnəʊ/', 'PHR', 'tanyşmak, öwrenmek', 'познакомиться', 'to become familiar with a person or place', 'It takes time to get to know a new colleague.', 'Täze işdeşi tanamak üçin wagt gerek.', 'A2'),
    ('get hold of', '/ˌɡet ˈhəʊld əv/', 'PHR', 'habarlaşmak, tapmak', 'связаться с', 'to contact or find someone or something', 'I could not get hold of the doctor yesterday.', 'Düýn lukman bilen habarlaşyp bilmedim.', 'B2'),
    ('get rid of', '/ˌɡet ˈrɪd əv/', 'PHR', 'dynmak, aýyrmak', 'избавиться от', 'to remove or throw away something unwanted', 'We need to get rid of these old boxes.', 'Bu köne gutulardan dynmaly.', 'B1'),
    ('get your own back on', '/ˌɡet jɔːr ˌəʊn ˈbæk ɒn/', 'PHR', 'öç almak', 'отомстить', 'to do something unpleasant to someone who treated you badly', 'He got his own back on the bully with a clever trick.', 'Ol akylly hile bilen sütemkärden öç aldy.', 'C1'),
    ('get into trouble with', '/ˌɡet ˌɪntə ˈtrʌbl wɪð/', 'PHR', '... bilen başagaýlyga düşmek', 'попасть в неприятности из-за', 'to have problems because of something you did', 'She got into trouble with her boss for arriving late.', 'Gijä galandygy üçin ol ýolbaşçysy bilen başagaýlyga düşdi.', 'B2'),
    ('get out of the way', '/ˌɡet ˌaʊt əv ðə ˈweɪ/', 'PHR', 'ýoldan sowulmak', 'уйти с дороги', 'to move so that someone or something can pass', 'Please get out of the way of the ambulance.', 'Tiz kömek ulagynyň ýolundan sowluň.', 'B1'),
    ('get real', '/ˌɡet ˈrɪəl/', 'PHR', 'hakykata ýüzlenmek', 'смотреть на вещи реально', 'used to tell someone to be realistic', 'Get real — we cannot afford that house.', 'Hakykata ýüzlen — şol jaýy alyp bilmeris.', 'B2'),
    ('get a life', '/ˌɡet ə ˈlaɪf/', 'PHR', 'öz durmuşyň bilen meşgullan', 'найди себе занятие', 'used rudely to tell someone to do more interesting things', 'He spends all day criticizing people online; he needs to get a life.', 'Ol bütin gün internetde adamlary tankytlaýar; başga işe güýmenmeli.', 'C1'),
    ('get nowhere', '/ˌɡet ˈnəʊweə/', 'PHR', 'netije gazanmazlyk', 'не продвигаться', 'to make no progress', 'We got nowhere with the crossword.', 'Krosswordy çözmekde hiç öňe gidip bilmedik.', 'B2'),
    ("get on somebody's nerves", '/ˌɡet ɒn ˈsʌmbədiz nɜːvz/', 'PHR', 'biriniň gaharyna degmek', 'действовать кому-либо на нервы', 'to annoy someone', 'That constant tapping is getting on my nerves.', 'Üznüksiz şakyrdatmak meniň gaharyma degýär.', 'B2'),
    ('get your act together', '/ˌɡet jɔːr ˌækt təˈɡeðə/', 'PHR', 'özüňi ele almak', 'взяться за ум', 'to organize yourself and behave responsibly', 'You need to get your act together before the exams.', 'Synaglardan öň özüňi ele almaly.', 'B2'),
    ('get on like a house on fire', '/ˌɡet ɒn laɪk ə ˌhaʊs ɒn ˈfaɪə/', 'PHR', 'örän gowy düşünişmek', 'очень быстро найти общий язык', 'to like each other and become friendly very quickly', 'The two new colleagues got on like a house on fire.', 'Täze işdeşleriň ikisi bada-bat gowy düşünişdiler.', 'C1'),
    ('get a move on', '/ˌɡet ə ˈmuːv ɒn/', 'PHR', 'howlukmak', 'поторопиться', 'to hurry', 'We need to get a move on or we will miss the train.', 'Howlukmaly, ýogsam otla gijä galarys.', 'B2'),
    ('get on a bit', '/ˌɡet ˈɒn ə bɪt/', 'PHR', 'ýaşamak, ýaşy ulalmak', 'быть уже в возрасте', 'to be rather old', 'Your grandfather must be getting on a bit now.', 'Atan indi ýaşy birçene baran bolmaly.', 'C1'),
    ('get the message', '/ˌɡet ðə ˈmesɪdʒ/', 'PHR', 'aýdyljak bolýan zada düşünmek', 'понять намёк', 'to understand what someone is trying to tell you', 'I hinted about the noise, but he did not get the message.', 'Şowhun barada yşarat etdim, ýöne ol düşünmedi.', 'B2'),
    ('get your own way', '/ˌɡet jɔːr əʊn ˈweɪ/', 'PHR', 'islän zadyňa ýetmek', 'добиться своего', 'to make other people do what you want', 'She always gets her own way with her parents.', 'Ol ene-atasyndan hemişe islän zadyny alýar.', 'B2'),
    ('get on with', '/ˌɡet ˈɒn wɪð/', 'PHR', 'dowam etmek', 'продолжать', 'to continue doing something', 'Please get on with your work while I am away.', 'Men ýok wagtym işiňi dowam et.', 'B1'),
    ('get into', '/ˌɡet ˈɪntə/', 'PHR', 'bir işe ýa-da hünäre başlamak', 'начать заниматься', 'to start doing or become involved in something', 'She hopes to get into banking after university.', 'Ol uniwersitetden soň bank işine başlamagy umyt edýär.', 'B2'),
    ('get around', '/ˌɡet əˈraʊnd/', 'PHR', 'bir ýerden başga ýere hereket etmek', 'передвигаться', 'to travel or move from place to place', 'It is easy to get around the city by bus.', 'Şäherde awtobus bilen hereket etmek aňsat.', 'B1'),
    ('get behind', '/ˌɡet bɪˈhaɪnd/', 'PHR', 'yza galmak', 'отстать', 'to fail to do enough work on time', 'I got behind with my studies during the holiday.', 'Dynç alyşda sapaklarymdan yza galdym.', 'B2'),
    ('get someone down', '/ˌɡet ˈsʌmwʌn daʊn/', 'PHR', 'birini ruhdan düşürmek', 'удручать кого-либо', 'to make someone feel unhappy', 'The dark winter weather gets me down.', 'Gyşyň garaňky howasy meni ruhdan düşürýär.', 'B2'),
    ('get out of', '/ˌɡet ˈaʊt əv/', 'PHR', 'borçdan gaçmak', 'увильнуть от', 'to avoid doing something you should do', 'He got out of helping us by saying he was busy.', 'Ol işli diýmek bilen bize kömek etmekden gaçdy.', 'B2'),
    ('get back to', '/ˌɡet ˈbæk tuː/', 'PHR', 'soňra jogap bermek ýa-da habarlaşmak', 'связаться позже', 'to contact someone again later', 'I will get back to you with an answer tomorrow.', 'Ertir jogap bilen size habarlaşaryn.', 'B1'),
]

# ---- Vocabulary Bank — Conflict and warfare -> 3B ----
T['conflict'] = [
    ('battlefield', '/ˈbætlfiːld/', 'N', 'söweş meýdany', 'поле боя', 'a place where a battle happens', 'The battlefield is now a museum.', 'Söweş meýdany indi muzeý.', 'B1'),
    ('casualty', '/ˈkæʒuəlti/', 'N', 'pidalar (ýitgiler)', 'жертвы, потери', 'a person killed or injured in war', 'The battle caused many casualties.', 'Söweş köp pidalara sebäp boldy.', 'B2'),
    ('civilian', '/səˈvɪliən/', 'N', 'asuda ilat', 'мирный житель', 'a person not in the army', 'The war harmed many civilians.', 'Uruş köp asuda ilata zyýan ýetirdi.', 'B1'),
    ('defeat', '/dɪˈfiːt/', 'V', 'ýeňmek', 'побеждать (в войне)', 'to win against an enemy', 'The army defeated the invaders.', 'Goşun basyp alýjylary ýeňdi.', 'A2'),
    ('defend', '/dɪˈfend/', 'V', 'goramak', 'защищать', 'to protect from attack', 'The soldiers defended the city.', 'Esgirler şäheri gorady.', 'A2', 'defend against'),
    ('enemy', '/ˈenəmi/', 'N', 'duşman', 'враг', 'a person or country you fight', 'The enemy attacked at dawn.', 'Duşman dan atacasy hüjüm etdi.', 'A2'),
    ('invade', '/ɪnˈveɪd/', 'V', 'basyp almak', 'вторгаться', 'to enter a country by force', 'The invaders crossed the border.', 'Basyp alýjylar serhetden geçdi.', 'B1'),
    ('rescue', '/ˈreskjuː/', 'V', 'halas etmek', 'спасать', 'to save someone from danger', 'Firefighters rescued the family.', 'Ýangyn söndürijiler maşgalany halas etdi.', 'A2', 'rescue someone'),
    ('siege', '/siːdʒ/', 'N', 'gabaw', 'осада', 'surrounding a place to force surrender', 'The siege lasted three months.', 'Gabaw üç aý dowam etdi.', 'B2', 'under siege'),
    ('soldier', '/ˈsəʊldʒə(r)/', 'N', 'esger', 'солдат', 'a member of an army', 'The soldier returned home.', 'Esger öýüne gaýtdy.', 'A2'),
    ('surrender', '/səˈrendə(r)/', 'V', 'boýun egmek', 'сдаваться', 'to stop fighting and admit defeat', 'The troops were forced to surrender.', 'Goşun boýun egmäge mejbur boldy.', 'B1'),
    ('victim', '/ˈvɪktɪm/', 'N', 'pida', 'жертва', 'a person harmed by something', 'The victims received help quickly.', 'Pidalar kömegi tiz aldy.', 'A2', 'victim of'),
    ('weapon', '/ˈwepən/', 'N', 'ýarag', 'оружие', 'an object used for fighting', 'The museum displays old weapons.', 'Muzeý köne ýaraglary görkezýär.', 'A2', 'carry a weapon'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('ally', '/ˈælaɪ/', 'N', 'hyzmatdaş, ýaran', 'союзник', 'a country or person that gives help and support', 'The two countries became allies during the war.', 'Uruş döwründe iki ýurt ýaran boldy.', 'B1'),
    ('armed forces', '/ˌɑːmd ˈfɔːsɪz/', 'N', 'ýaragly güýçler', 'вооружённые силы', 'a country’s army, navy, and air force', 'The armed forces were sent to protect the border.', 'Serhedi goramak üçin ýaragly güýçler iberildi.', 'B2'),
    ('commander', '/kəˈmɑːndə/', 'N', 'serkerde, buýruk beriji', 'командир', 'an officer who is in charge of a military operation', 'The commander ordered the troops to retreat.', 'Serkerde goşuna yza çekilmegi buýurdy.', 'B1'),
    ('refugee', '/ˌrefjuˈdʒiː/', 'N', 'bosgun', 'беженец', 'a person forced to leave their home or country', 'The refugee family crossed the border safely.', 'Bosgun maşgala serhetden sag-aman geçdi.', 'B1'),
    ('sniper', '/ˈsnaɪpə/', 'N', 'mergen', 'снайпер', 'a soldier who shoots from a hidden position', 'The sniper was hidden on a rooftop.', 'Mergen üçegiň üstünde gizlenipdi.', 'B2'),
    ('survivor', '/səˈvaɪvə/', 'N', 'aman galan adam', 'выживший', 'a person who stays alive after danger or disaster', 'The survivors were found two days later.', 'Aman galan adamlar iki günden soň tapyldy.', 'B1'),
    ('troops', '/truːps/', 'N', 'goşun', 'войска', 'soldiers, especially in a large organized group', 'The troops arrived before sunrise.', 'Goşun gün dogmanka geldi.', 'B1'),
    ('the wounded', '/ðə ˈwuːndɪd/', 'N', 'ýaralananlar', 'раненые', 'people injured in a war or battle', 'The wounded were taken to a nearby hospital.', 'Ýaralananlary golaýdaky hassahana äkitdiler.', 'B2'),
    ('ceasefire', '/ˈsiːsfaɪə/', 'N', 'ot açmagy wagtlaýyn bes etmek', 'перемирие', 'an agreement to stop fighting for a period of time', 'The ceasefire lasted for three days.', 'Ot açmagy bes etmek baradaky ylalaşyk üç gün dowam etdi.', 'B2'),
    ('civil war', '/ˌsɪvl ˈwɔː/', 'N', 'raýat urşy', 'гражданская война', 'a war between groups of people in one country', 'The civil war forced thousands of people to flee.', 'Raýat urşy müňlerçe adamy gaçmaga mejbur etdi.', 'B2'),
    ('coup', '/kuː/', 'N', 'döwlet agdarylyşygy', 'государственный переворот', 'a sudden, often violent, attempt to take control of a government', 'The coup changed the country’s leadership overnight.', 'Döwlet agdarylyşygy bir gijede ýurduň ýolbaşçylaryny üýtgetdi.', 'C1'),
    ('rebellion', '/rɪˈbeljən/', 'N', 'gozgalaň', 'восстание', 'an attempt to change a government using force', 'The rebellion spread to several towns.', 'Gozgalaň birnäçe şähere ýaýrady.', 'B2'),
    ('revolution', '/ˌrevəˈluːʃn/', 'N', 'rewolýusiýa', 'революция', 'a major change of government, often made by people', 'The revolution began in the capital.', 'Rewolýusiýa paýtagtda başlandy.', 'B1'),
    ('treaty', '/ˈtriːti/', 'N', 'şertnama', 'договор', 'a formal agreement between countries', 'The two sides signed a peace treaty.', 'Iki tarap parahatçylyk şertnamasyna gol çekdi.', 'B2'),
    ('blow up', '/ˌbləʊ ˈʌp/', 'V', 'partlatmak', 'взорвать', 'to destroy something with an explosion', 'The soldiers blew up the bridge.', 'Esgerler köprini partlatdylar.', 'B1'),
    ('break out', '/ˌbreɪk ˈaʊt/', 'PHR', 'başlamak, duýdansyz ýüze çykmak', 'вспыхнуть, начаться', 'to start suddenly, especially a war, fire, or disease', 'Fighting broke out near the border.', 'Serhediň golaýynda söweş başlandy.', 'B2'),
    ('capture', '/ˈkæptʃə/', 'V', 'tutmak, ýesir almak', 'захватить, пленить', 'to take a person or place by force', 'The army captured the town at dawn.', 'Goşun şäheri daň bilen basyp aldy.', 'B1'),
    ('declare war on', '/dɪˌkleə ˈwɔː ɒn/', 'PHR', '... bilen uruş yglan etmek', 'объявить войну', 'to officially announce that a country will fight another', 'The country declared war on its neighbour.', 'Ýurt goňşusyna uruş yglan etdi.', 'B2'),
    ('execute', '/ˈeksɪkjuːt/', 'V', 'jeza hökmünde öldürmek', 'казнить', 'to kill someone as a legal or political punishment', 'The prisoners were executed after the trial.', 'Kazyýetden soň tussaglary jezalandyryp öldürdiler.', 'B2'),
    ('loot', '/luːt/', 'V', 'talamak', 'грабить', 'to steal things from shops or buildings during trouble', 'The rebels looted several empty shops.', 'Gozgalaňçylar birnäçe boş dükany taladylar.', 'B2'),
    ('overthrow', '/ˌəʊvəˈθrəʊ/', 'V', 'häkimiýetden agdarmak', 'свергнуть', 'to remove a government or leader using force', 'The rebels tried to overthrow the government.', 'Gozgalaňçylar hökümeti agdarmaga synanyşdylar.', 'B2'),
    ('release', '/rɪˈliːs/', 'V', 'boşatmak, goýbermek', 'освободить', 'to allow someone to leave captivity', 'The army released the prisoners on Friday.', 'Goşun tussaglary anna güni boşatdy.', 'B1'),
    ('shell (v.)', '/ʃel/', 'V', 'artilleriýa bilen ok atmak', 'обстреливать', 'to attack a place by firing shells from large guns', 'The army shelled the rebel positions.', 'Goşun gozgalaňçylaryň ýerlerine artilleriýa bilen ok atdy.', 'C1'),
    ('retreat', '/rɪˈtriːt/', 'V', 'yza çekilmek', 'отступать', 'to move back from an enemy or dangerous situation', 'The soldiers retreated across the river.', 'Esgerler derýanyň aňyrsyna yza çekildiler.', 'B2'),
]

# ---- in-lesson 4A — describing books and films ----
T['books_films'] = [
    ('bestseller', '/ˌbestˈselə(r)/', 'N', 'iň köp satylýan kitap', 'бестселлер', 'a book that sells in huge numbers', 'Her novel became a bestseller.', 'Romany iň köp satylýan kitap boldy.', 'A2'),
    ('blockbuster', '/ˈblɒkbʌstə(r)/', 'N', 'uly üstünlikli film', 'блокбастер', 'a very successful film', 'The blockbuster earned millions.', 'Uly üstünlikli film millionlar gazandy.', 'A2'),
    ('cliffhanger', '/ˈklɪfhæŋə(r)/', 'N', 'yzy gyzykly gutarýan', 'захватывающая концовка', 'an ending that leaves you wanting more', 'The series ended on a cliffhanger.', 'Serial yzy gyzykly gutardy.', 'B2'),
    ('gripping', '/ˈɡrɪpɪŋ/', 'ADJ', 'özüne bend edýän', 'захватывающий', 'so exciting you cannot stop', 'It was a gripping thriller.', 'Özüne bend edýän triller boldy.', 'B1'),
    ('masterpiece', '/ˈmɑːstəpiːs/', 'N', 'şedewr', 'шедевр', 'an excellent work of art', 'The painting is a true masterpiece.', 'Surat hakyky şedewr.', 'B1'),
    ('moving', '/ˈmuːvɪŋ/', 'ADJ', 'täsirli (duýgur)', 'трогательный', 'making you feel strong emotions', 'The ending was deeply moving.', 'Soňy örän täsirli boldy.', 'A2'),
    ('sequel', '/ˈsiːkwəl/', 'N', 'dowamy (kitap/film)', 'продолжение, сиквел', 'a story that continues an earlier one', 'The sequel comes out next year.', 'Dowamy indiki ýyl çykýar.', 'A2'),
    ('thriller', '/ˈθrɪlə(r)/', 'N', 'triller', 'триллер', 'an exciting story about crime', 'I love a good thriller.', 'Gowy trilleri gowy görýärin.', 'A2'),
    ('trailer', '/ˈtreɪlə(r)/', 'N', 'film mahabaty', 'трейлер', 'a short advertisement for a film', 'The trailer looks amazing.', 'Film mahabaty ajaýyp görünýär.', 'A2', 'watch a trailer'),
    ('twist', '/twɪst/', 'N', 'garaşylmadyk öwrüm', 'неожиданный поворот', 'a surprising change in a story', 'The final twist shocked everyone.', 'Soňky öwrüm hemmäni şok etdi.', 'B1', 'plot twist'),
]

# ---- Vocabulary Bank — Sounds and the human voice -> 4B ----
T['voice'] = [
    ('accent', '/ˈæksent/', 'N', 'talaffuz (şiwä)', 'акцент', 'a way of speaking from a region', 'She has a beautiful accent.', 'Owadan talaffuzy bar.', 'A2', 'foreign accent'),
    ('echo', '/ˈekəʊ/', 'N', 'ýaň', 'эхо', 'a sound that comes back', 'Our voices made an echo.', 'Seslerimiz ýaň etdi.', 'A2'),
    ('hoarse', '/hɔːs/', 'ADJ', 'ýogyn (sesi ýatyk)', 'охрипший', 'with a rough voice', 'He was hoarse after shouting.', 'Gygyrandan soň sesi ýatyk boldy.', 'B2'),
    ('mumble', '/ˈmʌmbl/', 'V', 'pyşyrdamak (aňsat eşitmezlik)', 'бормотать', 'to speak unclearly and quietly', 'He mumbled an apology.', 'Ötünç sorap pyşyrdady.', 'B2'),
    ('mutter', '/ˈmʌtə(r)/', 'V', 'zöldürdemek', 'ворчать себе под нос', 'to complain quietly under the breath', 'She muttered about the price.', 'Baha barada zöldürdedi.', 'B2'),
    ('scream', '/skriːm/', 'V', 'gygyrmak (gaty)', 'кричать, вопить', 'to make a loud high sound', 'The fans screamed with joy.', 'Janköýerler şatlykdan gygyrdy.', 'A2'),
    ('shout', '/ʃaʊt/', 'V', 'gygyrmak', 'кричать', 'to say something very loudly', 'Do not shout at the children.', 'Çagalara gygyrma.', 'A2', 'shout at'),
    ('sigh', '/saɪ/', 'V', 'ah çekmek', 'вздыхать', 'to breathe out slowly with feeling', 'She sighed with relief.', 'Ýeňillik bilen ah çekdi.', 'A2'),
    ('squeak', '/skwiːk/', 'V', 'çyrlamak (ýuka ses)', 'пищать', 'to make a short high sound', 'The mouse squeaked in the trap.', 'Syçan duzakda çyrlady.', 'B2'),
    ('whisper', '/ˈwɪspə(r)/', 'V', 'pyşyrdamak', 'шептать', 'to speak very quietly', 'She whispered the answer.', 'Jogaby pyşyrdady.', 'A2', 'whisper to'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('bang', '/bæŋ/', 'N', 'güýçli ses, patlama sesi', 'грохот, удар', 'a sudden loud noise', 'We heard a loud bang from the kitchen.', 'Aşhanadan güýçli ses eşitdik.', 'B1'),
    ('buzz', '/bʌz/', 'N', 'jürrüldi, zyňňyldy', 'жужжание', 'a low continuous sound made by an insect or machine', 'A fly made a quiet buzz near the window.', 'Penjiräniň ýanynda siňek ýuwaşja zyňňyldy.', 'B1'),
    ('click', '/klɪk/', 'N', 'çykgyldy', 'щелчок', 'a short sharp sound', 'I heard a click as the door locked.', 'Gapy gulplananda çykgyldy eşitdim.', 'A2'),
    ('creak', '/kriːk/', 'N', 'jygyldy', 'скрип', 'a long high sound made by something moving slowly', 'The old floor made a creak under my feet.', 'Köne pol aýagymyň aşagynda jygyldy etdi.', 'B2'),
    ('crunch', '/krʌntʃ/', 'N', 'harsyldy', 'хруст', 'a loud sound made by something being crushed', 'There was a crunch as he stepped on the dry leaves.', 'Ol gury ýapraklaryň üstüne basanda harsyldy boldy.', 'B2'),
    ('drip', '/drɪp/', 'N', 'damja sesi', 'капание', 'a small drop of liquid or the sound it makes', 'The drip from the tap kept me awake.', 'Kran suwyň damjasy meni uklatmadı.', 'A2'),
    ('hiss', '/hɪs/', 'N', 'sykylyk, sykylyk sesi', 'шипение', 'a long quiet sound like air escaping', 'We heard a hiss as the tyre went flat.', 'Şin boşanda sykylyk eşitdik.', 'B2'),
    ('hoot', '/huːt/', 'N', 'baýguşuň ýa-da ulagyň sesi', 'уханье; гудок', 'a loud call made by an owl or a car horn', 'An owl gave a hoot in the dark.', 'Garaňkyda baýguş uwlady.', 'B2'),
    ('hum', '/hʌm/', 'N', 'pes we üznüksiz ses', 'гудение', 'a low continuous sound', 'The fridge makes a soft hum at night.', 'Sowadyjy gijelerine pes ses çykarýar.', 'B1'),
    ('rattle', '/ˈrætl/', 'N', 'şakyrdy', 'дребезжание', 'a series of short hard sounds', 'The windows gave a rattle in the wind.', 'Ýelde penjireler şakyrdady.', 'B2'),
    ('roar', '/rɔː/', 'N', 'güýçli gürrüldi ýa-da gykylyk', 'рёв, гул', 'a very loud deep sound', 'We heard the roar of an engine outside.', 'Daşarda motoryň gürrüldisini eşitdik.', 'B1'),
    ('screech', '/skriːtʃ/', 'N', 'ýiti gykylyk', 'визг', 'a very high unpleasant sound', 'The brakes made a screech as the bus stopped.', 'Awtobus saklananda tormozlar ýiti ses çykardy.', 'B2'),
    ('slam', '/slæm/', 'N', 'güýçli şarkyldy', 'хлопок', 'a loud sound made by something hitting or closing forcefully', 'The door shut with a slam.', 'Gapy güýçli şarkyldap ýapyldy.', 'B1'),
    ('slurp', '/slɜːp/', 'N', 'şoruldama sesi', 'хлюпанье', 'a noisy sucking sound when drinking or eating', 'I could hear him slurp his soup.', 'Onuň çorba içende şoruldadanyny eşitdim.', 'B2'),
    ('sniff', '/snɪf/', 'N', 'burnuňy çekmegiň sesi', 'шмыганье носом', 'a short breath taken in through the nose', 'She gave a sniff and reached for a tissue.', 'Ol burnuny çekip, salfetka uzatdy.', 'B1'),
    ('snore', '/snɔː/', 'N', 'hor çekmek', 'храп', 'the noisy breathing some people make while sleeping', 'His loud snore kept everyone awake.', 'Onuň gaty hor çekmegi hemmäni uklatmady.', 'B1'),
    ('splash', '/splæʃ/', 'N', 'şapyrdy', 'всплеск', 'the sound or movement of liquid being hit', 'We heard a splash from the swimming pool.', 'Howuzdan şapyrdy eşitdik.', 'A2'),
    ('tap', '/tæp/', 'N', 'ýeňil takyldatmak', 'стук', 'a light repeated sound made by hitting something', 'There was a tap at the window.', 'Penjirä ýeňil takyldatdylar.', 'A2'),
    ('tick', '/tɪk/', 'N', 'sagat sesi', 'тиканье', 'the short regular sound of a clock', 'The tick of the clock was very loud.', 'Sagat sesi örän güýçlüdi.', 'B1'),
    ('whistle', '/ˈwɪsl/', 'N', 'sygylyk sesi', 'свист', 'a high sound made by blowing air through the lips', 'A whistle came from the referee.', 'Araçy sygylyk çaldy.', 'A2'),
    ('giggle', '/ˈɡɪɡl/', 'V', 'jikirdemek', 'хихикать', 'to laugh quietly in a silly or nervous way', 'The children began to giggle during the film.', 'Film wagtynda çagalar jikirdäp başladylar.', 'B1'),
    ('groan', '/ɡrəʊn/', 'V', 'iňňildemek', 'стонать', 'to make a long low sound because you are in pain or annoyed', 'He groaned when he saw the bill.', 'Hasaby görende ol iňňildedi.', 'B1'),
    ('sob', '/sɒb/', 'V', 'hopuklap aglamak', 'рыдать', 'to cry noisily with short breaths', 'She sobbed when she heard the news.', 'Habary eşidende ol hopuklap aglady.', 'B1'),
    ('stammer', '/ˈstæmə/', 'V', 'sakawlap gürlemek', 'заикаться', 'to speak with difficulty, repeating sounds', 'He began to stammer when he felt nervous.', 'Alada galanda ol sakawlap başlady.', 'B2'),
    ('yell', '/jel/', 'V', 'gaty ses bilen gygyrmak', 'кричать', 'to shout loudly, often because you are angry', 'Please do not yell at your brother.', 'Dogaňyza gaty ses bilen gygyrmaň.', 'B1'),
]
# ---- Vocabulary Bank — Expressions with time -> 5A ----
T['time_expr'] = [
    ('ahead of time', '/əˈhed əv taɪm/', 'PHR', 'öňünden', 'заранее', 'earlier than planned', 'We finished ahead of time.', 'Öňünden gutardy.', 'A2'),
    ('behind schedule', '/bɪˈhaɪnd ˈʃedjuːl/', 'PHR', 'meýilnamadan yza galan', 'с опозданием от графика', 'later than planned', 'The project is two weeks behind schedule.', 'Taslama iki hepde yza galdy.', 'B1'),
    ('for the time being', '/fə ðə taɪm ˈbiːɪŋ/', 'PHR', 'häzirlikçe', 'на данный момент', 'for now, but not for ever', 'Stay here for the time being.', 'Häzirlikçe şu ýerde gal.', 'B1'),
    ('in advance', '/ɪn ədˈvɑːns/', 'PHR', 'öňünden (öňünden tölemek)', 'заблаговременно', 'before something happens', 'Book the tickets in advance.', 'Biletleri öňünden bronla.', 'A2', 'pay in advance'),
    ('in no time', '/ɪn nəʊ taɪm/', 'PHR', 'göz açyp ýumasy salymda', 'в мгновение ока', 'very quickly', 'Dinner will be ready in no time.', 'Agşamlyk göz açyp ýumasy salymda taýyn bolar.', 'A2'),
    ('on time', '/ɒn taɪm/', 'PHR', 'wagtynda', 'вовремя', 'at the planned time', 'The train arrived on time.', 'Otluda wagtynda geldi.', 'A1'),
    ('in time', '/ɪn taɪm/', 'PHR', 'wagty ýetip (giç galman)', 'вовремя (успеть)', 'early enough to do something', 'We got there in time for dinner.', 'Agşamlyk nahara wagty ýetip ýetdik.', 'A2', 'in time for'),
    ('time after time', '/taɪm ˈɑːftə taɪm/', 'PHR', 'gaýta-gaýta', 'раз за разом', 'again and again', 'He has warned you time after time.', 'Saňa gaýta-gaýta duýdurdy.', 'B1'),
    ('from time to time', '/frɒm taɪm tuː taɪm/', 'PHR', 'wagtal-wagtal', 'время от времени', 'sometimes, not often', 'We visit them from time to time.', 'Wagtal-wagtal olara baryp görýäris.', 'A2'),
    ('kill time', '/kɪl taɪm/', 'PHR', 'wagt öldürmek', 'коротать время', 'to do something while waiting', 'We killed time at the airport.', 'Howa menzilinde wagt öldürdik.', 'A2'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('make up for lost time', '/ˌmeɪk ˌʌp fə ˌlɒst ˈtaɪm/', 'PHR', 'ýitirilen wagtyň öwezini dolmak', 'наверстать упущенное время', 'to do something faster or more often after a delay', 'After the delay, we drove on to make up for lost time.', 'Gijikmeden soň ýitirilen wagtyň öwezini dolmak üçin tiz sürdük.', 'B2'),
    ('make good time', '/ˌmeɪk ɡʊd ˈtaɪm/', 'PHR', 'ýoly çalt geçmek', 'быстро продвигаться', 'to travel or progress faster than expected', 'We made good time and reached the coast by noon.', 'Ýoly çalt geçip, günortana çenli kenara ýetdik.', 'B2'),
    ('take your time', '/ˌteɪk jɔː ˈtaɪm/', 'PHR', 'howlukmazlyk', 'не торопиться', 'to do something without hurrying', 'Take your time; there is no need to rush.', 'Howlukma, alada etmegiň geregi ýok.', 'A2'),
    ('have a hard time', '/ˌhæv ə hɑːd ˈtaɪm/', 'PHR', 'kynçylyk çekmek', 'тяжело переживать', 'to experience difficulty doing something', 'She had a hard time finding a new job.', 'Täze iş tapmakda ol kynçylyk çekdi.', 'B1'),
    ('run out of time', '/ˌrʌn ˈaʊt əv taɪm/', 'PHR', 'wagtyň gutarmagy', 'не хватить времени', 'to have no time left', 'We ran out of time before the final question.', 'Soňky soraga ýetmän wagtymyz gutardy.', 'B1'),
    ('save time', '/ˌseɪv ˈtaɪm/', 'PHR', 'wagt tygşytlamak', 'сэкономить время', 'to do something in a way that takes less time', 'Using the train will save time.', 'Otly bilen gitmek wagt tygşytlar.', 'A2'),
    ('spare time', '/ˌspeə ˈtaɪm/', 'N', 'boş wagt', 'свободное время', 'time when you are not working or busy', 'I read novels in my spare time.', 'Boş wagtymda roman okaýaryn.', 'A2'),
    ('spend time', '/ˌspend ˈtaɪm/', 'PHR', 'wagt geçirmek', 'проводить время', 'to use time doing something or being somewhere', 'We spent the afternoon at the museum.', 'Günüň ikinji ýarymyny muzeýde geçirdik.', 'A2'),
    ('waste time', '/ˌweɪst ˈtaɪm/', 'PHR', 'wagty biderek geçirmek', 'тратить время впустую', 'to use time without doing anything useful', 'Do not waste time worrying about things you cannot change.', 'Üýtgedip bilmejek zatlaryň barada alada edip wagtyňy biderek geçirme.', 'B1'),
    ('time off', '/ˌtaɪm ˈɒf/', 'N', 'işden rugsat, dynç alyş wagty', 'отгул, свободное время', 'a period when you do not have to work', 'I need a few days off to rest.', 'Dynç almak üçin maňa birnäçe gün rugsat gerek.', 'B1'),
    ('before my time', '/bɪˌfɔː maɪ ˈtaɪm/', 'PHR', 'men ýaşamanka, meniň döwrümden öň', 'до моего времени', 'before the period when you were old enough to know about something', 'That singer was famous before my time.', 'Şol aýdymçy meniň döwrümden öň meşhur eken.', 'B2'),
    ('by the time', '/baɪ ðə ˈtaɪm/', 'CONJ', '...wagta çenli', 'к тому времени как', 'at or before the moment when something happens', 'By the time we arrived, the show had ended.', 'Biz barýançak tomaşa tamam bolupdy.', 'B1'),
    ('behind the times', '/bɪˌhaɪnd ðə ˈtaɪmz/', 'PHR', 'zaman bilen aýakdaş däl', 'отставший от времени', 'old-fashioned and not keeping up with changes', 'The company’s website looks behind the times.', 'Kompaniýanyň saýty zaman bilen aýakdaş däl ýaly.', 'B2'),
    ('one thing at a time', '/ˌwʌn θɪŋ ət ə ˈtaɪm/', 'PHR', 'bir gezekde bir zat', 'по одному делу за раз', 'used to say that you should do things separately', 'Let us deal with one thing at a time.', 'Geliň, bir gezekde bir meselä seredeliň.', 'B1'),
    ("time's up", '/ˌtaɪmz ˈʌp/', 'PHR', 'wagt gutardy', 'время вышло', 'used to say that there is no more time', 'Time’s up; please put down your pens.', 'Wagt gutardy, galamlaryňyzy goýuň.', 'A2'),
    ('short of time', '/ˌʃɔːt əv ˈtaɪm/', 'PHR', 'wagty az', 'не хватать времени', 'not having enough time', 'We are short of time, so let us take a taxi.', 'Wagtymyz az, şonuň üçin taksi alalyň.', 'B1'),
    ('time on your hands', '/ˌtaɪm ɒn jɔː ˈhændz/', 'PHR', 'boş wagtyň köp bolmagy', 'много свободного времени', 'a lot of free time, especially when you do not know what to do', 'Since retiring, he has more time on his hands.', 'Pensiýa çykandan soň onuň boş wagty köpeldi.', 'B2'),
    ('a matter of time', '/ə ˌmætə əv ˈtaɪm/', 'PHR', 'wagtyň meselesi', 'вопрос времени', 'something that will certainly happen sooner or later', 'It is only a matter of time before they find out.', 'Olaryň bilmegi diňe wagtyň meselesi.', 'B2'),
    ('with time to spare', '/wɪð ˌtaɪm tə ˈspeə/', 'PHR', 'wagty ýeterlik bolup', 'имея запас времени', 'with time left after finishing something', 'We reached the station with time to spare.', 'Wokzala ýeterlik wagt galanda ýetdik.', 'B2'),
    ('this time next week', '/ˌðɪs taɪm nekst ˈwiːk/', 'PHR', 'indiki hepde şu wagt', 'в это время на следующей неделе', 'at the same time one week from now', 'This time next week, I will be on holiday.', 'Indiki hepde şu wagt dynç alyşda bolaryn.', 'B1'),
]

# ---- Vocabulary Bank — Money -> 5B ----
T['money2'] = [
    ('bankrupt', '/ˈbæŋkrʌpt/', 'ADJ', 'müflüs', 'банкрот', 'unable to pay your debts', 'The company went bankrupt last year.', 'Kompaniýa geçen ýyl müflüs boldy.', 'B1', 'go bankrupt'),
    ('budget', '/ˈbʌdʒɪt/', 'N', 'büjet', 'бюджет', 'a plan for spending money', 'We are on a tight budget this month.', 'Şu aý büjetimiz gysyk.', 'A2', 'on a budget'),
    ('currency', '/ˈkʌrənsi/', 'N', 'walýuta', 'валюта', 'the money used in a country', 'The local currency is the manat.', 'Ýerli walýuta manat.', 'A2', 'foreign currency'),
    ('debt', '/det/', 'N', 'karz (bergi)', 'долг', 'money that you owe', 'He paid off all his debts.', 'Ähli bergilerini töledi.', 'B1', 'pay off a debt'),
    ('deposit', '/dɪˈpɒzɪt/', 'N', 'depozit (öňünden töleg)', 'залог, депозит', 'part of the money paid first', 'We paid a deposit for the flat.', 'Öý üçin depozit töledik.', 'B1', 'pay a deposit'),
    ('fortune', '/ˈfɔːtʃuːn/', 'N', 'uly baýlyk', 'состояние, состояние денег', 'a very large amount of money', 'The car cost a fortune.', 'Maşyn uly baýlyga durdy.', 'A2', 'cost a fortune'),
    ('income', '/ˈɪnkʌm/', 'N', 'girdeji (aýlyk)', 'доход', 'money received regularly', 'Their income covers all expenses.', 'Girdejileri ähli çykdajylary örtýär.', 'A2', 'monthly income'),
    ('instalment', '/ɪnˈstɔːlmənt/', 'N', 'bölekleýin töleg', 'взнос, рассрочка', 'one part of a total payment', 'We pay the loan in monthly instalments.', 'Karzy aýlyk bölekleýin töleýäris.', 'B2', 'pay in instalments'),
    ('pension', '/ˈpenʃn/', 'N', 'pensiýa (pul)', 'пенсия', 'money paid after retirement', 'Her pension is paid monthly.', 'Pensiýasy aýlyk tölenýär.', 'A2', 'state pension'),
    ('tax', '/tæks/', 'N', 'salyk', 'налог', 'money paid to the government', 'Income tax went up this year.', 'Girdeji salygy şu ýyl galdy.', 'A2', 'pay tax'),
    ('cheque', '/tʃek/', 'N', 'çek', 'чек', 'a paper order to a bank to pay', 'He paid the rent by cheque.', 'Kärendäni çek bilen töledi.', 'A2', 'pay by cheque'),
    ('coin', '/kɔɪn/', 'N', 'teňňe', 'монета', 'a small flat piece of metal money', 'He tossed a coin to decide.', 'Karar bermek üçin teňňe zyňdy.', 'A1'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('donation', '/dəʊˈneɪʃn/', 'N', 'haýyr-sahawat', 'пожертвование', 'money given to help an organization or person', 'They made a donation to the animal charity.', 'Olar haýwan haýyr-sahawat guramasyna pul berdiler.', 'B1'),
    ('fare', '/feə/', 'N', 'ýol puly', 'плата за проезд', 'the money paid for a journey by bus, train, plane, or taxi', 'The bus fare has gone up this year.', 'Şu ýyl awtobus puly ýokarlandy.', 'A2'),
    ('fee', '/fiː/', 'N', 'hyzmat tölegi', 'сбор, гонорар', 'money paid for a professional service', 'The lawyer charged a high fee.', 'Hukukçy ýokary hyzmat tölegini aldy.', 'B1'),
    ('fine', '/faɪn/', 'N', 'jerime', 'штраф', 'money paid as a punishment for breaking a rule', 'She had to pay a fine for parking there.', 'Ol şol ýerde ulag goýandygy üçin jerime tölemeli boldy.', 'A2'),
    ('grant', '/ɡrɑːnt/', 'N', 'maksatly maliýe kömegi', 'грант', 'money given by an organization for a particular purpose', 'The university gave him a research grant.', 'Uniwersitet oňa ylmy barlag üçin grant berdi.', 'B2'),
    ('loan', '/ləʊn/', 'N', 'karz', 'заём', 'money borrowed from a bank or another person', 'They took out a loan to buy a car.', 'Maşyn almak üçin bankdan karz aldylar.', 'A2', 'take out a loan'),
    ('lump sum', '/ˌlʌmp ˈsʌm/', 'N', 'bir gezeklik uly töleg', 'единовременная сумма', 'a single payment of a large amount of money', 'The company paid her a lump sum when she retired.', 'Pensiýa çykanda kompaniýa oňa bir gezeklik uly töleg berdi.', 'B2'),
    ('quote', '/kwəʊt/', 'N', 'bahanyň öňünden hasaby', 'смета, расценка', 'a statement of how much a job or service will cost', 'We asked three builders for a quote.', 'Üç gurluşykçydan işiň bahasyny soradyk.', 'B2', 'ask for a quote'),
    ('will', '/wɪl/', 'N', 'wesýetnama', 'завещание', 'a legal document saying what happens to your money after you die', 'She left the house to her son in her will.', 'Ol wesýetnamasynda jaýyny ogluna galdyrdy.', 'B2', 'make a will'),
    ('consumer society', '/kənˌsjuːmə səˈsaɪəti/', 'N', 'sarp ediş jemgyýeti', 'общество потребления', 'a society where buying goods is very important', 'Many people feel that we live in a consumer society.', 'Köp adam sarp ediş jemgyýetinde ýaşaýarys diýip hasaplaýar.', 'B2'),
    ('standard of living', '/ˌstændəd əv ˈlɪvɪŋ/', 'N', 'ýaşaýyş derejesi', 'уровень жизни', 'the amount of money and comfort people have', 'The standard of living has improved in the region.', 'Sebitde ýaşaýyş derejesi ýokarlandy.', 'B2'),
    ('cost of living', '/ˌkɒst əv ˈlɪvɪŋ/', 'N', 'ýaşaýyş çykdajylary', 'стоимость жизни', 'the money needed for basic things such as food and housing', 'The cost of living is higher in the capital.', 'Paýtagtda ýaşaýyş çykdajylary has ýokary.', 'B2'),
    ('inflation', '/ɪnˈfleɪʃn/', 'N', 'hümmetsizlenme', 'инфляция', 'a general rise in prices over time', 'Inflation has made food more expensive.', 'Hümmetsizlenme azyk önümlerini gymmatlatdy.', 'B1'),
    ('online banking', '/ˌɒnlaɪn ˈbæŋkɪŋ/', 'N', 'internet arkaly bank hyzmaty', 'интернет-банкинг', 'using a bank’s website or app to manage money', 'Online banking lets me pay bills at home.', 'Internet arkaly bank hyzmaty öýde oturyp töleg etmäge mümkinçilik berýär.', 'B1'),
    ('balance', '/ˈbæləns/', 'N', 'hasapdaky galyndy', 'остаток на счёте', 'the amount of money in a bank account', 'I checked my account balance on my phone.', 'Telefonymdan bank hasabymdaky galyndyny barladym.', 'A2', 'bank balance'),
    ('bank transfer', '/ˈbæŋk ˌtrænsfɜː/', 'N', 'bank arkaly pul geçirmek', 'банковский перевод', 'an electronic movement of money between bank accounts', 'I paid the rent by bank transfer.', 'Kärendäni bank arkaly pul geçirip töledim.', 'B1'),
    ('interest rate', '/ˈɪntrəst reɪt/', 'N', 'göterim derejesi', 'процентная ставка', 'the percentage charged for borrowing money or paid on savings', 'The bank lowered its interest rate.', 'Bank göterim derejesini peseltdi.', 'B2'),
    ('mortgage', '/ˈmɔːɡɪdʒ/', 'N', 'ipoteka', 'ипотека', 'a loan used to buy a house or flat', 'They got a mortgage to buy their first home.', 'Ilkinji öýlerini almak üçin ipoteka karzyny aldylar.', 'B1', 'take out a mortgage'),
    ('share', '/ʃeə/', 'N', 'paý, aksiýa', 'акция', 'one of the parts into which a company is divided', 'She bought shares in a technology company.', 'Ol tehnologiýa kompaniýasynyň paýnamalaryny satyn aldy.', 'B1', 'buy shares'),
    ('stock market', '/ˈstɒk ˌmɑːkɪt/', 'N', 'gymmatly kagyzlar bazary', 'фондовый рынок', 'a place or system for buying and selling company shares', 'The stock market fell after the announcement.', 'Yglan edilenden soň gymmatly kagyzlar bazary pese düşdi.', 'B2'),
    ('exchange rate', '/ɪksˈtʃeɪndʒ reɪt/', 'N', 'walýuta hümmeti', 'обменный курс', 'the value of one currency compared with another', 'The exchange rate changes every day.', 'Walýuta hümmeti her gün üýtgeýär.', 'B1'),
    ('recession', '/rɪˈseʃn/', 'N', 'ykdysady pese gaçyş', 'рецессия', 'a period when a country’s economy becomes weaker', 'Several small firms closed during the recession.', 'Ykdysady pese gaçyş döwründe birnäçe kiçi kärhana ýapyldy.', 'B2'),
    ('affluent', '/ˈæfluənt/', 'ADJ', 'baý, üpjün', 'состоятельный', 'having a lot of money and a high standard of living', 'The affluent neighbourhood has expensive houses.', 'Baý etrapda gymmat jaýlar bar.', 'C1'),
    ('loaded', '/ˈləʊdɪd/', 'ADJ', 'örän baý', 'богатый (разг.)', 'having a lot of money; informal', 'He must be loaded if he can afford that yacht.', 'Şol ýahtany alyp bilýän bolsa, ol örän baý bolmaly.', 'B2'),
    ('wealthy', '/ˈwelθi/', 'ADJ', 'baý', 'богатый', 'having a lot of money or valuable possessions', 'The wealthy couple donated money to the museum.', 'Baý är-aýal muzeýe pul bagyşlady.', 'B1'),
    ('broke', '/brəʊk/', 'ADJ', 'pulsuz', 'без денег', 'having no money, especially for a short time', 'I cannot go out tonight; I am completely broke.', 'Şu gün agşam daşary çykyp bilemok, pulum ýok.', 'B1'),
    ('hard up', '/ˌhɑːd ˈʌp/', 'ADJ', 'pul taýdan kynçylyk çekýän', 'испытывающий нехватку денег', 'having very little money', 'They were hard up after paying the rent.', 'Kärendäni tölänlerinden soň pul taýdan kynçylyk çekdiler.', 'B2'),
    ('penniless', '/ˈpeniləs/', 'ADJ', 'teňňesiz, düýbünden pulsuz', 'без гроша', 'having no money at all', 'He arrived in the city penniless.', 'Ol şähere düýbünden pulsuz geldi.', 'B2'),
    ('grand', '/ɡrænd/', 'N', 'müň dollar ýa-da funt (gepleşikde)', 'тысяча (разг.)', 'one thousand pounds or dollars; informal', 'The old car cost three grand.', 'Köne ulag üç müň funt tutdy.', 'B2'),
    ('buck', '/bʌk/', 'N', 'dollar (gepleşikde)', 'доллар (разг.)', 'a dollar; informal', 'The ticket costs ten bucks.', 'Bilet on dollar tutýar.', 'B1'),
    ('quid', '/kwɪd/', 'N', 'funt sterling (gepleşikde)', 'фунт стерлингов (разг.)', 'a pound sterling; informal British English', 'I bought the book for five quid.', 'Kitaby bäş funt sterlinge aldym.', 'B1'),
    ('fiver', '/ˈfaɪvə/', 'N', 'bäş funtlyk kagyz pul', 'пятёрка (банкнота)', 'a five-pound note; informal British English', 'Could you lend me a fiver?', 'Maňa bäş funtlyk karz berip bilersiňmi?', 'B2'),
    ('tenner', '/ˈtenə/', 'N', 'on funtlyk kagyz pul', 'десятка (банкнота)', 'a ten-pound note; informal British English', 'I found a tenner in my coat pocket.', 'Paltomyň jübüsinden on funtlyk tapdym.', 'B2'),
]

# ---- in-lesson 6A — compound adjectives ----
T['compound_adjs2'] = [
    ('absent-minded', '/ˌæbsnt ˈmaɪndɪd/', 'ADJ', 'ünsüz (huşsuz)', 'рассеянный', 'often forgetting things', 'The absent-minded professor lost his keys.', 'Ünsüz professor açarlaryny ýitirdi.', 'B1'),
    ('broad-minded', '/ˌbrɔːd ˈmaɪndɪd/', 'ADJ', 'giň pikirli', 'широко мыслящий', 'accepting different opinions', 'Her broad-minded parents welcomed everyone.', 'Giň pikirli ene-atasy hemmäni garşylady.', 'B2'),
    ('deep-fried', '/ˌdiːp ˈfraɪd/', 'ADJ', 'ýagda gowrulan', 'жаренный во фритюре', 'cooked in deep hot oil', 'Deep-fried food is not healthy.', 'Ýagda gowrulan nahar peýdaly däl.', 'B1'),
    ('first-class', '/ˌfɜːst ˈklɑːs/', 'ADJ', 'birinji derejeli', 'первоклассный', 'of the best quality', 'We travelled first-class to London.', 'Londona birinji derejeli gatnadyk.', 'A2'),
    ('hard-working', '/ˌhɑːd ˈwɜːkɪŋ/', 'ADJ', 'zähmetsöýer', 'трудолюбивый', 'putting a lot of effort into work', 'She is an honest, hard-working student.', 'Dogruçyl, zähmetsöýer talyp.', 'A2'),
    ('ill-mannered', '/ˌɪl ˈmænəd/', 'ADJ', 'edebsiz', 'невоспитанный', 'having bad manners', 'The ill-mannered guest interrupted everyone.', 'Edebsiz myhman hemmäniň sözünü kesdi.', 'B2'),
    ('short-sighted', '/ˌʃɔːt ˈsaɪtɪd/', 'ADJ', 'uzagy görmeyän', 'близорукий; недальновидный', 'unable to see far, or not planning ahead', 'It was a short-sighted decision.', 'Uzagy görmeyän karar boldy.', 'B2'),
    ('well-behaved', '/ˌwel bɪˈheɪvd/', 'ADJ', 'edeply', 'воспитанный (о поведении)', 'behaving politely', 'The well-behaved children sat quietly.', 'Edepli çagalar sessiz otyrdy.', 'B1'),
    ('well-dressed', '/ˌwel ˈdrest/', 'ADJ', 'oňat geýnen', 'хорошо одетый', 'wearing nice clothes', 'The well-dressed guests arrived at eight.', 'Oňat geýnen myhmanlar sekizde geldi.', 'A2'),
    ('well-off', '/ˌwel ˈɒf/', 'ADJ', 'halatly (baý)', 'состоятельный', 'having plenty of money', 'Her well-off family helped with the fees.', 'Halatly maşgalasy töleglere kömek etdi.', 'B1'),
    ('time-consuming', '/ˌtaɪm kənˈsjuːmɪŋ/', 'ADJ', 'wagt talap edýän', 'трудоёмкий', 'taking a lot of time', 'Sorting photos is time-consuming.', 'Suratlary tertiplemek wagt talap edýän iş.', 'B2'),
    ('mouth-watering', '/ˌmaʊθ ˈwɔːtərɪŋ/', 'ADJ', 'agyz suwardyjy', 'аппетитный', 'looking or smelling delicious', 'The cake looked mouth-watering.', 'Tort agyz suwardyjy görünýärdi.', 'B2'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('air-conditioned', '/ˌeə kənˈdɪʃnd/', 'ADJ', 'howasy sowadyjy enjamly', 'с кондиционером', 'cooled by a machine that controls the air temperature', 'We waited in an air-conditioned room.', 'Biz howasy sowadyjy enjamly otagda garaşdyk.', 'B1'),
    ('narrow-minded', '/ˌnærəʊ ˈmaɪndɪd/', 'ADJ', 'dar düşünjeli', 'ограниченный', 'unwilling to accept new or different ideas', 'His narrow-minded attitude surprised me.', 'Onuň dar düşünjeli garaýşy meni geň galdyrdy.', 'B2'),
    ('old-fashioned', '/ˌəʊld ˈfæʃnd/', 'ADJ', 'köneçe', 'старомодный', 'not modern or no longer popular', 'They live in an old-fashioned house.', 'Olar köneçe jaýda ýaşaýarlar.', 'A2'),
    ('high-risk', '/ˌhaɪ ˈrɪsk/', 'ADJ', 'ýokary töwekgelçilikli', 'высокорискованный', 'involving a strong possibility of danger or failure', 'Climbing without a guide is a high-risk activity.', 'Ýolbaşçysyz dyrmaşmak ýokary töwekgelçilikli iş.', 'B2'),
    ('second-hand', '/ˌsekənd ˈhænd/', 'ADJ', 'ulanylan, ikinji el', 'подержанный', 'owned by someone else before you buy it', 'She bought a second-hand bicycle.', 'Ol ulanylan welosiped satyn aldy.', 'A2'),
    ('home-made', '/ˌhəʊm ˈmeɪd/', 'ADJ', 'öýde taýýarlanan', 'домашний', 'made at home rather than in a factory or restaurant', 'We had home-made soup for lunch.', 'Günortan öýde taýýarlanan çorba içdik.', 'A2'),
    ('self-conscious', '/ˌself ˈkɒnʃəs/', 'ADJ', 'özüni oňaýsyz duýýan', 'стесняющийся', 'nervous or embarrassed about what other people think of you', 'He feels self-conscious when people take photos.', 'Adamlar surat alanda ol özüni oňaýsyz duýýar.', 'B2'),
    ('last-minute', '/ˌlɑːst ˈmɪnɪt/', 'ADJ', 'iň soňky pursatdaky', 'в последнюю минуту', 'happening or done just before it is too late', 'We made a last-minute change to the plan.', 'Meýilnama iň soňky pursatda üýtgeşme girizdik.', 'B2'),
    ('worn-out', '/ˌwɔːn ˈaʊt/', 'ADJ', 'könelip ýyrtylan; örän ýadaw', 'изношенный; измученный', 'damaged by long use, or extremely tired', 'He wore worn-out jeans to the concert.', 'Ol konserte könelip ýyrtylan jins geýdi.', 'B1'),
    ('eco-friendly', '/ˌiːkəʊ ˈfrendli/', 'ADJ', 'tebigata zyýansyz', 'экологичный', 'designed to cause little or no damage to the environment', 'We use eco-friendly cleaning products.', 'Biz tebigata zyýansyz arassalaýjy önümleri ulanýarys.', 'B2'),
    ('extra-curricular', '/ˌekstrəkəˈrɪkjələ/', 'ADJ', 'sapakdan daşary', 'внеклассный', 'organized by a school but not part of normal lessons', 'She joined an extra-curricular drama club.', 'Ol sapakdan daşary drama gurnagyna goşuldy.', 'C1'),
    ('feel-good', '/ˈfiːl ɡʊd/', 'ADJ', 'keýpi göterýän', 'жизнеутверждающий', 'making you feel happy and positive', 'We watched a feel-good film together.', 'Biz bilelikde keýp göterýän filme tomaşa etdik.', 'B2'),
    ('groundbreaking', '/ˈɡraʊndbreɪkɪŋ/', 'ADJ', 'täze ýol açýan', 'новаторский', 'new and important, changing the way something is done', 'The scientist published groundbreaking research.', 'Alym täze ýol açýan barlagyny çap etdi.', 'C1'),
    ('high-heeled', '/ˌhaɪ ˈhiːld/', 'ADJ', 'beýik ökjeli', 'на высоком каблуке', 'having shoes with tall heels', 'She wore high-heeled shoes to the ceremony.', 'Ol dabara beýik ökjeli aýakgap geýdi.', 'B1'),
    ('high-pitched', '/ˌhaɪ ˈpɪtʃt/', 'ADJ', 'ýiti, inçe sesli', 'высокий (о звуке)', 'having a very high sound', 'A high-pitched alarm woke the baby.', 'Ýiti sesli duýduryş çagany oýardy.', 'B2'),
    ('labour-saving', '/ˈleɪbə ˌseɪvɪŋ/', 'ADJ', 'zähmeti ýeňilleşdirýän', 'трудосберегающий', 'reducing the amount of work needed', 'A dishwasher is a useful labour-saving device.', 'Gap-gaç ýuwujy enjam zähmeti ýeňilleşdirýän peýdaly enjamdyr.', 'B2'),
    ('life-changing', '/ˈlaɪf ˌtʃeɪndʒɪŋ/', 'ADJ', 'durmuşy üýtgedýän', 'меняющий жизнь', 'having a very great effect on someone’s life', 'Moving to another country was life-changing.', 'Başga ýurda göçmek durmuşymy düýpli üýtgetdi.', 'B2'),
    ('low-cost', '/ˌləʊ ˈkɒst/', 'ADJ', 'arzan bahaly', 'недорогой', 'available for a low price', 'Low-cost airlines have made travel easier.', 'Arzan bahaly awiakompaniýalar syýahaty aňsatlaşdyrdy.', 'B1'),
]

# ---- in-lesson 6B — phones and technology ----
T['phones_tech'] = [
    ('backup', '/ˈbækʌp/', 'N', 'ätiýaç nusga', 'резервная копия', 'a copy of data kept safe', 'Always make a backup of your files.', 'Faýllaryňyzyň ätiýaç nusgasyny hemişe ediň.', 'A2', 'make a backup'),
    ('browser', '/ˈbraʊzə(r)/', 'N', 'brauzer', 'браузер', 'a program for using the internet', 'Open the browser and type the address.', 'Brauzeri açyň we salgyny ýazyň.', 'A2', 'web browser'),
    ('crash', '/kræʃ/', 'V', 'işlemez bolmak', 'зависать, падать (о программе)', 'to stop working suddenly', 'My computer crashed twice today.', 'Kompýuterim şu gün iki gezek işlemez boldy.', 'A2'),
    ('gadget', '/ˈɡædʒɪt/', 'N', 'enjamjagaz (gajet)', 'гаджет', 'a small clever device', 'He loves the latest gadgets.', 'Iň täze gajetleri gowy görýär.', 'B1', 'electronic gadget'),
    ('glitch', '/ɡlɪtʃ/', 'N', 'kiçi näsazlyk', 'мелкий сбой', 'a small technical problem', 'A glitch delayed the update.', 'Kiçi näsazlyk täzelenmäni giçikdirdi.', 'B2'),
    ('network', '/ˈnetwɜːk/', 'N', 'tor', 'сеть', 'a system of connected computers', 'The network is down again.', 'Tor ýene işlemeýär.', 'A2', 'mobile network'),
    ('notification', '/ˌnəʊtɪfɪˈkeɪʃn/', 'N', 'habarnama', 'уведомление', 'a message telling you something', 'Turn off the notifications.', 'Habarnamalary öçür.', 'A2', 'push notification'),
    ('password', '/ˈpɑːswɜːd/', 'N', 'açarsöz', 'пароль', 'a secret word to enter a system', 'Never share your password.', 'Açarsözüňizi hiç wagt paýlaşmaň.', 'A1', 'change your password'),
    ('software', '/ˈsɒftweə(r)/', 'N', 'programma üpjünçiligi', 'программное обеспечение', 'programs that run on computers', 'The software needs an update.', 'Programma üpjünçiligi täzelenmeli.', 'A2', 'install software'),
    ('spam', '/spæm/', 'N', 'islenmeýän hatlar', 'спам', 'unwanted email messages', 'My inbox is full of spam.', 'Poçta gutym islenmeýän hatlardan doly.', 'A2', 'spam email'),
    ('update', '/ˈʌpdeɪt/', 'V', 'täzelemek', 'обновлять', 'to make software newer', 'Update the app before the trip.', 'Syýahatdan öň programmany täzeläň.', 'A2', 'software update'),
    ('virus', '/ˈvaɪrəs/', 'N', 'wirus', 'вирус (компьютерный)', 'a program that damages computers', 'A virus deleted all my files.', 'Wirus ähli faýllarymy pozdy.', 'A2', 'computer virus'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('screen', '/skriːn/', 'N', 'ekran', 'экран', 'the flat surface on a phone, computer, or television', 'The screen is difficult to read in sunlight.', 'Gün şöhlesinde ekrany okamak kyn.', 'A1'),
    ('touch screen', '/ˈtʌtʃ skriːn/', 'N', 'sensorly ekran', 'сенсорный экран', 'a screen that responds when you touch it', 'You can open the map by tapping the touch screen.', 'Sensorly ekrana basyp kartany açyp bilersiňiz.', 'B1'),
    ('keypad', '/ˈkiːpæd/', 'N', 'düwmeli panel', 'клавиатура с кнопками', 'a small set of buttons used to operate a device', 'Enter your code on the phone keypad.', 'Kody telefon düwmeli paneline giriziň.', 'B1'),
    ('keyboard', '/ˈkiːbɔːd/', 'N', 'klawiatura', 'клавиатура', 'the set of keys used for typing on a computer or device', 'I prefer typing on a physical keyboard.', 'Men hakyky klawiaturada ýazmagy halaýaryn.', 'A2'),
    ('passcode', '/ˈpɑːskəʊd/', 'N', 'giriş kody', 'код доступа', 'a secret set of numbers used to unlock a device', 'You need a passcode to unlock the tablet.', 'Planşeti açmak üçin giriş kody gerek.', 'B1'),
    ('contact', '/ˈkɒntækt/', 'N', 'telefon sanawyda saklanan adam', 'контакт', 'a person’s name and details stored on a phone or computer', 'I saved the new client as a contact.', 'Täze müşderini telefon sanawyna goşdum.', 'A2'),
    ('settings', '/ˈsetɪŋz/', 'N', 'sazlamalar', 'настройки', 'the choices that control how a device or program works', 'Change the sound settings on your phone.', 'Telefonyň ses sazlamalaryny üýtget.', 'A2'),
    ('broadband', '/ˈbrɔːdbænd/', 'N', 'ýokary tizlikli internet', 'широкополосный интернет', 'a fast connection to the internet', 'We switched to faster broadband last month.', 'Geçen aý has çalt internet birikmesine geçdik.', 'B1'),
    ('wi-fi', '/ˈwaɪfaɪ/', 'N', 'wi-fi, simsiz internet', 'вай-фай', 'a way of connecting to the internet without wires', 'The café offers free wi-fi.', 'Kafede mugt wi-fi bar.', 'A2'),
    ('pop-up', '/ˈpɒp ʌp/', 'N', 'ekranda öz-özünden açylýan penjire', 'всплывающее окно', 'a window that suddenly appears on a computer screen', 'A pop-up appeared while I was reading the article.', 'Makala okaýarkam ekranda penjire peýda boldy.', 'B2'),
    ('coverage', '/ˈkʌvərɪdʒ/', 'N', 'aragatnaşyk elýeterliligi', 'зона покрытия', 'the area where a phone or internet signal is available', 'Mobile coverage is weak in this valley.', 'Bu jülgede telefon aragatnaşygy gowşak.', 'B1'),
    ('signal', '/ˈsɪɡnəl/', 'N', 'signal', 'сигнал', 'the waves or information sent to a phone or device', 'I cannot get a mobile signal inside this building.', 'Bu binanyň içinde mobil signal alyp bilemok.', 'A2'),
    ('download', '/ˌdaʊnˈləʊd/', 'V', 'internetden ýükläp almak', 'скачивать', 'to copy a file from the internet to your device', 'You can download the guide as a PDF.', 'Gollanmany PDF görnüşinde ýükläp alyp bilersiňiz.', 'A2'),
    ('stream', '/striːm/', 'V', 'internet arkaly göni diňlemek ýa-da görmek', 'смотреть или слушать онлайн', 'to play audio or video over the internet without saving it first', 'We streamed the concert on the train.', 'Otlyda konserti internet arkaly gördük.', 'B1'),
    ('scroll', '/skrəʊl/', 'V', 'ekranda ýokary-aşak süýşürmek', 'прокручивать', 'to move text or images up or down on a screen', 'Scroll down to see the rest of the page.', 'Sahypanyň galanyny görmek üçin aşak süýşür.', 'A2'),
    ('swipe', '/swaɪp/', 'V', 'barmak bilen ekranda süýşürmek', 'проводить пальцем по экрану', 'to move your finger quickly across a touch screen', 'Swipe left to see the next photo.', 'Indiki suraty görmek üçin barmagyňy çepe süýşür.', 'B1'),
    ('hang up', '/ˌhæŋ ˈʌp/', 'PHR', 'jaňy kesmek', 'повесить трубку', 'to end a telephone call', 'She said goodbye and hung up.', 'Ol hoşlaşyp, jaňy kesdi.', 'A2'),
    ('top up', '/ˌtɒp ˈʌp/', 'PHR', 'hasabyňy ýa-da telefonyňy doldurmak', 'пополнить баланс', 'to add more money or credit to a phone account', 'I need to top up my phone before the trip.', 'Syýahatdan öň telefonymyň hasabyny doldurmaly.', 'B1'),
    ('put through', '/ˌpʊt ˈθruː/', 'PHR', 'jaňy gerekli adama birikdirmek', 'соединить по телефону', 'to connect someone by telephone to the person they want', 'Could you put me through to the sales department?', 'Meni satuw bölümine birikdirip bilersiňizmi?', 'B2'),
    ('get through to', '/ˌɡet ˈθruː tuː/', 'PHR', 'düşündirip başarmak; telefon arkaly habarlaşmak', 'достучаться до кого-либо; дозвониться до кого-либо', 'to make someone understand you, or to succeed in speaking to someone by phone', 'It’s impossible to get through to my son about his studies, and I still can’t get through to the doctor by phone.', 'Ogluma okuw barada düşündirip bilemok, lukmana hem telefon arkaly jaň edip bilemok.', 'B2', 'get through to someone; get through to a doctor by phone'),
    ('switch off', '/ˌswɪtʃ ˈɒf/', 'PHR', 'öçürmek', 'выключить', 'to turn off a device', 'Please switch off your phone during the meeting.', 'Maslahat wagtynda telefonyňyzy öçüriň.', 'A2'),
    ('unplug', '/ʌnˈplʌɡ/', 'V', 'tokdan aýyrmak', 'отключить от сети', 'to disconnect a device from its power supply', 'Unplug the charger when the battery is full.', 'Batareýa dolanda zarýad berijini tokdan aýyr.', 'B1'),
]


# ---- in-lesson 6B — adjectives + prepositions ----
T['adjectives_preps'] = [
    ('obsessed with', '/əbˈsest wɪð/', 'PHR', '... bilen aşa gyzyklanýan', 'одержимый чем-либо', 'thinking about something all the time in an unhealthy way', 'He is obsessed with online games.', 'Ol internet oýunlaryna aşa berlen.', 'B2'),
    ('addicted to', '/əˈdɪktɪd tuː/', 'PHR', '... endik eden, garaşly', 'зависимый от', 'unable to stop using or doing something harmful', 'She is addicted to social media.', 'Ol sosial ulgamlara garaşly.', 'B2'),
    ('hooked on', '/ˈhʊkt ɒn/', 'PHR', '... endik eden', 'подсевший на', 'very interested in something and unable to stop', 'My brother is hooked on video games.', 'Doganım wideo oýunlaryna endik eden.', 'B2'),
    ('mad about', '/ˈmæd əˌbaʊt/', 'PHR', '... örän halaýan', 'без ума от', 'very enthusiastic about something', 'She is mad about football.', 'Ol futboly örän gowy görýär.', 'B1'),
    ('dependent on', '/dɪˈpendənt ɒn/', 'PHR', '... garaşly', 'зависимый от', 'needing or relying on someone or something', 'Many people are dependent on their phones.', 'Köp adam telefonlaryna garaşly.', 'B1'),
    ('fed up with', '/ˌfed ˈʌp wɪð/', 'PHR', '... ýadamak, bizar bolmak', 'сытый по горло', 'annoyed or bored because something has continued too long', 'I am fed up with all the traffic noise.', 'Ulag seslerinden bizar boldum.', 'B1'),
    ('open to', '/ˈəʊpən tuː/', 'PHR', '... kabul etmäge taýýar', 'открытый к', 'willing to consider new ideas or suggestions', 'Our manager is open to new ideas.', 'Ýolbaşçymyz täze pikirleri kabul etmäge taýýar.', 'B1'),
    ('sick of', '/ˈsɪk əv/', 'PHR', '... bizar bolmak', 'устать от', 'annoyed or bored with something', 'She is sick of hearing the same excuse.', 'Ol şol bir bahanany eşitmekden bizar boldy.', 'B1'),
    ('aware of', '/əˈweə əv/', 'PHR', '... habarly', 'осведомлённый о', 'knowing that something exists or is happening', 'Are you aware of the risks?', 'Töwekgelçiliklerden habaryň barmy?', 'B1'),
    ('keen on', '/ˈkiːn ɒn/', 'PHR', '... halaýan, höwesli', 'увлекающийся', 'very interested in or enthusiastic about something', 'He is keen on getting married abroad.', 'Ol daşary ýurtda öýlenmäge höwesli.', 'B1'),
    ('unsuitable for', '/ʌnˈsuːtəbl fɔː/', 'PHR', '... üçin laýyk däl', 'неподходящий для', 'not right or appropriate for a particular purpose', 'The film is unsuitable for young children.', 'Film kiçi çagalar üçin laýyk däl.', 'B1'),
    ('suspicious of', '/səˈspɪʃəs əv/', 'PHR', '... şübhelenýän', 'подозрительный к', 'thinking that someone may be dishonest or harmful', 'They were suspicious of the new offer.', 'Olar täze teklipden şübhelendiler.', 'B2'),
    ('dissatisfied with', '/dɪsˈsætɪsfaɪd wɪð/', 'PHR', '... kanagatlanmaýan', 'недовольный', 'not pleased with someone or something', 'Customers were dissatisfied with the service.', 'Müşderiler hyzmatdan kanagatlanmadylar.', 'B2'),
    ('accustomed to', '/əˈkʌstəmd tuː/', 'PHR', '... öwrenişen', 'привыкший к', 'familiar with something because you have experienced it often', 'People are becoming accustomed to working online.', 'Adamlar internet arkaly işlemäge öwrenişýärler.', 'B2'),
    ('attached to', '/əˈtætʃt tuː/', 'PHR', '... berk bagly', 'привязанный к', 'feeling strong affection for someone or something', 'She is very attached to her old car.', 'Ol köne ulagyna berk bagly.', 'B2'),
]

# ---- Vocabulary Bank — Prefixes -> 7A ----
T['prefixes'] = [
    ('antisocial', '/ˌæntiˈsəʊʃl/', 'ADJ', 'jemgyýete garşy', 'антисоциальный', 'avoiding other people', 'Staying home every night seems antisocial.', 'Her agşam öýde galmak jemgyýete garşy görünýär.', 'B1'),
    ('co-founder', '/ˌkəʊ ˈfaʊndə(r)/', 'N', 'bilelikde esaslandyryjy', 'сооснователь', 'a person who starts a company with others', 'She is the co-founder of the app.', 'Programmanyň bilelikde esaslandyryjysy.', 'B2'),
    ('counter-attack', '/ˌkaʊntər əˈtæk/', 'N', 'jogap hüjümi', 'контратака', 'an attack in reply to another', 'The team scored on a counter-attack.', 'Topar jogap hüjüminde utuk gazandy.', 'B2'),
    ('devalue', '/ˌdiːˈvæljuː/', 'V', 'bahasyny gaçyrmak', 'обесценивать', 'to reduce the value of something', 'The currency was devalued.', 'Walýutanyň bahasy gaçyryldy.', 'B2'),
    ('extraordinary', '/ɪkˈstrɔːdnri/', 'ADJ', 'adatdan daşary', 'необычайный', 'very unusual and impressive', 'She has an extraordinary memory.', 'Adatdan daşary ýady bar.', 'A2'),
    ('forearm', '/ˈfɔːrɑːm/', 'N', 'baldyr (el)', 'предплечье', 'the part of the arm below the elbow', 'He tattooed his forearm.', 'Eliniň baldyryna nakgaş etdirdi.', 'B1'),
    ('international', '/ˌɪntəˈnæʃnəl/', 'ADJ', 'halkara', 'международный', 'involving several countries', 'The airport handles international flights.', 'Howa menzili halkara uçuşlary kabul edýär.', 'A2'),
    ('multimedia', '/ˌmʌltiˈmiːdiə/', 'N', 'multimedia', 'мультимедиа', 'using sound, video and text together', 'The lesson used multimedia tools.', 'Sapak multimedia gurallaryny ulandy.', 'B1'),
    ('nonstop', '/ˌnɒnˈstɒp/', 'ADV', 'tohtamanzyn (fasylasysyz)', 'безостановочно', 'without stopping', 'We flew nonstop to Ashgabat.', 'Aşgabada tohtamanzyn uçduk.', 'A2'),
    ('postgraduate', '/ˌpəʊstˈɡrædʒuət/', 'N', 'aspirant', 'аспирант', 'a student studying after a degree', 'She is a postgraduate in physics.', 'Fizika boýunça aspirant.', 'B2'),
    ('preview', '/ˈpriːvjuː/', 'N', 'öňünden görkezme', 'предварительный просмотр', 'an early look at something', 'We saw a preview of the film.', 'Filmiň öňünden görkezmesini gördük.', 'A2', 'sneak preview'),
    ('semicircle', '/ˈsemisɜːkl/', 'N', 'ýarym tegelek', 'полукруг', 'half of a circle', 'The chairs stood in a semicircle.', 'Stullar ýarym tegelek bolup durdy.', 'B1'),
    ('transfer', '/trænsˈfɜː(r)/', 'V', 'geçirmek', 'переводить, перемещать', 'to move from one place to another', 'He transferred to another department.', 'Başga bölüme geçdi.', 'A2', 'transfer money'),
    ('underwear', '/ˈʌndəweə(r)/', 'N', 'içki geýim', 'нижнее бельё', 'clothes worn under other clothes', 'Pack some clean underwear.', 'Arassa içki geýim ýygnap goý.', 'A2'),
    ('upgrade', '/ˈʌpɡreɪd/', 'V', 'gowulandyrmak (täzelemek)', 'модернизировать', 'to improve to a better version', 'They upgraded our hotel room.', 'Myhmanhana otagymyzy gowulandyrdylar.', 'A2', 'upgrade to'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('disagree', '/ˌdɪsəˈɡriː/', 'V', 'razy bolmazlyk', 'не соглашаться', 'to have a different opinion', 'I disagree with the final point.', 'Soňky pikir bilen razylaşamok.', 'A2', 'disagree with'),
    ('inappropriate', '/ˌɪnəˈprəʊpriət/', 'ADJ', 'laýyksyz, ýerliksiz', 'неподходящий', 'not suitable for a particular situation', 'That joke was inappropriate for a work meeting.', 'Şol degişme iş maslahatyna ýerliksizdi.', 'B2'),
    ('unattractive', '/ˌʌnəˈtræktɪv/', 'ADJ', 'özüne çekiji däl', 'непривлекательный', 'not pleasant or interesting to look at', 'The building looks unattractive from the outside.', 'Bina daşyndan özüne çekiji däl görünýär.', 'B1'),
    ('incapable', '/ɪnˈkeɪpəbl/', 'ADJ', 'başarmaýan', 'неспособный', 'not able to do something', 'The old computer is incapable of running this program.', 'Köne kompýuter bu programmany işletmäge ukypsyz.', 'B2', 'incapable of'),
    ('incoherent', '/ˌɪnkəʊˈhɪərənt/', 'ADJ', 'manysy düşnüksiz', 'несвязный', 'not expressed clearly or logically', 'His explanation was confused and incoherent.', 'Onuň düşündirişi bulaşyk we düşnüksiz boldy.', 'C1'),
    ('incompetent', '/ɪnˈkɒmpɪtənt/', 'ADJ', 'başarnyksyz', 'некомпетентный', 'not having the ability or skill to do a job well', 'The report showed that the manager was incompetent.', 'Hasabat ýolbaşçynyň başarnyksyzdygyny görkezdi.', 'B2'),
    ('discontinue', '/ˌdɪskənˈtɪnjuː/', 'V', 'bes etmek, dowam etmezlik', 'прекратить', 'to stop making or doing something', 'The company discontinued the old model.', 'Kompaniýa köne görnüşi öndürmegi bes etdi.', 'B2'),
    ('undo', '/ʌnˈduː/', 'V', 'yzyna gaýtarmak', 'отменить, обратить', 'to reverse the effect of an action', 'You can undo the last change by pressing this button.', 'Şu düwmä basyp soňky üýtgeşmäni yzyna gaýtaryp bilersiňiz.', 'B1'),
    ('disembark', '/ˌdɪsɪmˈbɑːk/', 'V', 'ulagdan düşmek', 'сойти с транспорта', 'to get off a ship, plane, or other vehicle', 'Passengers will disembark at the next stop.', 'Ýolagçylar indiki duralgada düşerler.', 'C1'),
    ('unhelpful', '/ʌnˈhelpfl/', 'ADJ', 'kömegi degmeýän', 'бесполезный', 'not useful or willing to help', 'The instructions were unhelpful and confusing.', 'Görkezmeler peýdasyz hem bulaşyk boldy.', 'B1'),
    ('dishonest', '/dɪsˈɒnɪst/', 'ADJ', 'dogruçyl däl', 'нечестный', 'not telling the truth or not behaving fairly', 'It was dishonest to hide the mistake.', 'Ýalňyşy gizlemek dogruçyl däldi.', 'B1'),
    ('inhospitable', '/ˌɪnhɒˈspɪtəbl/', 'ADJ', 'myhmansöýer däl, ýaramaz şertli', 'негостеприимный', 'unfriendly or difficult to live in', 'The desert is an inhospitable place for plants.', 'Çöl ösümlikler üçin ýaşaýyş şertleri ýaramaz ýer.', 'C1'),
    ('illegitimate', '/ˌɪlɪˈdʒɪtɪmət/', 'ADJ', 'kanuny däl', 'незаконный', 'not allowed by law or accepted rules', 'The court rejected the illegitimate claim.', 'Kazyýet kanuny däl talaby ret etdi.', 'C1'),
    ('illiterate', '/ɪˈlɪtərət/', 'ADJ', 'okap-ýazyp bilmeýän', 'неграмотный', 'unable to read or write', 'The programme helps adults who are illiterate.', 'Maksatnama okap-ýazyp bilmeýän ululara kömek edýär.', 'B2'),
    ('illogical', '/ɪˈlɒdʒɪkl/', 'ADJ', 'mantyksyz', 'нелогичный', 'not reasonable or sensible', 'His conclusion seemed illogical to the group.', 'Onuň netijesi topara mantyksyz görünýärdi.', 'B2'),
    ('immobile', '/ɪˈməʊbaɪl/', 'ADJ', 'hereket edip bilmeýän', 'неподвижный', 'unable to move', 'After the accident, his leg was temporarily immobile.', 'Awariýadan soň aýagy wagtlaýyn hereket edip bilmedi.', 'B2'),
    ('immoral', '/ɪˈmɒrəl/', 'ADJ', 'ahlaksyz', 'аморальный', 'not considered right or honest by most people', 'They believed the decision was immoral.', 'Olar bu karary ahlaksyz hasapladylar.', 'B2'),
    ('unofficial', '/ˌʌnəˈfɪʃl/', 'ADJ', 'resmi däl', 'неофициальный', 'not formally approved or announced', 'We had an unofficial meeting after work.', 'Işden soň resmi däl duşuşygymyz boldy.', 'B1'),
    ('impersonal', '/ɪmˈpɜːsənl/', 'ADJ', 'şahsy däl, sowuk', 'безличный', 'not showing personal feelings or interest', 'The hotel service felt impersonal.', 'Myhmanhananyň hyzmaty sowuk ýaly duýuldy.', 'B2'),
    ('impractical', '/ɪmˈpræktɪkl/', 'ADJ', 'amaly taýdan oňaýsyz', 'непрактичный', 'not suitable or sensible in practice', 'Those shoes are impractical for walking in snow.', 'Şol aýakgaplar garda ýöremek üçin oňaýsyz.', 'B2'),
    ('irrational', '/ɪˈræʃənl/', 'ADJ', 'mantyksyz, akyla sygmaýan', 'иррациональный', 'not based on reason or clear thought', 'Fear made him behave in an irrational way.', 'Gorky ony mantyksyz hereket etmäge mejbur etdi.', 'B2'),
    ('irregular', '/ɪˈreɡjələ/', 'ADJ', 'tertipsiz, kadaly däl', 'нерегулярный', 'not happening at fixed or equal times', 'She works irregular hours at the hospital.', 'Ol hassahanada tertipsiz iş sagatlarynda işleýär.', 'B1'),
    ('irrelevant', '/ɪˈreləvənt/', 'ADJ', 'degişli däl', 'не относящийся к делу', 'not connected with the subject being discussed', 'That detail is irrelevant to our decision.', 'Şol jikme-jiklik biziň kararymyza degişli däl.', 'B2'),
    ('irreplaceable', '/ˌɪrɪˈpleɪsəbl/', 'ADJ', 'çalşyryp bolmaýan', 'незаменимый', 'so valuable or special that nothing can replace it', 'Her experience is irreplaceable.', 'Onuň tejribesiniň ornuny tutup bolmaýar.', 'B2'),
    ('outgrow', '/ˌaʊtˈɡrəʊ/', 'V', 'ulalyp geýimi dar gelmek; gyzyklanmasyny ýitirmek', 'вырасти из; перерасти', 'to become too big for something or stop liking it as you mature', 'The children have outgrown their winter coats.', 'Çagalar gyşky paltolaryndan ulaldylar.', 'B2'),
    ('monosyllabic', '/ˌmɒnəsɪˈlæbɪk/', 'ADJ', 'bir bogunly', 'односложный', 'having only one syllable', '“Book” is a monosyllabic word.', '“Book” bir bogunly söz.', 'C1'),
    ('rebuild', '/ˌriːˈbɪld/', 'V', 'täzeden gurmak', 'перестроить', 'to build something again after it has been damaged', 'The town had to rebuild after the earthquake.', 'Ýertitremeden soň şäheri täzeden gurmaly boldy.', 'B1'),
    ('outpatient', '/ˈaʊtpeɪʃnt/', 'N', 'hassahanada ýatman bejergi alýan näsag', 'амбулаторный пациент', 'a patient who visits a hospital for treatment but does not stay there', 'The clinic sees outpatients every afternoon.', 'Klinika her gün öýlän hassahanada ýatmaýan näsaglary kabul edýär.', 'C1'),
    ('ill-treated', '/ˌɪl ˈtriːtɪd/', 'ADJ', 'ýaramaz çemeleşilen', 'плохо обращались', 'treated in a cruel or careless way', 'The ill-treated dog was taken to a shelter.', 'Ýaramaz çemeleşilen iti haýwan penahanasyna alyp gitdiler.', 'B2'),
    ('multivitamin', '/ˌmʌltiˈvɪtəmɪn/', 'N', 'köp witaminli derman', 'мультивитамин', 'a pill or drink containing several vitamins', 'The doctor recommended a multivitamin.', 'Lukman köp witaminli dermany maslahat berdi.', 'B2'),
    ('misunderstand', '/ˌmɪsʌndəˈstænd/', 'V', 'nädogry düşünmek', 'неправильно понять', 'to understand something in the wrong way', 'I misunderstood the instructions and went to the wrong room.', 'Görkezmelere nädogry düşünip, başga otaga gitdim.', 'B1'),
    ('antivirus', '/ˈæntivaɪrəs/', 'N', 'antivirus programma', 'антивирус', 'a program that finds and removes computer viruses', 'Install antivirus software before downloading the file.', 'Faýly ýükläp almazdan öň antivirus programma guruň.', 'B2'),
    ('deforestation', '/diːˌfɒrɪˈsteɪʃn/', 'N', 'tokaýlaryň çapylmagy', 'вырубка лесов', 'the cutting down of large areas of forest', 'Deforestation destroys the homes of many animals.', 'Tokaýlaryň çapylmagy köp haýwanyň ýaşaýan ýerini ýok edýär.', 'B2'),
    ('precondition', '/ˌpriːkənˈdɪʃn/', 'N', 'öňünden zerur şert', 'предварительное условие', 'something that must happen before something else is possible', 'Trust is a precondition for a successful partnership.', 'Ynam üstünlikli hyzmatdaşlygyň öňünden zerur şertidir.', 'C1'),
    ('oversleep', '/ˌəʊvəˈsliːp/', 'V', 'artyk uklap, gijä galmak', 'проспать', 'to sleep longer than planned', 'I overslept and missed the early train.', 'Artyk uklap, irki otla gijä galdym.', 'B1'),
    ('biannual', '/baɪˈænjuəl/', 'ADJ', 'ýylda iki gezek bolýan', 'двухгодичный; дважды в год', 'happening twice a year', 'The committee holds biannual meetings in spring and autumn.', 'Geňeş ýazda we güýzde ýylda iki gezek ýygnak geçirýär.', 'C1'),
    ('coexist', '/ˌkəʊɪɡˈzɪst/', 'V', 'bilelikde ýaşamak', 'сосуществовать', 'to live or exist together at the same time', 'Different communities coexist peacefully in the city.', 'Şäherde dürli jemgyýetler parahatçylykly bile ýaşaýarlar.', 'B2'),
    ('substandard', '/ˌsʌbˈstændəd/', 'ADJ', 'talap edilýän derejeden pes', 'ниже стандарта', 'below the quality that is expected', 'The building was closed because of substandard safety.', 'Howpsuzlyk derejesi pes bolany üçin bina ýapyldy.', 'C1'),
    ('intergovernmental', '/ˌɪntəˌɡʌvənˈmentl/', 'ADJ', 'hökümetara', 'межправительственный', 'involving two or more governments', 'An intergovernmental group discussed climate policy.', 'Hökümetara topar howa syýasatyny ara alyp maslahatlaşdy.', 'C1'),
    ('understaffed', '/ˌʌndəˈstɑːft/', 'ADJ', 'işgäri ýeterlik däl', 'недоукомплектованный', 'having fewer workers than are needed', 'The restaurant is understaffed on busy evenings.', 'Işli agşamlarda restoranda işgär ýeterlik däl.', 'C1'),
    ('superhuman', '/ˌsuːpəˈhjuːmən/', 'ADJ', 'adama mahsus bolmadyk güýçli', 'сверхчеловеческий', 'much stronger or more capable than an ordinary person', 'It took superhuman effort to lift the stone.', 'Daşy galdyrmak üçin adatdan daşary güýç gerek boldy.', 'B2'),
    ('autofocus', '/ˈɔːtəʊfəʊkəs/', 'N', 'awtomatik fokus', 'автофокус', 'a camera feature that focuses the lens automatically', 'The camera’s autofocus works well in low light.', 'Kameranyň awtomatik fokusu pes ýagtylykda gowy işleýär.', 'B2'),
    ('microorganism', '/ˌmaɪkrəʊˈɔːɡənɪzəm/', 'N', 'mikroorganizm', 'микроорганизм', 'a very small living thing that can be seen only with a microscope', 'Some microorganisms are useful to humans.', 'Käbir mikroorganizmler adamlara peýdalydyr.', 'B2'),
    ('outnumber', '/ˌaʊtˈnʌmbə/', 'V', 'sany taýdan agdyk gelmek', 'превосходить числом', 'to be greater in number than another group', 'In this class, girls outnumber boys.', 'Bu synpda gyzlar oglanlardan köpräk.', 'B2'),
    ('outskirts', '/ˈaʊtskɜːts/', 'N', 'şäheriň gyrasy', 'окраина', 'the parts of a town or city furthest from the centre', 'They live on the outskirts of London.', 'Olar Londonyň şäher gyrasynda ýaşaýarlar.', 'B2'),
    ('demystify', '/ˌdiːˈmɪstɪfaɪ/', 'V', 'düşnüksizligi aýyrmak', 'развеять тайну', 'to make something complicated easier to understand', 'The guide helps demystify the application process.', 'Gollanma ýüz tutma işiniň düşnüksizligini aýyrmaga kömek edýär.', 'C1'),
]

# ---- in-lesson 7B — art · colour idioms ----
T['art_colour'] = [
    ('artwork', '/ˈɑːtwɜːk/', 'N', 'sungat eseri', 'произведение искусства', 'a painting or drawing', 'The gallery displays modern artwork.', 'Galereýa häzirki zaman sungat eserlerini görkezýär.', 'A2'),
    ('canvas', '/ˈkænvəs/', 'N', 'kanwas', 'холст', 'cloth that paintings are done on', 'The artist painted on a huge canvas.', 'Suratkeş ägirt kanwasda surat çekdi.', 'B1'),
    ('contemporary', '/kənˈtemprəri/', 'ADJ', 'häzirki zaman', 'современный', 'belonging to the present time', 'She collects contemporary art.', 'Häzirki zaman sungatyny ýygnaýar.', 'B1', 'contemporary art'),
    ('exhibition', '/ˌeksɪˈbɪʃn/', 'N', 'sergi', 'выставка', 'a public show of art', 'The exhibition opens on Friday.', 'Sergi anna güni açylýar.', 'A2', 'visit an exhibition'),
    ('landscape', '/ˈlændskeɪp/', 'N', 'tebigat görnüşi', 'пейзаж', 'a picture of countryside', 'He painted a mountain landscape.', 'Dag görnüşini surat çekdi.', 'A2'),
    ('portrait', '/ˈpɔːtrət/', 'N', 'portret', 'портрет', 'a picture of a person', 'The portrait hangs in the hall.', 'Portret zalyň diwarynda asylgy.', 'A2', 'paint a portrait'),
    ('sculpture', '/ˈskʌlptʃə(r)/', 'N', 'heýkel', 'скульптура', 'a statue or carved art', 'The sculpture stands in the park.', 'Heýkel parkyň içinde dur.', 'A2'),
    ('sketch', '/sketʃ/', 'N', 'çyzgy (garalama)', 'набросок, эскиз', 'a quick simple drawing', 'She made a sketch of the old man.', 'Garry adamyň çyzgysyny etdi.', 'A2', 'make a sketch'),
    ('still life', '/ˌstɪl ˈlaɪf/', 'N', 'natýurmort', 'натюрморт', 'a painting of objects like fruit', 'The still life shows apples and grapes.', 'Natýurmortda alma we üzüm görkezilýär.', 'B1'),
    ('out of the blue', '/aʊt əv ðə bluː/', 'PHR', 'duýdansyz', 'как гром среди ясного неба', 'suddenly and unexpectedly', 'She called me out of the blue.', 'Duýdansyz maňa jaň etdi.', 'B1'),
    ('red tape', '/ˌred ˈteɪp/', 'N', 'kagyzbazlyk', 'бюрократия, волокита', 'too many official rules', 'Red tape delayed the project.', 'Kagyzbazlyk taslamany giçikdirdi.', 'B2'),
    ('white lie', '/ˌwaɪt ˈlaɪ/', 'N', 'ýumşak ýalan', 'невинная ложь', 'a small lie that does not hurt', 'It was just a white lie.', 'Diňe ýumşak ýalan boldy.', 'B1', 'tell a white lie'),
]

# ---- in-lesson 8A — health and medicine ----
T['health'] = [
    ('antibiotic', '/ˌæntibaɪˈɒtɪk/', 'N', 'antibiotik', 'антибиотик', 'medicine that kills bacteria', 'The doctor prescribed an antibiotic.', 'Lukman antibiotik ýazdy.', 'A2', 'take antibiotics'),
    ('check-up', '/ˈtʃek ʌp/', 'N', 'lukmançylyk barlagy', 'медосмотр', 'a general medical examination', 'I have a check-up next week.', 'Indiki hepde lukmançylyk barlagym bar.', 'A2', 'medical check-up'),
    ('cure', '/kjʊə(r)/', 'N', 'bejergi (emel)', 'лекарство, средство', 'a treatment that ends an illness', 'There is no cure yet.', 'Entek emel ýok.', 'A2', 'find a cure'),
    ('diagnosis', '/ˌdaɪəɡˈnəʊsɪs/', 'N', 'kesel anyklama', 'диагноз', "a doctor's judgement of an illness", 'The diagnosis was made quickly.', 'Diaгноз tiz goýuldy.', 'B1', 'make a diagnosis'),
    ('dose', '/dəʊs/', 'N', 'doza', 'доза', 'an amount of medicine', 'Take one dose every morning.', 'Her irden bir doza içiň.', 'A2', 'a dose of'),
    ('GP', '/ˌdʒiː ˈpiː/', 'N', 'maşgala lukmany', 'врач общей практики', 'a general practice doctor', 'Make an appointment with the GP.', 'Maşgala lukmanyna ýazylyň.', 'A2', 'go to the GP'),
    ('injection', '/ɪnˈdʒekʃn/', 'N', 'ukol (sanjym)', 'укол, инъекция', 'medicine given with a needle', 'The injection did not hurt.', 'Ukol agyrmady.', 'A2', 'give an injection'),
    ('operation', '/ˌɒpəˈreɪʃn/', 'N', 'operasiýa', 'операция', 'a medical procedure inside the body', 'She had an operation on her heart.', 'Ýüregine operasiýa etdirdi.', 'A2', 'have an operation'),
    ('remedy', '/ˈremədi/', 'N', 'emel (halk bejergisi)', 'средство (от болезни)', 'something that cures a problem', 'Honey is a good remedy for coughs.', 'Bal üsgülewüğe gowy emel.', 'B1', 'home remedy'),
    ('side effect', '/ˌsaɪd ɪˈfekt/', 'N', 'gapdal täsiri', 'побочный эффект', 'an unwanted effect of medicine', 'The pill has no side effects.', 'Dermanyň gapdal täsiri ýok.', 'A2'),
    ('surgeon', '/ˈsɜːdʒən/', 'N', 'hirurg', 'хирург', 'a doctor who does operations', 'The surgeon explained the risks.', 'Hirurg howplary düşündirdi.', 'A2'),
    ('treatment', '/ˈtriːtmənt/', 'N', 'bejergi', 'лечение', 'care given for an illness', 'The treatment worked well.', 'Bejergi gowy netije berdi.', 'A2', 'medical treatment'),
    ('vaccination', '/ˌvæksɪˈneɪʃn/', 'N', 'waksina (sanjym)', 'вакцинация', 'an injection that prevents disease', 'The vaccination protects children.', 'Waksina çagalary goraýar.', 'A2', 'get a vaccination'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('sore throat', '/ˌsɔː ˈθrəʊt/', 'N', 'bokurdagyň agyrmagy', 'боль в горле', 'pain in your throat, especially when you swallow', 'I stayed home because I had a sore throat.', 'Bokurdagym agyrýandygy üçin öýde galdym.', 'A2'),
    ('sneeze', '/sniːz/', 'V', 'asgyrmak', 'чихать', 'to suddenly breathe air out through your nose', 'Dust makes me sneeze.', 'Tozan meni asgyrdýar.', 'A2'),
    ('high temperature', '/ˌhaɪ ˈtemprətʃə/', 'N', 'ýokary gyzgyn', 'высокая температура', 'a body temperature above the normal level', 'The child has a high temperature and needs to rest.', 'Çaganyň gyzgyny ýokary, ol dynç almaly.', 'A2'),
    ('fever', '/ˈfiːvə/', 'N', 'gyzzyrma', 'лихорадка', 'a high body temperature, usually caused by illness', 'He has a fever and a bad cough.', 'Onuň gyzzyrmasy we güýçli üsgülewügi bar.', 'A2'),
    ('aches and pains', '/ˌeɪks ən ˈpeɪnz/', 'N', 'beden agyrylary', 'ломота и боли', 'general pains in different parts of the body', 'After the long walk, I had aches and pains everywhere.', 'Uzak ýörişden soň bedenimiň ähli ýeri agyrdy.', 'B1'),
]

# ---- Vocabulary Bank — Travel and tourism -> 8B ----
T['travel_tourism'] = [
    ('accommodation', '/əˌkɒməˈdeɪʃn/', 'N', 'ýaşaýyş ýeri', 'жильё, размещение', 'a place to stay', 'The price includes accommodation.', 'Baha ýaşaýyş ýerini hem öz içine alýar.', 'A2', 'book accommodation'),
    ('attraction', '/əˈtrækʃn/', 'N', 'görmeli ýer', 'достопримечательность', 'a place tourists visit', 'The old city is the main attraction.', 'Köne şäher esasy görmeli ýer.', 'A2', 'tourist attraction'),
    ('backpacker', '/ˈbækpækə(r)/', 'N', 'ýeňil sumkaly syýahatçy', 'бэкпекер', 'a traveller with a big bag', 'Backpackers prefer cheap hostels.', 'Ýeňil sumkaly syýahatçylar arzan ýatakhanalary gowy görýär.', 'B1'),
    ('brochure', '/ˈbrəʊʃə(r)/', 'N', 'buklet', 'брошюра', 'a small book of travel information', 'The brochure lists all the hotels.', 'Buklet ähli myhmanhanalary sanlaýar.', 'A2', 'travel brochure'),
    ('destination', '/ˌdestɪˈneɪʃn/', 'N', 'barmaly ýer', 'пункт назначения', 'the place you travel to', 'Paris is a popular destination.', 'Parij meşhur barmaly ýer.', 'A2', 'tourist destination'),
    ('excursion', '/ɪkˈskɜːʃn/', 'N', 'ekskursiýa', 'экскурсия', 'a short organised trip', 'We went on a boat excursion.', 'Gaýyk ekskursiýasyna gitdik.', 'A2', 'go on an excursion'),
    ('itinerary', '/aɪˈtɪnərəri/', 'N', 'syýahat meýilnamasy', 'маршрут', 'a plan of a journey', 'The itinerary includes three cities.', 'Syýahat meýilnamasy üç şäheri öz içine alýar.', 'B1', 'plan an itinerary'),
    ('sightseeing', '/ˈsaɪtsiːɪŋ/', 'N', 'görmeli ýerleri görmek', 'осмотр достопримечательностей', 'visiting famous places', 'We spent the morning sightseeing.', 'Irdeniň dowamynda görmeli ýerleri gördük.', 'A2', 'go sightseeing'),
    ('tourist', '/ˈtʊərɪst/', 'N', 'turist', 'турист', 'a person visiting a place for pleasure', 'The old town is full of tourists.', 'Köne şäher turistlerden doly.', 'A1'),
    ('resort', '/rɪˈzɔːt/', 'N', 'dynç alyş ýeri', 'курорт', 'a place for holidays', 'Awaza is a seaside resort.', 'Awaza deňiz kenaryndaky dynç alyş ýeri.', 'A2', 'beach resort'),
    ('travel agent', '/ˈtrævl eɪdʒənt/', 'N', 'syýahat agenti', 'турагент', 'a person who arranges trips', 'The travel agent found us a deal.', 'Syýahat agenti bize arzan tapdy.', 'A2'),
    ('holidaymaker', '/ˈhɒlədeɪmeɪkə(r)/', 'N', 'dynç alyşçy', 'отпускник', 'a person on holiday', 'The beach was crowded with holidaymakers.', 'Kenar dynç alyşçylardan doly boldy.', 'B1'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('breathtaking', '/ˈbreθteɪkɪŋ/', 'ADJ', 'haýran galdyryjy', 'захватывающий дух', 'extremely impressive or beautiful', 'The view from the mountain was breathtaking.', 'Dagdan görünýän görnüş haýran galdyryjydy.', 'B2'),
    ('iconic', '/aɪˈkɒnɪk/', 'ADJ', 'nyşana öwrülen, meşhur', 'знаковый', 'very famous and representing a particular place or idea', 'The bridge is an iconic symbol of the city.', 'Köpri şäheriň meşhur nyşanydyr.', 'B2'),
    ('imposing', '/ɪmˈpəʊzɪŋ/', 'ADJ', 'ägirt we täsir galdyryjy', 'величественный', 'large and impressive in appearance', 'An imposing palace stood at the end of the street.', 'Köçäniň aňyrsynda ägirt köşk durdy.', 'B2'),
    ('lively', '/ˈlaɪvli/', 'ADJ', 'janly, şowhunly', 'оживлённый', 'full of energy and activity', 'The old town is lively at night.', 'Köne şäher gijelerine janly bolýar.', 'A2'),
    ('off the beaten track', '/ˌɒf ðə ˈbiːtn træk/', 'PHR', 'köp adamyň barmaýan ýerinde', 'в стороне от проторённых дорог', 'away from places where most people go', 'We found a quiet café off the beaten track.', 'Köp adamyň barmaýan ýerinde asuda kafe tapdyk.', 'B2'),
    ('picturesque', '/ˌpɪktʃəˈresk/', 'ADJ', 'surat ýaly owadan', 'живописный', 'pretty, especially in an old-fashioned way', 'They stayed in a picturesque fishing village.', 'Olar surat ýaly owadan balykçy obasynda galdylar.', 'B2'),
    ('remote', '/rɪˈməʊt/', 'ADJ', 'uzakda ýerleşýän', 'отдалённый', 'far away from towns or other people', 'The remote island has no airport.', 'Uzakdaky adada howa menzili ýok.', 'B1'),
    ('unspoilt', '/ˌʌnˈspɔɪlt/', 'ADJ', 'tebigy gözelligi bozulmadyk', 'нетронутый', 'beautiful because it has not been changed by people', 'We walked along an unspoilt stretch of coast.', 'Tebigy gözelligi bozulmadyk kenar bilen gezdik.', 'B2'),
    ('dull', '/dʌl/', 'ADJ', 'ýürekgysdyryjy, gyzyksyz', 'скучный', 'not interesting or exciting', 'The town felt dull after sunset.', 'Gün ýaşandan soň şäher gyzyksyz duýuldy.', 'A2'),
    ('overcrowded', '/ˌəʊvəˈkraʊdɪd/', 'ADJ', 'aşa köp adamly', 'переполненный', 'containing too many people', 'The beach gets overcrowded in August.', 'Awgustda kenarda adam aşa köp bolýar.', 'B2'),
    ('overrated', '/ˌəʊvəˈreɪtɪd/', 'ADJ', 'artykmaç öwülen', 'переоценённый', 'considered better than it really is', 'I thought the restaurant was overrated.', 'Restorany hakykatdan artykmaç öwüpdirler diýip pikir etdim.', 'B2'),
    ('soulless', '/ˈsəʊlləs/', 'ADJ', 'häsiýetsiz, ýakymsyz', 'безликий', 'lacking character or warmth', 'The new shopping centre feels soulless.', 'Täze söwda merkezi häsiýetsiz görünýär.', 'C1'),
    ('touristy', '/ˈtʊərɪsti/', 'ADJ', 'syýahatçylara niýetlenen', 'туристический (с оттенком массовости)', 'designed mainly to attract tourists', 'The main street is too touristy for my taste.', 'Esasy köçe meniň üçin aşa syýahatçylyk görnüşinde.', 'B2'),
    ('pricey', '/ˈpraɪsi/', 'ADJ', 'gymmat', 'дороговатый', 'rather expensive; informal', 'The hotel was nice but a little pricey.', 'Myhmanhana gowy, ýöne biraz gymmatdy.', 'B1'),
    ('run-down', '/ˌrʌn ˈdaʊn/', 'ADJ', 'köne we ýaramaz ýagdaýda', 'обветшалый', 'in poor condition because it has not been cared for', 'They renovated a run-down old hotel.', 'Olar ýaramaz ýagdaýdaky köne myhmanhanany abatladylar.', 'B2'),
    ('spoilt', '/spɔɪlt/', 'ADJ', 'zaýalanan, öňki gözelligi bozulan', 'испорченный', 'damaged or made less attractive', 'The coastline was spoilt by large new hotels.', 'Täze uly myhmanhanalar kenaryň gözelligini bozdy.', 'B2'),
    ('tacky', '/ˈtæki/', 'ADJ', 'owadan däl we arzan görünýän', 'безвкусный', 'cheap-looking and lacking good taste', 'The souvenir shop sold tacky plastic models.', 'Ýadygärlik dükany owadan däl plastmassa şekilleri satýardy.', 'B2'),
    ('unimposing', '/ˌʌnɪmˈpəʊzɪŋ/', 'ADJ', 'täsir galdyrmaýan, sada', 'невзрачный', 'not large or impressive', 'The entrance is unimposing, but the hall is beautiful.', 'Girelge ýönekeý, ýöne zal owadan.', 'C1'),
    ('set off', '/ˌset ˈɒf/', 'PHR', 'ýola düşmek', 'отправиться в путь', 'to begin a journey', 'We set off early to avoid the traffic.', 'Ulag dyknyşygyndan gaça durmak üçin ir ýola düşdük.', 'B1'),
    ('set out', '/ˌset ˈaʊt/', 'PHR', 'ýola düşmek, maksat edinmek', 'отправиться; поставить цель', 'to begin a journey or start doing something with a purpose', 'They set out before dawn to reach the village.', 'Oba ýetmek üçin daň atmanka ýola düşdüler.', 'B2'),
    ('go camping', '/ˌɡəʊ ˈkæmpɪŋ/', 'PHR', 'çadyrlap dynç almaga gitmek', 'поехать в поход с палатками', 'to spend a holiday living in a tent', 'We go camping by the lake every summer.', 'Her tomus kölüň ýanynda çadyrlap dynç alýarys.', 'A2'),
    ('go backpacking', '/ˌɡəʊ ˈbækpækɪŋ/', 'PHR', 'ýeňil goş bilen syýahat etmek', 'путешествовать с рюкзаком', 'to travel on a low budget carrying your things in a backpack', 'They went backpacking around South America.', 'Olar Günorta Amerikada ýeňil goş bilen syýahat etdiler.', 'B2'),
    ('go sightseeing', '/ˌɡəʊ ˈsaɪtsiːɪŋ/', 'PHR', 'taryhy ýerleri görmäge gitmek', 'осматривать достопримечательности', 'to visit famous or interesting places', 'We went sightseeing on our first day in Rome.', 'Rimde ilkinji günümiz gözel ýerleri görmäge gitdik.', 'A2'),
    ('go for a stroll', '/ˌɡəʊ fər ə ˈstrəʊl/', 'PHR', 'gezelenje çykmak', 'пойти на прогулку', 'to go for a slow, relaxed walk', 'We went for a stroll around the old town.', 'Köne şäherde gezelenje çykdyk.', 'B1'),
    ('go on a trip', '/ˌɡəʊ ɒn ə ˈtrɪp/', 'PHR', 'syýahata gitmek', 'отправиться в поездку', 'to travel somewhere for a short time', 'The class went on a trip to the coast.', 'Synp kenara syýahata gitdi.', 'A2'),
    ('go on an outing', '/ˌɡəʊ ɒn ən ˈaʊtɪŋ/', 'PHR', 'gezelenje çykmak', 'отправиться на прогулку', 'to go on a short trip for pleasure', 'The family went on an outing to the countryside.', 'Maşgala oba ýerlerine gezelenje çykdy.', 'B2'),
    ('go on a safari', '/ˌɡəʊ ɒn ə səˈfɑːri/', 'PHR', 'safari syýahatyna gitmek', 'отправиться на сафари', 'to take a trip to watch wild animals', 'They went on a safari in Kenya.', 'Olar Keniýada safari syýahatyna gitdiler.', 'B2'),
    ('go on a trek', '/ˌɡəʊ ɒn ə ˈtrek/', 'PHR', 'uzak pyýada ýörişe gitmek', 'отправиться в длительный поход', 'to go on a long, difficult walk', 'We went on a trek through the mountains.', 'Daglaryň içinden uzak pyýada ýörişe gitdik.', 'B2'),
    ('go on a cruise', '/ˌɡəʊ ɒn ə ˈkruːz/', 'PHR', 'kruiz syýahatyna gitmek', 'отправиться в круиз', 'to take a holiday on a ship', 'My parents went on a cruise around the islands.', 'Ene-atam adalaryň daşyndan kruiz syýahatyna gitdiler.', 'B1'),
    ('go on a journey', '/ˌɡəʊ ɒn ə ˈdʒɜːni/', 'PHR', 'ýola düşmek, uzak ýol gitmek', 'отправиться в путешествие', 'to travel from one place to another, usually a long way', 'They went on a long journey by train.', 'Olar otly bilen uzak ýola düşdüler.', 'A2'),
    ('put off', '/ˌpʊt ˈɒf/', 'PHR', 'soňraky wagta süýşürmek', 'отложить', 'to arrange for something to happen later', 'We had to put off our visit until Monday.', 'Saparymyzy duşenbe gününe çenli süýşürmeli bolduk.', 'B1'),
    ('wander round', '/ˌwɒndə ˈraʊnd/', 'PHR', 'asuda aýlanyp görmek', 'бродить, прогуливаться', 'to walk around a place without a fixed plan', 'We wandered round the market for an hour.', 'Bazarda bir sagatlap asuda aýlandyk.', 'B2'),
    ('soak up', '/ˌsəʊk ˈʌp/', 'PHR', 'siňdirmek, doly duýmak', 'впитывать, наслаждаться', 'to enjoy and experience an atmosphere or culture', 'We sat outside to soak up the atmosphere.', 'Howany doly duýmak üçin daşarda oturdyk.', 'B2'),
    ('sample', '/ˈsɑːmpl/', 'V', 'dadyp görmek, synap görmek', 'попробовать', 'to try a small amount of food or drink', 'Visitors can sample local cheese at the market.', 'Myhmanlar bazarda ýerli peýniri dadyp bilerler.', 'B1'),
    ('recharge your batteries', '/ˌriːtʃɑːdʒ jɔː ˈbætriz/', 'PHR', 'güýjüňi dikeltmek', 'восстановить силы', 'to rest so that you have more energy', 'A quiet weekend helped me recharge my batteries.', 'Asuda dynç günleri güýjümi dikeltmäge kömek etdi.', 'B2'),
    ('extend your stay', '/ɪkˌstend jɔː ˈsteɪ/', 'PHR', 'galýan wagtyňy uzaltmak', 'продлить пребывание', 'to stay somewhere longer than planned', 'We decided to extend our stay by two nights.', 'Iki gije artyk galmagy karar etdik.', 'B2'),
    ('get away from it all', '/ˌɡet əˈweɪ frəm ɪt ˈɔːl/', 'PHR', 'hemme zatdan dynç almak üçin gaçyp gitmek', 'уехать от всего', 'to go somewhere peaceful to escape daily life', 'We rented a cabin in the hills to get away from it all.', 'Gündelik durmuşdan dynç almak üçin baýyrda öýjagaz kireýine aldyk.', 'B2'),
    ('take it all in', '/ˌteɪk ɪt ɔːl ˈɪn/', 'PHR', 'daş-töweregi synlap, täsirini duýmak', 'впитать впечатления', 'to look at, hear, and fully experience what is around you', 'We stopped at the viewpoint to take it all in.', 'Ähli görnüşi synlamak üçin tomaşa ýerine saklandyk.', 'B2'),
]

# ---- Vocabulary Bank — Animal matters -> 9A ----
T['animal_matters'] = [
    ('animal rights', '/ˌænɪml ˈraɪts/', 'N', 'haýwan hukuklary', 'права животных', 'the idea that animals deserve care', 'She campaigns for animal rights.', 'Haýwan hukuklary üçin kampaniýa alyp barýar.', 'B1'),
    ('cage', '/keɪdʒ/', 'N', 'gapas', 'клетка', 'a box with bars for animals', 'The parrot escaped from its cage.', 'Tötüji gapasdan gaçdy.', 'A2', 'in a cage'),
    ('cruelty', '/ˈkruːəlti/', 'N', 'rehimsizlik', 'жестокость', 'behaviour that causes suffering', 'Cruelty to animals is a crime.', 'Haýwanlara rehimsizlik jenaýat.', 'B1', 'animal cruelty'),
    ('extinction', '/ɪkˈstɪŋkʃn/', 'N', 'ýok bolmak (görnüşiň)', 'вымирание', 'when a species dies out', 'The tiger faces extinction.', 'Ýolbars ýok bolmak howpy astynda.', 'B1', 'face extinction'),
    ('fur', '/fɜː(r)/', 'N', 'ýüň (haýwanyň)', 'мех', 'the soft hair on animals', 'The cat has soft white fur.', 'Pişigiň ýumşak ak ýüňi bar.', 'A2'),
    ('habitat', '/ˈhæbɪtæt/', 'N', 'ýaşaýyş gurşawy', 'среда обитания', 'the natural home of an animal', 'Cutting trees destroys habitats.', 'Agaçlary çapmak ýaşaýyş gurşawyny weýran edýär.', 'B1', 'natural habitat'),
    ('hunt', '/hʌnt/', 'V', 'awlamak', 'охотиться', 'to chase animals to catch them', 'Lions hunt at night.', 'Ýolbarslar gije awlaýar.', 'A2'),
    ('poacher', '/ˈpəʊtʃə(r)/', 'N', 'bikanun awçy', 'браконьер', 'a person who hunts illegally', 'Poachers killed the rhino.', 'Bikanun awçylar karkidany öldürdi.', 'B1'),
    ('stray', '/streɪ/', 'ADJ', 'eýesiz (haýwan)', 'бездомный (о животном)', 'lost, with no home', 'A stray dog followed us home.', 'Eýesiz it yzymyzdan öýe geldi.', 'A2', 'stray cat'),
    ('wildlife', '/ˈwaɪldlaɪf/', 'N', 'ýabany tebigat', 'дикая природа', 'animals and plants in nature', 'The reserve protects wildlife.', 'Goraghana ýabany tebigaty goraýar.', 'A2', 'wildlife reserve'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('calf', '/kɑːf/', 'N', 'göle', 'теленок', 'a young cow or other large mammal', 'The calf stayed close to its mother.', 'Göle enesiniň ýanynda galdy.', 'A2'),
    ('chick', '/tʃɪk/', 'N', 'jüýje', 'цыплёнок', 'a young bird, especially a chicken', 'The hen led her chicks across the yard.', 'Towuk jüýjelerini howlydan alyp geçdi.', 'A2'),
    ('cub', '/kʌb/', 'N', 'haýwanyň balasy', 'детёныш', 'a young bear, lion, fox, or similar animal', 'The lion cub played beside its mother.', 'Ýolbarsyň balasy enesiniň ýanynda oýnady.', 'B1'),
    ('foal', '/fəʊl/', 'N', 'taý', 'жеребёнок', 'a young horse', 'The foal was born during the night.', 'Taý gijäniň dowamynda dünýä indi.', 'B2'),
    ('kid', '/kɪd/', 'N', 'owlak', 'козлёнок', 'a young goat', 'The kid followed the goat into the field.', 'Owlak geçiniň yzy bilen meýdana gitdi.', 'B1'),
    ('puppy', '/ˈpʌpi/', 'N', 'güjük', 'щенок', 'a very young dog', 'The puppy chewed one of my shoes.', 'Güjük aýakgabymyň birini çeýnedi.', 'A2'),
    ('beak', '/biːk/', 'N', 'guşuň çüňki', 'клюв', 'the hard pointed part of a bird’s mouth', 'The parrot opened its beak to call.', 'Toty gygyrmak üçin çüňküni açdy.', 'B1'),
    ('claw', '/klɔː/', 'N', 'dyrnak', 'коготь', 'a sharp curved nail on an animal’s foot', 'The cat caught the toy with one claw.', 'Pişik oýnawajy bir dyrnagy bilen tutdy.', 'B1'),
    ('feather', '/ˈfeðə/', 'N', 'ýelek', 'перо', 'one of the soft parts covering a bird’s body', 'A blue feather lay on the path.', 'Ýodada gök ýelek ýatyrdy.', 'A2'),
    ('hoof', '/huːf/', 'N', 'toýnak', 'копыто', 'the hard part of the foot of a horse or similar animal', 'The horse hurt its hoof on a stone.', 'At daşda toýnagyny agyrtdy.', 'B2'),
    ('paw', '/pɔː/', 'N', 'haýwanyň penjesi', 'лапа', 'the foot of an animal such as a cat or dog', 'The dog placed a paw on my knee.', 'It penjesini dyzyma goýdy.', 'A2'),
    ('shell', '/ʃel/', 'N', 'gaty daşky gabyk', 'панцирь, раковина', 'the hard outer covering of some animals', 'The turtle pulled its head into its shell.', 'Pyşbaga kellesini gabygyň içine çekdi.', 'A2'),
    ('tail', '/teɪl/', 'N', 'guýrugy', 'хвост', 'the part that extends from the back of an animal', 'The puppy wagged its tail excitedly.', 'Güjük guýrugyny şatlyk bilen bulaýlady.', 'A2'),
    ('whisker', '/ˈwɪskə/', 'N', 'murt', 'ус', 'one of the long stiff hairs on an animal’s face', 'The cat’s whiskers moved as it sniffed the air.', 'Howany yslanda pişigiň murtlary gymyldady.', 'B2'),
    ('wing', '/wɪŋ/', 'N', 'ganat', 'крыло', 'one of the parts birds use to fly', 'The injured bird could not lift its wing.', 'Ýaralanan guş ganatyny galdyryp bilmedi.', 'A2'),
    ('hive', '/haɪv/', 'N', 'ary öýi', 'улей', 'a structure where bees live', 'The beekeeper checked the hive carefully.', 'Ary bakyjy ary öýüni üns bilen barlady.', 'B1'),
    ('stable', '/ˈsteɪbl/', 'N', 'at athanasy', 'конюшня', 'a building where horses are kept', 'The horses returned to the stable at dusk.', 'Atlar agşamlyk athana dolandylar.', 'B1'),
    ('kennel', '/ˈkenl/', 'N', 'it öýjagazy', 'собачья будка', 'a small shelter or building for a dog', 'The dog slept in its kennel outside.', 'It daşardaky öýjagazynda ýatdy.', 'B2'),
    ('tank', '/tæŋk/', 'N', 'akwarýum, balyk saklanýan gap', 'аквариум', 'a large container for keeping fish or other animals', 'The goldfish live in a glass tank.', 'Altynbalyklar aýna akwarýumda ýaşaýarlar.', 'A2'),
    ('nest', '/nest/', 'N', 'guş höwürtgesi', 'гнездо', 'a place that a bird makes to lay eggs', 'We saw a nest high in the tree.', 'Agajyň ýokarsynda höwürtge gördük.', 'A2'),
    ('bark', '/bɑːk/', 'V', 'üýrmek', 'лаять', 'to make the loud short sound that a dog makes', 'The dog barked when the post arrived.', 'Poçta gelende it üýrdi.', 'A2'),
    ('neigh', '/neɪ/', 'V', 'kişňemek', 'ржать', 'to make the loud sound of a horse', 'The horse neighed when it saw the food.', 'Iti görende at kişňedi.', 'B2'),
    ('meow', '/miˈaʊ/', 'V', 'miyawlamak', 'мяукать', 'to make the sound that a cat makes', 'The cat meowed outside the bedroom door.', 'Pişik ýatylýan otagyň gapysynda miyawlady.', 'B1'),
    ('grunt', '/ɡrʌnt/', 'V', 'hüňürdemek', 'хрюкать; grunt', 'to make a short low sound like a pig', 'The pig grunted as it searched for food.', 'Iýmit gözlände doňuz hüňürdedi.', 'B2'),
    ('twitter', '/ˈtwɪtə/', 'V', 'jürküldemek', 'щебетать', 'to make a series of short high bird sounds', 'Birds were twittering in the garden.', 'Bagda guşlar jürküldeýärdi.', 'B2'),
    ('animal charity', '/ˌænɪml ˈtʃærəti/', 'N', 'haýwanlary goraýan haýyr-sahawat guramasy', 'благотворительная организация по защите животных', 'an organization that helps and protects animals', 'The animal charity found homes for abandoned dogs.', 'Haýwanlary goraýan gurama taşlanan itlere öý tapdy.', 'B2'),
    ('animal rights activist', '/ˌænɪml raɪts ˈæktɪvɪst/', 'N', 'haýwan hukuklaryny goraýjy', 'активист за права животных', 'a person who campaigns for animals to be treated fairly', 'An animal rights activist spoke outside the laboratory.', 'Haýwan hukuklaryny goraýjy barlaghananyň daşynda çykyş etdi.', 'C1'),
    ('animal testing', '/ˌænɪml ˈtestɪŋ/', 'N', 'haýwanlarda synag geçirmek', 'испытания на животных', 'using animals to test products or medicines', 'The company promised to stop animal testing.', 'Kompaniýa haýwanlarda synag geçirmegi bes etjekdigini wada berdi.', 'B2'),
    ('medical research', '/ˌmedɪkl rɪˈsɜːtʃ/', 'N', 'lukmançylyk ylmy barlagy', 'медицинское исследование', 'the study of health and illness to find new treatments', 'Medical research has improved many treatments.', 'Lukmançylyk ylmy barlaglary köp bejergini gowulandyrdy.', 'B2'),
    ('national park', '/ˌnæʃnəl ˈpɑːk/', 'N', 'milli seýilgäh', 'национальный парк', 'a large area of countryside protected by a government', 'We saw wild horses in the national park.', 'Milli seýilgähde ýabany atlary gördük.', 'A2'),
    ('conservation area', '/ˌkɒnsəˈveɪʃn ˌeəriə/', 'N', 'tebigaty goraýyş zolagy', 'охраняемая природная территория', 'an area protected to preserve nature or wildlife', 'The wetland is a conservation area for rare birds.', 'Batgalyk seýrek guşlar üçin tebigaty goraýyş zolagydyr.', 'B2'),
    ('endangered species', '/ɪnˌdeɪndʒəd ˈspiːʃiːz/', 'N', 'ýok bolup gitmek howpyndaky görnüş', 'виды под угрозой исчезновения', 'types of animals or plants that may soon disappear', 'The reserve protects several endangered species.', 'Goraghana ýok bolup gitmek howpyndaky birnäçe görnüşi goraýar.', 'B2'),
    ('in captivity', '/ɪn kæpˈtɪvəti/', 'PHR', 'ýesirlikde, kapasada', 'в неволе', 'kept in a cage or controlled environment', 'Some of these birds were born in captivity.', 'Bu guşlaryň käbiri kapasada dünýä indi.', 'B2'),
    ('breed', '/briːd/', 'V', 'köpeltmek, nesil öndürmek', 'разводить', 'to keep animals so that they produce young', 'The centre breeds rare birds for release into the wild.', 'Merkez seýrek guşlary tebigata goýbermek üçin köpeldýär.', 'B1'),
    ('reintroduce', '/ˌriːɪntrəˈdjuːs/', 'V', 'täzeden tebigata goýbermek', 'повторно выпустить', 'to bring an animal or plant back to an area where it lived before', 'They hope to reintroduce wolves to the region.', 'Olar möjekleri sebite täzeden goýbermegi umyt edýärler.', 'C1'),
    ('inhumane', '/ˌɪnhjuːˈmeɪn/', 'ADJ', 'rehimsiz, adamkärçiliksiz', 'негуманный', 'cruel and causing unnecessary suffering', 'The animals were kept in inhumane conditions.', 'Haýwanlar rehimsiz şertlerde saklanypdyr.', 'C1'),
    ('veal calf', '/ˈviːl kɑːf/', 'N', 'göle eti üçin ösdürilýän göle', 'телёнок на откорм', 'a young calf raised for its meat', 'The report discussed the treatment of veal calves.', 'Hasabat göle eti üçin ösdürilýän gölelere çemeleşmäni ara alyp maslahatlaşdy.', 'C1'),
    ('circus', '/ˈsɜːkəs/', 'N', 'sirk', 'цирк', 'a show with performers and sometimes trained animals', 'The town banned wild animals from the circus.', 'Şäher ýabany haýwanlaryň sirkde çykyş etmegini gadagan etdi.', 'A2'),
]

# ---- Vocabulary Bank — Preparing food -> 9B ----
T['preparing_food'] = [
    ('beat', '/biːt/', 'V', 'çalmak (ýumurtga)', 'взбивать', 'to mix quickly, like eggs', 'Beat the eggs with sugar.', 'Ýumurtgalary şeker bilen çal.', 'A2', 'beat the eggs'),
    ('dice', '/daɪs/', 'V', 'kubik dogramak', 'нарезать кубиками', 'to cut into small cubes', 'Dice the onions and carrots.', 'Sogany we käşiri kubik dogra.', 'B1'),
    ('grate', '/ɡreɪt/', 'V', 'gyrkmak (rende)', 'тереть на тёрке', 'to rub food into small pieces', 'Grate the cheese over the pasta.', 'Peýniri makaronyň üstüne gyrk.', 'B1', 'grate the cheese'),
    ('knead', '/niːd/', 'V', 'ýugurmak (hamyr)', 'месить (тесто)', 'to press dough with the hands', 'Knead the dough for ten minutes.', 'Hamry on minut ýugur.', 'B1'),
    ('melt', '/melt/', 'V', 'eremek', 'таять, топить', 'to become liquid with heat', 'Melt the butter in a pan.', 'Ýagy gazanda eredýiň.', 'A2', 'melt the butter'),
    ('peel', '/piːl/', 'V', 'gabygyny soýmak', 'чистить (кожуру)', 'to take the skin off fruit', 'Peel the potatoes first.', 'Ilki ýeralmanyň gabygyny sow.', 'A2', 'peel the potatoes'),
    ('saucepan', '/ˈsɔːspən/', 'N', 'gazanjagaz', 'кастрюля', 'a deep pan for cooking', 'Put the milk in a saucepan.', 'Süýdi gazanjagaza guý.', 'A2'),
    ('seasoning', '/ˈsiːznɪŋ/', 'N', 'tagam beriji', 'приправа', 'salt, pepper and herbs', 'Add seasoning to taste.', 'Tagamyna görä tagam beriji goşuň.', 'B1', 'add seasoning'),
    ('sieve', '/sɪv/', 'N', 'ele', 'сито', 'a tool with holes for separating', 'Sift the flour through a sieve.', 'Uny elekden geçir.', 'B2', 'through a sieve'),
    ('simmer', '/ˈsɪmə(r)/', 'V', 'haýal gaýnatmak', 'томить на медленном огне', 'to cook just below boiling', 'Simmer the soup for twenty minutes.', 'Çorbany ýigrimi minut haýal gaýnat.', 'B1'),
    ('whisk', '/wɪsk/', 'V', 'galtaşdyryp çalmak', 'взбивать венчиком', 'to beat with a special tool', 'Whisk the cream until thick.', 'Gaýmagy goýalýança galtaşdyryp çal.', 'B1'),
    ('marinade', '/ˈmærɪneɪd/', 'V', 'duzlama ýatyrmak', 'мариновать', 'to leave food in a flavoured liquid', 'Marinade the chicken for an hour.', 'Towugy bir sagat duzlamada ýatyryň.', 'B1'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('bake', '/beɪk/', 'V', 'peçde bişirmek', 'печь', 'to cook food in an oven', 'We baked figs with honey for dessert.', 'Süýjülik üçin injiri bal bilen peçde bişirdik.', 'A2', 'bake a cake'),
    ('barbecue', '/ˈbɑːbɪkjuː/', 'V', 'otda, gözenekde bişirmek', 'жарить на гриле', 'to cook food over an open fire or hot coals', 'They barbecued pork ribs in the garden.', 'Olar bagda doňuz gapyrgasyny otda bişirdiler.', 'B1'),
    ('boil', '/bɔɪl/', 'V', 'gaýnatmak', 'варить', 'to cook food in water that is bubbling', 'Boil the rice for fifteen minutes.', 'Tüwini on bäş minut gaýnat.', 'A2'),
    ('chop', '/tʃɒp/', 'V', 'ownuk dogramak', 'рубить, нарезать', 'to cut something into small pieces', 'Chop the parsley before adding it to the sauce.', 'Sousa goşmazdan öň petruşkany ownuk dogra.', 'B1'),
    ('deep-fry', '/ˌdiːp ˈfraɪ/', 'V', 'köp gyzgyn ýagda gowurmak', 'жарить во фритюре', 'to cook food completely covered in hot oil', 'They deep-fried the onion rings until golden.', 'Sogan halkalaryny altynsow bolýança köp ýagda gowurdylar.', 'B2'),
    ('grill', '/ɡrɪl/', 'V', 'grilde ýa-da otda bişirmek', 'жарить на гриле', 'to cook food on a metal frame over heat', 'We grilled the fish with lemon.', 'Balygy limon bilen grilde bişirdik.', 'A2'),
    ('mash', '/mæʃ/', 'V', 'ezmek', 'разминать', 'to crush cooked food until it is soft', 'Mash the potatoes with a little butter.', 'Ýeralmany azajyk ýag bilen ez.', 'B1'),
    ('mince', '/mɪns/', 'V', 'maýda edip çapmak', 'мелко нарезать', 'to cut food into very small pieces', 'Mince the beef and fry it with onions.', 'Sygyr etini maýda çapyp, sogan bilen gowur.', 'B2'),
    ('poach', '/pəʊtʃ/', 'V', 'suwda ýa-da başga suwuklykda pes otda bişirmek', 'варить без скорлупы; припускать', 'to cook food gently in hot water or another liquid', 'She poached an egg for breakfast.', 'Ol ertirlik üçin ýumurtgany suwda bişirdi.', 'B2'),
    ('roast', '/rəʊst/', 'V', 'peçde ýag bilen gowurmak', 'запекать, жарить', 'to cook food in an oven, usually with fat', 'We roasted lamb with garlic and herbs.', 'Guzynyň etini sarymsak we otlar bilen peçde bişirdik.', 'A2'),
    ('scramble', '/ˈskræmbl/', 'V', 'garyşdyryp gowurmak', 'готовить яичницу-болтунью', 'to cook eggs while stirring them', 'He scrambled two eggs for breakfast.', 'Ol ertirlik üçin iki ýumurtgany garyşdyryp gowurdy.', 'B2'),
    ('slice', '/slaɪs/', 'V', 'dilimlemek', 'нарезать ломтиками', 'to cut food into thin, flat pieces', 'Slice the bread while it is still warm.', 'Çöregi entek ýylyka dilimle.', 'A2'),
    ('steam', '/stiːm/', 'V', 'bugda bişirmek', 'готовить на пару', 'to cook food over boiling water', 'Steam the mussels until their shells open.', 'Midiýalary gabyklary açylýança bugda bişir.', 'B1'),
    ('stew', '/stjuː/', 'V', 'haýal gaýnadyp bişirmek', 'тушить', 'to cook food slowly in liquid', 'Stew the plums with a little sugar.', 'Erikleri azajyk şeker bilen haýal gaýnat.', 'B2'),
    ('stuff', '/stʌf/', 'V', 'içini doldurmak', 'фаршировать', 'to fill food with a mixture before cooking', 'They stuffed the chicken breast with herbs.', 'Olar towuk göwsüni otlar bilen doldurdylar.', 'B2'),
    ('toast', '/təʊst/', 'V', 'tostlamak, gyzardyp bişirmek', 'поджаривать', 'to make bread brown and crisp with heat', 'I toasted a sandwich for lunch.', 'Günortanlyk üçin sendwiçi tostladym.', 'A2'),
    ('whip', '/wɪp/', 'V', 'güýçli garyşdyryp köpürjikletmek', 'взбивать', 'to beat cream or eggs until they become light', 'Whip the cream until it forms soft peaks.', 'Gaýmagy ýumşak depeler emele gelýänçä çal.', 'B2'),
    ('baking tray', '/ˈbeɪkɪŋ treɪ/', 'N', 'peç üçin demir gap', 'противень', 'a flat metal dish used for baking food', 'Put the biscuits on a baking tray.', 'Kökeleri peç üçin demir gabyň üstünde goý.', 'B1'),
    ('chopping board', '/ˈtʃɒpɪŋ bɔːd/', 'N', 'dograma tagtasy', 'разделочная доска', 'a flat board used for cutting food', 'Use a clean chopping board for the vegetables.', 'Gök önümler üçin arassa dograma tagtasyny ulan.', 'B1'),
    ('colander', '/ˈkɒləndə/', 'N', 'süzgüçli gap', 'дуршлаг', 'a bowl with holes used for draining liquid from food', 'Drain the pasta in a colander.', 'Makaron suwuny süzgüçli gapda süz.', 'B2'),
    ('food processor', '/ˈfuːd ˌprəʊsesə/', 'N', 'azyk önümlerini ownuklaýan enjam', 'кухонный комбайн', 'an electric machine that cuts, mixes, or prepares food', 'The food processor chopped the onions in seconds.', 'Azyk enjamy sogany birnäçe sekuntda dogrady.', 'B1'),
    ('frying pan', '/ˈfraɪɪŋ pæn/', 'N', 'gowurma gap', 'сковорода', 'a flat metal pan used for frying food', 'Heat some oil in a frying pan.', 'Gowurma gapda biraz ýag gyzdyr.', 'A2'),
    ('mixing bowl', '/ˈmɪksɪŋ bəʊl/', 'N', 'garyşdyrma jamy', 'миска для смешивания', 'a large bowl used for mixing ingredients', 'Put the flour and eggs in a mixing bowl.', 'Uny we ýumurtgalary garyşdyrma jamyna sal.', 'B1'),
    ('scales', '/skeɪlz/', 'N', 'tereziler', 'весы', 'a device for measuring how heavy something is', 'Use kitchen scales to weigh the flour.', 'Uny ölçemek üçin aşhana terezisini ulan.', 'A2'),
    ('spatula', '/ˈspætʃələ/', 'N', 'spatula, tekiz aşhana pilçesi', 'лопатка', 'a flat tool used for mixing or turning food', 'Turn the pancakes with a spatula.', 'Blini spatula bilen öwür.', 'B2'),
]

# ---- in-lesson 10A — word building ----
T['word_building2'] = [
    ('achievement', '/əˈtʃiːvmənt/', 'N', 'üstünlik (gazanylan)', 'достижение', 'something important you succeed in', 'Graduating was a great achievement.', 'Uniwersiteti gutarmak uly üstünlik boldy.', 'A2', 'great achievement'),
    ('agreement', '/əˈɡriːmənt/', 'N', 'ylalaşyk', 'соглашение', 'a decision people accept together', 'Both sides signed the agreement.', 'Iki tarap hem ylalaşyga gol çekdi.', 'A2', 'sign an agreement'),
    ('appointment', '/əˈpɔɪntmənt/', 'N', 'bellenen wagt (duşuşyk)', 'встреча, запись (на приём)', 'an arranged meeting', 'I have a dentist appointment at four.', 'Sagat dörtde diş lukmanyna ýazyldym.', 'A2', 'make an appointment'),
    ('arrangement', '/əˈreɪndʒmənt/', 'N', 'gurnama (meýilleşdirme)', 'договорённость', 'a plan made for something', 'We made arrangements for the trip.', 'Syýahat üçin gurnama etdik.', 'A2', 'make arrangements'),
    ('assessment', '/əˈsesmənt/', 'N', 'bahalandyryş', 'оценка, аттестация', 'a judgement of quality', 'The assessment takes one hour.', 'Bahalandyryş bir sagat alýar.', 'B1', 'assessment test'),
    ('commitment', '/kəˈmɪtmənt/', 'N', 'ygrarlylyk', 'преданность, обязательство', 'a promise to work hard at something', 'The job needs real commitment.', 'Iş hakyky ygrarlylyk talap edýär.', 'B1', 'make a commitment'),
    ('development', '/dɪˈveləpmənt/', 'N', 'ösüş', 'развитие', 'the process of growing', 'The city saw rapid development.', 'Şäher çalt ösüş gördi.', 'A2', 'economic development'),
    ('employment', '/ɪmˈplɔɪmənt/', 'N', 'iş bilen üpjünçilik', 'занятость', 'having a paid job', 'Employment rose in the spring.', 'Ýazda iş bilen üpjünçilik artdy.', 'B1', 'full employment'),
    ('entertainment', '/ˌentəˈteɪnmənt/', 'N', 'güýme', 'развлечение', 'things that amuse people', 'The city offers great entertainment.', 'Şäher ajaýyp güýme hödürleýär.', 'A2', 'live entertainment'),
    ('equipment', '/ɪˈkwɪpmənt/', 'N', 'enjam', 'оборудование', 'the things needed for an activity', 'The camping equipment is new.', 'Kemping enjamy täze.', 'A2', 'sports equipment'),
    ('failure', '/ˈfeɪljə(r)/', 'N', 'şowsuzlyk', 'неудача, провал', 'not succeeding', 'Failure taught him a lot.', 'Şowsuzlyk oňa köp zat övretdi.', 'A2', 'fear of failure'),
    ('payment', '/ˈpeɪmənt/', 'N', 'töleg', 'платёж', 'the act of paying', 'Payment is due at the end of the month.', 'Töleg aýyň ahyrynda edilmeli.', 'A2', 'make a payment'),
    ('performance', '/pəˈfɔːməns/', 'N', 'çykyş (tomaşa)', 'выступление, представление', 'a show or act', 'Her performance was brilliant.', 'Çykyşy ajaýyp boldy.', 'A2', 'live performance'),
    ('replacement', '/rɪˈpleɪsmənt/', 'N', 'çalşylma (çalyşma)', 'замена', 'a person or thing that replaces another', 'We need a replacement for the old printer.', 'Köne printere çalşylma gerek.', 'B1', 'replacement parts'),
    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.
    ('width', '/wɪdθ/', 'N', 'ini', 'ширина', 'the distance from one side of something to the other', 'Measure the width of the table.', 'Stoluň inini ölçäň.', 'B1'),
    ('depth', '/depθ/', 'N', 'çuňlugy', 'глубина', 'the distance from the top or front of something to its bottom or back', 'The depth of the pool is marked on the wall.', 'Howzuň çuňlugy diwarda görkezilen.', 'B1'),
    ('length', '/leŋθ/', 'N', 'uzynlygy', 'длина', 'the measurement from one end of something to the other', 'The bridge is one kilometre in length.', 'Köpriniň uzynlygy bir kilometr.', 'A2'),
    ('height', '/haɪt/', 'N', 'beýikligi', 'высота', 'the distance from the bottom to the top of something', 'What is the height of the building?', 'Binanyň beýikligi näçe?', 'A2'),
    ('weak', '/wiːk/', 'ADJ', 'gowşak', 'слабый', 'not strong or powerful', 'The signal is weak in this room.', 'Bu otagda signal gowşak.', 'A2'),
    ('weaken', '/ˈwiːkən/', 'V', 'gowşamak, gowşatmak', 'ослабевать, ослаблять', 'to become less strong or make something less strong', 'The storm weakened during the night.', 'Tupan gijäniň dowamynda gowşady.', 'B1'),
    ('strength', '/streŋθ/', 'N', 'güýç', 'сила', 'the quality of being physically or mentally strong', 'Swimming can improve your strength.', 'Ýüzmek güýjüňi artdyryp biler.', 'A2'),
    ('strengthen', '/ˈstreŋθən/', 'V', 'güýçlendirmek', 'укреплять', 'to make something stronger', 'The new rules should strengthen the team.', 'Täze düzgünler topary güýçlendirmeli.', 'B1'),
]

# ---- in-lesson 10B — words often confused ----
T['confused_words'] = [
    ('advice', '/ədˈvaɪs/', 'N', 'maslahat', 'совет (существительное)', 'an opinion about what to do', 'She gave me good advice.', 'Gowy maslahat berdi.', 'A2', 'a piece of advice'),
    ('advise', '/ədˈvaɪz/', 'V', 'maslahat bermek', 'советовать', 'to give an opinion about what to do', 'I advise you to see a doctor.', 'Lukmana görünmegi maslahat berýärin.', 'A2', 'advise someone to do'),
    ('beside', '/bɪˈsaɪd/', 'PREP', 'ýanynda', 'рядом с', 'next to something', 'The bag is beside the door.', 'Sumka gapynyň ýanynda.', 'A2'),
    ('besides', '/bɪˈsaɪdz/', 'ADV', 'mundan başga-da', 'кроме того', 'in addition', 'Besides, it was too late.', 'Mundan başga-da, gaty giçdi.', 'A2'),
    ('compliment', '/ˈkɒmplɪmənt/', 'N', 'taryp', 'комплимент', 'words that praise someone', 'He paid her a nice compliment.', 'Oňa owadan taryp aýtdy.', 'A2', 'pay a compliment'),
    ('complement', '/ˈkɒmplɪment/', 'V', 'üstüni ýetirmek', 'дополнять', 'to go well with something', 'The sauce complements the fish.', 'Sous balygyň üstüni ýetirýär.', 'B2'),
    ('economic', '/ˌiːkəˈnɒmɪk/', 'ADJ', 'ykdysady', 'экономический', 'about the economy', 'The country faces economic problems.', 'Ýurt ykdysady kynçylyklar bilen ýüzbe-ýüz.', 'A2', 'economic growth'),
    ('historic', '/hɪˈstɒrɪk/', 'ADJ', 'taryhy (möhüm)', 'исторический (знаменательный)', 'famous in history', 'It was a historic victory.', 'Taryhy ýeňiş boldy.', 'B1', 'historic event'),
    ('historical', '/hɪˈstɒrɪkl/', 'ADJ', 'taryhy (taryha degişli)', 'исторический (связанный с историей)', 'about the past', 'She loves historical novels.', 'Taryhy romanlary gowy görýär.', 'B1', 'historical novel'),
    ('job', '/dʒɒb/', 'N', 'iş (bir wezipe)', 'работа (конкретная)', 'a particular piece of work', 'He found a new job in May.', 'Maý aýynda täze iş tapdy.', 'A1'),
    ('shade', '/ʃeɪd/', 'N', 'kölege (ýagtylykdan)', 'тень (от солнца)', 'a place protected from sun', 'We sat in the shade of the tree.', 'Agaçyň kölegesinde oturduk.', 'A2', 'in the shade'),
    ('shadow', '/ˈʃædəʊ/', 'N', 'saýa', 'тень (силуэт)', 'a dark shape made by light', 'His shadow stretched across the wall.', 'Saýasy diwara düşdi.', 'A2', 'cast a shadow'),
    ('travel', '/ˈtrævl/', 'N', 'syýahat', 'путешествие (вообще)', 'the activity of travelling', 'Air travel is cheaper now.', 'Howa syýahaty indi arzan.', 'A1', 'air travel'),
    ('trip', '/trɪp/', 'N', 'sapar (gysga)', 'поездка (конкретная)', 'a short journey somewhere', 'We had a lovely trip to the mountains.', 'Daglara ajaýyp sapar etdik.', 'A1', 'day trip'),
    ('price', '/praɪs/', 'N', 'baha (satuwda)', 'цена', 'the amount something costs', 'The price includes breakfast.', 'Baha ertirligi hem öz içine alýar.', 'A1', 'ticket price'),
    ('prize', '/praɪz/', 'N', 'baýrak', 'приз, премия', 'something won in a competition', 'She won first prize.', 'Birinji baýragy gazandy.', 'A2', 'win a prize'),
]

# ---- Colloquial English episodes ----
T['ce_work_family'] = [
    ('How do you manage?', '/haʊ du ju ˈmænɪdʒ/', 'PHR', 'Nädip hötdeleýärsiň?', 'Как вы справляетесь?', 'used to ask how someone copes', 'How do you manage with two jobs?', 'Iki işi nädip hötdeleýärsiň?', 'A2'),
    ('work-life balance', '/ˌwɜːk laɪf ˈbæləns/', 'N', 'iş-öý deňagramlylygy', 'баланс работы и жизни', 'an equal mix of work and home life', 'Good work-life balance keeps you healthy.', 'Gowy iş-öý deňagramlylygy sagdyn saklaýar.', 'B1'),
    ('I work from home.', '/aɪ wɜːk frɒm həʊm/', 'PHR', 'Öýden işleýärin.', 'Я работаю из дома.', 'used to say where you work', 'I work from home twice a week.', 'Hepdede iki gezek öýden işleýärin.', 'A2'),
    ('It runs in the family.', '/ɪt rʌnz ɪn ðə ˈfæməli/', 'PHR', 'Maşgalada bar.', 'Это семейное (передаётся по наследству).', 'used when a trait is inherited', 'Musical talent — it runs in the family.', 'Saz zehini — maşgalada bar.', 'B1'),
    ('family business', '/ˈfæməli ˈbɪznəs/', 'N', 'maşgala kärhanasy', 'семейный бизнес', 'a company owned by a family', 'They run a small family business.', 'Kiçi maşgala kärhanasyny dolandyrýarlar.', 'A2'),
    ('the breadwinner', '/ðə ˈbredwɪnə(r)/', 'N', 'maşgala ekleýji', 'кормилец', 'the person who earns for a family', 'She is the main breadwinner.', 'Maşgalanyň esasy ekleýjisi ol.', 'B2'),
    ('work long hours', '/wɜːk lɒŋ ˈaʊəz/', 'PHR', 'uzak sagat işlemek', 'работать подолгу', 'to work a lot', 'Doctors often work long hours.', 'Lukmanlar köplenç uzak sagat işleýär.', 'A2'),
    ('quality time', '/ˈkwɒləti taɪm/', 'N', 'hil wagty (maşgala bilen)', 'качественное время (с близкими)', 'time spent giving full attention', 'Spend quality time with your children.', 'Çagalaryňyz bilen hil wagtyny geçiriň.', 'A2'),
]

T['ce_history'] = [
    ('date back to', '/deɪt bæk tuː/', 'PHR', 'şol döwürden galan', 'относиться к (о времени)', 'used to say how old something is', 'The castle dates back to the twelfth century.', 'Gala on ikinji asyrdan galan.', 'A2'),
    ('steeped in history', '/stiːpt ɪn ˈhɪstri/', 'PHR', 'taryha baý', 'насыщенный историей', 'used for very historic places', 'The old city is steeped in history.', 'Köne şäher taryha baý.', 'B2'),
    ('ancient ruins', '/ˈeɪnʃnt ˈruːɪnz/', 'N', 'gadymy harabalar', 'древние руины', 'old buildings that have fallen', 'We explored the ancient ruins.', 'Gadymy harabalary öwrendik.', 'A2'),
    ('a turning point', '/ə ˈtɜːnɪŋ pɔɪnt/', 'N', 'öwrülişik nokady', 'поворотный момент', 'a moment that changes everything', 'The battle was a turning point.', 'Söweş öwrülişik nokady boldy.', 'B1'),
    ('go down in history', '/ɡəʊ daʊn ɪn ˈhɪstri/', 'PHR', 'taryha girmek', 'войти в историю', 'to be remembered for ever', 'She went down in history as a pioneer.', 'Öňdebaryjy hökmünde taryha girdi.', 'A2'),
    ('back in the day', '/bæk ɪn ðə deɪ/', 'PHR', 'köne döwürlerde', 'в былые времена', 'used about the past', 'Back in the day, there was no internet.', 'Köne döwürlerde internet ýokdy.', 'A2'),
    ('living history', '/ˈlɪvɪŋ ˈhɪstri/', 'N', 'ýaşaýan taryh', 'живая история', 'old traditions still alive today', 'The market is living history.', 'Bazar ýaşaýan taryh.', 'B1'),
    ('pass into legend', '/pɑːs ˈɪntə ˈledʒənd/', 'PHR', 'rowaýata öwrülmek', 'войти в легенды', 'to become famous in stories', 'The hero passed into legend.', 'Gahryman rowaýata öwrüldi.', 'B2'),
]

T['ce_stress'] = [
    ('I\'m stressed out.', '/aɪm ˌstrest ˈaʊt/', 'PHR', 'Dartgynly ýagdaýda.', 'Я в стрессе.', 'used to say you feel too much pressure', 'I am stressed out before exams.', 'Synagdan öň dartgynly ýagdaýda bolýaryn.', 'A2'),
    ('wind down', '/waɪnd daʊn/', 'PHR', 'köşeşmek (dynç almak)', 'расслабляться (постепенно)', 'to relax after activity', 'I wind down with a book.', 'Kitap bilen köşeşýärin.', 'B1'),
    ('recharge my batteries', '/ˌriːˈtʃɑːdʒ maɪ ˈbætriz/', 'PHR', 'güýjümi dikeltmek', 'подзарядиться', 'to get energy back', 'A weekend at the lake recharges my batteries.', 'Köl kenaryndaky hepde ahyry güýjümi dikeldýär.', 'A2'),
    ('helps me unwind', '/helps miː ˌʌnˈwaɪnd/', 'PHR', 'maňa köşeşmäge kömek edýär', 'помогает мне расслабиться', 'used to say what relaxes you', 'Walking helps me unwind.', 'Ýöremek maňa köşeşmäge kömek edýär.', 'A2'),
    ('burnout', '/ˈbɜːnaʊt/', 'N', 'ýadawlyk (işden)', 'выгорание', 'exhaustion from working too hard', 'He had to stop working to avoid burnout.', 'Ýadawlykdan gaça durmak üçin işi bes etmeli boldy.', 'B2'),
    ('chill out', '/tʃɪl aʊt/', 'PHR', 'dynç almak (gowşurmak)', 'расслабиться, отдохнуть', 'to relax completely', 'Let us chill out by the pool.', 'Geliň, howzuň ýanynda dynç alalyň.', 'A2'),
    ('at breaking point', '/ət ˈbreɪkɪŋ pɔɪnt/', 'PHR', 'çydap bilmeýän ýagdaýda', 'на грани срыва', 'almost unable to cope', 'She was at breaking point after the exams.', 'Synaglardan soň çydap bilmeýän ýagdaýda boldy.', 'B2'),
    ('let off steam', '/let ɒf stiːm/', 'PHR', 'gaharyny çykarmak', 'выпустить пар', 'to get rid of strong feelings', 'He runs to let off steam.', 'Gaharyny çykarmak üçin ylgaw edýär.', 'B1'),
]

T['ce_illustration'] = [
    ('beautifully illustrated', '/ˈbjuːtɪfli ˈɪləstreɪtɪd/', 'ADJ', 'owadan suratlandyrylan', 'красочно иллюстрированный', 'with lovely pictures', 'It is a beautifully illustrated book.', 'Owadan suratlandyrylan kitap.', 'A2'),
    ('bring it to life', '/brɪŋ ɪt tuː laɪf/', 'PHR', 'jana getirýär', 'оживляет', 'used when pictures make a story vivid', 'The drawings bring the story to life.', 'Çyzgylar hekaýany jana getirýär.', 'A2'),
    ('graphic novel', '/ˈɡræfɪk ˈnɒvl/', 'N', 'komiks roman', 'графический роман', 'a novel told in pictures', 'He reads graphic novels.', 'Komiks romanlary okaýar.', 'B1'),
    ('eye-catching', '/ˈaɪ kætʃɪŋ/', 'ADJ', 'göze ilýän', 'бросающийся в глаза', 'immediately noticed', 'The poster is very eye-catching.', 'Plakat gaty göze ilýän.', 'B1'),
    ('the visuals', '/ðə ˈvɪʒuəlz/', 'N', 'wizual taraplary', 'визуальный ряд', 'the images in a film or book', 'The visuals are stunning.', 'Wizual taraplary haýran galdyryjy.', 'B2'),
    ('The cover draws you in.', '/ðə ˈkʌvə(r) drɔːz juː ɪn/', 'PHR', 'Muqawasy özüne çekýär.', 'Обложка притягивает.', 'used to praise a book cover', 'The cover draws you in immediately.', 'Muqawasy dessine özüne çekýär.', 'A2'),
    ('caption', '/ˈkæpʃn/', 'N', 'surat ýazgysy', 'подпись (к рисунку)', 'words under a picture', 'Read the caption below the photo.', 'Suratyň aşagyndaky ýazgyny oka.', 'B1', 'photo caption'),
    ('full-page spread', '/ˌfʊl peɪdʒ ˈspred/', 'N', 'tutuş sahypa ýaýran', 'разворот на всю страницу', 'a picture across a whole page', 'The map is a full-page spread.', 'Karta tutuş sahypa ýaýran.', 'B2'),
]

T['ce_insects'] = [
    ('give me the creeps', '/ɡɪv miː ðə kriːps/', 'PHR', 'tenim ürkýär', 'меня пробирает дрожь', 'used to say something scares you', 'Spiders give me the creeps.', 'Mör-möjekler tenimi ürküzýär.', 'A2'),
    ('bee sting', '/ˈbiː stɪŋ/', 'N', 'ary çakmasy', 'укус пчелы', 'a wound from a bee', 'A bee sting can hurt a lot.', 'Ary çakmasy gaty agyryp biler.', 'A2'),
    ('insect bite', '/ˈɪnsekt baɪt/', 'N', 'möjek çakmasy', 'укус насекомого', 'a mark from an insect', 'Put cream on the insect bite.', 'Möjek çakmasyna krem çal.', 'A2'),
    ('creepy-crawly', '/ˈkriːpi krɔːli/', 'N', 'ýyldyryjy mör-möjek', 'букашка (разг.)', 'an insect or spider (informal)', 'There is a creepy-crawly on the wall!', 'Diwarda ýyldyryjy mör-möjek bar!', 'A2'),
    ('harmless', '/ˈhɑːmləs/', 'ADJ', 'zyýansyz', 'безвредный', 'causing no harm', 'The spider is completely harmless.', 'Mör-möjek düýbünden zyýansyz.', 'A2'),
    ('leave it alone', '/liːv ɪt əˈləʊn/', 'PHR', 'Ona degme.', 'Не трогай его.', 'used to say do not disturb', 'That beetle is harmless — leave it alone.', 'Şol tomzak zyýansyz — ona degme.', 'A2'),
    ('spider web', '/ˈspaɪdə(r) web/', 'N', 'möjek tory', 'паутина', 'the net a spider spins', 'A spider web covered the corner.', 'Möjek tory burçy örtüpdi.', 'A2'),
    ('swarm', '/swɔːm/', 'N', 'topar (mör-möjek)', 'рой', 'a large moving group of insects', 'A swarm of bees flew past.', 'Ary topary uçup geçdi.', 'B1', 'a swarm of bees'),
]
LESSONS = {
    '1A': (1,  'We are family', 'personality', ['personality']),
    '1B': (1,  'A job for life?', 'work', ['work2']),
    '2A': (2,  'Do you remember...?', 'word building: abstract nouns', ['abstract_nouns']),
    '2B': (2,  'On the tip of my tongue', 'lexical areas: relationships', ['relationships']),
    '3A': (3,  'A love-hate relationship', 'phrases with get', ['get_phrases']),
    '3B': (3,  'Dramatic licence', 'conflict and warfare', ['conflict']),
    '4A': (4,  'An open book', 'describing books and films', ['books_films']),
    '4B': (4,  'The sound of silence', 'sounds and the human voice', ['voice']),
    '5A': (5,  'No time for anything', 'expressions with time', ['time_expr']),
    '5B': (5,  'Not for profit?', 'money', ['money2']),
    '6A': (6,  'Help, I need somebody!', 'compound adjectives', ['compound_adjs2']),
    '6B': (6,  "Can't give it up", 'phones, technology, adjectives + prepositions', ['phones_tech', 'adjectives_preps']),
    '7A': (7,  'As a matter of fact...', 'word formation: prefixes', ['prefixes']),
    '7B': (7,  'A masterpiece?', 'art · colour idioms', ['art_colour']),
    '8A': (8,  'The best medicine?', 'health and medicine', ['health']),
    '8B': (8,  "A 'must-see' attraction", 'travel and tourism', ['travel_tourism']),
    '9A': (9,  'Pet hates', 'animal matters', ['animal_matters']),
    '9B': (9,  'How to cook, how to eat', 'preparing food', ['preparing_food']),
    '10A': (10, 'On your marks, set, go!', 'word building: adjectives, nouns, and verbs', ['word_building2']),
    '10B': (10, 'No direction home', 'words that are often confused', ['confused_words']),
}

WORD_LESSON = {}


def lesson_for(topic, en, fallback):
    key = en.strip().lower()
    return WORD_LESSON.get(key, fallback)


# Advanced has ten units; the five Colloquial English episodes sit after
# units 1, 3, 5, 7 and 9 in the book. In the data they carry unit 11 so they
# do not collide with the real units, and the app shows each episode right
# after the unit it follows.
PE_UNIT = 11
for code, n, title, topic, key in (
    ('CE1', 11, 'Talking about work and family', 'colloquial English 1', 'ce_work_family'),
    ('CE2', 11, 'Talking about history', 'colloquial English 2 and 3', 'ce_history'),
    ('CE3', 11, 'Talking about stress and relaxation', 'colloquial English 4 and 5', 'ce_stress'),
    ('CE4', 11, 'Talking about illustration', 'colloquial English 6 and 7', 'ce_illustration'),
    ('CE5', 11, 'Talking about insects and animals', 'colloquial English 8 and 9', 'ce_insects'),
):
    LESSONS[code] = (PE_UNIT, title, topic, [key])


def lesson_sort_key(code):
    m = re.match(r'^(\d+)(.*)$', code)
    if m:
        return (int(m.group(1)), m.group(2))
    return (11, code)


# Printed Student’s Book pages for exact source provenance. Vocabulary Banks use their back-of-book pages.
TOPIC_PAGE = {'personality': 162, 'work2': 163, 'get_phrases': 164, 'conflict': 165, 'voice': 166, 'time_expr': 167, 'money2': 168, 'prefixes': 169, 'travel_tourism': 170, 'animal_matters': 171, 'preparing_food': 172, 'compound_adjs2': 59, 'phones_tech': 60, 'adjectives_preps': 63, 'health': 76, 'word_building2': 97}
LESSON_PAGE = {'1A': 6, '1B': 10, 'CE1': 14, '2A': 16, '2B': 20, '3A': 26, '3B': 30, 'CE2': 34, '4A': 36, '4B': 40, '5A': 46, '5B': 50, 'CE3': 54, '6A': 56, '6B': 60, '7A': 65, '7B': 70, 'CE4': 74, '8A': 76, '8B': 80, '9A': 86, '9B': 90, 'CE5': 94, '10A': 96, '10B': 100}

def main():
    words, seen, dups = [], {}, []

    for lesson in sorted(LESSONS, key=lesson_sort_key):
        unit, title, topic, topics = LESSONS[lesson]
        if lesson[0].isdigit() and lesson[:-1] != str(unit):
            raise SystemExit(f'lesson {lesson} says unit {unit}')
        for t in topics:
            if t not in T:
                raise SystemExit(f'lesson {lesson} refers to unknown topic "{t}"')
            for e in T[t]:
                if lesson_for(t, e[0], lesson) != lesson:
                    continue   # this word belongs to another lesson
                en, ipa, pos, tm, ru, de, ex, exTm, cefr = e[:9]
                coll = e[9] if len(e) > 9 else ''
                key = en.strip().lower()
                if key in seen:
                    dups.append(f'{lesson}: "{en}" (already in {seen[key]})')
                    continue
                seen[key] = lesson
                words.append({
                    'en': en, 'ipa': ipa, 'pos': pos, 'tm': tm, 'ru': ru,
                    'def': de, 'ex': ex, 'exTm': exTm, 'cefr': cefr,
                    'ox': 'Oxford 3000' if cefr in ('A1', 'A2') else 'Oxford 5000',
                    'syn': '—', 'coll': coll or '—', 'stage': 'New',
                    'books': [{'book': 'adv', 'unit': unit, 'lesson': lesson,
                               'page': TOPIC_PAGE.get(t, LESSON_PAGE.get(lesson))}],
                    'proofread': False,
                    'confidence': 'medium' if key in {'sore throat', 'sneeze', 'high temperature', 'fever', 'aches and pains'} else 'high',
                })

    if dups:
        raise SystemExit('duplicate headwords:\n  ' + '\n  '.join(dups))

    used = set(t for ts in LESSONS.values() for t in ts[3])
    unused = sorted(set(T) - used)
    if unused:
        raise SystemExit('topics declared but never used by a lesson: ' + ', '.join(unused))

    lessons = []
    empty = []
    for lesson in sorted(LESSONS, key=lesson_sort_key):
        unit, title, topic, topics = LESSONS[lesson]
        n = sum(1 for w in words if w['books'][0]['lesson'] == lesson)
        if not n:
            empty.append(lesson)
            continue
        lessons.append({'lesson': lesson, 'unit': unit, 'title': title, 'topic': topic,
                        'words': n})
    if empty:
        raise SystemExit('lessons with no words — fill them: ' + ', '.join(empty))

    pack = {
        'book': 'adv',
        'title': 'English File Advanced (4th edition) — vocabulary, by lesson',
        'lessons': lessons,
        'words': words,
    }
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(pack, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f'wrote {os.path.normpath(OUT)}: {len(words)} words, {len(lessons)} lessons')
    by_unit = {}
    for l in lessons:
        by_unit.setdefault(l['unit'], []).append(l)
    for unit in sorted(by_unit):
        print(f"\nunit {unit:>2} — {sum(l['words'] for l in by_unit[unit])} words")
        for l in by_unit[unit]:
            print(f"    {l['lesson']:<4} {l['words']:>3} words  {l['title']}")


if __name__ == '__main__':
    main()
