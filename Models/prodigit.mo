block Prodigit

	parameter Real T = 0.75; // Tempo di aggiornamento di prodigit := 45 minuti
	
	NumberGenerator r_down(samplePeriod=T, globalSeed=450, localSeed=52200);
	
	//numero massimo posti dell'aula selezionata
	Integer maxPosti; 
	
	//studenti prenotati
	Integer prenotati;
	
	Boolean prodDown;

	//Campi info gomp
	InputBool gompDown;

	//Campi info aula
	
	InputBool aulaAgibile;
	InputInt postiAula_in;
	
	//Campi info studente
	
	//Boolean che definisce se lo studente può o non può usare prodigit
	InputBool studenteAbilitato;
	
	//Se true prenota, altrimenti cancella 
	InputBool opStudente; 
	
	//Campi output
	
	//Numero studenti prenotati
	OutputInt studPren; 
	
	//Stato matricola dello studente
	OutputBool studAbilitato_out;
	
	//Stato aula ottenuto da prodigit
	OutputBool statoAula_out;
	
	//Operazione scelta dallo studente memorizzata in prodigit
	OutputBool opStud_out;
	
	//Contatore down prodigit
	OutputInt prodDown_cont;
	
	//Se prodigit è down restituisce true, false altrimenti
	OutputBool prodDown_out;
	
algorithm
	when initial() then
		prenotati := 0;
		maxPosti := postiAula_in;
		studPren := prenotati;
		prodDown_cont := 0;
	end when;
	
	when sample(0,T) then
		prodDown := false;
		
		//Se il gomp è down, allora prodigit lo sarà al 20%
		if(gompDown) then
			prodDown := r_down.r1024 <= 0.2;
		end if;
		
		if(not prodDown) then		
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
		else 
			prodDown_cont := pre(prodDown_cont) + 1; //Incremento di 1 il contatore delle volte che prodigit è down
		end if;
		
		studPren := prenotati;
		statoAula_out := aulaAgibile;
		studAbilitato_out := studenteAbilitato;
		opStud_out := opStudente;
		prodDown_out := prodDown;
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




