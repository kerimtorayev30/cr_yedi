#!/usr/bin/env python3
"""One-shot curator patch: append reviewed Advanced vocabulary and provenance."""
import ast, json, re
from pathlib import Path

ROOT = Path('/home/user')
GEN = ROOT / 'content/tools/gen_adv.py'
OUT = ROOT / 'content/pdf/adv-candidates.json'
ADDITIONS = {}

# Each E tuple follows gen_adv.py's word row layout.
def E(en, ipa, pos, tm, ru, definition, example, ex_tm, cefr='B1', coll=None):
    row = (en, ipa, pos, tm, ru, definition, example, ex_tm, cefr)
    return row + ((coll,) if coll else ())

ADDITIONS['personality'] = [
 E('bright','/braɪt/','ADJ','zehinli','сообразительный','intelligent and quick to learn','She is a bright student who asks good questions.','Ol gowy soraglary berýän zehinli talyp.','A2'),
 E('conscientious','/ˌkɒnʃiˈenʃəs/','ADJ','jogapkärli, ünsli','добросовестный','careful to do your work well and properly','A conscientious employee checks every detail.','Jogapkärli işgär her jikme-jigi barlaýar.','B2'),
 E('determined','/dɪˈtɜːmɪnd/','ADJ','tutanýerli, aýgytly','решительный','not willing to give up','She was determined to finish the course.','Ol okuwy tamamlamagy ýüregine düwdi.','B1'),
 E('resourceful','/rɪˈzɔːsfl/','ADJ','ugurtapyjy','находчивый','good at finding quick ways to solve problems','The resourceful team fixed the problem quickly.','Ugurtapyjy topar meseläni tiz çözdi.','B2'),
 E('sarcastic','/sɑːˈkæstɪk/','ADJ','kinayeli','саркастичный','using words that mean the opposite to mock someone','His sarcastic comment made everyone uncomfortable.','Onuň kinayeli sözi hemmäni oňaýsyz ýagdaýa saldy.','B2'),
 E('self-sufficient','/ˌself səˈfɪʃnt/','ADJ','özbaşdak','самостоятельный','able to manage without help from others','The village is almost self-sufficient in food.','Oba azyk babatda diýen ýaly özbaşdak.','B2'),
 E('spontaneous','/spɒnˈteɪniəs/','ADJ','duýdansyz, öz-özünden bolan','спонтанный','done naturally without planning','We made a spontaneous decision to stay another night.','Ýene bir gije galmak barada duýdansyz karar etdik.','B2'),
 E('steady','/ˈstedi/','ADJ','durnukly, ygtybarly','устойчивый, надёжный','calm and reliable, or not changing suddenly','She has a steady personality and rarely panics.','Onuň häsiýeti durnukly, ol seýrek howsala düşýär.','B1'),
 E('straightforward','/ˌstreɪtˈfɔːwəd/','ADJ','gönümel, açyk','прямолинейный','honest and direct in what you say','He is straightforward about his opinions.','Ol pikirlerini gönümel aýdýar.','B2'),
 E('sympathetic','/ˌsɪmpəˈθetɪk/','ADJ','duýgudaş','сочувствующий','kind and understanding when someone has a problem','My manager was sympathetic when I was ill.','Kesellänimde ýolbaşçym maňa duýgudaşlyk bildirdi.','B1'),
 E('thorough','/ˈθʌrə/','ADJ','jikme-jik, örän ünsli','тщательный','careful to include every detail','The inspector made a thorough check of the building.','Barlagçy binany jikme-jik barlady.','B2'),
 E('control freak','/kənˈtrəʊl friːk/','N','hemme zady dolandyrmaga çalyşýan adam','человек, стремящийся всё контролировать','someone who insists on controlling everything','My sister is a bit of a control freak.','Uýam hemme zady dolandyrmaga biraz aşa çalyşýar.','B2'),
 E('too trusting','/tuː ˈtrʌstɪŋ/','ADJ','aşa ynanjaň','слишком доверчивый','too ready to believe that people are honest','He is too trusting and people sometimes take advantage of him.','Ol aşa ynanjaň, adamlar käwagt ondan peýdalanýarlar.','B2'),
 E('tend to','/tend tuː/','PHR','adatça etmek, meýilli bolmak','иметь склонность','to usually do or be something','I tend to avoid arguments.','Men adatça jedellerden gaça durýaryn.','B1'),
 E('come across as','/kʌm əˈkrɒs æz/','PHR','... bolup görünmek','производить впечатление','to seem to have a particular quality','She comes across as confident, but she is shy.','Ol özüne ynamly bolup görünýär, ýöne utanjaň.','B2'),
 E('deep down','/ˌdiːp ˈdaʊn/','ADV','içinden, aslynda','в глубине души','when you consider someone’s real feelings','Deep down, he knows that she is right.','Ol içinden onuň mamladygyny bilýär.','B2'),
 E('on the surface','/ɒn ðə ˈsɜːfɪs/','PHR','daşyndan seredeniňde','на первый взгляд','judging only by what is visible','On the surface, the job seems easy.','Daşyndan seredeniňde, iş aňsat ýaly.','B2'),
 E('on the whole','/ɒn ðə həʊl/','ADV','umuman alanyňda','в целом','in general, considering everything','On the whole, the team worked well together.','Umuman alanyňda, topar bilelikde gowy işledi.','B1'),
 E('heart of gold','/ˌhɑːt əv ˈɡəʊld/','PHR','altyn ýürekli','золотое сердце','a very kind and generous nature','My grandfather has a heart of gold.','Atamyň ýüregi altyn ýaly.','B2'),
 E('down to earth','/ˌdaʊn tuː ˈɜːθ/','PHR','sada we durmuşa ýakyn','простой и практичный','sensible, practical, and not pretentious','Despite her success, she is very down to earth.','Üstünlik gazansa-da, ol örän sada.','B2'),
 E('cold fish','/ˌkəʊld ˈfɪʃ/','PHR','sowukganly, duýgusyny görkezmeýän adam','холодный, замкнутый человек','an unfriendly person who does not show emotion','He seemed like a cold fish at first.','Ilkibaşda ol sowukganly adam ýaly göründi.','B2'),
 E('pain in the neck','/ˌpeɪn ɪn ðə ˈnek/','PHR','örän bizar ediji adam ýa-da zat','страшно надоедливый человек или предмет','someone or something very annoying','Waiting in that queue was a real pain in the neck.','Şol nobata garaşmak örän bizar edijidi.','B2'),
 E('soft touch','/ˌsɒft ˈtʌtʃ/','PHR','ýüregi ýumşak, aňsat razy bolýan adam','мягкий, уступчивый человек','someone who is easily persuaded to give or do something','Ask Dad for a loan; he is a soft touch.','Kakadan karz sora, ol aňsat razy bolýar.','B2'),
 E('quick temper','/ˌkwɪk ˈtempə/','PHR','çalt gaharlanýan häsiýet','вспыльчивый характер','a tendency to become angry easily','My brother has a quick temper.','Doganım çalt gaharlanýar.','B2'),
 E('full of yourself','/ˌfʊl əv jəˈself/','PHR','özüni aşa gowy görýän','самовлюблённый','too pleased with yourself and your importance','He is so full of himself that nobody enjoys his company.','Ol özüni şeýle gowy görýär welin, hiç kim onuň ýanynda bolasy gelenok.','B2'),
 E("wouldn't hurt a fly",'/ˌwʊdnt hɜːt ə ˈflaɪ/','PHR','hiç kime zyýan ýetirmez','мухи не обидит','is very gentle and harmless','She looks serious, but she wouldn’t hurt a fly.','Ol çynlakaý görünýär, ýöne hiç kime zyýan ýetirmez.','B2'),
 E('lift a finger','/ˌlɪft ə ˈfɪŋɡə/','PHR','kiçijik hem kömek etmezlik','палец о палец не ударить','to make even a small effort to help','He never lifts a finger to help with the housework.','Ol öý işlerine kömek etmek üçin barmagyny-da gymyldatmaýar.','B2'),
 E('life and soul of the party','/ˌlaɪf ən ˌsəʊl əv ðə ˈpɑːti/','PHR','oturyşyň şowhunly merkezi','душа компании','the person who makes a social event enjoyable','Mina is always the life and soul of the party.','Mina hemişe oturyşyň şowhunly merkezi bolýar.','B2'),
]

ADDITIONS['work2'] = [
 E('challenging','/ˈtʃælɪndʒɪŋ/','ADJ','kyn, synagly','сложный, требующий усилий','difficult in an interesting way','Teaching a large class can be challenging.','Uly synpa sapak bermek kyn bolup biler.','B1'),
 E('monotonous','/məˈnɒtənəs/','ADJ','birmeňzeş we ýürekgysdyryjy','монотонный','boring because it never changes','The work became monotonous after a few months.','Birnäçe aýdan soň iş birmeňzeş we ýürekgysdyryjy boldy.','B2'),
 E('repetitive','/rɪˈpetətɪv/','ADJ','gaýtalanýan','повторяющийся','involving the same actions again and again','The job is repetitive, but it is not difficult.','Iş gaýtalanýar, ýöne kyn däl.','B2'),
 E('rewarding','/rɪˈwɔːdɪŋ/','ADJ','kanagatlandyryjy','приносящий удовлетворение','making you feel that your work is valuable','Working with children is very rewarding.','Çagalar bilen işlemek örän kanagatlandyryjy.','B1'),
 E('fulfilling','/fʊlˈfɪlɪŋ/','ADJ','manyly, ruhy taýdan kanagatlandyryjy','приносящий удовлетворение','giving you a strong feeling of satisfaction','She finds her job as a nurse fulfilling.','Ol şepagat uýasy işini manyly hasaplaýar.','B2'),
 E('motivating','/ˈməʊtɪveɪtɪŋ/','ADJ','höweslendiriji','мотивирующий','making you want to work or achieve more','A supportive manager can be very motivating.','Goldaýan ýolbaşçy örän höweslendiriji bolup biler.','B2'),
 E('demanding','/dɪˈmɑːndɪŋ/','ADJ','köp güýç we zähmet talap edýän','требовательный, тяжёлый','needing a lot of time, energy, or skill','Being a surgeon is a demanding job.','Hirurg bolmak köp zähmet talap edýän iş.','B2'),
 E('tedious','/ˈtiːdiəs/','ADJ','ýürekgysdyryjy, iriziji','утомительный, скучный','boring and continuing for too long','Entering all the data by hand is tedious.','Ähli maglumatlary el bilen girizmek ýürekgysdyryjy.','B2'),
 E('dead-end','/ˌded ˈend/','ADJ','ösüş mümkinçiligi bolmadyk','бесперспективный','offering no chance of promotion or progress','He left his dead-end job and went back to college.','Ol ösüş mümkinçiligi bolmadyk işinden çykyp, kolleje dolandy.','B2'),
 E('high-powered','/ˌhaɪ ˈpaʊəd/','ADJ','ýokary derejeli we jogapkärçiligi uly','высокопоставленный','important and involving a lot of responsibility','She has a high-powered job in finance.','Maliýe ulgamynda ýokary derejeli işi bar.','B2'),
 E('career move','/kəˈrɪə muːv/','PHR','karýera ädimi','карьерный шаг','a decision that helps or changes your career','Moving abroad was a smart career move.','Daşary ýurda göçmek karýera üçin oňat ädim boldy.','B2'),
 E('job hunting','/ˈdʒɒb ˌhʌntɪŋ/','N','iş gözlemek','поиск работы','the activity of looking for a job','He is job hunting after finishing university.','Uniwersiteti tamamlandan soň ol iş gözleýär.','B1'),
 E('event manager','/ɪˈvent ˌmænɪdʒə/','N','çäreleri gurnaýjy','организатор мероприятий','a person who plans and organizes events','The event manager arranged the conference.','Çäreleri gurnaýjy maslahaty gurady.','B2'),
 E('qualification','/ˌkwɒlɪfɪˈkeɪʃn/','N','hünär derejesi, şahadatnama','квалификация','an exam result or skill needed for a job','This position requires a teaching qualification.','Bu wezipe mugallymçylyk hünär derejesini talap edýär.','B1'),
 E('work experience','/ˈwɜːk ɪkˌspɪəriəns/','N','iş tejribesi','опыт работы','knowledge and skills gained by doing a job','The advert asks for two years of work experience.','Bildirişde iki ýyl iş tejribesi soralýar.','B1'),
 E('career ladder','/kəˈrɪə ˌlædə/','N','karýera basgançagy','карьерная лестница','the series of jobs that lead to higher positions','She hopes to move up the career ladder.','Ol karýera basgançagyndan ýokary galmagy umyt edýär.','B2'),
 E('civil servant','/ˌsɪvl ˈsɜːvənt/','N','döwlet gullukçysy','государственный служащий','a person who works for a government department','My aunt is a civil servant in the health department.','Daýzam saglygy goraýyş bölüminde döwlet gullukçysy.','B2'),
 E('fast track','/ˌfɑːst ˈtræk/','N','çalt öňe gidiş ýoly','ускоренный путь к успеху','a quick route to promotion or success','The company put its best graduates on the fast track.','Kompaniýa iň gowy uçurymlaryny çalt öňe gidiş ýoluna goşdy.','B2'),
 E('colleague','/ˈkɒliːɡ/','N','işdeşim','коллега','a person you work with','One of my colleagues is moving to another office.','Işdeşlerimiň biri başga edara geçýär.','A2'),
 E('co-worker','/ˌkəʊ ˈwɜːkə/','N','işdeşim','сослуживец','a person who works with you','I get on well with my co-workers.','Işdeşlerim bilen oňat düşünişýärin.','B1'),
 E('quit','/kwɪt/','V','işden çykmak, bes etmek','увольняться, бросать','to leave a job or stop doing something','She decided to quit her job and travel.','Ol işinden çykyp, syýahat etmegi karar etdi.','A2'),
 E('resign','/rɪˈzaɪn/','V','işden meýletin çykmak','увольняться','to formally leave a job','He resigned after ten years as director.','Ol on ýyl direktor bolandan soň işden çykdy.','B2'),
 E('staff','/stɑːf/','N','işgärler','персонал','all the people who work for an organization','The hotel staff were very helpful.','Myhmanhananyň işgärleri örän kömek etdi.','A2'),
 E('lay off','/ˌleɪ ˈɒf/','V','işgär sanyny azaltmak üçin işden çykarmak','увольнять из-за сокращения','to stop employing someone because there is not enough work','The factory laid off fifty workers.','Zawod elli işgäri işden çykardy.','B2'),
 E('make redundant','/ˌmeɪk rɪˈdʌndənt/','PHR','wezipe zerur bolmansoň işden çykarmak','увольнять из-за сокращения штата','to end someone’s job because it is no longer needed','The company made several employees redundant.','Kompaniýa birnäçe işgäri wezipäniň gysgaldylmagy sebäpli çykardy.','B2'),
 E('out of work','/ˌaʊt əv ˈwɜːk/','PHR','işsiz','без работы','without a job','He has been out of work since January.','Ýanwardan bäri ol işsiz.','B1'),
 E('off work','/ˌɒf ˈwɜːk/','PHR','işe çykmaýan, işden rugsatly','не на работе','not at work, often because you are ill or on holiday','I am off work this week with a bad cold.','Güýçli dümew sebäpli şu hepde işe çykamok.','B1'),
 E('sack','/sæk/','V','işden kowmak','увольнять','to make someone leave their job','The manager sacked him for repeated lateness.','Ýolbaşçy ony yzygiderli gijä galýandygy üçin işden kowdy.','B1'),
 E('fire','/ˈfaɪə/','V','işden çykarmak','увольнять','to make someone leave a job, especially because of poor work','They fired the employee for breaking the rules.','Düzgüni bozandygy üçin işgäri işden çykardylar.','B1'),
 E('promote','/prəˈməʊt/','V','wezipe galdyrmak','повышать в должности','to give someone a higher position at work','The company promoted her to team leader.','Kompaniýa ony topar ýolbaşçysy wezipesine galdyrdy.','B1'),
 E('pay rise','/ˈpeɪ raɪz/','N','aýlyk ýokarlanmasy','повышение зарплаты','an increase in the money you earn','He asked his boss for a pay rise.','Ol ýolbaşçysyndan aýlygynyň ýokarlandyrylmagyny sorady.','B1'),
 E('skill','/skɪl/','N','başarnyk','навык','an ability to do something well','Good communication skills are useful in this job.','Gowy aragatnaşyk başarnyklary bu işde peýdaly.','A2'),
 E('hire','/ˈhaɪə/','V','işe almak','нанимать','to give someone a job','The company plans to hire two designers.','Kompaniýa iki dizaýneri işe almagy meýilleşdirýär.','A2'),
 E('employ','/ɪmˈplɔɪ/','V','işe almak','нанимать','to give work to someone and pay them','The hotel employs over a hundred people.','Myhmanhana ýüzden gowrak adamy işe alýar.','A2'),
 E('perk','/pɜːk/','N','goşmaça ýeňillik','льгота, бонус','an extra benefit provided by a job','Free lunches are one of the perks of the job.','Mugt günortanlyk bu işiň goşmaça ýeňillikleriniň biridir.','B2'),
 E('benefit','/ˈbenɪfɪt/','N','goşmaça ýeňillik','льгота, преимущество','an extra advantage provided by an employer','The benefits include health insurance.','Goşmaça ýeňilliklere saglyk ätiýaçlandyryşy girýär.','B1'),
 E('freelance','/ˈfriːlɑːns/','ADJ','erkin işleýän','внештатный','working for different companies rather than one employer','She does freelance translation from home.','Ol öýünden erkin terjime işini edýär.','B2'),
 E('paternity leave','/pəˈtɜːnəti liːv/','N','atanyň çaga doglandan soňky rugsady','отцовский отпуск','time off work for a father after a baby is born','He took two weeks of paternity leave.','Ol iki hepde atalyk rugsadyny aldy.','B2'),
 E('permanent','/ˈpɜːmənənt/','ADJ','hemişelik','постоянный','continuing for a long time or without an end','She is looking for a permanent position.','Ol hemişelik wezipe gözleýär.','B1'),
 E('sick leave','/ˈsɪk liːv/','N','kesel sebäpli rugsat','больничный отпуск','time away from work because you are ill','He is on sick leave until Friday.','Ol anna gününe çenli kesel rugsadynda.','B1'),
 E('compassionate leave','/kəmˈpæʃənət liːv/','N','maşgala ýagdaýy sebäpli berilýän rugsat','отпуск по семейным обстоятельствам','time off work after a serious family event','She took compassionate leave after her father died.','Kakasy aradan çykandan soň ol maşgala rugsadyny aldy.','C1'),
 E('full-time','/ˌfʊl ˈtaɪm/','ADJ','doly iş güni','полный рабочий день','working the normal number of hours each week','He has a full-time job at the bank.','Ol bankda doly iş gününde işleýär.','A2'),
 E('unpaid','/ˌʌnˈpeɪd/','ADJ','tölegsiz','неоплачиваемый','not receiving money for work or time off','She took a month of unpaid leave.','Ol bir aý tölegsiz rugsat aldy.','B1'),
 E('zero-hours contract','/ˌzɪərəʊ ˈaʊəz ˌkɒntrækt/','N','iş sagady kepillendirilmeýän şertnama','контракт без гарантированных часов','a work contract with no guaranteed minimum hours','He works weekends on a zero-hours contract.','Ol dynç günleri iş sagady kepillendirilmeýän şertnama bilen işleýär.','C1'),
]

