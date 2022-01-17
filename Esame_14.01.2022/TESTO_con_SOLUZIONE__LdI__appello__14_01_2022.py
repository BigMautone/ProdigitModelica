def funzione_1(s):
    """

    Hidden Number.

    Questa funzione
    prende in input una stringa,
    in codice o non in codice,
    e deve restituire in output
    il numero codificato al suo interno.

    Tutte le stringhe codificate
    iniziano con la parola "allora",
    dove se i caratteri sono in maiuscolo o minuscolo
    NON HA ALCUNA IMPORTANZA.

    Il numero codificato all'interno di una stringa codificata
    e' sempre un intero positivo maggiore uguale a zero.

    Nelle stringhe codificate,
    le cifre decimali vengono codificate in accordo alle seguenti regole:
    La lettera "o" (maiuscola o minuscola) e' associata alla cifra decimale 0,
    La lettera "e" (maiuscola o minuscola) e' associata alla cifra decimale 1,
    La lettera "i" (maiuscola o minuscola) e' associata alla cifra decimale 2,
    La lettera "u" (maiuscola o minuscola) e' associata alla cifra decimale 3,
    La lettera "y" (maiuscola o minuscola) e' associata alla cifra decimale 4,
    La lettera "m" (maiuscola o minuscola) e' associata alla cifra decimale 5,
    La lettera "n" (maiuscola o minuscola) e' associata alla cifra decimale 6,
    La lettera "b" (maiuscola o minuscola) e' associata alla cifra decimale 7,
    La lettera "v" (maiuscola o minuscola) e' associata alla cifra decimale 8,
    La lettera "c" (maiuscola o minuscola) e' associata alla cifra decimale 9,

    L'ordine di apparizione delle cifre del numero codificato
    all'interno di una stringa codificata
    e' coerente con l'ordine che le cifre hanno
    nella rappresentazione numerica del numero stesso.

    Se in input viene fornita una stringa non codificata,
    la funzione deve restituire in output il valore intero 0.
    Se in input viene fornita una stringa codificata,
    la funzione deve restituire in output il valore intero
    codificato all'interno della stringa in input.

    ATTENZIONE: La funzione NON deve MAI restituire una stringa in output!

    Si consiglia l'uso della funzione python
    int()
    per convertire un valore numerico rappresentato come stringa
    in una variabile intera, esempio:
            variabile_intera = int("100")

    Esempi:
print(funzione_1("si', un po'."))  # --> 0
print(funzione_1("Allora, si', un po'."))  # --> 2360
print(funzione_1("1000 euro."))  # --> 0
print(funzione_1("Allora, 1000 euro."))  # --> 130
print(funzione_1("Si' o No?"))  # --> 0
print(funzione_1("ALLORA! Si' o No?"))  # --> 2060
print(funzione_1("poi ci penseremo."))  # --> 0
print(funzione_1("allora, poi ci pensero'."))  # --> 2921610
print(funzione_1("E' stato un caso."))  # --> 0
print(funzione_1("Allora... e' stato un caso."))  # --> 103690
print(funzione_1("CAVALLINO"))  # --> 0
print(funzione_1("Allora... CAVALLINO"))  # --> 98260
print(funzione_1("HxH?"))  # --> 0
print(funzione_1("Allora? HxH?"))  # --> 0

    """
    output = 0
    #
    prefisso_stringa_in_input = s[:6]
    prefisso_stringa_in_input = prefisso_stringa_in_input.lower()
    if prefisso_stringa_in_input == "allora":
        #
        numero_nascosto = ""
        #
        index = 0
        while index < len(s):
            carattere_corrente = s[index]
            carattere_corrente = carattere_corrente.lower()
            #
            if carattere_corrente == "o":
                numero_nascosto = numero_nascosto + "0"
            if carattere_corrente == "e":
                numero_nascosto = numero_nascosto + "1"
            if carattere_corrente == "i":
                numero_nascosto = numero_nascosto + "2"
            if carattere_corrente == "u":
                numero_nascosto = numero_nascosto + "3"
            if carattere_corrente == "y":
                numero_nascosto = numero_nascosto + "4"
            if carattere_corrente == "m":
                numero_nascosto = numero_nascosto + "5"
            if carattere_corrente == "n":
                numero_nascosto = numero_nascosto + "6"
            if carattere_corrente == "b":
                numero_nascosto = numero_nascosto + "7"
            if carattere_corrente == "v":
                numero_nascosto = numero_nascosto + "8"
            if carattere_corrente == "c":
                numero_nascosto = numero_nascosto + "9"
            #
            index = index + 1
        #
        output = int(numero_nascosto)
        #
    return output


