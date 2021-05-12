block MonitorDown
	
	//Contatore di down di prodigit
	InputInt numProd;
	
	//Contatore di down del gomp
	InputInt numGomp;
	
	Boolean statoReq;
	
	OutputBool downReq;
	
initial equation
	statoReq = false;
	
//equation

algorithm
	when sample(299,1) then
		statoReq := numProd > ((numGomp*80)/100);
	end when;
	
	when edge(statoReq) then
		downReq := true;
	end when;
	
end MonitorDown;
