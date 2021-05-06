class MonitorFun

	InputInt prenotazioni;
	InputInt postiAula;
	
	Boolean statoFun;
	
	//Se requisiti funzionali violati, allora diventa true
	OutputBool vincolo;
	
initial equation
	vincolo = false;
	
equation
	statoFun = (prenotazioni > postiAula) and (prenotazioni < postiAula);
	
algorithm
	when edge(statoFun) then
		vincolo := true;
	end when;
	
		
	

end MonitorFun;
