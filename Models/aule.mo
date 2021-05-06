block Aula
//aula agibile 8 volte su 10

	parameter Real T = 0.25; // := 30 min 
	
	
	NumberGenerator r(samplePeriod = T, globalSeed=124, localSeed=22301);
	Boolean aulaParziale;
	
	OutputBool statoAula;

algorithm
	
	when sample(0,T) then
		aulaParziale := false;
		
		if(r.r1024 <= 0.80) then
			statoAula := true;
			if(r.r1024 > 0.60 and r.r1024 <= 0.80) then //se 61%-80%, allora l'aula è parzialmente inagibile
				aulaParziale := true;
			end if;
			
		else //aula non agibile
			statoAula := false;
		end if;
		
		
	end when;

end Aula;
