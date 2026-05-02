###### Partition



 	Vlastnosť		| MBR (Master Boot Record) | GPT (GUID Partition Table)

 	------------------------|--------------------------|------------------------------

 	Status			| Legacy (stare)	   | Moderny štandard

 	limit kapacity		| max 2TB		   | Nad 2TB

 	boot rezim		| legacy BIOS		   | UEFI boot

 	pocet particii		| max 4			   | prakticky neobmedzené



###### Súborové systémy

 

 	NTFS:	štandard pre windows, podpora ACL, kompresii a kvót

 	FAT32:	limit 4GB na subor, pouz na kompatibilitu

 	exFAT: 	odporúčané pre externé médiá a kompatibilitu s linuxom

 	ReFS: 	(resilient file system), vysoko odolný voči korupcii dát, podpora veľkých zvázkov, vie sa opraviť



######  

###### 

###### DAS (Direct attach storage)

 	**definícia:**  	block level storage, disky pripojene priamo k PC

 	**Výhody:**		najnižšia cena, jednoduchá konfigurácia a inštalácia, rýchlosť je vyžšia, dedikovanosť

 	**Nevýhody:**	obmedzená škálovateľnosť a kapacita, prenos, rozšírenie kúpou nového disku



###### NAS (Network attached storage)

 	**definícia:** 	file level storage, pripojený cez ethernet, určené pre viac uživateľov na prístup k dátam

 	**Výhody:** 	data sú chránené (ak je raid), jednoduchá konfigurácia, kapacita, rozšíriteľnosť, podpora backup,

 			široké možnosti použitia

 	**Nevýhody:**	cena, rýchlosť, dosah

 

###### SAN (storage array network)

 	**definícia:**	block level storage, vyžadujúci dedikovanú sieť.

 	**Výhody:**		rýchlosť (od 10GB), šírka pásma, nižšia latencia

 	**Nevýhody:**	cena, komplikovanosť inštalácie, krehkosť, citlivosť, dosah





##### storage spaces

 	**definícia:** 	táto technológia umožňuje virtualizovať úložisko bez nutnosti drahého HW, **je predinstalovaná**

 	**manažment:**	pomocou server manager

 	**prerekvizitá:**	disky su online, unallcated a min 4GB

 	**vlastnosti:** 	tier aware (automaticky presun hot a cold dát na ssd alebo hdd)

 			QoS - quality of service (možnosti nastaviť priority pre rôzne typy prevádzky)



  storage layouts:

 	**Simple:**		žiadna ochrana dát, najväčšia rýchlosť, min 1 disk

 	**Mirror:**		**2-way (min 2 disky)
3-way (min 5 diskov)**

 	**Parity:**		eqivalent RAID 5
**min 3. disky (ochrana 1ho disku)
ochranu 2 diskov min 7 diskov**





##### Služby file server

######  DFS (distributed file system):

 

######    DFSN:

 	**definícia:**	spravy namespace, zjednoti servre/shary pod 1 namespace
userom tak treba vediet len ten jeden namespace

 	**obmedzenia:**	nie je mozne dat do failover clustra

 			musi mat NTFS volume

 			min win server 2012

 			**can share only SMB shared folders**

 	**elementy:**	namespace server

 			namespace root

 			folder

 			folder targets

######    DFSR:

 	**definícia:**	roby duplikaciu medzi sharmi, ak pridame novy server vieme ho SYNC

 			moze replicovat sharovat akykolvek subor

 	**problem:** 	pri presune nevieme ci veci ostanu sharovane a menia sa prava





######  FSRM (File Server Resource Manager):



 	**umožňuje:** 	quota management - limity kapacity

 			file screening - kontrola suborov a moznos blokovania (napr mp4, .exe)

 			obsahuje detailné reporty o user správaní



######  iSCSI Target Server



 	**definícia:**	poskytuje blokový priestor iným serverom cez sieť ()

 			ak mame cluster mame shared storage box, to je ale drahe, tak dame

 			novy server a ten sa bude tvarit ako storage box



 

 	**požiadavky:**	vyžaduje target a initiator-a (poskytovatela a klienta), **port 3260 TCP**

 	**bezpečnosť:**	podpora CHAP a reverse CHAP

 	bottleneck:	speed disku

 			sieť (nekonecno lunov ale nie nekonecno miesta v sieti)

 			veľkosť storage

&nbsp;	typy iSCSI diskov:	fixed	- alokuje cely definovany priestor okamzite, 
 					- nedovoluje thin provisioning

&nbsp;				dynamically expanding	- zabera iba realne zapisane data

&nbsp;							- podporuje thin provisioning

&nbsp;				differencing	- parent disk (funguje ako read only template)
 						- klient - kazdy ma vlastny child disky 
						- klienti citaju z parent disku ale zapisuju na child disk



######  iné:

   **data deduplication:**	nahrádza duplikáty s linkami

   **work folder:**		provides sync-on-shutdown, po vrateni sa online zmeni sa opatovne syncnu

   **BranchCache:**		prvy download je z centraly, ostatne su z lokalneho cache

   **VSS agent service:**	ujistuje konzistenciu dát pomocou flush cache na disk pred zálohou

   **Server for NFS:**	kompatibilita zdielania medzi windows a linux





##### Storage spaces direct (S2D):



 	definícia:	architektúra pre failover clustre, kt vytvara zdieľaný cross-node datastore z

 			lokalných diskov z nodov v clusteri



 	Výkon:		sa meria v IOPS (input/output operations per second)
EIDE/SATA slowest

 			SCSI 150 IOPS
SAS 210 IOPS

 			SSD 1,5 mil IOPS





Thin Provisioning → logicky pridelíš viac miesta, než fyzicky máš

Over Provisioning → celkový súčet pridelených LUN je väčší než reálny storage



