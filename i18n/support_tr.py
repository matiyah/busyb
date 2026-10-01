# -*- coding: utf-8 -*-
# Strings of support.html, in order. EN must match the English page exactly;
# every language list below has the same length and order. Run i18n/build.py.
EN = [
# 0 <title>
"Busy B: Support",
# 1 h1
"Support",
# 2 subtitle under h1
"Busy B (listed on the App Store as \"Busy B Planner\")",
# 3
"Need help with Busy B? We usually reply within a day or two.",
# 4 mail button
"Email support@busybplanner.com",
# 5
"How do I sync between my iPhone and iPad?",
# 6
"Busy B syncs automatically through iCloud. Make sure you're signed into the\nsame iCloud account on both devices, with iCloud Drive enabled in\n<strong>Settings &gt; [your name] &gt; iCloud</strong>.",
# 7
"How do I restore a purchase on a new device?",
# 8
"Open Busy B, go to <strong>Settings</strong>, and tap\n<strong>Restore purchases</strong>. Make sure you're signed into the same\nApple ID you used for the original purchase.",
# 9
"How do I cancel or manage my subscription?",
# 10
"Go to <strong>Settings &gt; [your name] &gt; Subscriptions</strong> on your\ndevice, or tap <strong>Manage subscription</strong> inside Busy B's Settings\nscreen.",
# 11
"Do the AI features send my tasks anywhere?",
# 12
"No. The daily briefing, one-tap filing, and Catch-up all run entirely on\nyour device using\n<a href=\"https://www.apple.com/apple-intelligence/\" target=\"_blank\" rel=\"noopener\">Apple Intelligence</a>.\nYour task titles, categories, and due dates are never sent to us or to any\nexternal server for AI analysis, and nothing you put in Busy B is ever used\nto train an AI model. If a device can't run Apple Intelligence, these\nfeatures simply don't appear and the rest of the app works exactly as\nbefore.",
# 13
"Something's not working. What do I do?",
# 14
"Email us at\n<a href=\"mailto:support@busybplanner.com\">support@busybplanner.com</a> with a\ndescription of the issue and, if possible, your device model and iOS\nversion. Screenshots help a lot.",
# 15
"More",
# 16
"See our <a href=\"privacy.html\">Privacy Policy</a> and\n<a href=\"https://www.apple.com/legal/itunes/appstore/dev/stdeula\" target=\"_blank\" rel=\"noopener\">Terms of Use</a> (Apple's standard EULA, the same one used in the app).",
]

PRIV = "../privacy.html"   # the privacy page is English only for now

LANGS = {}

LANGS["en-gb"] = list(EN)

LANGS["fr"] = [
"Busy B : Assistance",
"Assistance",
"Busy B (nom sur l'App Store : « Busy B Planner »)",
"Besoin d'aide avec Busy B ? Nous répondons en général sous un jour ou deux.",
"Écrire à support@busybplanner.com",
"Comment synchroniser mon iPhone et mon iPad ?",
"Busy B se synchronise automatiquement via iCloud. Vérifie que tu es connecté au\nmême compte iCloud sur les deux appareils, avec iCloud Drive activé dans\n<strong>Réglages &gt; [ton nom] &gt; iCloud</strong>.",
"Comment restaurer un achat sur un nouvel appareil ?",
"Ouvre Busy B, va dans <strong>Réglages</strong> et appuie sur\n<strong>Restaurer les achats</strong>. Vérifie que tu es connecté avec le même\nIdentifiant Apple que pour l'achat d'origine.",
"Comment résilier ou gérer mon abonnement ?",
"Va dans <strong>Réglages &gt; [ton nom] &gt; Abonnements</strong> sur ton\nappareil, ou appuie sur <strong>Gérer l'abonnement</strong> dans l'écran Réglages\nde Busy B.",
"Les fonctions d'IA envoient-elles mes tâches quelque part ?",
"Non. Le point du jour, le classement express et le rattrapage s'exécutent entièrement sur\nton appareil avec\n<a href=\"https://www.apple.com/apple-intelligence/\" target=\"_blank\" rel=\"noopener\">Apple Intelligence</a>.\nLes titres, catégories et échéances de tes tâches ne nous sont jamais envoyés, ni à aucun\nserveur externe pour une analyse par IA, et rien de ce que tu notes dans Busy B ne sert jamais\nà entraîner un modèle d'IA. Si un appareil ne peut pas faire fonctionner Apple Intelligence, ces\nfonctions n'apparaissent simplement pas et le reste de l'appli fonctionne exactement comme\navant.",
"Quelque chose ne fonctionne pas. Que faire ?",
"Écris-nous à\n<a href=\"mailto:support@busybplanner.com\">support@busybplanner.com</a> avec une\ndescription du problème et, si possible, le modèle de ton appareil et ta version\nd'iOS. Les captures d'écran aident beaucoup.",
"Plus",
"Consulte notre <a href=\"../privacy.html\">politique de confidentialité</a> (en anglais) et les\n<a href=\"https://www.apple.com/legal/itunes/appstore/dev/stdeula\" target=\"_blank\" rel=\"noopener\">conditions d'utilisation</a> (le CLUF standard d'Apple, le même que dans l'appli).",
]

