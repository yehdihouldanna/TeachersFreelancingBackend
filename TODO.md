+ Teacher :
- *Register [x] rectify the subject*
- *Login [x]*
- *Profil, details de compte,*  ,*(chargement de documents)*
- *Librairie*  
- Chargement de compte [x]
- Historique (des demandes affectées à ce prof)

+ Student : 
- *Register*
- *Login*
- *Liste des profs*
- *Listes des livres demandables*
- *Liste des documents (publiques)*
- Listes des formations ouvertes par les écoles
- Demande de document
- Demande de Lesson
- Historique des demandes de documents
- Historique des demandes de Lessons

+ Admin :
- *Creation des écoles*
- *Validation des comptes des profs*
- Validation des transactions 
- Création d'une transaction de créditation
- *Création des formations*
- *Validation des demandes de documents*

+ Ecole : 
- 

+ Fixes
+ Création class pour sujet
+ Changement de teacher subject to foreign key
+ Atomisation de la création des differentes objects
+ Rating on the demand anytime (as a patch the demande CRUD view) :: add rating attribute to the damande
+ Add prof rating based on the average of the ratings of the demnads that relate him.
+ Automatisation de transactions
+ Return only profs with solds > 500 in the list_profs view
+ Création d'un model pour classe
+ Création d'un model pour spécialité




+ Student's -- Demande --admin(validation) -- Admin(contact the prof) -- and answer the student.
+ Add status attribute to demande,
+ In student demand view (add two options one open and one exlusive)
    The open option should be something along the lines:
    لتبية طلبكم من المستحسن وضع اختيار مفتوح.
    ننصح المتخدم بوضع طلب مفتوح لزيادة فرصة تلبية الطلب

+ Rating profs based on the rating of the demands, (the student can rate the professor after the first the damande reachs pahse 2)

+ DEMANDE STATUS : {phase 1 : pending , phase 2 : processed}
    the phase 1 is marked by the student posting the demand on the platform
    the phase 2 is marked by the admin contacting the professor and validating the demand with him,
    -- and then reconnecting the student with the professor.

+ limit disponibility to week days,
+ APIs historiques : Api listes des lessons demandé, Api listes des documents demandés
+ APIs Listes des documents publiques




Create a script to automate the intialisation of the database values :
days , subjects, specialties, base accounts for testing, platform, wallets ...


+----------------------------+ 
+ Create user paltforme
+ Create subjects
+ Create classes
+----------------------------+
+ Test user_student_creation
+ Test user_teacher_creation
+ Test user_login
+ Test Demande_de_lesson
+ Test demande de document
+ Test List des profs
+ Test List des documents
+ Test List des livres
+ Test School Creation
+ Test Document Creation
+ Test Chargement de compte
+ Test affectation de demande et la transaction impliqué


