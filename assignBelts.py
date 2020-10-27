
def belts2flights(belts, flights):
    """Belts assigned to flights.
    Requires: belts is a list of pairs, where the first component is the number of
    the belt and the second component the next time this belt will be available,
    sorted according to their increasing hour of availability, and flights is a list
    of tuples, as described in the quizz, each corresponding to one flight, sorted
    according to their increasing arrival time.
    Ensures: list of lists whose first element is a belt, the second the time when it
    is available, and the third a flight (represented as a tuple)"""

    main_list=[]
    entry=[]
  
    for i in range(flights):   # browse the list of flights and add to itself the information of each carpet
      entry=[belts[i][0],belts[i][1],flights[i]]
      main_list.append(entry)
    return main_list





def beltsTimes2flights(beltsflights):
    """Time of start and end of operation of belts assigned to flights, ensuring
    minimal time of wait for the passengers of each fligh.
    Requires: beltsflights is a list of lists whose first element is a belt, the
    second the time when it is available, and the third a flight (represented as a
    tuple)
    Ensures: list of lists whose first element is a belt, the second the time when it
    starts into operation, the third when it stops, and the fourth the flight
    (represented as a tuple) delivering its lugages via that belt"""

    main_list=[]
    entry=[]
    
    for i in range(beltsflights): # end time
        entry=[beltsflights[i][0],beltsflights[i][1],calcula_fim(beltsflights[i]),beltsflight[i][2]]
        main_list.append(entry)
    return main_list

def calcula_fim(calc): #estimated time that the carpet takes to make the "belts" of flights / returns the time the belt is available

    
    bagagens=calc[2][-1]
    minutos= int(bagagens * 30/200)
    tempo_fim_horas=int(calc[1][:2])
    tempo_fim_minutos=int(calc[1][3:])
    while minutos>=60 :
        minutos = minutos-60
        tempo_fim_horas=tempo_fim_horas+1
    tempo_fim_minutos = tempo_fim_minutos+minutos
    if tempo_fim_minutos >= 60:
        tempo_fim_horas=tempo_fim_horas +1
        tempo_fim_minutos =tempo_fim_minutos%60
    tempo_fim=""+str(tempo_fim_horas)+":"+str(tempo_fim_minutos)
    return tempo_fim
    
    

    
    
    
        