ADDITIONS['get_phrases'] = [
 E('get the chance','/ˌɡet ðə ˈtʃɑːns/','PHR','mümkinçilik gazanmak','получить возможность','to have an opportunity to do something','We got the chance to meet the author.','Awtory bilen duşuşmaga mümkinçilik gazandyk.','B1'),
 E('get the impression','/ˌɡet ði ɪmˈpreʃn/','PHR','täsir almak, pikir döremek','создаётся впечатление','to begin to think that something is true','I get the impression that he is worried.','Ol aladaly ýaly bolup görünýär.','B2'),
 E('get the wrong end of the stick','/ˌɡet ðə ˌrɒŋ end əv ðə ˈstɪk/','PHR','nädogry düşünmek','неправильно понять','to misunderstand a situation','I think you got the wrong end of the stick.','Meniňçe, sen ýagdaýy nädogry düşündiň.','C1'),
 E('get the joke','/ˌɡet ðə ˈdʒəʊk/','PHR','degişmä düşünmek','понять шутку','to understand why something is funny','Nobody got the joke about the old computer.','Köne kompýuter baradaky degişmä hiç kim düşünmedi.','B1'),
 E('get to know','/ˌɡet tə ˈnəʊ/','PHR','tanyşmak, öwrenmek','познакомиться','to become familiar with a person or place','It takes time to get to know a new colleague.','Täze işdeşi tanamak üçin wagt gerek.','A2'),
 E('get hold of','/ˌɡet ˈhəʊld əv/','PHR','habarlaşmak, tapmak','связаться с','to contact or find someone or something','I could not get hold of the doctor yesterday.','Düýn lukman bilen habarlaşyp bilmedim.','B2'),
 E('get rid of','/ˌɡet ˈrɪd əv/','PHR','dynmak, aýyrmak','избавиться от','to remove or throw away something unwanted','We need to get rid of these old boxes.','Bu köne gutulardan dynmaly.','B1'),
 E('get your own back on','/ˌɡet jɔːr ˌəʊn ˈbæk ɒn/','PHR','öç almak','отомстить','to do something unpleasant to someone who treated you badly','He got his own back on the bully with a clever trick.','Ol akylly hile bilen sütemkärden öç aldy.','C1'),
 E('get into trouble with','/ˌɡet ˌɪntə ˈtrʌbl wɪð/','PHR','... bilen başagaýlyga düşmek','попасть в неприятности из-за','to have problems because of something you did','She got into trouble with her boss for arriving late.','Gijä galandygy üçin ol ýolbaşçysy bilen başagaýlyga düşdi.','B2'),
 E('get out of the way','/ˌɡet ˌaʊt əv ðə ˈweɪ/','PHR','ýoldan sowulmak','уйти с дороги','to move so that someone or something can pass','Please get out of the way of the ambulance.','Tiz kömek ulagynyň ýolundan sowluň.','B1'),
 E('get real','/ˌɡet ˈrɪəl/','PHR','hakykata ýüzlenmek','смотреть на вещи реально','used to tell someone to be realistic','Get real — we cannot afford that house.','Hakykata ýüzlen — şol jaýy alyp bilmeris.','B2'),
 E('get a life','/ˌɡet ə ˈlaɪf/','PHR','öz durmuşyň bilen meşgullan','найди себе занятие','used rudely to tell someone to do more interesting things','He spends all day criticizing people online; he needs to get a life.','Ol bütin gün internetde adamlary tankytlaýar; başga işe güýmenmeli.','C1'),
 E('get nowhere','/ˌɡet ˈnəʊweə/','PHR','netije gazanmazlyk','не продвигаться','to make no progress','We got nowhere with the crossword.','Krosswordy çözmekde hiç öňe gidip bilmedik.','B2'),
 E("get on somebody's nerves",'/ˌɡet ɒn ˈsʌmbədiz nɜːvz/','PHR','biriniň gaharyna degmek','действовать кому-либо на нервы','to annoy someone','That constant tapping is getting on my nerves.','Üznüksiz şakyrdatmak meniň gaharyma degýär.','B2'),
 E('get your act together','/ˌɡet jɔːr ˌækt təˈɡeðə/','PHR','özüňi ele almak','взяться за ум','to organize yourself and behave responsibly','You need to get your act together before the exams.','Synaglardan öň özüňi ele almaly.','B2'),
 E('get on like a house on fire','/ˌɡet ɒn laɪk ə ˌhaʊs ɒn ˈfaɪə/','PHR','örän gowy düşünişmek','очень быстро найти общий язык','to like each other and become friendly very quickly','The two new colleagues got on like a house on fire.','Täze işdeşleriň ikisi bada-bat gowy düşünişdiler.','C1'),
 E('get a move on','/ˌɡet ə ˈmuːv ɒn/','PHR','howlukmak','поторопиться','to hurry','We need to get a move on or we will miss the train.','Howlukmaly, ýogsam otla gijä galarys.','B2'),
 E('get on a bit','/ˌɡet ˈɒn ə bɪt/','PHR','ýaşamak, ýaşy ulalmak','быть уже в возрасте','to be rather old','Your grandfather must be getting on a bit now.','Atan indi ýaşy birçene baran bolmaly.','C1'),
 E('get the message','/ˌɡet ðə ˈmesɪdʒ/','PHR','aýdyljak bolýan zada düşünmek','понять намёк','to understand what someone is trying to tell you','I hinted about the noise, but he did not get the message.','Şowhun barada yşarat etdim, ýöne ol düşünmedi.','B2'),
 E('get your own way','/ˌɡet jɔːr əʊn ˈweɪ/','PHR','islän zadyňa ýetmek','добиться своего','to make other people do what you want','She always gets her own way with her parents.','Ol ene-atasyndan hemişe islän zadyny alýar.','B2'),
 E('get on with','/ˌɡet ˈɒn wɪð/','PHR','dowam etmek','продолжать','to continue doing something','Please get on with your work while I am away.','Men ýok wagtym işiňi dowam et.','B1'),
 E('get into','/ˌɡet ˈɪntə/','PHR','bir işe ýa-da hünäre başlamak','начать заниматься','to start doing or become involved in something','She hopes to get into banking after university.','Ol uniwersitetden soň bank işine başlamagy umyt edýär.','B2'),
 E('get around','/ˌɡet əˈraʊnd/','PHR','bir ýerden başga ýere hereket etmek','передвигаться','to travel or move from place to place','It is easy to get around the city by bus.','Şäherde awtobus bilen hereket etmek aňsat.','B1'),
 E('get behind','/ˌɡet bɪˈhaɪnd/','PHR','yza galmak','отстать','to fail to do enough work on time','I got behind with my studies during the holiday.','Dynç alyşda sapaklarymdan yza galdym.','B2'),
 E('get someone down','/ˌɡet ˈsʌmwʌn daʊn/','PHR','birini ruhdan düşürmek','удручать кого-либо','to make someone feel unhappy','The dark winter weather gets me down.','Gyşyň garaňky howasy meni ruhdan düşürýär.','B2'),
 E('get out of','/ˌɡet ˈaʊt əv/','PHR','borçdan gaçmak','увильнуть от','to avoid doing something you should do','He got out of helping us by saying he was busy.','Ol işli diýmek bilen bize kömek etmekden gaçdy.','B2'),
 E('get back to','/ˌɡet ˈbæk tuː/','PHR','soňra jogap bermek ýa-da habarlaşmak','связаться позже','to contact someone again later','I will get back to you with an answer tomorrow.','Ertir jogap bilen size habarlaşaryn.','B1'),
]

