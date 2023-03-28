# Vaatimusmäärittely
## Sovellus:
Sovellus on kaikille tuttu Tetris peli, jossa on mahdollista tallentaa oma suoritus tietokantaan. Muiden suoritukset näkyvät ```leaderboards```-taulukosta.

## Käyttöliittymä:
Pelin käyttöliittymä on koodattu Pythonin ```pygame```-kirjastoa hyödyntäen. Käyttöliittymästä näkee myös ```leaderboards```-taulukon.
## Tetris:
* Peli randomoi palikan (I, J, L, O, S, T, Z), joka alkaa liikkumaan ruudulla alaspäin
* Palikkaa liikutetaan sivuille nuolinäppäimistä
* Palikan rotaatio tapahtuu painamalla nuolinäpääintä ylös
* Palikka ei voi mennä ruudun yli mistään suunnasta
* Palikka pysähtyy pohjalle tai jos se osuu toiseen palikkaan
* Täytetty rivi tyhjennetään
* Peli loppuu kun jokin palikka osuu yläreunaan
* Pelin päätyttyä tulos talletetaan tietokantaan valitsemalla nimellä

## Jatko kehitys:
* Mahdollisuus luoda käyttäjä ja kirjautua sisään ennen pelin alkua
