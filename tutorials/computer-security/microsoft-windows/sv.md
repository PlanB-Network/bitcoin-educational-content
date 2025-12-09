---
name: Windows 11
description: Automatisk installation av Microsoft Windows 11 via konfigurationsfil
---
![cover](assets/cover.webp)


I den här handledningen lär vi oss hur du installerar Windows 11 automatiskt med en annan metod än Windows standardinstallationsprocess.


## Ladda ner!


Det första du behöver är en installationsfil. Den säkraste och mest pålitliga platsen att ladda ner den är direkt från Microsofts officiella webbplats.


Besök bara länken nedan och följ instruktionerna för att ladda ner [Windows 11 ISO-fil] (https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


När du är på nedladdningssidan bläddrar du ner till avsnittet för nedladdning av ISO-filen.


![Image](assets/en/01.webp)


och välj rätt version.


![Image](assets/en/03.webp)


När du har valt Windows 11 klickar du på knappen Bekräfta.


I detta steg kan det ta några sekunder att behandla begäran, och sedan kommer du att se följande sida:


![Image](assets/en/04.webp)


Efter att du har bekräftat begäran måste du välja önskat språk.


![Image](assets/en/05.webp)


Efter att du har valt språk och klickat på knappen Bekräfta kommer begäran att behandlas. Detta steg kan ta några sekunder.


När begäran har behandlats kommer du att se en sida med nedladdningslänken för .iso-filen. Klicka på knappen 64-bitars nedladdning för att starta nedladdningen.


Filstorleken är ca 5,5 GB och den genererade länken är giltig i 24 timmar.


## Automation!


I det här skedet måste vi göra ändringar i standardinstallationen av Windows. I det här steget, med hjälp av Unattended install, bestämmer vi vilka objekt som ska installeras, utan användarens inmatning efteråt. I själva verket används i denna metod en XML-fil för att konfigurera installationsstegen och tjänsterna som installeras i Windows. Användningen av filen Unattended.xml skapar med andra ord en automatiseringsprocess under installationen, vilket gör att användaren inte behöver välja flera alternativ och slipper de tråkiga steg som vanligtvis krävs under installationen. Den här metoden är en ovanlig men standardiserad metod som har introducerats av Microsoft. Mer information finns på [Microsofts officiella webbplats] (https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Det finns olika verktyg tillgängliga på internet för att generera Unattended-filer. Vissa av dem är online, medan andra är offline. Ett av onlineverktygen för att skapa den här filen är [denna webbplats] (https://schneegans.de/windows/unattend-generator). Efter att ha öppnat den presenteras vi med följande sida:


![Image](assets/en/06.webp)


Som nämnts högst upp på sidan kan den här metoden användas för att installera Windows 10 och 11. I det första steget väljer vi Windows-språket. Om vi behöver lägga till ett andra eller till och med ett tredje språk i listan över Windows skärm- och tangentbordsspråk kan vi använda rutan nedan:


![Image](assets/en/07.webp)


I nästa steg väljer vi önskad plats.


![Image](assets/en/08.webp)


I det här steget kan vi också specificera processorarkitekturen för datorn. I det här steget kan vi:

1. Bestäm om du vill ignorera säkerhetsfunktioner i Windows, t.ex. TPM och Secure Boot. Secure Boot-funktionen säkerställer att om några av Windows kärnfiler manipuleras under startprocessen, upptäcks problemet och deras exekvering förhindras. Den här funktionen hjälper också till att skydda systemet från att installera skadliga uppdateringar i Windows. Att aktivera alternativet för att kringgå dessa funktioner är ibland oundvikligt på vissa datorer, särskilt äldre modeller. Det rekommenderas dock i allmänhet att hålla funktioner som Secure Boot aktiverade.

2. Ignorera kravet på en internetanslutning för att slutföra processen. Detta är användbart i situationer där en trådbunden LAN-anslutning inte är tillgänglig, eftersom det trådlösa kortet i de flesta fall ännu inte känns igen under Windows-installationen och internetåtkomst via kabel krävs. Om du aktiverar det här alternativet löses problem som är relaterade till det här steget.


I nästa steg kan vi välja ett namn på datorn.


![Image](assets/en/09.webp)


Vi kan också låta Windows välja ett namn på systemet. I det här steget kan du välja typ av Windows, komprimerad eller okomprimerad, eller låta Windows bestämma lämplig version utifrån datorns specifikationer. Tidszonen kan också ställas in i detta skede.


Nästa steg innebär partitionsinställningar:


![Image](assets/en/10.webp)


I det här skedet kan vi ange partitionstypen för installation av Windows, samt de inställningar som krävs för installation av Windows Recovery Environment. Om du väljer det första alternativet skjuts valet av partition och partitionering upp till Windows-installationen, och under installationen ställs dessa frågor precis som i den normala installationsmetoden.


I det här steget väljer vi vilken version av Windows som ska installeras:


![Image](assets/en/11.webp)


Om en produktnyckel finns tillgänglig kan den också anges i detta skede.


Nästa steg innebär att konfigurera Windows-inloggningskontot:


![Image](assets/en/12.webp)


## Kontonummer


I det här skedet:


1. Vi kan definiera ett namn och ett lösenord för administratörskontot. Det är också möjligt att skapa flera användar- eller administratörskonton.

2. Här anger vi vilket konto vi ska logga in på första gången efter installationen av Windows. De olika alternativen för detta avsnitt visas på bilden.

3. Om du inte vill att några konton ska skapas rensar du alla konton och väljer det här alternativet. I det här fallet kommer du efter installationen av Windows automatiskt att loggas in på Windows administratörskonto.


Nästa steg innebär att konfigurera lösenord och inställningar för värdfilen:


![Image](assets/en/13.webp)


I det här skedet avgör vi om lösenorden ska ha en utgångsperiod. Dessutom innehåller detta avsnitt säkerhetsinställningar relaterade till misslyckade inloggningsförsök, som kan aktiveras eller inaktiveras utifrån dina behov.


Längst ned i detta avsnitt finns inställningar för filvisning. Inget av dessa alternativ är tillgängliga under en vanlig Windows-installation utan måste konfigureras efter installationen. Med installationsmetoden Unattended är dessa inställningar däremot lättillgängliga.


Nästa steg innebär att du konfigurerar Windows säkerhetsinställningar:


![Image](assets/en/14.webp)


## Säkerhetsinställningar


I det här skedet:


1. Windows Defender kan aktiveras eller inaktiveras. Den här funktionen fungerar som säkerhetsprogram i Windows och hjälper till att förhindra att skadliga filer körs, vissa nätverksattacker med mera.

2. Automatiska Windows-uppdateringar kan avaktiveras. Detta är en av de vanligaste utmaningarna som Windows-användare står inför!

3. I det här avsnittet kan du aktivera eller inaktivera UAC (User Account Control). Den här funktionen förhindrar att misstänkta program körs med förhöjda läs- och skrivbehörigheter.

4. Denna funktion används av Windows för att upptäcka potentiellt skadlig programvara.

5. Aktivera eller inaktivera stöd för långa sökvägar i Windows-program, t.ex. PowerShell och andra.

6. Aktivera eller inaktivera Fjärrskrivbord för fjärråtkomst till systemet.


Beroende på vilken Windows-version som används kan det hända att vissa av dessa funktioner inte stöds.


Nästa steg är att konfigurera ikonerna:


![Image](assets/en/15.webp)


I detta avsnitt:


1. Skrivbordsikoner listas, som kan läggas till eller tas bort efter behov.

2. Startmenyikonerna är listade, och de kan också läggas till eller tas bort beroende på behov.

3. I det här avsnittet kan du konfigurera om virtualiseringsrelaterade verktyg ska installeras eller inte. Det här alternativet är specifikt för Windows 11 och gäller inte för Windows 10.


Nästa steg innebär att konfigurera Wi-Fi-inställningar:


![Image](assets/en/16.webp)


I det här avsnittet kan du konfigurera inställningar för Wi-Fi-nätverk. Som tidigare nämnts känns Wi-Fi-kortet i de flesta fall inte igen under Windows-installationen, så det är vanligtvis inte möjligt att ansluta under installationen. Men genom att konfigurera det här avsnittet kan systemet ansluta till Internet om det trådlösa kortet upptäcks.


Nästa steg innebär en viktig inställning:


![Image](assets/en/17.webp)


I det här avsnittet anger vi om information om systemproblem ska skickas till Microsoft eller inte.


Nästa steg är att konfigurera standardapplikationer:


![Image](assets/en/18.webp)


## Standardprogramvara aktiverar/avaktiverar


I det här avsnittet kan vi välja alla program som vi inte vill ska installeras som standard. Vi kan till exempel välja att inte installera Cortana eller Copilot.


Nästa steg omfattar säkerhetsinställningar som rör programkörning:


![Image](assets/en/19.webp)


Genom att tillämpa WDAC-inställningar kan utförandet av vissa applikationer förhindras.


Slutligen, efter att ha tillämpat önskade inställningar, kan den genererade XML-filen laddas ner:


![Image](assets/en/20.webp)


Genom att klicka på Download XML File hämtas filen autounattend.xml. För att använda den här filen monterar du helt enkelt den nedladdade ISO-enheten på en USB-enhet, placerar filen autounattend.xml i rotkatalogen och fortsätter sedan med Windows-installationen.


Ett av de verktyg som finns tillgängliga för att skapa en startbar USB-enhet är Rufus. Rufus kan skapa en startbar Windows-installation flash-enhet, med en given Windows-installation ISO-fil. Det är snabbt och enkelt, du kan ladda ner det [här](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


I den här programvaran klickar vi på Start efter att ha valt önskad USB-enhet och lämplig ISO-fil.


![Image](assets/en/22.webp)


I det här skedet inaktiverar vi alla alternativ, eftersom aktivering av dem kan orsaka konflikter när den genererade Unattend-filen används. När filerna har kopierats till USB-enheten placerar vi filen autounattend.xml i rotkatalogen:


![Image](assets/en/23.webp)


Nu är USB-enheten redo att användas för att installera Windows automatiskt och installationen kan startas med hjälp av USB-enheten.


## ISO-redigering


Om du behöver installera Windows på en virtuell maskin kan du använda programvara för att skapa och redigera ISO-filer. En sådan programvara är AnyBurn. När du har extraherat innehållet i ISO-filen som hämtats från Microsofts webbplats placerar du filen autounattend.xml i rotkatalogen. Använd sedan AnyBurn för att skapa en ny ISO-fil med det uppdaterade innehållet.


AnyBurn är en multifunktionell programvara för att arbeta med ISO-filer. Det erbjuder olika funktioner för hantering av ISO-filer, varav en är att skapa startbara ISO-bilder; [här](https://www.anyburn.com/download.php) är den ursprungliga webbplatsen.


På programvarans huvudsida väljer du "Skapa bild från fil / mapp":


![Image](assets/en/24.webp)


På nästa sida väljer du alla filer som extraherats från ISO tillsammans med filen autounattend.xml.


![Image](assets/en/25.webp)


I det här steget konfigurerar vi inställningarna för att göra ISO-filen startbar:


![Image](assets/en/26.webp)


I detta skede måste sökvägen till filen bootfix.bin anges för att göra ISO:n startbar. Den här filen ligger i roten av ISO, i startmappen. Det rekommenderas också att aktivera både ISO9660- och UDF-alternativen i avsnittet Egenskaper.


![Image](assets/en/27.webp)


Efter detta steg skapar du ISO-filen genom att klicka på Nästa. Den här filen kan användas i virtualiseringsprogram som Oracle VirtualBox. Nedan hittar du en handledning om VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65