ADDITIONS['conflict'] = [
 E('ally','/ˈælaɪ/','N','hyzmatdaş, ýaran','союзник','a country or person that gives help and support','The two countries became allies during the war.','Uruş döwründe iki ýurt ýaran boldy.','B1'),
 E('armed forces','/ˌɑːmd ˈfɔːsɪz/','N','ýaragly güýçler','вооружённые силы','a country’s army, navy, and air force','The armed forces were sent to protect the border.','Serhedi goramak üçin ýaragly güýçler iberildi.','B2'),
 E('commander','/kəˈmɑːndə/','N','serkerde, buýruk beriji','командир','an officer who is in charge of a military operation','The commander ordered the troops to retreat.','Serkerde goşuna yza çekilmegi buýurdy.','B1'),
 E('refugee','/ˌrefjuˈdʒiː/','N','bosgun','беженец','a person forced to leave their home or country','The refugee family crossed the border safely.','Bosgun maşgala serhetden sag-aman geçdi.','B1'),
 E('sniper','/ˈsnaɪpə/','N','mergen','снайпер','a soldier who shoots from a hidden position','The sniper was hidden on a rooftop.','Mergen üçegiň üstünde gizlenipdi.','B2'),
 E('survivor','/səˈvaɪvə/','N','aman galan adam','выживший','a person who stays alive after danger or disaster','The survivors were found two days later.','Aman galan adamlar iki günden soň tapyldy.','B1'),
 E('troops','/truːps/','N','goşun','войска','soldiers, especially in a large organized group','The troops arrived before sunrise.','Goşun gün dogmanka geldi.','B1'),
 E('the wounded','/ðə ˈwuːndɪd/','N','ýaralananlar','раненые','people injured in a war or battle','The wounded were taken to a nearby hospital.','Ýaralananlary golaýdaky hassahana äkitdiler.','B2'),
 E('ceasefire','/ˈsiːsfaɪə/','N','ot açmagy wagtlaýyn bes etmek','перемирие','an agreement to stop fighting for a period of time','The ceasefire lasted for three days.','Ot açmagy bes etmek baradaky ylalaşyk üç gün dowam etdi.','B2'),
 E('civil war','/ˌsɪvl ˈwɔː/','N','raýat urşy','гражданская война','a war between groups of people in one country','The civil war forced thousands of people to flee.','Raýat urşy müňlerçe adamy gaçmaga mejbur etdi.','B2'),
 E('coup','/kuː/','N','döwlet agdarylyşygy','государственный переворот','a sudden, often violent, attempt to take control of a government','The coup changed the country’s leadership overnight.','Döwlet agdarylyşygy bir gijede ýurduň ýolbaşçylaryny üýtgetdi.','C1'),
 E('rebellion','/rɪˈbeljən/','N','gozgalaň','восстание','an attempt to change a government using force','The rebellion spread to several towns.','Gozgalaň birnäçe şähere ýaýrady.','B2'),
 E('revolution','/ˌrevəˈluːʃn/','N','rewolýusiýa','революция','a major change of government, often made by people','The revolution began in the capital.','Rewolýusiýa paýtagtda başlandy.','B1'),
 E('treaty','/ˈtriːti/','N','şertnama','договор','a formal agreement between countries','The two sides signed a peace treaty.','Iki tarap parahatçylyk şertnamasyna gol çekdi.','B2'),
 E('blow up','/ˌbləʊ ˈʌp/','V','partlatmak','взорвать','to destroy something with an explosion','The soldiers blew up the bridge.','Esgerler köprini partlatdylar.','B1'),
 E('break out','/ˌbreɪk ˈaʊt/','PHR','başlamak, duýdansyz ýüze çykmak','вспыхнуть, начаться','to start suddenly, especially a war, fire, or disease','Fighting broke out near the border.','Serhediň golaýynda söweş başlandy.','B2'),
 E('capture','/ˈkæptʃə/','V','tutmak, ýesir almak','захватить, пленить','to take a person or place by force','The army captured the town at dawn.','Goşun şäheri daň bilen basyp aldy.','B1'),
 E('declare war on','/dɪˌkleə ˈwɔː ɒn/','PHR','... bilen uruş yglan etmek','объявить войну','to officially announce that a country will fight another','The country declared war on its neighbour.','Ýurt goňşusyna uruş yglan etdi.','B2'),
 E('execute','/ˈeksɪkjuːt/','V','jeza hökmünde öldürmek','казнить','to kill someone as a legal or political punishment','The prisoners were executed after the trial.','Kazyýetden soň tussaglary jezalandyryp öldürdiler.','B2'),
 E('loot','/luːt/','V','talamak','грабить','to steal things from shops or buildings during trouble','The rebels looted several empty shops.','Gozgalaňçylar birnäçe boş dükany taladylar.','B2'),
 E('overthrow','/ˌəʊvəˈθrəʊ/','V','häkimiýetden agdarmak','свергнуть','to remove a government or leader using force','The rebels tried to overthrow the government.','Gozgalaňçylar hökümeti agdarmaga synanyşdylar.','B2'),
 E('release','/rɪˈliːs/','V','boşatmak, goýbermek','освободить','to allow someone to leave captivity','The army released the prisoners on Friday.','Goşun tussaglary anna güni boşatdy.','B1'),
 E('shell (v.)','/ʃel/','V','artilleriýa bilen ok atmak','обстреливать','to attack a place by firing shells from large guns','The army shelled the rebel positions.','Goşun gozgalaňçylaryň ýerlerine artilleriýa bilen ok atdy.','C1'),
 E('retreat','/rɪˈtriːt/','V','yza çekilmek','отступать','to move back from an enemy or dangerous situation','The soldiers retreated across the river.','Esgerler derýanyň aňyrsyna yza çekildiler.','B2'),
]

ADDITIONS['voice'] = [
 E('bang','/bæŋ/','N','güýçli ses, patlama sesi','грохот, удар','a sudden loud noise','We heard a loud bang from the kitchen.','Aşhanadan güýçli ses eşitdik.','B1'),
 E('buzz','/bʌz/','N','jürrüldi, zyňňyldy','жужжание','a low continuous sound made by an insect or machine','A fly made a quiet buzz near the window.','Penjiräniň ýanynda siňek ýuwaşja zyňňyldy.','B1'),
 E('click','/klɪk/','N','çykgyldy','щелчок','a short sharp sound','I heard a click as the door locked.','Gapy gulplananda çykgyldy eşitdim.','A2'),
 E('creak','/kriːk/','N','jygyldy','скрип','a long high sound made by something moving slowly','The old floor made a creak under my feet.','Köne pol aýagymyň aşagynda jygyldy etdi.','B2'),
 E('crunch','/krʌntʃ/','N','harsyldy','хруст','a loud sound made by something being crushed','There was a crunch as he stepped on the dry leaves.','Ol gury ýapraklaryň üstüne basanda harsyldy boldy.','B2'),
 E('drip','/drɪp/','N','damja sesi','капание','a small drop of liquid or the sound it makes','The drip from the tap kept me awake.','Kran suwyň damjasy meni uklatmadı.','A2'),
 E('hiss','/hɪs/','N','sykylyk, sykylyk sesi','шипение','a long quiet sound like air escaping','We heard a hiss as the tyre went flat.','Şin boşanda sykylyk eşitdik.','B2'),
 E('hoot','/huːt/','N','baýguşuň ýa-da ulagyň sesi','уханье; гудок','a loud call made by an owl or a car horn','An owl gave a hoot in the dark.','Garaňkyda baýguş uwlady.','B2'),
 E('hum','/hʌm/','N','pes we üznüksiz ses','гудение','a low continuous sound','The fridge makes a soft hum at night.','Sowadyjy gijelerine pes ses çykarýar.','B1'),
 E('rattle','/ˈrætl/','N','şakyrdy','дребезжание','a series of short hard sounds','The windows gave a rattle in the wind.','Ýelde penjireler şakyrdady.','B2'),
 E('roar','/rɔː/','N','güýçli gürrüldi ýa-da gykylyk','рёв, гул','a very loud deep sound','We heard the roar of an engine outside.','Daşarda motoryň gürrüldisini eşitdik.','B1'),
 E('screech','/skriːtʃ/','N','ýiti gykylyk','визг','a very high unpleasant sound','The brakes made a screech as the bus stopped.','Awtobus saklananda tormozlar ýiti ses çykardy.','B2'),
 E('slam','/slæm/','N','güýçli şarkyldy','хлопок','a loud sound made by something hitting or closing forcefully','The door shut with a slam.','Gapy güýçli şarkyldap ýapyldy.','B1'),
 E('slurp','/slɜːp/','N','şoruldama sesi','хлюпанье','a noisy sucking sound when drinking or eating','I could hear him slurp his soup.','Onuň çorba içende şoruldadanyny eşitdim.','B2'),
 E('sniff','/snɪf/','N','burnuňy çekmegiň sesi','шмыганье носом','a short breath taken in through the nose','She gave a sniff and reached for a tissue.','Ol burnuny çekip, salfetka uzatdy.','B1'),
 E('snore','/snɔː/','N','hor çekmek','храп','the noisy breathing some people make while sleeping','His loud snore kept everyone awake.','Onuň gaty hor çekmegi hemmäni uklatmady.','B1'),
 E('splash','/splæʃ/','N','şapyrdy','всплеск','the sound or movement of liquid being hit','We heard a splash from the swimming pool.','Howuzdan şapyrdy eşitdik.','A2'),
 E('tap','/tæp/','N','ýeňil takyldatmak','стук','a light repeated sound made by hitting something','There was a tap at the window.','Penjirä ýeňil takyldatdylar.','A2'),
 E('tick','/tɪk/','N','sagat sesi','тиканье','the short regular sound of a clock','The tick of the clock was very loud.','Sagat sesi örän güýçlüdi.','B1'),
 E('whistle','/ˈwɪsl/','N','sygylyk sesi','свист','a high sound made by blowing air through the lips','A whistle came from the referee.','Araçy sygylyk çaldy.','A2'),
 E('giggle','/ˈɡɪɡl/','V','jikirdemek','хихикать','to laugh quietly in a silly or nervous way','The children began to giggle during the film.','Film wagtynda çagalar jikirdäp başladylar.','B1'),
 E('groan','/ɡrəʊn/','V','iňňildemek','стонать','to make a long low sound because you are in pain or annoyed','He groaned when he saw the bill.','Hasaby görende ol iňňildedi.','B1'),
 E('sob','/sɒb/','V','hopuklap aglamak','рыдать','to cry noisily with short breaths','She sobbed when she heard the news.','Habary eşidende ol hopuklap aglady.','B1'),
 E('stammer','/ˈstæmə/','V','sakawlap gürlemek','заикаться','to speak with difficulty, repeating sounds','He began to stammer when he felt nervous.','Alada galanda ol sakawlap başlady.','B2'),
 E('yell','/jel/','V','gaty ses bilen gygyrmak','кричать','to shout loudly, often because you are angry','Please do not yell at your brother.','Dogaňyza gaty ses bilen gygyrmaň.','B1'),
]

ADDITIONS['time_expr'] = [
 E('make up for lost time','/ˌmeɪk ˌʌp fə ˌlɒst ˈtaɪm/','PHR','ýitirilen wagtyň öwezini dolmak','наверстать упущенное время','to do something faster or more often after a delay','After the delay, we drove on to make up for lost time.','Gijikmeden soň ýitirilen wagtyň öwezini dolmak üçin tiz sürdük.','B2'),
 E('make good time','/ˌmeɪk ɡʊd ˈtaɪm/','PHR','ýoly çalt geçmek','быстро продвигаться','to travel or progress faster than expected','We made good time and reached the coast by noon.','Ýoly çalt geçip, günortana çenli kenara ýetdik.','B2'),
 E('take your time','/ˌteɪk jɔː ˈtaɪm/','PHR','howlukmazlyk','не торопиться','to do something without hurrying','Take your time; there is no need to rush.','Howlukma, alada etmegiň geregi ýok.','A2'),
 E('have a hard time','/ˌhæv ə hɑːd ˈtaɪm/','PHR','kynçylyk çekmek','тяжело переживать','to experience difficulty doing something','She had a hard time finding a new job.','Täze iş tapmakda ol kynçylyk çekdi.','B1'),
 E('run out of time','/ˌrʌn ˈaʊt əv taɪm/','PHR','wagtyň gutarmagy','не хватить времени','to have no time left','We ran out of time before the final question.','Soňky soraga ýetmän wagtymyz gutardy.','B1'),
 E('save time','/ˌseɪv ˈtaɪm/','PHR','wagt tygşytlamak','сэкономить время','to do something in a way that takes less time','Using the train will save time.','Otly bilen gitmek wagt tygşytlar.','A2'),
 E('spare time','/ˌspeə ˈtaɪm/','N','boş wagt','свободное время','time when you are not working or busy','I read novels in my spare time.','Boş wagtymda roman okaýaryn.','A2'),
 E('spend time','/ˌspend ˈtaɪm/','PHR','wagt geçirmek','проводить время','to use time doing something or being somewhere','We spent the afternoon at the museum.','Günüň ikinji ýarymyny muzeýde geçirdik.','A2'),
 E('waste time','/ˌweɪst ˈtaɪm/','PHR','wagty biderek geçirmek','тратить время впустую','to use time without doing anything useful','Do not waste time worrying about things you cannot change.','Üýtgedip bilmejek zatlaryň barada alada edip wagtyňy biderek geçirme.','B1'),
 E('time off','/ˌtaɪm ˈɒf/','N','işden rugsat, dynç alyş wagty','отгул, свободное время','a period when you do not have to work','I need a few days off to rest.','Dynç almak üçin maňa birnäçe gün rugsat gerek.','B1'),
 E('before my time','/bɪˌfɔː maɪ ˈtaɪm/','PHR','men ýaşamanka, meniň döwrümden öň','до моего времени','before the period when you were old enough to know about something','That singer was famous before my time.','Şol aýdymçy meniň döwrümden öň meşhur eken.','B2'),
 E('by the time','/baɪ ðə ˈtaɪm/','CONJ','...wagta çenli','к тому времени как','at or before the moment when something happens','By the time we arrived, the show had ended.','Biz barýançak tomaşa tamam bolupdy.','B1'),
 E('behind the times','/bɪˌhaɪnd ðə ˈtaɪmz/','PHR','zaman bilen aýakdaş däl','отставший от времени','old-fashioned and not keeping up with changes','The company’s website looks behind the times.','Kompaniýanyň saýty zaman bilen aýakdaş däl ýaly.','B2'),
 E('one thing at a time','/ˌwʌn θɪŋ ət ə ˈtaɪm/','PHR','bir gezekde bir zat','по одному делу за раз','used to say that you should do things separately','Let us deal with one thing at a time.','Geliň, bir gezekde bir meselä seredeliň.','B1'),
 E("time's up",'/ˌtaɪmz ˈʌp/','PHR','wagt gutardy','время вышло','used to say that there is no more time','Time’s up; please put down your pens.','Wagt gutardy, galamlaryňyzy goýuň.','A2'),
 E('short of time','/ˌʃɔːt əv ˈtaɪm/','PHR','wagty az','не хватать времени','not having enough time','We are short of time, so let us take a taxi.','Wagtymyz az, şonuň üçin taksi alalyň.','B1'),
 E('time on your hands','/ˌtaɪm ɒn jɔː ˈhændz/','PHR','boş wagtyň köp bolmagy','много свободного времени','a lot of free time, especially when you do not know what to do','Since retiring, he has more time on his hands.','Pensiýa çykandan soň onuň boş wagty köpeldi.','B2'),
 E('a matter of time','/ə ˌmætə əv ˈtaɪm/','PHR','wagtyň meselesi','вопрос времени','something that will certainly happen sooner or later','It is only a matter of time before they find out.','Olaryň bilmegi diňe wagtyň meselesi.','B2'),
 E('with time to spare','/wɪð ˌtaɪm tə ˈspeə/','PHR','wagty ýeterlik bolup','имея запас времени','with time left after finishing something','We reached the station with time to spare.','Wokzala ýeterlik wagt galanda ýetdik.','B2'),
 E('this time next week','/ˌðɪs taɪm nekst ˈwiːk/','PHR','indiki hepde şu wagt','в это время на следующей неделе','at the same time one week from now','This time next week, I will be on holiday.','Indiki hepde şu wagt dynç alyşda bolaryn.','B1'),
]

