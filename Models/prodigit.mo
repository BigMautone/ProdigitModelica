block Prodigit

	parameter Real T = 0.75; // Tempo di aggiornamento di prodigit := 45 minuti
	
	NumberGenerator r_down(samplePeriod=T, globalSeed=450, localSeed=52200);
	
	Integer maxPosti; //numero massimo posti dell'aula selezionata
	Integer prenotati; //studenti prenotati
	Boolean prodDown;

	//Campi info gomp
	InputBool gompDown;

	//Campi info aula
	
	InputBool aulaAgibile;
	InputInt postiAula_in;
	
	//Campi info studente
	
	InputBool studenteAbilitato; //Boolean che definisce se lo studente può o non può usare prodigit
	InputBool opStudente; //Se true prenota, altrimenti cancella
	
	//Campi output
	
	//Numero studenti prenotati
	OutputInt studPren; 
	
	//Stato matricola dello studente
	OutputBool studAbilitato_out;
	
	//Stato aula ottenuto da prodigit
	OutputBool statoAula_out;
	
	//Operazione scelta dallo studente memorizzata in prodigit
	OutputBool opStud_out;
	
algorithm
	when initial() then
		prenotati := 0;
		maxPosti := postiAula_in;
		studPren := prenotati;
	end when;
	
	when sample(0,T) then
		if(gompDown) then
			prodDown := r_down.r1024 <= 0.8;
			
		else
		
			if(aulaAgibile and studenteAbilitato) then
				if(opStudente) then
					if(prenotati < maxPosti and prenotati >= 0) then
						prenotati := pre(prenotati) +1;
					end if;
				else 
					if(prenotati > 0 and prenotati <= maxPosti) then
						prenotati := pre(prenotati) - 1;
					end if;
				end if;
			end if;
		end if;
		
		studPren := prenotati;
		statoAula_out := aulaAgibile;
		studAbilitato_out := studenteAbilitato;
		opStud_out := opStudente;
		
	end when;


	
end Prodigit;


//Operazione di prenotazione da parte di uno studente  
function Prenota

	InputInt p_in;
	
	OutputInt p_out;
	
algorithm
	p_out := p_in - 1;
	
end Prenota;


//Funzione di cancellazione di una prenotazione da parte di uno studente
function CancellaPrenotazione
	
	InputInt p_in;

	OutputInt p_out;

algorithm
	p_out := p_in + 1;
	
end CancellaPrenotazione;




