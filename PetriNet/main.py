# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pm4py.objects.petri import petrinet, marking

    #Use a breakpoint in the code line below to debug your script.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Creazione della rete di Petri
    petri_net = petrinet.PetriNet()

    # Creazione dei posti
    p1 = petrinet.Place("Sveglia suonata")
    p2 = petrinet.Place("Bagno")
    p3 = petrinet.Place("Colazione")
    p4 = petrinet.Place("Soggiorno")
    p5 = petrinet.Place("Studio")
    p6 = petrinet.Place("Pranzo")
    p7 = petrinet.Place("Pisolino")
    p8 = petrinet.Place("TV/Amici")
    p9 = petrinet.Place("Cena")
    p10 = petrinet.Place("Letto")
    p11 = petrinet.Place("Libro")
    p12 = petrinet.Place("Colazione speciale")
    p13 = petrinet.Place("Fai da te")
    p14 = petrinet.Place("Garage")
    p15 = petrinet.Place("Cena speciale")
    p16 = petrinet.Place("Film")

    # Aggiunta dei posti alla rete di Petri
    petri_net.places.add(p1)
    petri_net.places.add(p2)
    petri_net.places.add(p3)
    petri_net.places.add(p4)
    petri_net.places.add(p5)
    petri_net.places.add(p6)
    petri_net.places.add(p7)
    petri_net.places.add(p8)
    petri_net.places.add(p9)
    petri_net.places.add(p10)
    petri_net.places.add(p11)
    petri_net.places.add(p12)
    petri_net.places.add(p13)
    petri_net.places.add(p14)
    petri_net.places.add(p15)
    petri_net.places.add(p16)

    #Creazione delle transizioni per il g. normale

    t1 = petrinet.Transition("Sveglia", "Suonare la sveglia alle 7:00")
    t2 = petrinet.Transition("Bagno", "Andare al bagno")
    t3 = petrinet.Transition("Colazione", "Preparare la colazione")
    t4 = petrinet.Transition("Soggiorno", "Andare nel soggiorno")
    t5 = petrinet.Transition("Studio", "Andare nello studio")
    t6 = petrinet.Transition("Pranzo", "Preparare il pranzo")
    t7 = petrinet.Transition("Pisolino", "Fare un pisolino")
    t8 = petrinet.Transition("TV/Amici", "Guardare la TV o incontrare amici")
    t9 = petrinet.Transition("Cena", "Preparare la cena")
    t10 = petrinet.Transition("Letto", "Andare a letto")

    #Creazione delle transizioni giorno festivo
    t11 = petrinet.Transition("Libro", "Leggere un libro")
    t12 = petrinet.Transition("Colazione speciale", "Preparare una colazione speciale")
    t13 = petrinet.Transition("Fai da te", "Lavorare al progetto di bricolage")
    t14 = petrinet.Transition("Garage", "Andare al garage")
    t15 = petrinet.Transition("Cena speciale", "Preparare una cena speciale")
    t16 = petrinet.Transition("Film", "Guardare un film")

    #Aggiunta

    petri_net.transitions.add(t1)
    petri_net.transitions.add(t2)
    petri_net.transitions.add(t3)
    petri_net.transitions.add(t4)
    petri_net.transitions.add(t5)
    petri_net.transitions.add(t6)
    petri_net.transitions.add(t7)
    petri_net.transitions.add(t8)
    petri_net.transitions.add(t9)
    petri_net.transitions.add(t10)
    petri_net.transitions.add(t11)
    petri_net.transitions.add(t12)
    petri_net.transitions.add(t13)
    petri_net.transitions.add(t14)
    petri_net.transitions.add(t15)
    petri_net.transitions.add(t16)

    # Creazione delle arcate per il giorno normale
    a1 = petrinet.Arc(p1, t1)
    a2 = petrinet.Arc(t1, p2)
    a3 = petrinet.Arc(p2, t2)
    a4 = petrinet.Arc(t2, p3)
    a5 = petrinet.Arc(p3, t3)
    a6 = petrinet.Arc(t3, p4)
    a7 = petrinet.Arc(p4, t4)
    a8 = petrinet.Arc(t4, p5)
    a9 = petrinet.Arc(p5, t5)
    a10 = petrinet.Arc(t5, p6)
    a11 = petrinet.Arc(p6, t6)
    a12 = petrinet.Arc(t6, p7)
    a13 = petrinet.Arc(p7, t7)
    a14 = petrinet.Arc(t7, p8)
    a15 = petrinet.Arc(p8, t8)
    a16 = petrinet.Arc(t8, p9)
    a17 = petrinet.Arc(p9, t9)
    a18 = petrinet.Arc(t9, p10)

    # creazione arcate giornate festive
    a19 = petrinet.Arc(p1, t11)
    a20 = petrinet.Arc(t11, p12)
    a21 = petrinet.Arc(p12, t12)
    a22 = petrinet.Arc(t12, p13)
    a23 = petrinet.Arc(p13, t13)
    a24 = petrinet.Arc(t13, p14)
    a25 = petrinet.Arc(p14, t14)
    a26 = petrinet.Arc(t14, p15)
    a27 = petrinet.Arc(p15, t15)
    a28 = petrinet.Arc(t15, p16)

    #aggiunta arcate
    petri_net.arcs.add(a1)
    petri_net.arcs.add(a2)
    petri_net.arcs.add(a3)
    petri_net.arcs.add(a4)
    petri_net.arcs.add(a5)
    petri_net.arcs.add(a6)
    petri_net.arcs.add(a7)
    petri_net.arcs.add(a8)
    petri_net.arcs.add(a9)
    petri_net.arcs.add(a10)
    petri_net.arcs.add(a11)
    petri_net.arcs.add(a12)
    petri_net.arcs.add(a13)
    petri_net.arcs.add(a14)
    petri_net.arcs.add(a15)
    petri_net.arcs.add(a16)
    petri_net.arcs.add(a17)
    petri_net.arcs.add(a18)
    petri_net.arcs.add(a19)
    petri_net.arcs.add(a20)
    petri_net.arcs.add(a21)
    petri_net.arcs.add(a22)
    petri_net.arcs.add(a23)
    petri_net.arcs.add(a24)
    petri_net.arcs.add(a25)
    petri_net.arcs.add(a26)
    petri_net.arcs.add(a27)
    petri_net.arcs.add(a28)

    #Marcatura giorno feriale
    initial_marking = marking.Marking()
    initial_marking[p1] = 1

    #Marcatura giorno festivo
    initial_marking_holiday = marking.Marking()
    initial_marking_holiday[p1] = 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
