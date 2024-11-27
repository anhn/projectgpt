import streamlit as st
import pandas as pd

feedback1 = "Students are divided into teams of six to eight students. Teams are formed by randomly assigning students; the members generally do not know each other beforehand. This is a typical situation in a real life setting, especially when working as a consultant. The students are free to choose the methods that best fit their projects. In some cases, the development approaches are enforced by customers due to existing working processes they have adopted in their organizations. Each team decides by themselves about their management and leadership mechanisms. In most of the cases, students organize themselves using a flat organizational structure within the team. Decision making is often done collectively and the reasons for important decisions are documented in the final reports. There are several lectures at the beginning of the course teaching topics such as project management, team dynamics, Scrum, architecture, and testing."
feedback2 = "Students typical engage in three phases of their projects, which are planning, execution and closing (refer to Figure 1). In the planning phase, the students get to know their team members, customers, and their project requirements. The students need to decide roles and areas of responsibility for each member. They also make a preliminary project plan and set up the working environment. In the execution phase, the student teams typically carry out sprints with frequent deliveries to their customers. Each project covers fundamental SE activities, i.e., requirement elicitation, architecture level design, coding, and testing. Students also write a project report that reflects their team’s progress. In the closing phase, the project results are submitted in a report; they are also demonstrated and presented to the customer and course staff (e.g., course instructor, supervising teaching assistant)."
feedback3 = "The course deliverables for each team include (1) an end of term demonstration of the software, (2) a presentation, and (3) a final project report. The course project work is evaluated on the basis of the quality of the project reports, the functioning prototype of the system, the presentation delivered at the end of the course, and the team dynamics. Customers consider their experience working with the team, the value of the software developed, and the delivered report in their evaluations. Supervisors, who are typically teaching assistants in the course, evaluate their teams’ performance and learning based on their observations throughout the course. The faculty member responsible for the course involves both the customer and the supervisor in an evaluation meeting to determine the final marks for students. In the evaluation scheme, a team with a poorly functioning application does not necessarily receive a low grade. Student teams that have difficult projects with poor functionality, but express quick learning curves and effective teamwork can achieve a good grade."

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

df = pd.DataFrame({
    "UserId": [1, 2, 3,4,5,6,7,8,9,10,11,12],
    "Exercise": [exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2,exercise2],
    "Feedback": [feedback1,feedback2,feedback3,feedback1,feedback2,feedback3,feedback1,feedback2,feedback3,feedback1,feedback2,feedback3],
    "FeedbackSent": [True,False,True,True,False,True,True,False,True,True,False,True]
})
edited_df = st.data_editor(df)

def click_button():
    edited_df.to_csv("data.csv", index=False)

st.button('Send feedback', on_click=click_button)
