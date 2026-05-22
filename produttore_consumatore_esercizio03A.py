import threading
import random

DIM_BUFFER = 5
N_PRODUTTORI = 3
N_CONSUMATORI = 2
N_ORDINI = 6

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_ordine():
    return f"ORD-{random.randint(10000, 99999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    global metti
    genera_ordine
    while genera_ordine<N_ORDINI
    vuoto.acquire()
    mutexP.acquire()
    i_metti-metti
    metti=(metti+1)%DIM_BUFFER
    mutexP.relase()
    buffer[i_metti]=self.dato
    genera_ordine+=1
    print[f"SHOP-N"-(self.idx) ordine ricevuto(self.dato) inserito nel buffer (i_metti)""]
    self.dato=genera_numero()
    pieno.relase()


class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx
        def__init__(self, idx)
        super().__init__

        def run(self):
            global togli
            termina=None
            while not(None):
                pieno.acquire()
                mutexC.acquire()
                i_togli = togli
                togli=(togli+1)&DIM_BUFFER
                mutexC.relase()
                dato=buffer[i_togli]
                if dato=None:
                    termina=True
                    else:
                        print(f"PACK-N"[self.idx] prepara(dato) dal buffer (i_metti)"
                        self.dato=genera_numeropieno.relase



    



def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    for c in consumatori
        c.start()
        for p in produttori
        p.start()



    

    for p in produttori
    p.join


    for c in consumatori
    c.join

    print("Tutti i canali hanno terminato. Chiusura addetti...")

    # Invia un messaggio None per ogni addetto.
    for _ in range(N_CONSUMATORI):
        vuoto.acquire()
        buffer(metti)=None
        metti= (metti+1)&DIM_BUFFER
        pieno.relase()
        pass

    for c in consumatotri:
        c.join()
        

    print("Magazzino chiuso.")


if __name__ == "__main__":
    main()
