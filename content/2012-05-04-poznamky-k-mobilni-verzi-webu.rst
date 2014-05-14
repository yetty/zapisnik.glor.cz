Poznámky k mobilní verzi webu
#############################

:tags: návod

.. class:: intro

Přistupování na web přes nějaký chytrý telefon, či podobné zařízení, jehož
rozměry nedosahují rozměrů stolních monitorů, je čím dál tím běžnější. A zdá
se, že tento trend bude pokračovat.

Na západ od nás je situace ještě výraznější. Objevily se
`první vlaštovky <http://www.zeldman.com/>`_, které
dokonce nenavrhují vzhled stránek pro počítač, ale rovnou pro mobil.

Proto není úplně vhodné mobilní verzi zanedbat. Pár tipů, které mohou usnadnit
její odladění.


Detekce mobilního zařízení
**************************

Obecně lze mobilní zařízení rozpoznat dvěma způsoby. Pomocí skriptu na straně
serveru a speciálním kódem ve stylech.


Rozpoznání na straně skriptu
----------------------------

Hotové řešení pro většinu běžných jazyků je k dispozici na webu
`detectmobilebrowsers.com <http://detectmobilebrowsers.com/>`_. Tuto podmínku
stačí zakomponovat do vašich stránek a pokud se mobilní zařízení jedná, načíst
např. speciální styl.

Toto řešení používám já. Jediné mi fungovalo spolehlivě.


Rozpoznání v CSS
----------------

Tento způsob funguje na základě načítání různých stylů podle šířky prohlížeče.
Má mnoho výhod - odpadají problémy s cachováním, lze velmi snadno vytvořit
styly pro různá zařízení (jinak široká). Na jediný problém jsem narazil - na
testovacím mobilu mi tento princip nefungoval.

Možné je buď načítat přímo speciální styl:

.. code::

    <link rel="stylesheet" media="screen and (max-device-width: 480px)" href="../mobile.css" type="text/css" />


Nebo až CSS souboru:

.. code::

    @media screen and (max-device-width: 480px) {
        ...
    }


Šířku je samozřejmě třeba nastavit podle zařízení.



Rozpoznání serverem
-------------------

Existuje ještě třetí způsob - rozeznat zařízení pomocí serveru. V podstatě se
jedná o podobný princip, jako v případě rozeznání skriptem. Jen se podmínka
přesouvá do .htaccessu (v případě Apache). Detailní popis je `k dispozici na
stackoverflow.com <http://stackoverflow.com/a/1005171>`_.



Nastavení škálování, správná šířka
**********************************

Problém, na který jsem narazil, bylo vykreslování pouze v úzkém pruhu. V
některých prohlížečích (Opera) s tím nešlo nic dělat, v některých se pruh sám
po načtení roztáhl na celou šířku.

Ke sjednocení a správnému vykreslování je potřeba do hlavičky HTML přidat meta
tag *viewport*. Tím je možné nastavit počáteční šířku, minimální i maximální
šířku a možnosti přibližování.

.. code::

    <meta name="viewport" content="width=device-width, initial-scale=1">


Podrobnosti a detailní návod k použití je rozepsán `na webu
Mozilly <https://developer.mozilla.org/en/Mobile/Viewport_meta_tag>`_.


Cachování a rozlišení verzí
***************************

Pokud nepoužijete rozlišování css styly, je potřeba jednotlivé verze rozlišit
adresou. Pokud by byla adresa stejná, docházelo by k cachování, které by
způsobilo, že i normálním uživatelům se zobrazuje verze pro mobily a obráceně.

Nejsnazší je přidat parametr GET:

.. code::

    http://mojeadresa.cz/stranka.html?mobile

a existenci parametru pak ověřovat (např. pomocí PHP):

.. code::

    if (isset($_GET['mobile'])) {
        ...
    }

Druhou možností je pak mít pro mobilní verzi vlastní subdoménu a rozlišovat
pomocí ``$_SERVER['HTTP_HOST']``:

.. code::

    if (preg_match('#^m\.#', $_SERVER['HTTP_HOST'])) {
        ...
    }


Testovaní
*********

Jak ověřit, že všechno funguje, jak má? Nejsnazší je vzít do ruky mobil a
adresu vyťukat. Další možností je rozběhnout nějaký emulátor na počítači,
třeba pro `Android <http://developer.android.com/index.html>`_.

Funguje také doplněk `User Agent
Switcher <https://addons.mozilla.org/cs/firefox/addon/user-agent-switcher/>`_ pro
Firefox, který se dokáže identifikovat jako libovolný prohlížeč. Vzhled díky
tomu moc neotestujete, tak alespoň to rozpoznávání.

Všelijaké online emulátory fungují velice pochybně.



Na co myslet při navrhování vzhledu?
************************************

A ještě pár praktických rad na závěr: udělejte to tak příjemně ovladatelné, jak
jen to je možné. To znamená, že navigaci musí být tak velká, aby se do ní dalo
trefit. Bez problémů.

Stejně tak i velikost písma musí být taková, aby i člověk na čtení nemusel brát
lupu. Musí se počítat s tím, že na malý displej se toho tolik nevleze. Není od
věci celý design zjednodušit a přebytečné prvky odstranit, schovat.

