block Studente
	
	parameter Real T = 0.5; //Tempo di refresh stato matricola studente := 30 minuti
	
	parameter Real probPren = 0.3;
	
	NumberGenerator r_matricola(samplePeriod = T, globalSeed=300, localSeed=12003);
	NumberGenerator r_P_or_C(samplePeriod = T, globalSeed=250, localSeed=14211);
	
	OutputBool canUse; //true se matricola giusta, false altrimenti
	OutputBool prenOrCanc; //Se true allora vuole prenotare, altrimenti vuole cancellare

algorithm
	when sample(0,T) then 
		if(r_matricola.r1024 >= 0.50) then
			canUse := true;
		else
			canUse := false;
		end if;
		
		if(r_P_or_C.r1024 < probPren) then //Se maggiore uguale di 0.3 prenota, altrimenti cancella
			prenOrCanc := false;
		else
			prenOrCanc := true;
		end if;
	end when;
	
end Studente;
