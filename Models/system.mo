block System

Aula aula;
Studente stud;
Gomp gomp;
Prodigit prodigit;
MonitorSafety saf;
MonitorLiveness live;
MonitorDown down;

equation

//Connect del gomp
connect(gomp.aulaAgibile_in, aula.statoAula);
connect(gomp.aulaParziale, aula.aulaParziale);

//Connect di prodigit
connect(prodigit.postiAula_in, gomp.postiAula_out);

connect(prodigit.aulaAgibile, gomp.aulaAgibile_out);

connect(prodigit.studenteAbilitato, stud.canUse);

connect(prodigit.opStudente, stud.prenOrCanc);

connect(prodigit.gompDown, gomp.gompDown_out);

//Connect monitor safety
connect(saf.prenotazioni, prodigit.studPren);

connect(saf.postiAula, gomp.postiAula_out);

//Connect del monitor di liveness. Prende in input tutti i dati(o quasi) da prodigit.
connect(live.opStud, prodigit.opStud_out);

connect(live.prenotazioni, prodigit.studPren);

connect(live.postiAula, gomp.postiAula_out);

connect(live.aulaAgibile, prodigit.statoAula_out);

connect(live.studAbilitato, prodigit.studAbilitato_out);

connect(live.prodDown_in, prodigit.prodDown_out);

//Connect del monitor per il requisito non funzionale di Down
connect(down.numProd, prodigit.prodDown_cont);

connect(down.numGomp, gomp.gompDown_cont);


end System;