ADDITIONS['money2'] = [
 E('donation','/dəʊˈneɪʃn/','N','haýyr-sahawat','пожертвование','money given to help an organization or person','They made a donation to the animal charity.','Olar haýwan haýyr-sahawat guramasyna pul berdiler.','B1'),
 E('fare','/feə/','N','ýol puly','плата за проезд','the money paid for a journey by bus, train, plane, or taxi','The bus fare has gone up this year.','Şu ýyl awtobus puly ýokarlandy.','A2'),
 E('fee','/fiː/','N','hyzmat tölegi','сбор, гонорар','money paid for a professional service','The lawyer charged a high fee.','Hukukçy ýokary hyzmat tölegini aldy.','B1'),
 E('fine','/faɪn/','N','jerime','штраф','money paid as a punishment for breaking a rule','She had to pay a fine for parking there.','Ol şol ýerde ulag goýandygy üçin jerime tölemeli boldy.','A2'),
 E('grant','/ɡrɑːnt/','N','maksatly maliýe kömegi','грант','money given by an organization for a particular purpose','The university gave him a research grant.','Uniwersitet oňa ylmy barlag üçin grant berdi.','B2'),
 E('loan','/ləʊn/','N','karz','заём','money borrowed from a bank or another person','They took out a loan to buy a car.','Maşyn almak üçin bankdan karz aldylar.','A2','take out a loan'),
 E('lump sum','/ˌlʌmp ˈsʌm/','N','bir gezeklik uly töleg','единовременная сумма','a single payment of a large amount of money','The company paid her a lump sum when she retired.','Pensiýa çykanda kompaniýa oňa bir gezeklik uly töleg berdi.','B2'),
 E('quote','/kwəʊt/','N','bahanyň öňünden hasaby','смета, расценка','a statement of how much a job or service will cost','We asked three builders for a quote.','Üç gurluşykçydan işiň bahasyny soradyk.','B2','ask for a quote'),
 E('will','/wɪl/','N','wesýetnama','завещание','a legal document saying what happens to your money after you die','She left the house to her son in her will.','Ol wesýetnamasynda jaýyny ogluna galdyrdy.','B2','make a will'),
 E('consumer society','/kənˌsjuːmə səˈsaɪəti/','N','sarp ediş jemgyýeti','общество потребления','a society where buying goods is very important','Many people feel that we live in a consumer society.','Köp adam sarp ediş jemgyýetinde ýaşaýarys diýip hasaplaýar.','B2'),
 E('standard of living','/ˌstændəd əv ˈlɪvɪŋ/','N','ýaşaýyş derejesi','уровень жизни','the amount of money and comfort people have','The standard of living has improved in the region.','Sebitde ýaşaýyş derejesi ýokarlandy.','B2'),
 E('cost of living','/ˌkɒst əv ˈlɪvɪŋ/','N','ýaşaýyş çykdajylary','стоимость жизни','the money needed for basic things such as food and housing','The cost of living is higher in the capital.','Paýtagtda ýaşaýyş çykdajylary has ýokary.','B2'),
 E('inflation','/ɪnˈfleɪʃn/','N','hümmetsizlenme','инфляция','a general rise in prices over time','Inflation has made food more expensive.','Hümmetsizlenme azyk önümlerini gymmatlatdy.','B1'),
 E('online banking','/ˌɒnlaɪn ˈbæŋkɪŋ/','N','internet arkaly bank hyzmaty','интернет-банкинг','using a bank’s website or app to manage money','Online banking lets me pay bills at home.','Internet arkaly bank hyzmaty öýde oturyp töleg etmäge mümkinçilik berýär.','B1'),
 E('balance','/ˈbæləns/','N','hasapdaky galyndy','остаток на счёте','the amount of money in a bank account','I checked my account balance on my phone.','Telefonymdan bank hasabymdaky galyndyny barladym.','A2','bank balance'),
 E('bank transfer','/ˈbæŋk ˌtrænsfɜː/','N','bank arkaly pul geçirmek','банковский перевод','an electronic movement of money between bank accounts','I paid the rent by bank transfer.','Kärendäni bank arkaly pul geçirip töledim.','B1'),
 E('interest rate','/ˈɪntrəst reɪt/','N','göterim derejesi','процентная ставка','the percentage charged for borrowing money or paid on savings','The bank lowered its interest rate.','Bank göterim derejesini peseltdi.','B2'),
 E('mortgage','/ˈmɔːɡɪdʒ/','N','ipoteka','ипотека','a loan used to buy a house or flat','They got a mortgage to buy their first home.','Ilkinji öýlerini almak üçin ipoteka karzyny aldylar.','B1','take out a mortgage'),
 E('share','/ʃeə/','N','paý, aksiýa','акция','one of the parts into which a company is divided','She bought shares in a technology company.','Ol tehnologiýa kompaniýasynyň paýnamalaryny satyn aldy.','B1','buy shares'),
 E('stock market','/ˈstɒk ˌmɑːkɪt/','N','gymmatly kagyzlar bazary','фондовый рынок','a place or system for buying and selling company shares','The stock market fell after the announcement.','Yglan edilenden soň gymmatly kagyzlar bazary pese düşdi.','B2'),
 E('exchange rate','/ɪksˈtʃeɪndʒ reɪt/','N','walýuta hümmeti','обменный курс','the value of one currency compared with another','The exchange rate changes every day.','Walýuta hümmeti her gün üýtgeýär.','B1'),
 E('recession','/rɪˈseʃn/','N','ykdysady pese gaçyş','рецессия','a period when a country’s economy becomes weaker','Several small firms closed during the recession.','Ykdysady pese gaçyş döwründe birnäçe kiçi kärhana ýapyldy.','B2'),
 E('affluent','/ˈæfluənt/','ADJ','baý, üpjün','состоятельный','having a lot of money and a high standard of living','The affluent neighbourhood has expensive houses.','Baý etrapda gymmat jaýlar bar.','C1'),
 E('loaded','/ˈləʊdɪd/','ADJ','örän baý','богатый (разг.)','having a lot of money; informal','He must be loaded if he can afford that yacht.','Şol ýahtany alyp bilýän bolsa, ol örän baý bolmaly.','B2'),
 E('wealthy','/ˈwelθi/','ADJ','baý','богатый','having a lot of money or valuable possessions','The wealthy couple donated money to the museum.','Baý är-aýal muzeýe pul bagyşlady.','B1'),
 E('broke','/brəʊk/','ADJ','pulsuz','без денег','having no money, especially for a short time','I cannot go out tonight; I am completely broke.','Şu gün agşam daşary çykyp bilemok, pulum ýok.','B1'),
 E('hard up','/ˌhɑːd ˈʌp/','ADJ','pul taýdan kynçylyk çekýän','испытывающий нехватку денег','having very little money','They were hard up after paying the rent.','Kärendäni tölänlerinden soň pul taýdan kynçylyk çekdiler.','B2'),
 E('penniless','/ˈpeniləs/','ADJ','teňňesiz, düýbünden pulsuz','без гроша','having no money at all','He arrived in the city penniless.','Ol şähere düýbünden pulsuz geldi.','B2'),
 E('grand','/ɡrænd/','N','müň dollar ýa-da funt (gepleşikde)','тысяча (разг.)','one thousand pounds or dollars; informal','The old car cost three grand.','Köne ulag üç müň funt tutdy.','B2'),
 E('buck','/bʌk/','N','dollar (gepleşikde)','доллар (разг.)','a dollar; informal','The ticket costs ten bucks.','Bilet on dollar tutýar.','B1'),
 E('quid','/kwɪd/','N','funt sterling (gepleşikde)','фунт стерлингов (разг.)','a pound sterling; informal British English','I bought the book for five quid.','Kitaby bäş funt sterlinge aldym.','B1'),
 E('fiver','/ˈfaɪvə/','N','bäş funtlyk kagyz pul','пятёрка (банкнота)','a five-pound note; informal British English','Could you lend me a fiver?','Maňa bäş funtlyk karz berip bilersiňmi?','B2'),
 E('tenner','/ˈtenə/','N','on funtlyk kagyz pul','десятка (банкнота)','a ten-pound note; informal British English','I found a tenner in my coat pocket.','Paltomyň jübüsinden on funtlyk tapdym.','B2'),
]

