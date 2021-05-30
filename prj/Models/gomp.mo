block Gomp

	parameter Real T = 1; 
	
	//Probabilità che il gomp sia down
	parameter Real probDown = 0.1;
	
	NumberGenerator r_down(samplePeriod=T, globalSeed = 745, localSeed = 45221);
	
	Integer postiAula;
	
	InputBool aulaAgibile_in; //"Stato dell'aula, fornito da aula.mo"
	
	OutputBool aulaAgibile_out; //Stato dell'aula
	OutputInt postiAula_out; //Posti aula calcolati dal gomp
	
	OutputBool gompDown_out;
	
	OutputInt gompDown_cont;

algorithm
	when initial() then
		postiAula := 60;
		postiAula_out := postiAula;
		gompDown_cont := 0;
		gompDown_out := false;
	end when;
	
	when sample(0,T) then
		
		postiAula_out := postiAula;
		aulaAgibile_out := aulaAgibile_in;

		gompDown_out := r_down.r1024 <= probDown;
		
		if(gompDown_out) then
			gompDown_cont := pre(gompDown_cont) + 1; 
		end if;
	
		
	end when;
	

end Gomp;