def funzione_2(lista__studId_votoMate_votoFis_PiazzamentoMate_PiazzamentoFis):
    """

    Selezione Possibili Candidati Olimpiadi della Fisica.

    Questa funzione prende in input una lista di liste,
    dove ogni elemento e' una lista contenente informazioni
    scolastiche su un particolare studente,
    e deve restituire in output
    la lista ordinata degli identificativi di tutti gli studenti
    selezionati come possibili candidati
    alle selezioni regionali delle olimpiadi della fisica.

    Ogni elemento della lista di liste in input
    rappresenta uno studente ed ha il seguente formato:
    [id_studente, voto_matematica, voto_fisica, piazzamento_gara_di_istituto_Matematica, piazzamento_gara_di_istituto_Fisica].
    -) "id_studente" e' l'identificativo numerico univoco dello studente.
    -) "voto_matematica" e' il voto che lo studente ha in matematica: numero intero compreso tra 0 (incluso) e 10 (incluso).
    -) "voto_fisica" e' il voto che lo studente ha in fisica: numero intero compreso tra 0 (incluso) e 10 (incluso).
    -) "piazzamento_gara_di_istituto_Matematica" e' un numero intero maggiore uguale ad uno
       che rappresenta il piazzamento in graduatoria dello studente
       nella competizione in matematica interna all'istituto.
       Il valore 1 rappresenta la prima posizione,
       Il valore 2 rappresenta la seconda posizione,
       Il valore 3 rappresenta la terza posizione, etc.
    -) "piazzamento_gara_di_istituto_Fisica" e' un numero intero maggiore uguale ad uno
       che rappresenta il piazzamento in graduatoria dello studente
       nella competizione in fisica interna all'istituto.
       Il valore 1 rappresenta la prima posizione,
       Il valore 2 rappresenta la seconda posizione,
       Il valore 3 rappresenta la terza posizione, etc.

    Uno studente viene selezionato come possibile candidato
    alle selezioni regionali delle olimpiadi della fisica se, e solo se,
    ha sia in matematica che in fisica un voto maggiore uguale a 9
    oppure nella competizione in matematica interna all'istituto ha raggiunto ALMENO la terza posizione
    oppure nella competizione in fisica     interna all'istituto ha raggiunto ALMENO la quinta posizione.

    La lista in output deve contenere, IN ORDINE CRESCENTE, tutti e soli gli identificativi di tutti gli studenti
    selezionati come possibili candidati alle selezioni regionali delle olimpiadi della fisica.

    In caso di lista vuota in input, la funzione deve restituire in output una lista vuota.

    Esempi:
print(funzione_2([[1, 7, 7, 10, 5], [2, 8, 8, 4, 9]]))  # --> [1]
print(funzione_2([[4, 9, 9, 20, 15], [5, 8, 8, 4, 9]]))  # --> [4]
print(funzione_2([[4, 8, 7, 1, 15], [3, 7, 8, 6, 7], [2, 8, 8, 4, 2]]))  # --> [2, 4]
print(funzione_2([]))  # --> []
    """
    output = []
    #
    index = 0
    while index < len(
            lista__studId_votoMate_votoFis_PiazzamentoMate_PiazzamentoFis):
        #
        record_corrente = lista__studId_votoMate_votoFis_PiazzamentoMate_PiazzamentoFis[
            index]
        #
        id_studente = record_corrente[0]
        voto_matematica = int(record_corrente[1])
        voto_fisica = int(record_corrente[2])
        posizione_gara_matematica = int(record_corrente[3])
        posizione_gara_fisica = int(record_corrente[4])
        #
        voti_superiori_alla_soglia = (voto_matematica >= 9) and (voto_fisica >= 9)
        posizione_gara_matematica_superiore_soglia = posizione_gara_matematica <= 3
        posizione_gara_fisica_superiore_soglia = posizione_gara_fisica <= 5
        #
        if voti_superiori_alla_soglia or posizione_gara_matematica_superiore_soglia or posizione_gara_fisica_superiore_soglia:
            output.append(id_studente)
        #
        index = index + 1
    #
    output = sorted(output)
    #
    return output


def funzione_3(d_1, d_2):
    """

    Dizionario unione con valori non in comune.

    Questa funzione prende in input due dizionari d_1 e d_2,
    che hanno come chiavi numeri interi e come valori set di interi,
    e deve restituire in output un dizionario avente:
    .) come chiavi, le chiavi contenute in almeno uno dei due dizionari in input.
    .) come valori associati alle chiavi,
       un set contenente tutti gli elementi
       contenuti
       solo in uno
       dei set associati alla stessa chiave nei dizionari in input,
       ovviamente questo set puo' essere vuoto.

    Qualora una chiave fosse presente solo in uno dei dizionari in input,
    il dizionario in output deve riportare
    la stessa coppia chiave-valore presente in input.

    In presenza di dizionari vuoti in input, la funzione deve restituire in output un dizionario vuoto.

    Esempi:
print(funzione_3({1: set([1, 11, 111])}, {1: set([11, 111, 1111])})) # --> {1: {1, 1111}}
print(funzione_3({1: set([1, 11, 111])}, {1: set([11, 1, 111])})) # --> {1: set()}
print(funzione_3({1: set([1, 11, 111]), 2: set([3, 11])}, {1: set([11, 111, 1111])})) # --> {2: {3, 11}, 1: {1, 1111}}
print(funzione_3({3: set([33, 3, 333])}, {})) # --> {3: {33, 3, 333}}
print(funzione_3({}, {})) # --> {}
    """
    d_output = dict()
    #
    for k in d_1:
        if k not in d_2:
            d_output[k] = d_1[k]
    for k in d_2:
        if k not in d_1:
            d_output[k] = d_2[k]
    for k in d_1:
        if k in d_2:
            #
            set_v_1 = d_1[k]
            set_v_2 = d_2[k]
            set_union = set_v_1 | set_v_2
            set_int = set_v_1 & set_v_2
            #
            new_set_v = set()
            for element in set_union:
                if element not in set_int:
                    new_set_v.add(element)
            d_output[k] = new_set_v
    #
    return d_output


