---
term: BGP-kapning
definition: Attack som manipulerar internetdirigering för att omdirigera trafik till ett skadligt nätverk, vilket kan användas för att isolera Bitcoin-noder.
---

Attack där en illasinnad aktör manipulerar BGP-annonser för att omdirigera internettrafik till sitt eget nätverk. Genom att låtsas vara det legitima ursprunget för vissa IP Address-områden kan angriparen fånga upp, övervaka eller blockera trafik som är avsedd för dessa adresser.


BGP (*Border Gateway Protocol*) är det protokoll som avgör hur trafiken dirigeras mellan de olika autonoma nätverken (AS) som utgör det globala Internet. Det avgör vilka vägar data tar för att komma från en punkt till en annan.


När det gäller Bitcoin kan BGP Hijacking användas för att omdirigera trafik mellan noder i Bitcoin-nätverket för att isolera vissa av dem. Denna attack kan också utföras på Stratum-servrar som används av Mining-pooler, för att omdirigera datorkraften hos choppers till den egna poolen. Eftersom choppers inte startar om sina maskiner särskilt ofta kan denna omdirigering kvarstå under lång tid. Den här attacken kanske inte bara syftar till direkt ekonomisk vinning genom att tillskansa sig blockbelöningar, utan också till att tillfälligt få mer makt över systemet.