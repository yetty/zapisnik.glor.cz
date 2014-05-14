Jak dostat velké panoráma na web?
#################################

:tags: fotky

.. class:: intro

Na blog často nahrávám panorámata krajinek a z důvodů omezeného místa na disku,
nepřizpůsobivého vzhledu stránek a dalších věcí, jsou obrázky poměrně malé.
Jak na web nahrát velký obrázek tak, aby si ho návštěvníci mohli vychutnat?

V tomto článku udělám něco nečekaného a doporučím hned tři služby Microsoftu.
Úplně nekritické to ale nebude.


Krok první: skládáme panoráma
*****************************

Dlouho jsem používat mocný nástroj Hugin. Nebyl jsem ho ale nikdy schopen úplně
zkrotit a tak jsem sáhl po něčem jednodušším. Po krátkém hledání jsem nalezl
Microsoft ICE, který mi celkem vyhovuje - naházíte do něj pár obrázků, on si je
rozumně pospojuje a výsledek neurazí.


Krok druhý: dostáváme panoráma na web
*************************************

Další důležitou částí je dostat obrázek na web. Takové panorama může mít klidně
pár desítek megabytů a nahrávat ho na vlastní hosting, pokud nemáte nějaký
neomezený,  nebývá to pravé.

Já sáhl po další službě Microsoftu - SkyDrive. Na zálohování je pro mne tato
služba nevyužitelná, protože klienta pro Linux jen tak mít nebude, tudíž si
fotkami nezaplácám omezený prostor.

Při registraci mne dokázal Microsoft překvapit. Maximální délka hesla je 16
znaků. Ani jsem nevěděl, že mám delší.

Na SkyDrivu jde pěkně nastavit sdílení, takže není problém zjistit URL adresu
obrázku. Jen si při nahrávání odškrtněte zmenšení na 2048px.


Krok třetí: připravujeme pro použití
************************************

A třetí a poslední služba Microsoft - `zoom.it <http://zoom.it>`_. Jednoduše
zadáte adresu obrázku, skript chvíli chroustá a vyplivne stránku, na které
můžete obrázek posouvat, zvětšovat a zmenšovat dle libosti.

Také ho můžete posílat nebo sdílet na stránkách. Pro ukázku použití jedno z
méně povedených panorámat z Jizerských hor:

.. raw:: html

    <script src="http://zoom.it/qCd5.js?width=auto&height=400px"></script>