LANGS["de"] = [
"Busy B: Support",
"Support",
"Busy B (im App Store als „Busy B Planner“ gelistet)",
"Brauchst du Hilfe mit Busy B? Wir antworten normalerweise innerhalb von ein bis zwei Tagen.",
"E-Mail an support@busybplanner.com",
"Wie synchronisiere ich zwischen iPhone und iPad?",
"Busy B synchronisiert automatisch über iCloud. Achte darauf, dass du auf beiden Geräten mit demselben\niCloud-Account angemeldet bist und iCloud Drive aktiviert ist unter\n<strong>Einstellungen &gt; [dein Name] &gt; iCloud</strong>.",
"Wie stelle ich einen Kauf auf einem neuen Gerät wieder her?",
"Öffne Busy B, gehe zu <strong>Einstellungen</strong> und tippe auf\n<strong>Käufe wiederherstellen</strong>. Achte darauf, dass du mit derselben\nApple-ID angemeldet bist, mit der du den Kauf getätigt hast.",
"Wie kündige oder verwalte ich mein Abo?",
"Gehe auf deinem Gerät zu <strong>Einstellungen &gt; [dein Name] &gt; Abos</strong>\noder tippe in den Einstellungen von Busy B auf <strong>Abo verwalten</strong>.",
"Senden die KI-Funktionen meine Aufgaben irgendwohin?",
"Nein. Tagesüberblick, Einsortieren per Tipp und Rückblick laufen komplett auf\ndeinem Gerät mit\n<a href=\"https://www.apple.com/apple-intelligence/\" target=\"_blank\" rel=\"noopener\">Apple Intelligence</a>.\nDeine Aufgabentitel, Kategorien und Fälligkeitsdaten werden weder an uns noch an einen\nexternen Server zur KI-Analyse gesendet, und nichts, was du in Busy B eingibst, wird jemals zum\nTrainieren eines KI-Modells verwendet. Wenn ein Gerät Apple Intelligence nicht ausführen kann, erscheinen diese\nFunktionen einfach nicht, und der Rest der App funktioniert genau wie\nvorher.",
"Etwas funktioniert nicht. Was tun?",
"Schreib uns an\n<a href=\"mailto:support@busybplanner.com\">support@busybplanner.com</a> mit einer\nBeschreibung des Problems und, wenn möglich, deinem Gerätemodell und deiner iOS-\nVersion. Screenshots helfen sehr.",
"Mehr",
"Lies unsere <a href=\"../privacy.html\">Datenschutzerklärung</a> (auf Englisch) und die\n<a href=\"https://www.apple.com/legal/itunes/appstore/dev/stdeula\" target=\"_blank\" rel=\"noopener\">Nutzungsbedingungen</a> (Apples Standard-EULA, dieselbe wie in der App).",
]

LANGS["es"] = [
"Busy B: Soporte",
"Soporte",
"Busy B (en el App Store aparece como «Busy B Planner»)",
"¿Necesitas ayuda con Busy B? Solemos responder en uno o dos días.",
"Escribe a support@busybplanner.com",
"¿Cómo sincronizo entre mi iPhone y mi iPad?",
"Busy B se sincroniza automáticamente a través de iCloud. Asegúrate de haber iniciado sesión con la\nmisma cuenta de iCloud en ambos dispositivos, con iCloud Drive activado en\n<strong>Ajustes &gt; [tu nombre] &gt; iCloud</strong>.",
"¿Cómo restauro una compra en un dispositivo nuevo?",
"Abre Busy B, ve a <strong>Ajustes</strong> y toca\n<strong>Restaurar compras</strong>. Asegúrate de haber iniciado sesión con el mismo\nID de Apple que usaste para la compra original.",
"¿Cómo cancelo o gestiono mi suscripción?",
"Ve a <strong>Ajustes &gt; [tu nombre] &gt; Suscripciones</strong> en tu\ndispositivo, o toca <strong>Gestionar suscripción</strong> dentro de la pantalla\nde Ajustes de Busy B.",
"¿Las funciones de IA envían mis tareas a algún sitio?",
"No. El resumen del día, la clasificación en un toque y el repaso se ejecutan por completo en\ntu dispositivo con\n<a href=\"https://www.apple.com/apple-intelligence/\" target=\"_blank\" rel=\"noopener\">Apple Intelligence</a>.\nLos títulos, las categorías y las fechas de tus tareas nunca se envían a nosotros ni a ningún\nservidor externo para análisis de IA, y nada de lo que pones en Busy B se usa jamás\npara entrenar un modelo de IA. Si un dispositivo no puede ejecutar Apple Intelligence, estas\nfunciones simplemente no aparecen y el resto de la app funciona exactamente igual que\nantes.",
"Algo no funciona. ¿Qué hago?",
"Escríbenos a\n<a href=\"mailto:support@busybplanner.com\">support@busybplanner.com</a> con una\ndescripción del problema y, si puedes, el modelo de tu dispositivo y la versión\nde iOS. Las capturas de pantalla ayudan mucho.",
"Más",
"Consulta nuestra <a href=\"../privacy.html\">política de privacidad</a> (en inglés) y los\n<a href=\"https://www.apple.com/legal/itunes/appstore/dev/stdeula\" target=\"_blank\" rel=\"noopener\">términos de uso</a> (el EULA estándar de Apple, el mismo que se usa en la app).",
]

