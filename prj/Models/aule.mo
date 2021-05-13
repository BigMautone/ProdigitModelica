block Aula
//aula agibile 8 volte su 10

	parameter Real T = 0.5; // := 30 min 
	
	NumberGenerator r(samplePeriod = T, globalSeed=124, localSeed=22301);

	OutputBool statoAula;
	
algorithm
	
	when sample(0,T) then
		statoAula := r.r1024 <= 0.80;		
	end when;

end Aula;
