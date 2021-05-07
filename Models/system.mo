block System

Aula aula;
Studente stud;
Gomp gomp;
Prodigit prodigit;
MonitorSafety saf;
MonitorLiveness live;

equation

//Connect del gomp
connect(gomp.aulaAgibile_in, aula.statoAula);

//Connect di prodigit
connect(prodigit.postiAula_in, gomp.postiAula_out);

connect(prodigit.aulaAgibile, gomp.aulaAgibile_out);

connect(prodigit.studenteAbilitato, stud.canUse);

connect(prodigit.opStudente, stud.prenOrCanc);

//Connect monitor safety
connect(saf.prenotazioni, prodigit.studPren);

connect(saf.postiAula, gomp.postiAula_out);

//Connect del monitor di liveness. Prende in input tutti i dati(o quasi) da prodigit.
connect(live.opStud, prodigit.opStud_out);

connect(live.prenotazioni, prodigit.studPren);

connect(live.postiAula, gomp.postiAula_out);

connect(live.aulaAgibile, prodigit.statoAula_out);

connect(live.studAbilitato, prodigit.studAbilitato_out);

end System;
