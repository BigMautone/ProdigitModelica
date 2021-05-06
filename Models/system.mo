block System

Aula aula;
Studente stud;
Gomp gomp;
Prodigit prodigit;
MonitorFun funz;

equation

connect(gomp.aulaAgibile_in, aula.statoAula);

connect(prodigit.postiAula_in, gomp.postiAula_out);

connect(prodigit.aulaAgibile, gomp.aulaAgibile_out);

connect(prodigit.studenteAbilitato, stud.canUse);

connect(prodigit.opStudente, stud.prenOrCanc);

connect(funz.prenotazioni, prodigit.studPren);

connect(funz.postiAula, gomp.postiAula_out);

end System;
