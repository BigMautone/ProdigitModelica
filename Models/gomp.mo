block Gomp

	parameter Real T = 0.8; 
	
	NumberGenerator r_down(samplePeriod=T, globalSeed = 745, localSeed = 45221);
	
	Integer postiAula;
	Real probDown = 0.1;
	
	//Boolean gompDown;
	
	InputBool aulaAgibile_in; //"Stato dell'aula, fornito da aula.mo"
	InputBool aulaParziale;
	
	OutputBool aulaAgibile_out; //"Stato dell'aula"
	OutputInt postiAula_out; //"Posti aula calcolati dal gomp"
	
	OutputBool gompDown_out;
	
	OutputInt gompDown_cont;

algorithm
	when initial() then
		
		postiAula := AssegnaPosti(aulaParziale);
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
	
		//gompDown_out := gompDown;
		
	end when;
	

end Gomp;

function AssegnaPosti

	InputBool aulaPar;
	
	OutputInt posti;

algorithm	
	if(aulaPar) then
		posti := 30;
	else
		posti := 60;
	end if;

end AssegnaPosti;