# Mexican Spanish: Spain text with vocabulary swaps.
_swaps = [("Ajustes", "Configuración"), ("gestiono", "administro"), ("Gestionar suscripción", "Administrar suscripción"),
          ("Asegúrate de haber iniciado sesión", "Asegúrate de haber iniciado sesión"),
          ("ve a", "ve a"), ("pantalla\nde Configuración", "pantalla\nde Configuración"),
          ("y el repaso se ejecutan", "y el repaso se ejecutan")]
LANGS["es-mx"] = []
for _s in LANGS["es"]:
    for _a, _b in _swaps:
        _s = _s.replace(_a, _b)
    LANGS["es-mx"].append(_s)

LANGS["it"] = [
"Busy B: Assistenza",
"Assistenza",
"Busy B (sull'App Store compare come «Busy B Planner»)",
"Ti serve aiuto con Busy B? Di solito rispondiamo entro un giorno o due.",
"Scrivi a support@busybplanner.com",
"Come sincronizzo iPhone e iPad?",
"Busy B si sincronizza automaticamente tramite iCloud. Assicurati di aver effettuato l'accesso con lo\nstesso account iCloud su entrambi i dispositivi, con iCloud Drive attivo in\n<strong>Impostazioni &gt; [il tuo nome] &gt; iCloud</strong>.",
"Come ripristino un acquisto su un nuovo dispositivo?",
"Apri Busy B, vai in <strong>Impostazioni</strong> e tocca\n<strong>Ripristina acquisti</strong>. Assicurati di aver effettuato l'accesso con lo stesso\nID Apple usato per l'acquisto originale.",
"Come annullo o gestisco il mio abbonamento?",
"Vai in <strong>Impostazioni &gt; [il tuo nome] &gt; Abbonamenti</strong> sul tuo\ndispositivo, oppure tocca <strong>Gestisci abbonamento</strong> nella schermata\nImpostazioni di Busy B.",
"Le funzioni di IA inviano le mie attività da qualche parte?",
"No. Il riepilogo del giorno, lo smistamento con un tocco e gli arretrati girano interamente sul\ntuo dispositivo con\n<a href=\"https://www.apple.com/apple-intelligence/\" target=\"_blank\" rel=\"noopener\">Apple Intelligence</a>.\nI titoli, le categorie e le scadenze delle tue attività non vengono mai inviati a noi né a nessun\nserver esterno per l'analisi con l'IA, e nulla di ciò che inserisci in Busy B viene mai usato\nper addestrare un modello di IA. Se un dispositivo non può eseguire Apple Intelligence, queste\nfunzioni semplicemente non compaiono e il resto dell'app funziona esattamente come\nprima.",
"Qualcosa non funziona. Che faccio?",
"Scrivici a\n<a href=\"mailto:support@busybplanner.com\">support@busybplanner.com</a> con una\ndescrizione del problema e, se possibile, il modello del tuo dispositivo e la versione\ndi iOS. Gli screenshot aiutano molto.",
"Altro",
"Consulta la nostra <a href=\"../privacy.html\">informativa sulla privacy</a> (in inglese) e i\n<a href=\"https://www.apple.com/legal/itunes/appstore/dev/stdeula\" target=\"_blank\" rel=\"noopener\">termini di utilizzo</a> (l'EULA standard di Apple, lo stesso usato nell'app).",
]