ADDITIONS['prefixes'] = [
 E('disagree','/ˌdɪsəˈɡriː/','V','razy bolmazlyk','не соглашаться','to have a different opinion','I disagree with the final point.','Soňky pikir bilen razylaşamok.','A2','disagree with'),
 E('inappropriate','/ˌɪnəˈprəʊpriət/','ADJ','laýyksyz, ýerliksiz','неподходящий','not suitable for a particular situation','That joke was inappropriate for a work meeting.','Şol degişme iş maslahatyna ýerliksizdi.','B2'),
 E('unattractive','/ˌʌnəˈtræktɪv/','ADJ','özüne çekiji däl','непривлекательный','not pleasant or interesting to look at','The building looks unattractive from the outside.','Bina daşyndan özüne çekiji däl görünýär.','B1'),
 E('incapable','/ɪnˈkeɪpəbl/','ADJ','başarmaýan','неспособный','not able to do something','The old computer is incapable of running this program.','Köne kompýuter bu programmany işletmäge ukypsyz.','B2','incapable of'),
 E('incoherent','/ˌɪnkəʊˈhɪərənt/','ADJ','manysy düşnüksiz','несвязный','not expressed clearly or logically','His explanation was confused and incoherent.','Onuň düşündirişi bulaşyk we düşnüksiz boldy.','C1'),
 E('incompetent','/ɪnˈkɒmpɪtənt/','ADJ','başarnyksyz','некомпетентный','not having the ability or skill to do a job well','The report showed that the manager was incompetent.','Hasabat ýolbaşçynyň başarnyksyzdygyny görkezdi.','B2'),
 E('discontinue','/ˌdɪskənˈtɪnjuː/','V','bes etmek, dowam etmezlik','прекратить','to stop making or doing something','The company discontinued the old model.','Kompaniýa köne görnüşi öndürmegi bes etdi.','B2'),
 E('undo','/ʌnˈduː/','V','yzyna gaýtarmak','отменить, обратить','to reverse the effect of an action','You can undo the last change by pressing this button.','Şu düwmä basyp soňky üýtgeşmäni yzyna gaýtaryp bilersiňiz.','B1'),
 E('disembark','/ˌdɪsɪmˈbɑːk/','V','ulagdan düşmek','сойти с транспорта','to get off a ship, plane, or other vehicle','Passengers will disembark at the next stop.','Ýolagçylar indiki duralgada düşerler.','C1'),
 E('unhelpful','/ʌnˈhelpfl/','ADJ','kömegi degmeýän','бесполезный','not useful or willing to help','The instructions were unhelpful and confusing.','Görkezmeler peýdasyz hem bulaşyk boldy.','B1'),
 E('dishonest','/dɪsˈɒnɪst/','ADJ','dogruçyl däl','нечестный','not telling the truth or not behaving fairly','It was dishonest to hide the mistake.','Ýalňyşy gizlemek dogruçyl däldi.','B1'),
 E('inhospitable','/ˌɪnhɒˈspɪtəbl/','ADJ','myhmansöýer däl, ýaramaz şertli','негостеприимный','unfriendly or difficult to live in','The desert is an inhospitable place for plants.','Çöl ösümlikler üçin ýaşaýyş şertleri ýaramaz ýer.','C1'),
 E('illegitimate','/ˌɪlɪˈdʒɪtɪmət/','ADJ','kanuny däl','незаконный','not allowed by law or accepted rules','The court rejected the illegitimate claim.','Kazyýet kanuny däl talaby ret etdi.','C1'),
 E('illiterate','/ɪˈlɪtərət/','ADJ','okap-ýazyp bilmeýän','неграмотный','unable to read or write','The programme helps adults who are illiterate.','Maksatnama okap-ýazyp bilmeýän ululara kömek edýär.','B2'),
 E('illogical','/ɪˈlɒdʒɪkl/','ADJ','mantyksyz','нелогичный','not reasonable or sensible','His conclusion seemed illogical to the group.','Onuň netijesi topara mantyksyz görünýärdi.','B2'),
 E('immobile','/ɪˈməʊbaɪl/','ADJ','hereket edip bilmeýän','неподвижный','unable to move','After the accident, his leg was temporarily immobile.','Awariýadan soň aýagy wagtlaýyn hereket edip bilmedi.','B2'),
 E('immoral','/ɪˈmɒrəl/','ADJ','ahlaksyz','аморальный','not considered right or honest by most people','They believed the decision was immoral.','Olar bu karary ahlaksyz hasapladylar.','B2'),
 E('unofficial','/ˌʌnəˈfɪʃl/','ADJ','resmi däl','неофициальный','not formally approved or announced','We had an unofficial meeting after work.','Işden soň resmi däl duşuşygymyz boldy.','B1'),
 E('impersonal','/ɪmˈpɜːsənl/','ADJ','şahsy däl, sowuk','безличный','not showing personal feelings or interest','The hotel service felt impersonal.','Myhmanhananyň hyzmaty sowuk ýaly duýuldy.','B2'),
 E('impractical','/ɪmˈpræktɪkl/','ADJ','amaly taýdan oňaýsyz','непрактичный','not suitable or sensible in practice','Those shoes are impractical for walking in snow.','Şol aýakgaplar garda ýöremek üçin oňaýsyz.','B2'),
 E('irrational','/ɪˈræʃənl/','ADJ','mantyksyz, akyla sygmaýan','иррациональный','not based on reason or clear thought','Fear made him behave in an irrational way.','Gorky ony mantyksyz hereket etmäge mejbur etdi.','B2'),
 E('irregular','/ɪˈreɡjələ/','ADJ','tertipsiz, kadaly däl','нерегулярный','not happening at fixed or equal times','She works irregular hours at the hospital.','Ol hassahanada tertipsiz iş sagatlarynda işleýär.','B1'),
 E('irrelevant','/ɪˈreləvənt/','ADJ','degişli däl','не относящийся к делу','not connected with the subject being discussed','That detail is irrelevant to our decision.','Şol jikme-jiklik biziň kararymyza degişli däl.','B2'),
 E('irreplaceable','/ˌɪrɪˈpleɪsəbl/','ADJ','çalşyryp bolmaýan','незаменимый','so valuable or special that nothing can replace it','Her experience is irreplaceable.','Onuň tejribesiniň ornuny tutup bolmaýar.','B2'),
 E('outgrow','/ˌaʊtˈɡrəʊ/','V','ulalyp geýimi dar gelmek; gyzyklanmasyny ýitirmek','вырасти из; перерасти','to become too big for something or stop liking it as you mature','The children have outgrown their winter coats.','Çagalar gyşky paltolaryndan ulaldylar.','B2'),
 E('monosyllabic','/ˌmɒnəsɪˈlæbɪk/','ADJ','bir bogunly','односложный','having only one syllable','“Book” is a monosyllabic word.','“Book” bir bogunly söz.','C1'),
 E('rebuild','/ˌriːˈbɪld/','V','täzeden gurmak','перестроить','to build something again after it has been damaged','The town had to rebuild after the earthquake.','Ýertitremeden soň şäheri täzeden gurmaly boldy.','B1'),
 E('outpatient','/ˈaʊtpeɪʃnt/','N','hassahanada ýatman bejergi alýan näsag','амбулаторный пациент','a patient who visits a hospital for treatment but does not stay there','The clinic sees outpatients every afternoon.','Klinika her gün öýlän hassahanada ýatmaýan näsaglary kabul edýär.','C1'),
 E('ill-treated','/ˌɪl ˈtriːtɪd/','ADJ','ýaramaz çemeleşilen','плохо обращались','treated in a cruel or careless way','The ill-treated dog was taken to a shelter.','Ýaramaz çemeleşilen iti haýwan penahanasyna alyp gitdiler.','B2'),
 E('multivitamin','/ˌmʌltiˈvɪtəmɪn/','N','köp witaminli derman','мультивитамин','a pill or drink containing several vitamins','The doctor recommended a multivitamin.','Lukman köp witaminli dermany maslahat berdi.','B2'),
 E('misunderstand','/ˌmɪsʌndəˈstænd/','V','nädogry düşünmek','неправильно понять','to understand something in the wrong way','I misunderstood the instructions and went to the wrong room.','Görkezmelere nädogry düşünip, başga otaga gitdim.','B1'),
 E('antivirus','/ˈæntivaɪrəs/','N','antivirus programma','антивирус','a program that finds and removes computer viruses','Install antivirus software before downloading the file.','Faýly ýükläp almazdan öň antivirus programma guruň.','B2'),
 E('deforestation','/diːˌfɒrɪˈsteɪʃn/','N','tokaýlaryň çapylmagy','вырубка лесов','the cutting down of large areas of forest','Deforestation destroys the homes of many animals.','Tokaýlaryň çapylmagy köp haýwanyň ýaşaýan ýerini ýok edýär.','B2'),
 E('precondition','/ˌpriːkənˈdɪʃn/','N','öňünden zerur şert','предварительное условие','something that must happen before something else is possible','Trust is a precondition for a successful partnership.','Ynam üstünlikli hyzmatdaşlygyň öňünden zerur şertidir.','C1'),
 E('oversleep','/ˌəʊvəˈsliːp/','V','artyk uklap, gijä galmak','проспать','to sleep longer than planned','I overslept and missed the early train.','Artyk uklap, irki otla gijä galdym.','B1'),
 E('biannual','/baɪˈænjuəl/','ADJ','ýylda iki gezek bolýan','двухгодичный; дважды в год','happening twice a year','The committee holds biannual meetings in spring and autumn.','Geňeş ýazda we güýzde ýylda iki gezek ýygnak geçirýär.','C1'),
 E('coexist','/ˌkəʊɪɡˈzɪst/','V','bilelikde ýaşamak','сосуществовать','to live or exist together at the same time','Different communities coexist peacefully in the city.','Şäherde dürli jemgyýetler parahatçylykly bile ýaşaýarlar.','B2'),
 E('substandard','/ˌsʌbˈstændəd/','ADJ','talap edilýän derejeden pes','ниже стандарта','below the quality that is expected','The building was closed because of substandard safety.','Howpsuzlyk derejesi pes bolany üçin bina ýapyldy.','C1'),
 E('intergovernmental','/ˌɪntəˌɡʌvənˈmentl/','ADJ','hökümetara','межправительственный','involving two or more governments','An intergovernmental group discussed climate policy.','Hökümetara topar howa syýasatyny ara alyp maslahatlaşdy.','C1'),
 E('understaffed','/ˌʌndəˈstɑːft/','ADJ','işgäri ýeterlik däl','недоукомплектованный','having fewer workers than are needed','The restaurant is understaffed on busy evenings.','Işli agşamlarda restoranda işgär ýeterlik däl.','C1'),
 E('superhuman','/ˌsuːpəˈhjuːmən/','ADJ','adama mahsus bolmadyk güýçli','сверхчеловеческий','much stronger or more capable than an ordinary person','It took superhuman effort to lift the stone.','Daşy galdyrmak üçin adatdan daşary güýç gerek boldy.','B2'),
 E('autofocus','/ˈɔːtəʊfəʊkəs/','N','awtomatik fokus','автофокус','a camera feature that focuses the lens automatically','The camera’s autofocus works well in low light.','Kameranyň awtomatik fokusu pes ýagtylykda gowy işleýär.','B2'),
 E('microorganism','/ˌmaɪkrəʊˈɔːɡənɪzəm/','N','mikroorganizm','микроорганизм','a very small living thing that can be seen only with a microscope','Some microorganisms are useful to humans.','Käbir mikroorganizmler adamlara peýdalydyr.','B2'),
 E('outnumber','/ˌaʊtˈnʌmbə/','V','sany taýdan agdyk gelmek','превосходить числом','to be greater in number than another group','In this class, girls outnumber boys.','Bu synpda gyzlar oglanlardan köpräk.','B2'),
 E('outskirts','/ˈaʊtskɜːts/','N','şäheriň gyrasy','окраина','the parts of a town or city furthest from the centre','They live on the outskirts of London.','Olar Londonyň şäher gyrasynda ýaşaýarlar.','B2'),
 E('demystify','/ˌdiːˈmɪstɪfaɪ/','V','düşnüksizligi aýyrmak','развеять тайну','to make something complicated easier to understand','The guide helps demystify the application process.','Gollanma ýüz tutma işiniň düşnüksizligini aýyrmaga kömek edýär.','C1'),
]

ADDITIONS['travel_tourism'] = [
 E('breathtaking','/ˈbreθteɪkɪŋ/','ADJ','haýran galdyryjy','захватывающий дух','extremely impressive or beautiful','The view from the mountain was breathtaking.','Dagdan görünýän görnüş haýran galdyryjydy.','B2'),
 E('iconic','/aɪˈkɒnɪk/','ADJ','nyşana öwrülen, meşhur','знаковый','very famous and representing a particular place or idea','The bridge is an iconic symbol of the city.','Köpri şäheriň meşhur nyşanydyr.','B2'),
 E('imposing','/ɪmˈpəʊzɪŋ/','ADJ','ägirt we täsir galdyryjy','величественный','large and impressive in appearance','An imposing palace stood at the end of the street.','Köçäniň aňyrsynda ägirt köşk durdy.','B2'),
 E('lively','/ˈlaɪvli/','ADJ','janly, şowhunly','оживлённый','full of energy and activity','The old town is lively at night.','Köne şäher gijelerine janly bolýar.','A2'),
 E('off the beaten track','/ˌɒf ðə ˈbiːtn træk/','PHR','köp adamyň barmaýan ýerinde','в стороне от проторённых дорог','away from places where most people go','We found a quiet café off the beaten track.','Köp adamyň barmaýan ýerinde asuda kafe tapdyk.','B2'),
 E('picturesque','/ˌpɪktʃəˈresk/','ADJ','surat ýaly owadan','живописный','pretty, especially in an old-fashioned way','They stayed in a picturesque fishing village.','Olar surat ýaly owadan balykçy obasynda galdylar.','B2'),
 E('remote','/rɪˈməʊt/','ADJ','uzakda ýerleşýän','отдалённый','far away from towns or other people','The remote island has no airport.','Uzakdaky adada howa menzili ýok.','B1'),
 E('unspoilt','/ˌʌnˈspɔɪlt/','ADJ','tebigy gözelligi bozulmadyk','нетронутый','beautiful because it has not been changed by people','We walked along an unspoilt stretch of coast.','Tebigy gözelligi bozulmadyk kenar bilen gezdik.','B2'),
 E('dull','/dʌl/','ADJ','ýürekgysdyryjy, gyzyksyz','скучный','not interesting or exciting','The town felt dull after sunset.','Gün ýaşandan soň şäher gyzyksyz duýuldy.','A2'),
 E('overcrowded','/ˌəʊvəˈkraʊdɪd/','ADJ','aşa köp adamly','переполненный','containing too many people','The beach gets overcrowded in August.','Awgustda kenarda adam aşa köp bolýar.','B2'),
 E('overrated','/ˌəʊvəˈreɪtɪd/','ADJ','artykmaç öwülen','переоценённый','considered better than it really is','I thought the restaurant was overrated.','Restorany hakykatdan artykmaç öwüpdirler diýip pikir etdim.','B2'),
 E('soulless','/ˈsəʊlləs/','ADJ','häsiýetsiz, ýakymsyz','безликий','lacking character or warmth','The new shopping centre feels soulless.','Täze söwda merkezi häsiýetsiz görünýär.','C1'),
 E('touristy','/ˈtʊərɪsti/','ADJ','syýahatçylara niýetlenen','туристический (с оттенком массовости)','designed mainly to attract tourists','The main street is too touristy for my taste.','Esasy köçe meniň üçin aşa syýahatçylyk görnüşinde.','B2'),
 E('pricey','/ˈpraɪsi/','ADJ','gymmat','дороговатый','rather expensive; informal','The hotel was nice but a little pricey.','Myhmanhana gowy, ýöne biraz gymmatdy.','B1'),
 E('run-down','/ˌrʌn ˈdaʊn/','ADJ','köne we ýaramaz ýagdaýda','обветшалый','in poor condition because it has not been cared for','They renovated a run-down old hotel.','Olar ýaramaz ýagdaýdaky köne myhmanhanany abatladylar.','B2'),
 E('spoilt','/spɔɪlt/','ADJ','zaýalanan, öňki gözelligi bozulan','испорченный','damaged or made less attractive','The coastline was spoilt by large new hotels.','Täze uly myhmanhanalar kenaryň gözelligini bozdy.','B2'),
 E('tacky','/ˈtæki/','ADJ','owadan däl we arzan görünýän','безвкусный','cheap-looking and lacking good taste','The souvenir shop sold tacky plastic models.','Ýadygärlik dükany owadan däl plastmassa şekilleri satýardy.','B2'),
 E('unimposing','/ˌʌnɪmˈpəʊzɪŋ/','ADJ','täsir galdyrmaýan, sada','невзрачный','not large or impressive','The entrance is unimposing, but the hall is beautiful.','Girelge ýönekeý, ýöne zal owadan.','C1'),
 E('set off','/ˌset ˈɒf/','PHR','ýola düşmek','отправиться в путь','to begin a journey','We set off early to avoid the traffic.','Ulag dyknyşygyndan gaça durmak üçin ir ýola düşdük.','B1'),
 E('set out','/ˌset ˈaʊt/','PHR','ýola düşmek, maksat edinmek','отправиться; поставить цель','to begin a journey or start doing something with a purpose','They set out before dawn to reach the village.','Oba ýetmek üçin daň atmanka ýola düşdüler.','B2'),
 E('go camping','/ˌɡəʊ ˈkæmpɪŋ/','PHR','çadyrlap dynç almaga gitmek','поехать в поход с палатками','to spend a holiday living in a tent','We go camping by the lake every summer.','Her tomus kölüň ýanynda çadyrlap dynç alýarys.','A2'),
 E('go backpacking','/ˌɡəʊ ˈbækpækɪŋ/','PHR','ýeňil goş bilen syýahat etmek','путешествовать с рюкзаком','to travel on a low budget carrying your things in a backpack','They went backpacking around South America.','Olar Günorta Amerikada ýeňil goş bilen syýahat etdiler.','B2'),
 E('go sightseeing','/ˌɡəʊ ˈsaɪtsiːɪŋ/','PHR','taryhy ýerleri görmäge gitmek','осматривать достопримечательности','to visit famous or interesting places','We went sightseeing on our first day in Rome.','Rimde ilkinji günümiz gözel ýerleri görmäge gitdik.','A2'),
 E('go for a stroll','/ˌɡəʊ fər ə ˈstrəʊl/','PHR','gezelenje çykmak','пойти на прогулку','to go for a slow, relaxed walk','We went for a stroll around the old town.','Köne şäherde gezelenje çykdyk.','B1'),
 E('go on a trip','/ˌɡəʊ ɒn ə ˈtrɪp/','PHR','syýahata gitmek','отправиться в поездку','to travel somewhere for a short time','The class went on a trip to the coast.','Synp kenara syýahata gitdi.','A2'),
 E('go on an outing','/ˌɡəʊ ɒn ən ˈaʊtɪŋ/','PHR','gezelenje çykmak','отправиться на прогулку','to go on a short trip for pleasure','The family went on an outing to the countryside.','Maşgala oba ýerlerine gezelenje çykdy.','B2'),
 E('go on a safari','/ˌɡəʊ ɒn ə səˈfɑːri/','PHR','safari syýahatyna gitmek','отправиться на сафари','to take a trip to watch wild animals','They went on a safari in Kenya.','Olar Keniýada safari syýahatyna gitdiler.','B2'),
 E('go on a trek','/ˌɡəʊ ɒn ə ˈtrek/','PHR','uzak pyýada ýörişe gitmek','отправиться в длительный поход','to go on a long, difficult walk','We went on a trek through the mountains.','Daglaryň içinden uzak pyýada ýörişe gitdik.','B2'),
 E('go on a cruise','/ˌɡəʊ ɒn ə ˈkruːz/','PHR','kruiz syýahatyna gitmek','отправиться в круиз','to take a holiday on a ship','My parents went on a cruise around the islands.','Ene-atam adalaryň daşyndan kruiz syýahatyna gitdiler.','B1'),
 E('go on a journey','/ˌɡəʊ ɒn ə ˈdʒɜːni/','PHR','ýola düşmek, uzak ýol gitmek','отправиться в путешествие','to travel from one place to another, usually a long way','They went on a long journey by train.','Olar otly bilen uzak ýola düşdüler.','A2'),
 E('put off','/ˌpʊt ˈɒf/','PHR','soňraky wagta süýşürmek','отложить','to arrange for something to happen later','We had to put off our visit until Monday.','Saparymyzy duşenbe gününe çenli süýşürmeli bolduk.','B1'),
 E('wander round','/ˌwɒndə ˈraʊnd/','PHR','asuda aýlanyp görmek','бродить, прогуливаться','to walk around a place without a fixed plan','We wandered round the market for an hour.','Bazarda bir sagatlap asuda aýlandyk.','B2'),
 E('soak up','/ˌsəʊk ˈʌp/','PHR','siňdirmek, doly duýmak','впитывать, наслаждаться','to enjoy and experience an atmosphere or culture','We sat outside to soak up the atmosphere.','Howany doly duýmak üçin daşarda oturdyk.','B2'),
 E('sample','/ˈsɑːmpl/','V','dadyp görmek, synap görmek','попробовать','to try a small amount of food or drink','Visitors can sample local cheese at the market.','Myhmanlar bazarda ýerli peýniri dadyp bilerler.','B1'),
 E('recharge your batteries','/ˌriːtʃɑːdʒ jɔː ˈbætriz/','PHR','güýjüňi dikeltmek','восстановить силы','to rest so that you have more energy','A quiet weekend helped me recharge my batteries.','Asuda dynç günleri güýjümi dikeltmäge kömek etdi.','B2'),
 E('extend your stay','/ɪkˌstend jɔː ˈsteɪ/','PHR','galýan wagtyňy uzaltmak','продлить пребывание','to stay somewhere longer than planned','We decided to extend our stay by two nights.','Iki gije artyk galmagy karar etdik.','B2'),
 E('get away from it all','/ˌɡet əˈweɪ frəm ɪt ˈɔːl/','PHR','hemme zatdan dynç almak üçin gaçyp gitmek','уехать от всего','to go somewhere peaceful to escape daily life','We rented a cabin in the hills to get away from it all.','Gündelik durmuşdan dynç almak üçin baýyrda öýjagaz kireýine aldyk.','B2'),
 E('take it all in','/ˌteɪk ɪt ɔːl ˈɪn/','PHR','daş-töweregi synlap, täsirini duýmak','впитать впечатления','to look at, hear, and fully experience what is around you','We stopped at the viewpoint to take it all in.','Ähli görnüşi synlamak üçin tomaşa ýerine saklandyk.','B2'),
]

