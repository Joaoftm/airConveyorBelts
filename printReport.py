
import readInput
import sort

def operationReport(inputFile, beltsflights, outputFile):
    """The file with the operation report.
    Requires: inputFile, for arrivals, is a text file with the structure indicated in
    the quizz, beltsflights is list of lists whose first element is a belt, the
    second the time when it starts into operation, the third when it stops, and the
    fourth the flight (represented as a tuple) delivering its lugages via that belt,
    and outputFile is a text file where the operation report will be written
    Ensures: text file with the operation report as described in the quizz"""
    fich=open(outputFile, 'w').close() #to "clean" the file if it has already been created
    fich=open(outputFile,"a") # "a" opens the file to add text without erasing what is already written

    lonDelTime=0
    avDelTime=0
    bagagens =0
    
    cabecalho=readInput.headerArrivalsFile(inputFile)  #begin
    arrivals=readInput.arrivalsFile(inputFile)
    sort.flights(arrivals)

    fich.write(cabecalho+"\n")
    fich.write("Belts:\n")
    for beltflight in beltsflights:
        fich.write(beltflight[0]+", "+beltflight[1]+", "+beltflight[2]+", ("+beltflight[3][0]+", "+beltflight[3][1]+", "+beltflight[3][2]+", "+str(beltflight[3][3])+", "+str(beltflight[3][4])+")\n")
    fich.write("Flights:\n")
    for beltflight in beltsflights:
        tMinE=calc(beltflight[3][2], beltflight[1], beltflight[2])
        tMaxE=calculaDif(beltflight[3][2],beltflight[2])
        bagagens=bagagens+beltflight[3][4]
        fich.write("("+beltflight[3][0]+", "+beltflight[3][1]+", "+beltflight[3][2]+", "+str(beltflight[3][3])+", "+str(beltflight[3][4])+"), "+beltflight[0]+", "+str(tMinE)+" min\n")
        avDelTime=avDelTime+tMinE*beltflight[3][4]
        lonDelTime=max(lonDelTime, tMaxE)
    fich.write("Global:\n")
    fich.write("Average delivery time = "+str(int(avDelTime/bagagens))+" min\n")
    fich.write("Longest delivery time = "+str(lonDelTime)+" min\n")
    fich.close()

def calc(voo, inicio, fim):    #calculate the average time of luggage waiting for a flight

    voo_inicio=calculaDif(voo,inicio)

    inicio_fim=calculaDif(inicio,fim)

    return voo_inicio+inicio_fim/2

def calculaDif(t1,t2):
    
    h1=int(t1[:2])
    m1=int(t1[3:])
    h2=int(t2[:2])
    m2=int(t2[3:])
    
    if h1==h2:
        return abs(m1-m2)
    elif abs(h1-h2)==1:
        return 60-abs(m1-m2)
    else:
        dh=abs(h1-h2)
        return dh*60+abs(m1+m2)














    
    

