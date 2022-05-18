# cities_traffic
Vogliamo realizzare una simulazione dove delle 'macchine' si spostano da una città all'altra, fino a quando tutte le vetture finiscono la loro 'benzina'. La rete delle città è descritta da un file csv con il seguente formato
Partenza | Arrivo | Distanza
------ | ------ | ------
Roma  |  Milano  |   123 

nono si può andare da una città a se stessa, i link sono bidirezionali (nell'esempio si può andare da roma a milano e da milano a roma, non è necessario che tutte le città siano collegate tra di loro, evitare di lasciare città scollegate
Le 'macchine' sono istanze di una classe CitiesCar, con due proprietà, 'Benzina', ovvero con quanta benzina iniziano il percorso e 'CittaVisitate' una lista che contiene alla fine della simulazione le città visitate

La simulazione funziona così
```
carica il file csv con la rete dentro un dataframe

estrai la lista delle città prese una sola volta e mettile in una lista
(è un algoritmo classico, ma non semplice da immaginare ....)

crea N istanze di CitiesCar e assegnale ad una lista

metti ogni macchina su una città (ovvero scrivi il nome di una citta SCELTA A CASO dentro la proprietà CittaVisitate di ogni macchina)

for t da 1 a 'Fine della simulazione'
 muovi ogni macchina dalla città dove si trova ad una collegata scelta a caso
 (ovvero aggiorna CittaVisitate
 
```

alla fine sarebbe comodo salvare su una file csv le liste CittaVisitate, così da poter fare statistiche
