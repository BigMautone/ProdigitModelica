model NumberGenerator

	parameter Real samplePeriod = 1.0;
	parameter Integer globalSeed = 30020;
	parameter Integer localSeed = 614657;
	
	OutputReal r1024; //Numero random generato con Xorshift1024star
	
protected 
	discrete Integer state1024[Modelica.Math.Random.Generators.Xorshift1024star.nState];

algorithm
	when initial() then
		//Genera lo stato iniziale dal local e il global seed
		
		state1024 := Modelica.Math.Random.Generators.Xorshift1024star.initialState(localSeed, globalSeed);
		r1024 := 0;
		
	elsewhen sample(0, samplePeriod) then
		(r1024,state1024) := Modelica.Math.Random.Generators.Xorshift1024star.random(pre(state1024));
	end when;

end NumberGenerator;