ADDITIONS['animal_matters'] = [
 E('calf','/kɑːf/','N','göle','теленок','a young cow or other large mammal','The calf stayed close to its mother.','Göle enesiniň ýanynda galdy.','A2'),
 E('chick','/tʃɪk/','N','jüýje','цыплёнок','a young bird, especially a chicken','The hen led her chicks across the yard.','Towuk jüýjelerini howlydan alyp geçdi.','A2'),
 E('cub','/kʌb/','N','haýwanyň balasy','детёныш','a young bear, lion, fox, or similar animal','The lion cub played beside its mother.','Ýolbarsyň balasy enesiniň ýanynda oýnady.','B1'),
 E('foal','/fəʊl/','N','taý','жеребёнок','a young horse','The foal was born during the night.','Taý gijäniň dowamynda dünýä indi.','B2'),
 E('kid','/kɪd/','N','owlak','козлёнок','a young goat','The kid followed the goat into the field.','Owlak geçiniň yzy bilen meýdana gitdi.','B1'),
 E('puppy','/ˈpʌpi/','N','güjük','щенок','a very young dog','The puppy chewed one of my shoes.','Güjük aýakgabymyň birini çeýnedi.','A2'),
 E('beak','/biːk/','N','guşuň çüňki','клюв','the hard pointed part of a bird’s mouth','The parrot opened its beak to call.','Toty gygyrmak üçin çüňküni açdy.','B1'),
 E('claw','/klɔː/','N','dyrnak','коготь','a sharp curved nail on an animal’s foot','The cat caught the toy with one claw.','Pişik oýnawajy bir dyrnagy bilen tutdy.','B1'),
 E('feather','/ˈfeðə/','N','ýelek','перо','one of the soft parts covering a bird’s body','A blue feather lay on the path.','Ýodada gök ýelek ýatyrdy.','A2'),
 E('hoof','/huːf/','N','toýnak','копыто','the hard part of the foot of a horse or similar animal','The horse hurt its hoof on a stone.','At daşda toýnagyny agyrtdy.','B2'),
 E('paw','/pɔː/','N','haýwanyň penjesi','лапа','the foot of an animal such as a cat or dog','The dog placed a paw on my knee.','It penjesini dyzyma goýdy.','A2'),
 E('shell','/ʃel/','N','gaty daşky gabyk','панцирь, раковина','the hard outer covering of some animals','The turtle pulled its head into its shell.','Pyşbaga kellesini gabygyň içine çekdi.','A2'),
 E('tail','/teɪl/','N','guýrugy','хвост','the part that extends from the back of an animal','The puppy wagged its tail excitedly.','Güjük guýrugyny şatlyk bilen bulaýlady.','A2'),
 E('whisker','/ˈwɪskə/','N','murt','ус','one of the long stiff hairs on an animal’s face','The cat’s whiskers moved as it sniffed the air.','Howany yslanda pişigiň murtlary gymyldady.','B2'),
 E('wing','/wɪŋ/','N','ganat','крыло','one of the parts birds use to fly','The injured bird could not lift its wing.','Ýaralanan guş ganatyny galdyryp bilmedi.','A2'),
 E('hive','/haɪv/','N','ary öýi','улей','a structure where bees live','The beekeeper checked the hive carefully.','Ary bakyjy ary öýüni üns bilen barlady.','B1'),
 E('stable','/ˈsteɪbl/','N','at athanasy','конюшня','a building where horses are kept','The horses returned to the stable at dusk.','Atlar agşamlyk athana dolandylar.','B1'),
 E('kennel','/ˈkenl/','N','it öýjagazy','собачья будка','a small shelter or building for a dog','The dog slept in its kennel outside.','It daşardaky öýjagazynda ýatdy.','B2'),
 E('tank','/tæŋk/','N','akwarýum, balyk saklanýan gap','аквариум','a large container for keeping fish or other animals','The goldfish live in a glass tank.','Altynbalyklar aýna akwarýumda ýaşaýarlar.','A2'),
 E('nest','/nest/','N','guş höwürtgesi','гнездо','a place that a bird makes to lay eggs','We saw a nest high in the tree.','Agajyň ýokarsynda höwürtge gördük.','A2'),
 E('bark','/bɑːk/','V','üýrmek','лаять','to make the loud short sound that a dog makes','The dog barked when the post arrived.','Poçta gelende it üýrdi.','A2'),
 E('neigh','/neɪ/','V','kişňemek','ржать','to make the loud sound of a horse','The horse neighed when it saw the food.','Iti görende at kişňedi.','B2'),
 E('meow','/miˈaʊ/','V','miyawlamak','мяукать','to make the sound that a cat makes','The cat meowed outside the bedroom door.','Pişik ýatylýan otagyň gapysynda miyawlady.','B1'),
 E('grunt','/ɡrʌnt/','V','hüňürdemek','хрюкать; grunt','to make a short low sound like a pig','The pig grunted as it searched for food.','Iýmit gözlände doňuz hüňürdedi.','B2'),
 E('twitter','/ˈtwɪtə/','V','jürküldemek','щебетать','to make a series of short high bird sounds','Birds were twittering in the garden.','Bagda guşlar jürküldeýärdi.','B2'),
 E('animal charity','/ˌænɪml ˈtʃærəti/','N','haýwanlary goraýan haýyr-sahawat guramasy','благотворительная организация по защите животных','an organization that helps and protects animals','The animal charity found homes for abandoned dogs.','Haýwanlary goraýan gurama taşlanan itlere öý tapdy.','B2'),
 E('animal rights activist','/ˌænɪml raɪts ˈæktɪvɪst/','N','haýwan hukuklaryny goraýjy','активист за права животных','a person who campaigns for animals to be treated fairly','An animal rights activist spoke outside the laboratory.','Haýwan hukuklaryny goraýjy barlaghananyň daşynda çykyş etdi.','C1'),
 E('animal testing','/ˌænɪml ˈtestɪŋ/','N','haýwanlarda synag geçirmek','испытания на животных','using animals to test products or medicines','The company promised to stop animal testing.','Kompaniýa haýwanlarda synag geçirmegi bes etjekdigini wada berdi.','B2'),
 E('medical research','/ˌmedɪkl rɪˈsɜːtʃ/','N','lukmançylyk ylmy barlagy','медицинское исследование','the study of health and illness to find new treatments','Medical research has improved many treatments.','Lukmançylyk ylmy barlaglary köp bejergini gowulandyrdy.','B2'),
 E('national park','/ˌnæʃnəl ˈpɑːk/','N','milli seýilgäh','национальный парк','a large area of countryside protected by a government','We saw wild horses in the national park.','Milli seýilgähde ýabany atlary gördük.','A2'),
 E('conservation area','/ˌkɒnsəˈveɪʃn ˌeəriə/','N','tebigaty goraýyş zolagy','охраняемая природная территория','an area protected to preserve nature or wildlife','The wetland is a conservation area for rare birds.','Batgalyk seýrek guşlar üçin tebigaty goraýyş zolagydyr.','B2'),
 E('endangered species','/ɪnˌdeɪndʒəd ˈspiːʃiːz/','N','ýok bolup gitmek howpyndaky görnüş','виды под угрозой исчезновения','types of animals or plants that may soon disappear','The reserve protects several endangered species.','Goraghana ýok bolup gitmek howpyndaky birnäçe görnüşi goraýar.','B2'),
 E('in captivity','/ɪn kæpˈtɪvəti/','PHR','ýesirlikde, kapasada','в неволе','kept in a cage or controlled environment','Some of these birds were born in captivity.','Bu guşlaryň käbiri kapasada dünýä indi.','B2'),
 E('breed','/briːd/','V','köpeltmek, nesil öndürmek','разводить','to keep animals so that they produce young','The centre breeds rare birds for release into the wild.','Merkez seýrek guşlary tebigata goýbermek üçin köpeldýär.','B1'),
 E('reintroduce','/ˌriːɪntrəˈdjuːs/','V','täzeden tebigata goýbermek','повторно выпустить','to bring an animal or plant back to an area where it lived before','They hope to reintroduce wolves to the region.','Olar möjekleri sebite täzeden goýbermegi umyt edýärler.','C1'),
 E('inhumane','/ˌɪnhjuːˈmeɪn/','ADJ','rehimsiz, adamkärçiliksiz','негуманный','cruel and causing unnecessary suffering','The animals were kept in inhumane conditions.','Haýwanlar rehimsiz şertlerde saklanypdyr.','C1'),
 E('veal calf','/ˈviːl kɑːf/','N','göle eti üçin ösdürilýän göle','телёнок на откорм','a young calf raised for its meat','The report discussed the treatment of veal calves.','Hasabat göle eti üçin ösdürilýän gölelere çemeleşmäni ara alyp maslahatlaşdy.','C1'),
 E('circus','/ˈsɜːkəs/','N','sirk','цирк','a show with performers and sometimes trained animals','The town banned wild animals from the circus.','Şäher ýabany haýwanlaryň sirkde çykyş etmegini gadagan etdi.','A2'),
]

