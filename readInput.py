


def arrivalsFile(file_name):
    """Reads part of an input file with the arrivals into a list of flights.
    Requires: file_name, for arrivals, is a text file with the structure indicated in
    the quizz
    Ensures: list of tuples, each corresponding to one flight"""

    ficheiro = open(file_name,'r')
    conteudo = ficheiro.readlines()
    ficheiro.close()
    arrivals=[]
    arrivals_aux=[]   # list of flights in the form of str
    for element in conteudo:
        retira=element.rstrip("\n") #strip the last element and change line
        arrivals_aux.append(retira)
    numeration=arrivals_aux.index("Arrivals:")
    for element in arrivals_aux[numeration+1:]:  # will iterate over the input of flights
        arrivals.append(Flightline(element))
    return arrivals


def Flightline(line):
    """Convert a line with a flight identification into a standard format.
    Requires: line is a string whose content correspond to one line/flight as
    indicated in the quizz (flight code, origin, arrival time, nb passengers, nb
    lugages), as in the example "TP539, Berlin, 08:40, 175, 237"
    Ensures: a tuple where each element corresponds to each element of the flight as
    indicated above"""

    new_line=line.split(", ")  # takes what is within and separate each element
    tuple(new_line)
    return new_line


def headerArrivalsFile(file_name): #general airport information
    """Reads the header of an input file with the arrivals into a string.
    Requires: file_name, for arrivals, is a text file with the structure indicated in
    the quizz
    Ensures: string representing the header of the file_name, including line breaks"""

    ficheiro=open(file_name,"r")
    conteudo=ficheiro.readlines()
    ficheiro.close()
    numeration=conteudo.index("Arrivals:\n") # takes the input start file
    header = conteudo[0]
    for line in conteudo [1:numeration-1]:            # reads the lines to arrivals
        header=header + "" + line
    header=header + (conteudo[-1])
    return header

    

def operationReport(file_report):  #belt and end time
    """Reads part of an input file with an operation report into a list of belts with
    the hours at which they are available to be used.
    Requires: file_report, for an operation report, is a text file with the structure
    indicated in the quizz
    Ensures: list of pairs, where the first component is the number of the belt and
    the second component the next time this belt will be available within the current
    period of operation"""

    ficheiro=open(file_report,"r")
    conteudo=ficheiro.readlines()
    ficheiro.close()
    name_time_list=[]
    Belts=conteudo[conteudo.index("Belts:\n")+1:conteudo.index("Flights:\n")]
    for belt in Belts:
        name=belt[:2] # takes the name of the belt
        if "not_used" in belt:   # if the belt is not being used
            time=belt[4:9] #if it is not being used takes the start time
        else:
            time=belt[11:16] # if it is used takes the time that has just been used
        name_time_t=(name,time) # ttuple with the name and time belt
        name_time_list.append(name_time_t)
    return name_time_list
        
            
            
            
    
        
    
    
    
    

    
        
    
    
