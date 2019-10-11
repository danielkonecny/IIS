            _
         __| |___
       .' _| |__ '.
     .' .- |    -. '.
    .' |   |( |\  | '.
    | <    |  | |  | |
    '. |   |( |/  | .'
     '. '-_|____-' .'
       '.________.'

MOJE
----
paging
singleplayer:
team co ma vic nez 1 hr nesmi pozadat o vstup do nesingleplayer. Do tohohle teamu se nesmi nikdo pridat. Mozna radsi udelat specialni podtridu pro singleplayer teamy.

///////////////////////////
                         //
POZNAMKY                 //
                         //
///////////////////////////

-odkazy na formulare radsi pres A, nepouzivat dva FORMy za sebou
-kdyz najdete bug, nejaky drobnosti tam budou, ty nejhorsi picoviny mi dat do issues a opravim je at se v tom nemusite nejak moc vrtat
-pouzivat django.contrib messages

///////////////////////////
                         //
ZBYTEK                   //
                         //
///////////////////////////

-pridat sponzora do turnaje
-implementovat zapasy, vysledky zapasu, rozlosovani a statistiky
-turnaj pujde editovat pouze do dokonceni, az se ukonci (tj pocet zapasu bude naplnenej, tak se deaktivuje)
-pokud pridava sebe do tymu, tak pridat primo a bez requestu
-kde je potreba prohodit uzivatelska jmena za skutecna a nastavit ulozeni first name a last name jako povinne u uzivatele
-nastavit picoviny jako ze na zaplej turnaj se neda registrovat atd.
-trochu si pohrat s sablonama, aby se neopakovaly tak je rozdelit na mensi (viz google "django generic views" nebo tak neco)
-v sablone profile html dat aby se nevypisovala tabulka kdyz nic neni v .all
-team by mel jit editovat stejne jako turnaj
-otestovat unicode
-presmerovavat z forms:'all' na stranku odkud prisel, jen nahradit forms:profile za neco jinyho vsude