ADDITIONS['preparing_food'] = [
 E('bake','/beɪk/','V','peçde bişirmek','печь','to cook food in an oven','We baked figs with honey for dessert.','Süýjülik üçin injiri bal bilen peçde bişirdik.','A2','bake a cake'),
 E('barbecue','/ˈbɑːbɪkjuː/','V','otda, gözenekde bişirmek','жарить на гриле','to cook food over an open fire or hot coals','They barbecued pork ribs in the garden.','Olar bagda doňuz gapyrgasyny otda bişirdiler.','B1'),
 E('boil','/bɔɪl/','V','gaýnatmak','варить','to cook food in water that is bubbling','Boil the rice for fifteen minutes.','Tüwini on bäş minut gaýnat.','A2'),
 E('chop','/tʃɒp/','V','ownuk dogramak','рубить, нарезать','to cut something into small pieces','Chop the parsley before adding it to the sauce.','Sousa goşmazdan öň petruşkany ownuk dogra.','B1'),
 E('deep-fry','/ˌdiːp ˈfraɪ/','V','köp gyzgyn ýagda gowurmak','жарить во фритюре','to cook food completely covered in hot oil','They deep-fried the onion rings until golden.','Sogan halkalaryny altynsow bolýança köp ýagda gowurdylar.','B2'),
 E('grill','/ɡrɪl/','V','grilde ýa-da otda bişirmek','жарить на гриле','to cook food on a metal frame over heat','We grilled the fish with lemon.','Balygy limon bilen grilde bişirdik.','A2'),
 E('mash','/mæʃ/','V','ezmek','разминать','to crush cooked food until it is soft','Mash the potatoes with a little butter.','Ýeralmany azajyk ýag bilen ez.','B1'),
 E('mince','/mɪns/','V','maýda edip çapmak','мелко нарезать','to cut food into very small pieces','Mince the beef and fry it with onions.','Sygyr etini maýda çapyp, sogan bilen gowur.','B2'),
 E('poach','/pəʊtʃ/','V','suwda ýa-da başga suwuklykda pes otda bişirmek','варить без скорлупы; припускать','to cook food gently in hot water or another liquid','She poached an egg for breakfast.','Ol ertirlik üçin ýumurtgany suwda bişirdi.','B2'),
 E('roast','/rəʊst/','V','peçde ýag bilen gowurmak','запекать, жарить','to cook food in an oven, usually with fat','We roasted lamb with garlic and herbs.','Guzynyň etini sarymsak we otlar bilen peçde bişirdik.','A2'),
 E('scramble','/ˈskræmbl/','V','garyşdyryp gowurmak','готовить яичницу-болтунью','to cook eggs while stirring them','He scrambled two eggs for breakfast.','Ol ertirlik üçin iki ýumurtgany garyşdyryp gowurdy.','B2'),
 E('slice','/slaɪs/','V','dilimlemek','нарезать ломтиками','to cut food into thin, flat pieces','Slice the bread while it is still warm.','Çöregi entek ýylyka dilimle.','A2'),
 E('steam','/stiːm/','V','bugda bişirmek','готовить на пару','to cook food over boiling water','Steam the mussels until their shells open.','Midiýalary gabyklary açylýança bugda bişir.','B1'),
 E('stew','/stjuː/','V','haýal gaýnadyp bişirmek','тушить','to cook food slowly in liquid','Stew the plums with a little sugar.','Erikleri azajyk şeker bilen haýal gaýnat.','B2'),
 E('stuff','/stʌf/','V','içini doldurmak','фаршировать','to fill food with a mixture before cooking','They stuffed the chicken breast with herbs.','Olar towuk göwsüni otlar bilen doldurdylar.','B2'),
 E('toast','/təʊst/','V','tostlamak, gyzardyp bişirmek','поджаривать','to make bread brown and crisp with heat','I toasted a sandwich for lunch.','Günortanlyk üçin sendwiçi tostladym.','A2'),
 E('whip','/wɪp/','V','güýçli garyşdyryp köpürjikletmek','взбивать','to beat cream or eggs until they become light','Whip the cream until it forms soft peaks.','Gaýmagy ýumşak depeler emele gelýänçä çal.','B2'),
 E('baking tray','/ˈbeɪkɪŋ treɪ/','N','peç üçin demir gap','противень','a flat metal dish used for baking food','Put the biscuits on a baking tray.','Kökeleri peç üçin demir gabyň üstünde goý.','B1'),
 E('chopping board','/ˈtʃɒpɪŋ bɔːd/','N','dograma tagtasy','разделочная доска','a flat board used for cutting food','Use a clean chopping board for the vegetables.','Gök önümler üçin arassa dograma tagtasyny ulan.','B1'),
 E('colander','/ˈkɒləndə/','N','süzgüçli gap','дуршлаг','a bowl with holes used for draining liquid from food','Drain the pasta in a colander.','Makaron suwuny süzgüçli gapda süz.','B2'),
 E('food processor','/ˈfuːd ˌprəʊsesə/','N','azyk önümlerini ownuklaýan enjam','кухонный комбайн','an electric machine that cuts, mixes, or prepares food','The food processor chopped the onions in seconds.','Azyk enjamy sogany birnäçe sekuntda dogrady.','B1'),
 E('frying pan','/ˈfraɪɪŋ pæn/','N','gowurma gap','сковорода','a flat metal pan used for frying food','Heat some oil in a frying pan.','Gowurma gapda biraz ýag gyzdyr.','A2'),
 E('mixing bowl','/ˈmɪksɪŋ bəʊl/','N','garyşdyrma jamy','миска для смешивания','a large bowl used for mixing ingredients','Put the flour and eggs in a mixing bowl.','Uny we ýumurtgalary garyşdyrma jamyna sal.','B1'),
 E('scales','/skeɪlz/','N','tereziler','весы','a device for measuring how heavy something is','Use kitchen scales to weigh the flour.','Uny ölçemek üçin aşhana terezisini ulan.','A2'),
 E('spatula','/ˈspætʃələ/','N','spatula, tekiz aşhana pilçesi','лопатка','a flat tool used for mixing or turning food','Turn the pancakes with a spatula.','Blini spatula bilen öwür.','B2'),
]


ADDITIONS['compound_adjs2'] = [
 E('air-conditioned','/ˌeə kənˈdɪʃnd/','ADJ','howasy sowadyjy enjamly','с кондиционером','cooled by a machine that controls the air temperature','We waited in an air-conditioned room.','Biz howasy sowadyjy enjamly otagda garaşdyk.','B1'),
 E('narrow-minded','/ˌnærəʊ ˈmaɪndɪd/','ADJ','dar düşünjeli','ограниченный','unwilling to accept new or different ideas','His narrow-minded attitude surprised me.','Onuň dar düşünjeli garaýşy meni geň galdyrdy.','B2'),
 E('old-fashioned','/ˌəʊld ˈfæʃnd/','ADJ','köneçe','старомодный','not modern or no longer popular','They live in an old-fashioned house.','Olar köneçe jaýda ýaşaýarlar.','A2'),
 E('high-risk','/ˌhaɪ ˈrɪsk/','ADJ','ýokary töwekgelçilikli','высокорискованный','involving a strong possibility of danger or failure','Climbing without a guide is a high-risk activity.','Ýolbaşçysyz dyrmaşmak ýokary töwekgelçilikli iş.','B2'),
 E('second-hand','/ˌsekənd ˈhænd/','ADJ','ulanylan, ikinji el','подержанный','owned by someone else before you buy it','She bought a second-hand bicycle.','Ol ulanylan welosiped satyn aldy.','A2'),
 E('home-made','/ˌhəʊm ˈmeɪd/','ADJ','öýde taýýarlanan','домашний','made at home rather than in a factory or restaurant','We had home-made soup for lunch.','Günortan öýde taýýarlanan çorba içdik.','A2'),
 E('self-conscious','/ˌself ˈkɒnʃəs/','ADJ','özüni oňaýsyz duýýan','стесняющийся','nervous or embarrassed about what other people think of you','He feels self-conscious when people take photos.','Adamlar surat alanda ol özüni oňaýsyz duýýar.','B2'),
 E('last-minute','/ˌlɑːst ˈmɪnɪt/','ADJ','iň soňky pursatdaky','в последнюю минуту','happening or done just before it is too late','We made a last-minute change to the plan.','Meýilnama iň soňky pursatda üýtgeşme girizdik.','B2'),
 E('worn-out','/ˌwɔːn ˈaʊt/','ADJ','könelip ýyrtylan; örän ýadaw','изношенный; измученный','damaged by long use, or extremely tired','He wore worn-out jeans to the concert.','Ol konserte könelip ýyrtylan jins geýdi.','B1'),
 E('eco-friendly','/ˌiːkəʊ ˈfrendli/','ADJ','tebigata zyýansyz','экологичный','designed to cause little or no damage to the environment','We use eco-friendly cleaning products.','Biz tebigata zyýansyz arassalaýjy önümleri ulanýarys.','B2'),
 E('extra-curricular','/ˌekstrəkəˈrɪkjələ/','ADJ','sapakdan daşary','внеклассный','organized by a school but not part of normal lessons','She joined an extra-curricular drama club.','Ol sapakdan daşary drama gurnagyna goşuldy.','C1'),
 E('feel-good','/ˈfiːl ɡʊd/','ADJ','keýpi göterýän','жизнеутверждающий','making you feel happy and positive','We watched a feel-good film together.','Biz bilelikde keýp göterýän filme tomaşa etdik.','B2'),
 E('groundbreaking','/ˈɡraʊndbreɪkɪŋ/','ADJ','täze ýol açýan','новаторский','new and important, changing the way something is done','The scientist published groundbreaking research.','Alym täze ýol açýan barlagyny çap etdi.','C1'),
 E('high-heeled','/ˌhaɪ ˈhiːld/','ADJ','beýik ökjeli','на высоком каблуке','having shoes with tall heels','She wore high-heeled shoes to the ceremony.','Ol dabara beýik ökjeli aýakgap geýdi.','B1'),
 E('high-pitched','/ˌhaɪ ˈpɪtʃt/','ADJ','ýiti, inçe sesli','высокий (о звуке)','having a very high sound','A high-pitched alarm woke the baby.','Ýiti sesli duýduryş çagany oýardy.','B2'),
 E('labour-saving','/ˈleɪbə ˌseɪvɪŋ/','ADJ','zähmeti ýeňilleşdirýän','трудосберегающий','reducing the amount of work needed','A dishwasher is a useful labour-saving device.','Gap-gaç ýuwujy enjam zähmeti ýeňilleşdirýän peýdaly enjamdyr.','B2'),
 E('life-changing','/ˈlaɪf ˌtʃeɪndʒɪŋ/','ADJ','durmuşy üýtgedýän','меняющий жизнь','having a very great effect on someone’s life','Moving to another country was life-changing.','Başga ýurda göçmek durmuşymy düýpli üýtgetdi.','B2'),
 E('low-cost','/ˌləʊ ˈkɒst/','ADJ','arzan bahaly','недорогой','available for a low price','Low-cost airlines have made travel easier.','Arzan bahaly awiakompaniýalar syýahaty aňsatlaşdyrdy.','B1'),
]

ADDITIONS['phones_tech'] = [
 E('screen','/skriːn/','N','ekran','экран','the flat surface on a phone, computer, or television','The screen is difficult to read in sunlight.','Gün şöhlesinde ekrany okamak kyn.','A1'),
 E('touch screen','/ˈtʌtʃ skriːn/','N','sensorly ekran','сенсорный экран','a screen that responds when you touch it','You can open the map by tapping the touch screen.','Sensorly ekrana basyp kartany açyp bilersiňiz.','B1'),
 E('keypad','/ˈkiːpæd/','N','düwmeli panel','клавиатура с кнопками','a small set of buttons used to operate a device','Enter your code on the phone keypad.','Kody telefon düwmeli paneline giriziň.','B1'),
 E('keyboard','/ˈkiːbɔːd/','N','klawiatura','клавиатура','the set of keys used for typing on a computer or device','I prefer typing on a physical keyboard.','Men hakyky klawiaturada ýazmagy halaýaryn.','A2'),
 E('passcode','/ˈpɑːskəʊd/','N','giriş kody','код доступа','a secret set of numbers used to unlock a device','You need a passcode to unlock the tablet.','Planşeti açmak üçin giriş kody gerek.','B1'),
 E('contact','/ˈkɒntækt/','N','telefon sanawyda saklanan adam','контакт','a person’s name and details stored on a phone or computer','I saved the new client as a contact.','Täze müşderini telefon sanawyna goşdum.','A2'),
 E('settings','/ˈsetɪŋz/','N','sazlamalar','настройки','the choices that control how a device or program works','Change the sound settings on your phone.','Telefonyň ses sazlamalaryny üýtget.','A2'),
 E('broadband','/ˈbrɔːdbænd/','N','ýokary tizlikli internet','широкополосный интернет','a fast connection to the internet','We switched to faster broadband last month.','Geçen aý has çalt internet birikmesine geçdik.','B1'),
 E('wi-fi','/ˈwaɪfaɪ/','N','wi-fi, simsiz internet','вай-фай','a way of connecting to the internet without wires','The café offers free wi-fi.','Kafede mugt wi-fi bar.','A2'),
 E('pop-up','/ˈpɒp ʌp/','N','ekranda öz-özünden açylýan penjire','всплывающее окно','a window that suddenly appears on a computer screen','A pop-up appeared while I was reading the article.','Makala okaýarkam ekranda penjire peýda boldy.','B2'),
 E('coverage','/ˈkʌvərɪdʒ/','N','aragatnaşyk elýeterliligi','зона покрытия','the area where a phone or internet signal is available','Mobile coverage is weak in this valley.','Bu jülgede telefon aragatnaşygy gowşak.','B1'),
 E('signal','/ˈsɪɡnəl/','N','signal','сигнал','the waves or information sent to a phone or device','I cannot get a mobile signal inside this building.','Bu binanyň içinde mobil signal alyp bilemok.','A2'),
 E('download','/ˌdaʊnˈləʊd/','V','internetden ýükläp almak','скачивать','to copy a file from the internet to your device','You can download the guide as a PDF.','Gollanmany PDF görnüşinde ýükläp alyp bilersiňiz.','A2'),
 E('stream','/striːm/','V','internet arkaly göni diňlemek ýa-da görmek','смотреть или слушать онлайн','to play audio or video over the internet without saving it first','We streamed the concert on the train.','Otlyda konserti internet arkaly gördük.','B1'),
 E('scroll','/skrəʊl/','V','ekranda ýokary-aşak süýşürmek','прокручивать','to move text or images up or down on a screen','Scroll down to see the rest of the page.','Sahypanyň galanyny görmek üçin aşak süýşür.','A2'),
 E('swipe','/swaɪp/','V','barmak bilen ekranda süýşürmek','проводить пальцем по экрану','to move your finger quickly across a touch screen','Swipe left to see the next photo.','Indiki suraty görmek üçin barmagyňy çepe süýşür.','B1'),
 E('hang up','/ˌhæŋ ˈʌp/','PHR','jaňy kesmek','повесить трубку','to end a telephone call','She said goodbye and hung up.','Ol hoşlaşyp, jaňy kesdi.','A2'),
 E('top up','/ˌtɒp ˈʌp/','PHR','hasabyňy ýa-da telefonyňy doldurmak','пополнить баланс','to add more money or credit to a phone account','I need to top up my phone before the trip.','Syýahatdan öň telefonymyň hasabyny doldurmaly.','B1'),
 E('put through','/ˌpʊt ˈθruː/','PHR','jaňy gerekli adama birikdirmek','соединить по телефону','to connect someone by telephone to the person they want','Could you put me through to the sales department?','Meni satuw bölümine birikdirip bilersiňizmi?','B2'),
 E('get through to','/ˌɡet ˈθruː tuː/','PHR','düşündirip başarmak; telefon arkaly habarlaşmak','достучаться до кого-либо; дозвониться до кого-либо','to make someone understand you, or to succeed in speaking to someone by phone','It’s impossible to get through to my son about his studies, and I still can’t get through to the doctor by phone.','Ogluma okuw barada düşündirip bilemok, lukmana hem telefon arkaly jaň edip bilemok.','B2','get through to someone; get through to a doctor by phone'),
 E('switch off','/ˌswɪtʃ ˈɒf/','PHR','öçürmek','выключить','to turn off a device','Please switch off your phone during the meeting.','Maslahat wagtynda telefonyňyzy öçüriň.','A2'),
 E('unplug','/ʌnˈplʌɡ/','V','tokdan aýyrmak','отключить от сети','to disconnect a device from its power supply','Unplug the charger when the battery is full.','Batareýa dolanda zarýad berijini tokdan aýyr.','B1'),
]

