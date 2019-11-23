            _
         __| |___
       .' _| |__ '.
     .' .- |    -. '.
    .' |   |( |\  | '.
    | <    |  | |  | |
    '. |   |( |/  | .'
     '. '-_|____-' .'
       '.________.'


## POZNAMKY

* kdyz najdete bug, nejaky tam budou, ty nejhorsi veci mi dat do issues na githubu a opravim je, at se v tom nemusite nejak moc vrtat
* pouzivat django.contrib.messages
* otestovat unicode
* hesla ke vsem profilum q1w1e1r1

## ZBYTEK

### VETSI VECI:
* implementovat zapasy, vysledky zapasu, rozlosovani a statistiky
* trochu si pohrat se vsema sablonama, aby se neopakovaly tak je rozdelit na mensi (viz google "django generic views" nebo tak neco). treba tri sablony pro index uzivatelu, kde by stacila jedina. strankovani do jedne sablony atd.
### DROBNOSTI:
* nastavit ze na bezici turnaj se neda registrovat atd.
* nastavit aby se na plnej turnaj nedaly posilat requesty o registraci
* turnaj pujde editovat pouze do dokonceni, az se ukonci (tj pocet zapasu bude naplnenej, tak se deaktivuje)
* v sablone profile.html dat aby se nevypisovala tabulka kdyz nic neni v .all
* team by mel jit editovat stejne jako turnaj, mozna s max poctem hracu?
* po operacich s formularem skacu na forms:profile, skakat jinam
* pridat do detailu usera seznam tymu ktery ridi a nejaky podobny picoviny, vsechno je nachystany

### KONZULTACE:
* Pri smazani posledniho hrace z teamu nemazeme team