def funzione_4(list__team, list__task):
    """

    Selezione Squadre piu' Economiche. 

    Questa funzione prende in input
    due liste di dizionari: "list__team" e "list__task".

    Ogni elemento della lista "list__team"
    e' un dizionario rappresentante un team di lavoratori
    dove alla chiave
    .) "id" viene associato l'identificativo numerico intero univoco del team,
    .) "costo" (intero) viene associato il prezzo di assunzione del team,
    .) "skills" viene associato un set di valori interi,
        dove ogni intero rappresenta l'identificativo di una abilita' (skill)
        posseduta dal team.

    Ogni elemento della lista "list__task"
    e' un dizionario rappresentante un compito (task)
    che deve essere svolto da un team,
    dove alla chiave
    .) "id" viene associato l'identificativo numerico univoco del task (compito),
    .) "skills" viene associato un set di interi,
        dove ogni intero rappresenta l'identificativo di una abilita' (skill).
        Questo set
        rappresenta tutte le skill (abilita') richieste dal task (compito),
        queste sono tutte le skill (abilita')
        che devono essere possedute da un team per svolgere il task (compito).

    Un team e' in grado di svolgere un compito (task) se, e solo se,
    POSSIEDE TUTTE LE SKILL RICHIESTE dal task (compito).

    La funzione deve restituire in output
    il set contenente
    tutti gli identificativi
    di tutti i team
    che sono in grado di svolgere TUTTI i task in input
    con costo di assunzione piu' basso.

    In caso di lista di team in input vuota,
    la funzione deve restituire in output un set vuoto.

    In caso di lista di task in input vuota,
    la funzione deve restituire in output un set
    contenente tutti gli identificativi
    di tutti i team con costo di assunzione piu' basso.

    In caso di entrambe liste vuote in input,
    la funzione deve restituire in output un set vuoto.

    Esempi:
print(funzione_4([{'id': 1, 'costo': 10, 'skills': set([1, 2])}, {'id': 2, 'costo': 20, 'skills': set([1, 2, 3])}, {'id': 3, 'costo': 20, 'skills': set([1, 2, 3, 4])}], [{'id': 1, 'skills': set([1, 2, 3])}, {'id': 2, 'skills': set([3])}])) # --> {2, 3}
print(funzione_4([], [{'id': 1, 'skills': set([1, 2, 3])}]))  # --> set()
print(funzione_4([{'id': 4, 'costo': 20, 'skills': set([4, 2])}, {'id': 2, 'costo': 10, 'skills': set([3, 2])}], []))  # --> {2}
print(funzione_4([], []))  # --> set()
    """
    set_output = set()
    #
    set__team_che_coprono_tutti_i_task = set()
    costo_minimo = -1
    #
    index_team = 0
    while index_team < len(list__team):
        team_corrente = list__team[index_team]
        #
        team_corrente_set_skills = team_corrente["skills"]
        #
        numero_task_coperti_dal_team_corrente = 0
        index_tasks = 0
        while index_tasks < len(list__task):
            #
            task_corrente = list__task[index_tasks]
            #
            task_corrente_set_skills = task_corrente["skills"]
            #
            il_team_copre_tutto_il_task = len(task_corrente_set_skills & team_corrente_set_skills) == len(
                task_corrente_set_skills)
            #
            if il_team_copre_tutto_il_task:
                numero_task_coperti_dal_team_corrente = numero_task_coperti_dal_team_corrente + 1
            #
            index_tasks = index_tasks + 1
        #
        if numero_task_coperti_dal_team_corrente == len(list__task):
            #
            id_team_corrente = team_corrente["id"]
            set__team_che_coprono_tutti_i_task.add(id_team_corrente)
            #
            costo_team_corrente = team_corrente["costo"]
            if len(set__team_che_coprono_tutti_i_task) == 1 or costo_team_corrente < costo_minimo:
                costo_minimo = costo_team_corrente
        #
        index_team = index_team + 1
    #
    index_team = 0
    while index_team < len(list__team):
        team_corrente = list__team[index_team]
        #
        id_team_corrente = team_corrente["id"]
        if id_team_corrente in set__team_che_coprono_tutti_i_task:
            #
            costo_team_corrente = team_corrente["costo"]
            #
            if costo_team_corrente == costo_minimo:
                set_output.add(id_team_corrente)
            #
        index_team = index_team + 1
    #
    return set_output
