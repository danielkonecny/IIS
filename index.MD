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
new / edit tournament
messages
paging
singleplayer
https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/

///////////////////////////
                         //
POZNAMKY                 //
                         //
///////////////////////////

-kdyz najdete bug, nejaky drobnosti tam budou, ty nejhorsi picoviny mi dat do issues a opravim je at se v tom nemusite nejak moc vrtat

///////////////////////////
                         //
ZBYTEK                   //
                         //
///////////////////////////

-implementovat zapasy, vysledky zapasu, rozlosovani a statistiky
-turnaj pujde editovat pouze do dokonceni, az se ukonci (tj pocet zapasu bude naplnenej, tak se deaktivuje)
-pokud pridava sebe do tymu, tak pridat primo a bez requestu
-pouzivat messages
-kde je potreba prohodit uzivatelska jmena za skutecna a nastavit ulozeni first name a last name jako povinne u uzivatele
-nastavit picoviny jako ze na zaplej turnaj se neda registrovat atd.
-trochu si pohrat s sablonama, aby se neopakovaly tak je rozdelit na mensi (viz google "django generic views" nebo tak neco)
-v sablone profile html dat aby se nevypisovala tabulka kdyz nic neni v .all
-trochu si pohra se sturkturou html, nekde je potreba nahradit P za DIVy
-team by mel jit editovat stejne jako turnaj
-otestovat unicode
-presmerovavat z forms:'all' na stranku odkud prisel, jen nahradit forms:profile za neco jinyho vsude
