block Gomp

	parameter Real T = 0.8 "equivale ad 1 ora" ; 
	
	Integer postiAula;
	
	InputBool aulaAgibile_in; //"Stato dell'aula, fornito da aula.mo"
	
	OutputBool aulaAgibile_out; //"Stato dell'aula"
	OutputInt postiAula_out; //"Posti aula calcolati dal gomp"

algorithm
	when initial() then
		postiAula := 60;
		postiAula_out := postiAula;
	end when;
	
	when sample(0,T) then
		
		postiAula_out := postiAula;
		aulaAgibile_out := aulaAgibile_in;
	
	end when;
	

end Gomp;
