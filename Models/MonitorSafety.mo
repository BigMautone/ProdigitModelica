block MonitorSafety

	//Prenotazioni effettuate 
	InputInt prenotazioni;
	
	//Posti aula totali
	InputInt postiAula;
	
	//stato del req. funz. safety
	Boolean statoSafety;
	
	//Se c'è overbooking diventa true
	OutputBool safety;
	
	
	
initial equation
	safety = false;
	
equation
	statoSafety = not(prenotazioni <= postiAula);

	
algorithm
	when edge(statoSafety) then
		safety := true;
	end when;
	
		
	

end MonitorSafety;
