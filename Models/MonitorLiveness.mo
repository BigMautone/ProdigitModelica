block MonitorLiveness
	
	parameter Real T = 0.75; //Tempo di aggiornamento del monitor. Leggermente maggiore di quello di prodigit
	
	//Posti totali aula
	InputInt postiAula;
	
	//Numero prenotazioni salvate da prodigit
	InputInt prenotazioni;
		
	//Operazione svolta dallo studente (true = prenota, false = cancella)
	InputBool opStud;
	
	//True se l'aula è agibile
	InputBool aulaAgibile;
	
	//Booleano che identifica se lo studente può o non può usare prodigit
	InputBool studAbilitato;
	
	//Contatore prenotazioni. Va di pari passo con le prenotazioni del gomp e serve per controllare se il req. è rispettato
	Integer contPren;
	
	//Stato momentaneo liveness
	Boolean statoLive;
	
	//Stato monitor finale
	OutputBool liveness;
	
initial equation
	liveness = false;
	contPren = 0;
	
	

algorithm
	
	when sample(0,T) then
		
		//Controllo se i requisiti per effettuare la prenotazione siano validi
		if(aulaAgibile and studAbilitato) then
		
			if(opStud) then //Lo studente prenota
			
				if(not(postiAula == prenotazioni)) then
					contPren := pre(contPren) + 1;
				else
					contPren := prenotazioni;
				end if;
				
				statoLive := not(contPren == prenotazioni); //Se il numero di prenotazioni di prodigit corrispone con quello del monitor il req. è rispettato, no altrimenti
			else //lo studente cancella la prenotazione
				contPren := prenotazioni;
				statoLive := false;
			end if;
		else 
			contPren := prenotazioni;
			statoLive := false;
		end if;
	end when;
	
	when edge(statoLive) then
		liveness := true;
	end when;


end MonitorLiveness;