ADDITIONS['adjectives_preps'] = [
 E('obsessed with','/əbˈsest wɪð/','PHR','... bilen aşa gyzyklanýan','одержимый чем-либо','thinking about something all the time in an unhealthy way','He is obsessed with online games.','Ol internet oýunlaryna aşa berlen.','B2'),
 E('addicted to','/əˈdɪktɪd tuː/','PHR','... endik eden, garaşly','зависимый от','unable to stop using or doing something harmful','She is addicted to social media.','Ol sosial ulgamlara garaşly.','B2'),
 E('hooked on','/ˈhʊkt ɒn/','PHR','... endik eden','подсевший на','very interested in something and unable to stop','My brother is hooked on video games.','Doganım wideo oýunlaryna endik eden.','B2'),
 E('mad about','/ˈmæd əˌbaʊt/','PHR','... örän halaýan','без ума от','very enthusiastic about something','She is mad about football.','Ol futboly örän gowy görýär.','B1'),
 E('dependent on','/dɪˈpendənt ɒn/','PHR','... garaşly','зависимый от','needing or relying on someone or something','Many people are dependent on their phones.','Köp adam telefonlaryna garaşly.','B1'),
 E('fed up with','/ˌfed ˈʌp wɪð/','PHR','... ýadamak, bizar bolmak','сытый по горло','annoyed or bored because something has continued too long','I am fed up with all the traffic noise.','Ulag seslerinden bizar boldum.','B1'),
 E('open to','/ˈəʊpən tuː/','PHR','... kabul etmäge taýýar','открытый к','willing to consider new ideas or suggestions','Our manager is open to new ideas.','Ýolbaşçymyz täze pikirleri kabul etmäge taýýar.','B1'),
 E('sick of','/ˈsɪk əv/','PHR','... bizar bolmak','устать от','annoyed or bored with something','She is sick of hearing the same excuse.','Ol şol bir bahanany eşitmekden bizar boldy.','B1'),
 E('aware of','/əˈweə əv/','PHR','... habarly','осведомлённый о','knowing that something exists or is happening','Are you aware of the risks?','Töwekgelçiliklerden habaryň barmy?','B1'),
 E('keen on','/ˈkiːn ɒn/','PHR','... halaýan, höwesli','увлекающийся','very interested in or enthusiastic about something','He is keen on getting married abroad.','Ol daşary ýurtda öýlenmäge höwesli.','B1'),
 E('unsuitable for','/ʌnˈsuːtəbl fɔː/','PHR','... üçin laýyk däl','неподходящий для','not right or appropriate for a particular purpose','The film is unsuitable for young children.','Film kiçi çagalar üçin laýyk däl.','B1'),
 E('suspicious of','/səˈspɪʃəs əv/','PHR','... şübhelenýän','подозрительный к','thinking that someone may be dishonest or harmful','They were suspicious of the new offer.','Olar täze teklipden şübhelendiler.','B2'),
 E('dissatisfied with','/dɪsˈsætɪsfaɪd wɪð/','PHR','... kanagatlanmaýan','недовольный','not pleased with someone or something','Customers were dissatisfied with the service.','Müşderiler hyzmatdan kanagatlanmadylar.','B2'),
 E('accustomed to','/əˈkʌstəmd tuː/','PHR','... öwrenişen','привыкший к','familiar with something because you have experienced it often','People are becoming accustomed to working online.','Adamlar internet arkaly işlemäge öwrenişýärler.','B2'),
 E('attached to','/əˈtætʃt tuː/','PHR','... berk bagly','привязанный к','feeling strong affection for someone or something','She is very attached to her old car.','Ol köne ulagyna berk bagly.','B2'),
]

ADDITIONS['health'] = [
 E('sore throat','/ˌsɔː ˈθrəʊt/','N','bokurdagyň agyrmagy','боль в горле','pain in your throat, especially when you swallow','I stayed home because I had a sore throat.','Bokurdagym agyrýandygy üçin öýde galdym.','A2'),
 E('sneeze','/sniːz/','V','asgyrmak','чихать','to suddenly breathe air out through your nose','Dust makes me sneeze.','Tozan meni asgyrdýar.','A2'),
 E('high temperature','/ˌhaɪ ˈtemprətʃə/','N','ýokary gyzgyn','высокая температура','a body temperature above the normal level','The child has a high temperature and needs to rest.','Çaganyň gyzgyny ýokary, ol dynç almaly.','A2'),
 E('fever','/ˈfiːvə/','N','gyzzyrma','лихорадка','a high body temperature, usually caused by illness','He has a fever and a bad cough.','Onuň gyzzyrmasy we güýçli üsgülewügi bar.','A2'),
 E('aches and pains','/ˌeɪks ən ˈpeɪnz/','N','beden agyrylary','ломота и боли','general pains in different parts of the body','After the long walk, I had aches and pains everywhere.','Uzak ýörişden soň bedenimiň ähli ýeri agyrdy.','B1'),
]

ADDITIONS['word_building2'] = [
 E('width','/wɪdθ/','N','ini','ширина','the distance from one side of something to the other','Measure the width of the table.','Stoluň inini ölçäň.','B1'),
 E('depth','/depθ/','N','çuňlugy','глубина','the distance from the top or front of something to its bottom or back','The depth of the pool is marked on the wall.','Howzuň çuňlugy diwarda görkezilen.','B1'),
 E('length','/leŋθ/','N','uzynlygy','длина','the measurement from one end of something to the other','The bridge is one kilometre in length.','Köpriniň uzynlygy bir kilometr.','A2'),
 E('height','/haɪt/','N','beýikligi','высота','the distance from the bottom to the top of something','What is the height of the building?','Binanyň beýikligi näçe?','A2'),
 E('weak','/wiːk/','ADJ','gowşak','слабый','not strong or powerful','The signal is weak in this room.','Bu otagda signal gowşak.','A2'),
 E('weaken','/ˈwiːkən/','V','gowşamak, gowşatmak','ослабевать, ослаблять','to become less strong or make something less strong','The storm weakened during the night.','Tupan gijäniň dowamynda gowşady.','B1'),
 E('strength','/streŋθ/','N','güýç','сила','the quality of being physically or mentally strong','Swimming can improve your strength.','Ýüzmek güýjüňi artdyryp biler.','A2'),
 E('strengthen','/ˈstreŋθən/','V','güýçlendirmek','укреплять','to make something stronger','The new rules should strengthen the team.','Täze düzgünler topary güýçlendirmeli.','B1'),
]

SOURCE = {
 'personality': ('1A', 162, 217, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Personality; Teacher’s Guide photocopiable 1A vocabulary worksheet'),
 'work2': ('1B', 163, 218, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Work; Teacher’s Guide photocopiable 1B vocabulary worksheet'),
 'get_phrases': ('3A', 164, 219, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Phrases with get; Teacher’s Guide photocopiable 3A vocabulary worksheet'),
 'conflict': ('3B', 165, 220, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Conflict and warfare; Teacher’s Guide photocopiable 3B vocabulary worksheet'),
 'voice': ('4B', 166, 221, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Sounds and the human voice; Teacher’s Guide photocopiable 4B vocabulary worksheet'),
 'time_expr': ('5A', 167, 222, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Expressions with time; Teacher’s Guide photocopiable 5A vocabulary worksheet'),
 'money2': ('5B', 168, 223, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Money; Teacher’s Guide photocopiable 5B vocabulary worksheet'),
 'prefixes': ('7A', 169, 224, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Prefixes; Teacher’s Guide photocopiable 7A vocabulary worksheet'),
 'travel_tourism': ('8B', 170, 225, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Travel and tourism; Teacher’s Guide photocopiable 8B vocabulary worksheet'),
 'animal_matters': ('9A', 171, 226, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Animal matters; Teacher’s Guide photocopiable 9A vocabulary worksheet'),
 'preparing_food': ('9B', 172, 227, 'vocabulary_bank', 'Student’s Book Vocabulary Bank — Preparing food; Teacher’s Guide photocopiable 9B vocabulary worksheet'),
 'compound_adjs2': ('6A', 59, 91, 'vocabulary', 'Student’s Book 6A compound-adjective box; Teacher’s Guide 6A lesson plan'),
 'phones_tech': ('6B', 60, 95, 'vocabulary', 'Student’s Book 6B phones-and-technology vocabulary box; Teacher’s Guide definitions and answer keys'),
 'adjectives_preps': ('6B', 63, 101, 'vocabulary', 'Student’s Book 6B adjectives-and-prepositions box; Teacher’s Guide Vocabulary notes'),
 'health': ('8A', 76, 119, 'vocabulary', 'Teacher’s Guide 8A Vocabulary notes naming symptom vocabulary; linked to Student’s Book lesson 8A'),
 'word_building2': ('10A', 97, 153, 'wordbuilding', 'Student’s Book 10A word-building section; Teacher’s Guide 10A Vocabulary notes'),
}

# Existing Advanced lesson -> printed Student’s Book page at which the lesson starts.
LESSON_PAGE = {
 '1A':6,'1B':10,'CE1':14,'2A':16,'2B':20,'3A':26,'3B':30,'CE2':34,
 '4A':36,'4B':40,'5A':46,'5B':50,'CE3':54,'6A':56,'6B':60,
 '7A':65,'7B':70,'CE4':74,'8A':76,'8B':80,'9A':86,'9B':90,'CE5':94,
 '10A':96,'10B':100,
}


def main():
    src = GEN.read_text(encoding='utf-8')
    original = src
    tree = ast.parse(src)
    nodes = {}
    for n in tree.body:
        if isinstance(n, ast.Assign):
            for target in n.targets:
                if isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name) and target.value.id == 'T':
                    try: key = ast.literal_eval(target.slice)
                    except Exception: continue
                    nodes[key] = n
    lines = src.splitlines(keepends=True)
    inserts = []
    for topic, entries in ADDITIONS.items():
        if topic not in nodes:
            if topic == 'adjectives_preps':
                continue  # defined as a new direct T[...] list below
            raise SystemExit(f'no existing topic list for {topic}')
        node = nodes[topic]
        close_line = node.value.end_lineno - 1
        block = [f'    # OCR-reviewed additions, sourced as recorded in content/pdf/adv-candidates.json.\n']
        for row in entries:
            block.append('    ' + repr(row) + ',\n')
        inserts.append((close_line, ''.join(block), topic))
    for line_no, block, topic in sorted(inserts, reverse=True):
        lines.insert(line_no, block)
    src = ''.join(lines)

    # Add a distinct 6B group for the dependent-preposition list, and wire it into LESSONS.
    marker = "# ---- Vocabulary Bank — Prefixes -> 7A ----"
    if 'T[\'adjectives_preps\']' not in src:
        extra = "\n# ---- in-lesson 6B — adjectives + prepositions ----\nT['adjectives_preps'] = [\n"
        for row in ADDITIONS['adjectives_preps']:
            extra += '    ' + repr(row) + ',\n'
        extra += ']\n\n'
        src = src.replace(marker, extra + marker, 1)
    # Add this topic to the lesson table, which currently contains only phones_tech.
    src = src.replace("'6B': (6,  \"Can't give it up\", 'phones and technology', ['phones_tech']),",
                      "'6B': (6,  \"Can't give it up\", 'phones, technology, adjectives + prepositions', ['phones_tech', 'adjectives_preps']),", 1)

    # Source pages: bank pages override the first-page-of-lesson fallback.
    page_map = {topic: meta[1] for topic, meta in SOURCE.items()}
    mapping = "\n# Printed Student’s Book pages for exact source provenance. Vocabulary Banks use their back-of-book pages.\nTOPIC_PAGE = " + repr(page_map) + "\nLESSON_PAGE = " + repr(LESSON_PAGE) + "\n"
    anchor = "\ndef main():\n    words, seen, dups = [], {}, []\n"
    if 'TOPIC_PAGE = ' not in src:
        if anchor not in src: raise SystemExit('cannot locate generator main anchor')
        src = src.replace(anchor, mapping + anchor, 1)
    # Add page to every Advanced source reference.
    old = "                    'books': [{'book': 'adv', 'unit': unit, 'lesson': lesson}],\n                    'proofread': False,"
    new = "                    'books': [{'book': 'adv', 'unit': unit, 'lesson': lesson,\n                               'page': TOPIC_PAGE.get(t, LESSON_PAGE.get(lesson))}],\n                    'proofread': False,\n                    'confidence': 'medium' if key in {'sore throat', 'sneeze', 'high temperature', 'fever', 'aches and pains'} else 'high',"
    if old in src:
        src = src.replace(old, new, 1)
    elif "'page': TOPIC_PAGE.get(t, LESSON_PAGE.get(lesson))" not in src:
        raise SystemExit('cannot locate books reference to add page provenance')

    if src == original:
        raise SystemExit('no generator changes made')
    GEN.write_text(src, encoding='utf-8')

    # Candidate file is a compact audit trail: the SB printed page is the page
    # shown in the app; TG page is the physical PDF page used for corroboration.
    candidates = []
    for topic, entries in ADDITIONS.items():
        lesson, sb_page, tg_page, section, evidence = SOURCE[topic]
        for row in entries:
            candidates.append({
                'en': row[0], 'lesson': lesson, 'section': section,
                'page': sb_page, 'tg_pdf_page': tg_page,
                'evidence': ('teacher_guide_vocabulary_notes' if topic == 'health' else
                             'student_book_wordbuilding_box' if topic == 'word_building2' else
                             'student_book_vocabulary_bank' if section == 'vocabulary_bank' else
                             'student_book_vocabulary_box'),
                'page_role': 'lesson_reference' if topic == 'health' else 'exact_student_book_page',
                'tg_evidence': evidence, 'decision': 'added',
                'confidence': 'medium' if topic == 'health' else 'high',
            })
    # A word may appear in two candidate topic groups. The generator rejects
    # duplicates within one book, so refuse before writing if one slipped in.
    names = [c['en'].casefold() for c in candidates]
    dups = sorted({x for x in names if names.count(x) > 1})
    if dups: raise SystemExit('duplicate candidate headwords: ' + ', '.join(dups))
    OUT.write_text(json.dumps(candidates, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'patched {GEN}: {sum(map(len, ADDITIONS.values()))} additions across {len(ADDITIONS)} topic groups')
    print(f'wrote {OUT}: {len(candidates)} candidate records')

if __name__ == '__main__':
    main()
