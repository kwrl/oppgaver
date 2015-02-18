---
title: Roterende kube
author: H. Kaurel
level: 4
---

#Introduksjon {.intro}
I denne oppgaven skal vi lage en kube som roterer, og vi skal gjøre det så kort og konsist som vi klarer. I denne oppgaven kommer jeg til å bruke et helt fantastisk python-bibliotek som heter itertools for å vise hvor kort og greit enkelte ting kan løses.

#Lag et tomt pygame-program{.activity}
Før vi begynner å lage kuben vår så må vi nok en gang skrive en del kode for å sette opp et vindu som vi kan tegne i. Dette ble dekket i forrige oppgave, så jeg kommer ikke til å gå grundig igjennom det her.

Programmet du lager skal åpne et vindu hvor vi kan tegne med OpenGL og kjøre helt til noen krysser ut vinduet.

##Sette riktig perspektiv{.info}
```python
gluPerspective(45, display[0]/display[1], 0.1, 50)
glTranslatef(0, 0, -5)
```

##Lage punkter
For å tegne kuben vår så trenger vi en rekke punkter som OpenGL kan tegne mellom. Vi tar utgangspunkt i hjørnene på kuben vår. Kuber har åtte hjørner, altså må vi definere åtte punkter. Vi kan gjøre det slik som vist under.
```python
vertices = [
  (-1, -1, -1),
  (-1, -1, 1),
  (-1, 1, -1),
  (-1, 1, 1),
  (1, -1, -1),
  (1, -1, 1),
  (1, 1, -1),
  (1, 1, 1),
]
```

Selv om dette er en helt grei måte å gjøre det på, så går det an å gjøre det på en annen og mer konsis måte.

```python
vertices = list(itertools.product((-1, 1), repeat=3))
```
Dette vil gi akkurat det samme resultatet, bare at det er skrevet litt mer konsist.

##Tegne mellom punktene
Nå har vi laget punktene våres, og det eneste som gjenstår er å tegne mellom dem i vinduet vårt. Som du trolig husker så bruker vi glBegin for å si at vi skal begynne å tegne med OpenGL, og avslutter med glEnd. Sist sendte vi inn GL_QUADS som parameter til glBegin, noe som resulterte i at OpenGL tegnet en flate mellom de fire punktene vi sendte inn. Denne gangen skal vi bare tegne noen enkle streker mellom forskjellige punkter. For å få til dette så sender vi inn GL_LINES til glBegin.

```python
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glBegin(GL_LINES)
glEnd()
```

Når vi bruker OpenGL så vil det bli tegnet mellom hvert par av punkter som vi sender inn med glVertex3fv, så hvilke punkter skal vi sende inn og i hvilken rekkefølge?

Siden jeg er litt lat så orker jeg ikke å tenke så nøye på dette, jeg tar en liten snarvei, jeg tegner mellom alle punktene!

```python
glClear(blabla.. )
glBegin(blabla.. )
for edge in itertools.combinations(vertices, 2):
    glVertex3fv(edge[0])
    glVertex3fv(edge[1])
glEnd()
```

Hvis du kjører programmet ditt og du har gjort alt riktig så skal du får opp noe som på sett og vis minner om en kube. Dessverre er det masse unødvendig streker som går på skrå rundt omkring også. Det vi trenger nå er en måte å la være å tegne skrå streker, vi vil bare ha de som går rett.

Gjør om på for-løkken din slik at den blir seende slik ut. Klarer du å forstå hva de to nye linjene gjør?

```python
for edge in itertools.combinations(vertices, 2):
    vec = tuple(map(sub, edge[0], edge[1]))
    if len([x for x in vec if abs(x)>0]) > 1: continue
    glVertex3fv(edge[0])
    glVertex3fv(edge[1])
```
