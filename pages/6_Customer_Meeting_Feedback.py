import streamlit as st
import pandas as pd

feedback1 = 8
feedback2 = 5
feedback3 = 9

exercise2="""Modul 2 – exercise 4.
Hovedsakelig kan man si at de aller fleste punktene på ønskelistene overholder disse seks punktene. Likevel finner man noen unntak, her er noen av dem:
-          Klarhet:
Membership Plans and Pricing: Kan virke uklar siden vi ikke får noen konkrete eksempler på når en kunde får rabatt eller hva som menes med «special offers».
-          Konsistens:
Floor plan: Mangel av en «floor plan» i ønskelisten.
-          Korrekt:
Alle punktene på ønskelisten er korrekte stemmer overens med primær målet.
-          Entydighet:
Clear and Engaging Headline: Hva som blir sett på som oppmerksomhetsfangende er subjektivt og kan bli tolket på ulike måter.
Compelling Visuals: Hva som er et høy kvalitets bilde/video kan også kan virke tvetydig siden hva man ser på som høy kvalitet kan variere.
Resten er lette å forstå og gir liten rom for tolkning.
-          Målbarhet:
De er alle målbare ved å enten gjøre egne tester for å teste om systemet faktisk fungerer og er kompatibelt med andre systemer som har andre spesifikasjoner. Eller man kan gjøre en rekke tester der man henter inn brukerrespons for å vurdere suksessen. 
-          Kontrollbarhet:
Testimonial and Reviews: Dette kan være halvveis kontrollerbart siden vi kan spørre nåværende medlemmer om attester. Men det garanterer ikke at vi har noen positive.
Resten er kontrollerbart.
1.   	Som et potensielt medlem, ønsker jeg å se en tydelig og engasjerende overskrift på nettstedet, slik at jeg blir nysgjerrig og vil vite mer om USNStart Coworking Space. 
2.   	Som et potensielt medlem, ønsker jeg å se høykvalitets bilder eller videoer av coworking-området, slik at jeg kan få en visuell forståelse av interiøret, arbeidsstasjonene, fellesområdene og fasilitetene.
3.   	Som et potensielt medlem, ønsker jeg å se en oversikt over medlemskapstilbudene og prisene, slik at jeg kan vurdere hvilket alternativ som passer best for mine behov og budsjett.
4.   	Som et potensielt medlem, ønsker jeg å vite hvilke fasiliteter og tjenester som tilbys på coworking-området, for eksempel høyhastighets internett, møterom, kaffelounge osv., slik at jeg kan vurdere om det oppfyller mine behov.
5.   	Som et potensielt medlem, ønsker jeg å se informasjon om beliggenheten til coworking-området, inkludert adressen, et kart og informasjon om offentlig transport eller parkeringsmuligheter i nærheten.
6.   	Som et potensielt medlem, ønsker jeg å lese positive attester eller anmeldelser fra nåværende medlemmer, slik at jeg kan bygge tillit og troverdighet til coworking-området.
7.   	Som et potensielt medlem, ønsker jeg å ha flere kontaktalternativer, for eksempel en e-postadresse, telefonnummer og et kontaktskjema, slik at det er enkelt for meg å komme i kontakt med USNStart Coworking Space.
8.   	Som et potensielt medlem, ønsker jeg å lese en kort oversikt over coworking-områdets historie, misjon og verdier, slik at jeg kan forstå hva som gjør fellesskapet unikt.
9.   	Som et potensielt medlem, ønsker jeg at nettstedet skal være responsivt og mobilvennlig, slik at det vises riktig på alle enheter og skjermstørrelser. 
10.   Som et potensielt medlem, ønsker jeg å se en tydelig og informativ seksjon om personvern og sikkerhet, slik at jeg kan være trygg på at mine personopplysninger vil bli beskyttet.
11.   Som et potensielt medlem, ønsker jeg å se en oversikt over den foreslåtte planløsningen og bilder av interiørdesign, slik at jeg kan få en visuell forståelse av hvordan coworking-området vil se ut.
12.   Som et nåværende medlem, ønsker jeg å kunne bestille ledige arbeidsplasser i det åpne arbeidsområdet med en dagpass eller månedlig medlemskap for gjeldende måned, slik at jeg kan sikre en plass i coworking-området.
13.   Som et nåværende medlem, ønsker jeg å motta en bekreftelse etter å ha gjort en reservasjon for å bekrefte at plassen er sikret.
14.   Som et nåværende medlem, ønsker jeg å kunne se en interaktiv og visuell floor plan for å velge og reservere en bestemt arbeidsplass i det åpne arbeidsområdet.
15.   Som en nåværende medlem, ønsker jeg å kunne se informasjon om tilgjengelige parkeringsplasser ved coworking-området, slik at jeg kan planlegge min ankomst og avgang
"""
st.selectbox("Class", options=["PRO1000 Bø", "PRO1000 Net", "PRO1000 Gol"], placeholder="Select an option", index=None)
st.selectbox("Exercise", options=["M1E1 - Stakeholder analysis", "M2E2 - Workbreakdown Structure", "M2E3 - User Stories", "M2E4 - GanttChart", "M3E1 - Risk management"], placeholder="Select an option", index=None)
st.button('Retrieve latest data')
df = pd.DataFrame({
    "UserId": [1, 2, 3,4,5,6,7,8,9,10,11,12],
    "SummaryOfCustomerMeetings": [exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2],
    "Grade": [feedback1,feedback2,feedback3,feedback1,feedback2,feedback3,feedback1,feedback2,feedback3,feedback1,feedback2,feedback3],
    "SummaryOfSprintPlanningMeetings": [exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2],
    "Grade": [feedback1,feedback2,feedback3,feedback1,feedback2,feedback3,feedback1,feedback2,feedback3,feedback1,feedback2,feedback3],
    "SummaryOfSprintRetrospectiveMeetings": [exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2],
    "Grade": [feedback1,feedback2,feedback3,feedback1,feedback2,feedback3,feedback1,feedback2,feedback3,feedback1,feedback2,feedback3],})

edited_df = st.data_editor(df)

def click_button():
    edited_df.to_csv("data.csv", index=False)

st.button('Save', on_click=click_button)
