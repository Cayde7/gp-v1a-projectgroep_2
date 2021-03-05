# gp-v1a-projectgroep_2

##Opdracht 2 databases

###pseudocode
Algemeen
```bash
Als de data in mongoDB de waarde's heeft die we nodig hebben worden ze gesplitst.
Vanuit de splitsing stoppen we de data in de database.
```
Profiles: 
```bash
Wanneer de profielen worden in geladen wordt er gekeken naar de bu_id of daar een waarde bij zit zodra er een waarde is gevonden wordt er uit de dictionairy de volgende gegevens gehaald: de ID, de BU_ID, uit recommendations worden  alleen de segment en recently_viewed gehaald zodat de onnodige informatie achterwegen blijven en de previously recomended. Mocht er geen BU_ID met waardes zijn wordt er een error weergegeven.
```
Sessions: 
```bash
Wanneer de sessions worden in geladen wordt er gekeken naar de bu_id of daar een waarde bij zit zodra er een waarde is gevonden wordt er uit de dictionairy de volgende gegevens gehaald: de BU_ID, de segment en de preferences. Mocht er geen BU_ID met waardes zijn wordt er een error weergegeven.
```
Products:
```bash
Wanneer de products worden in geladen wordt er gekeken naar de product_name of daar een waarde bij zit zodra er een waarde is gevonden wordt er uit de dictionairy de volgende gegevens gehaald: de ID, de brand, de category, de sub_category, de sub_sub_category, de sub_sub_sub_category, de gender, de fast_mover en de herhaalaankopen. Mocht er geen ID met waardes zijn wordt er een error weergegeven.
```