LANGS["nl"] = [
"Busy B: Support",
"Support",
"Busy B (in de App Store vermeld als \"Busy B Planner\")",
"Hulp nodig met Busy B? We antwoorden meestal binnen een dag of twee.",
"Mail naar support@busybplanner.com",
"Hoe synchroniseer ik tussen mijn iPhone en iPad?",
"Busy B synchroniseert automatisch via iCloud. Zorg dat je op beide apparaten bent ingelogd met hetzelfde\niCloud-account, met iCloud Drive ingeschakeld in\n<strong>Instellingen &gt; [je naam] &gt; iCloud</strong>.",
"Hoe herstel ik een aankoop op een nieuw apparaat?",
"Open Busy B, ga naar <strong>Instellingen</strong> en tik op\n<strong>Herstel aankopen</strong>. Zorg dat je bent ingelogd met dezelfde\nApple-account als waarmee je de oorspronkelijke aankoop deed.",
"Hoe zeg ik mijn abonnement op of beheer ik het?",
"Ga op je apparaat naar <strong>Instellingen &gt; [je naam] &gt; Abonnementen</strong>,\nof tik op <strong>Beheer abonnement</strong> in het scherm Instellingen van Busy B.",
"Sturen de AI-functies mijn taken ergens naartoe?",
"Nee. Het dagoverzicht, sorteren met één tik en de terugblik draaien volledig op\njouw apparaat met\n<a href=\"https://www.apple.com/apple-intelligence/\" target=\"_blank\" rel=\"noopener\">Apple Intelligence</a>.\nJe taaktitels, categorieën en vervaldatums worden nooit naar ons of naar een externe\nserver gestuurd voor AI-analyse, en niets wat je in Busy B zet wordt ooit gebruikt\nom een AI-model te trainen. Als een apparaat Apple Intelligence niet kan draaien, verschijnen deze\nfuncties gewoon niet en werkt de rest van de app precies zoals\nvoorheen.",
"Er werkt iets niet. Wat moet ik doen?",
"Mail ons op\n<a href=\"mailto:support@busybplanner.com\">support@busybplanner.com</a> met een\nbeschrijving van het probleem en, indien mogelijk, je apparaatmodel en iOS-\nversie. Schermafbeeldingen helpen enorm.",
"Meer",
"Bekijk ons <a href=\"../privacy.html\">privacybeleid</a> (in het Engels) en de\n<a href=\"https://www.apple.com/legal/itunes/appstore/dev/stdeula\" target=\"_blank\" rel=\"noopener\">gebruiksvoorwaarden</a> (Apples standaard-EULA, dezelfde als in de app).",
]

LANGS["pt-br"] = [
"Busy B: Suporte",
"Suporte",
"Busy B (listado na App Store como \"Busy B Planner\")",
"Precisa de ajuda com o Busy B? Normalmente respondemos em um ou dois dias.",
"Escreva para support@busybplanner.com",
"Como sincronizo entre o meu iPhone e o iPad?",
"O Busy B sincroniza automaticamente pelo iCloud. Confira se você está conectado à\nmesma conta do iCloud nos dois aparelhos, com o iCloud Drive ativado em\n<strong>Ajustes &gt; [seu nome] &gt; iCloud</strong>.",
"Como restauro uma compra em um aparelho novo?",
"Abra o Busy B, vá em <strong>Ajustes</strong> e toque em\n<strong>Restaurar compras</strong>. Confira se você está conectado com o mesmo\nID Apple usado na compra original.",
"Como cancelo ou gerencio a minha assinatura?",
"Vá em <strong>Ajustes &gt; [seu nome] &gt; Assinaturas</strong> no seu\naparelho, ou toque em <strong>Gerenciar assinatura</strong> na tela de Ajustes\ndo Busy B.",
"Os recursos de IA enviam as minhas tarefas para algum lugar?",
"Não. O resumo do dia, a organização com um toque e as pendências rodam inteiramente no\nseu aparelho com a\n<a href=\"https://www.apple.com/apple-intelligence/\" target=\"_blank\" rel=\"noopener\">Apple Intelligence</a>.\nOs títulos, as categorias e os prazos das suas tarefas nunca são enviados para nós nem para nenhum\nservidor externo para análise de IA, e nada do que você coloca no Busy B é usado\npara treinar um modelo de IA. Se um aparelho não consegue rodar a Apple Intelligence, esses\nrecursos simplesmente não aparecem e o resto do app funciona exatamente como\nantes.",
"Algo não está funcionando. O que eu faço?",
"Escreva para\n<a href=\"mailto:support@busybplanner.com\">support@busybplanner.com</a> com uma\ndescrição do problema e, se possível, o modelo do seu aparelho e a versão\ndo iOS. Capturas de tela ajudam muito.",
"Mais",
"Veja a nossa <a href=\"../privacy.html\">Política de Privacidade</a> (em inglês) e os\n<a href=\"https://www.apple.com/legal/itunes/appstore/dev/stdeula\" target=\"_blank\" rel=\"noopener\">Termos de Uso</a> (o EULA padrão da Apple, o mesmo usado no app).",
]
