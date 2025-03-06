# Pokazil se kávovar! - vstupní úloha pro stáže 2025

U nás v Edhouse teče káva proudem… Ehm, teda teď vlastně neteče, protože se nám pokazil kávovar.
I když možná kávu nepiješ a preferuješ čaj, zdá se, že se nám naskytla skvělá příležitost prověřit
tvé technické schopnosti.

## Zadání úlohy

Poslední, kdo se v kávovaru vrtal byl náš dobrý kamarád Eda – opravář kávovarů. Vypadá to, že klíč
k opravě leží v Edových kalibračních výpočtech, které najdeš přiložené k tomuto zadání v samostatném
textovém souboru. Zdá se ale, že výpočty nebude možné hned použít k opravě kávovaru, někdo totiž
z __výrazů na pravé straně vynechal znaménka__!

To ale znamená, že některé výpočty můžou být k ničemu, neboť k opravě se hodí pouze ty výpočty,
u kterých můžeme doplnit znaménka + (plus), nebo * (krát) mezi čísla na pravé straně (napravo od :)
tak, aby vznikl výraz, který po vyhodnocení dá číslo na straně levé (nalevo od :) – tzv.
testovací hodnotu.

Podívejme se na následující __příklad__ (jedná se pouze o příklad, skutečná vstupní data najdeš
v příloze):

```text
168: 8 21
4488: 81 55 33
93: 27 15
146: 5 16
3421: 5 2 1 55
263021: 33 10 123
531: 14 2 34
31834: 2 5 28 33
153: 20 7 5 18
97: 95 2 1 1
```

Každý řádek představuje jeden výpočet. Testovací hodnoty jsou uvedeny před jednotlivými dvojtečkami.
Tvým úkolem je zjistit, jestli je možné zbývající čísla na řádku zkombinovat operátory, aby vznikla
testovací hodnota.

__Operátory jsou vždy vyhodnocovány zleva doprava, nikoliv dle typických pravidel
pořadí operátorů__. Stejně tak není možné zaměňovat pořadí čísel na pravé straně.

V příkladu výše jsou pouze čtyři validní výpočty:

- Výpočet `168: 8 21` obsahuje pouze jednu pozici kam lze vložit operátor: mezi `8` a `21`.
  Vybereme-li `+`, získáme `29`, ale pokud naopak `*` obdržíme testovací hodnotu (`8 * 21 = 168`).
- V případě `4488: 81, 55, 33` jsou dvě místa pro operátor. Mezi čtyřmi možnými konfiguracemi
  operátorů jsou dvě, které po vyhodnocení produkují testovací hodnotu: `81 + 55 * 33`
  a `81 * 55 + 33` se oba rovnají `4488` (při dodržení pořadí vyhodnocení zleva doprava)!
- Výpočet `153: 20 7 5 18` je validní pouze v jediném případě: `20 + 7 * 5 + 18`.
- Výpočet `97: 95 2 1 1` je rovněž možné učinit validním pouze jedním způsobem `95 + 2 * 1 * 1`

Abychom mohli pokračovat s opravou kávovaru, potřebujeme zjistit součet testovacích hodnot ze všech
validních výpočtů. V příkladě výše je součet testovacích hodnot z validních výpočtů roven číslu `4906`.

## Vstupní data

Edových skutečných výpočtů je samozřejmě mnohem více a najdeš je v samostatném textovém souboru
`vypocty.txt` umístěném v kořeni tohoto repozitáře.

__Jaký je součet testovacích hodnot validních Edových výpočtů?__

## Pokyny k návrhu

- Zvolte jazyk a prostředí dle preference – C++ / C# / Java / Python / Rust / JavaScript. Jakmile
  zvolíte konkrétní jazyk, je nutné dodržet pokyny týkající se vývojového toolingu
  v sekci [Volba prostředí](#volba-prostředí)
- Napište program nazvaný `reseni`, který
  - načte data ze standardního vstupu (STDIN), viz upřesnění níže
  - co nejefektivněji vyřeší výše popsaný úkol
  - vypíše odpověď na standardní výstup (STDOUT)
- Pokud to prostředí dovolí, nerozdělujte kód do více souborů a používejte pouze standardní
  knihovny. Úloha je natolik jednoduchá, aby nevyžadovala složitější členění, či použití knihoven
  třetích stran.

Upřesnění: Chceme, aby bylo možné vaše programy snadno spouštět z příkazové řádky:

```text
%> reseni.exe < priklad.txt
4906

%>
```

V Pythonu, JS a TS je potřeba něco málo přidat, ale fungovat to bude stejně, např:

```text
%> python reseni.py < priklad.txt
4906

%>
```

## Pokyny k odevzdání

- Repozitář musí obsahovat zdrojový kód řešení a všechny náležitosti potřebné pro jeho sestavení
  a spuštění z příkazové řádky. Tooling závisí na volbě programovacího jazyka a je předepsán
  v následující sekci [Volba prostředí](#volba-prostředí).
- Repozitář musí mít očekávanou strukturu dle prostředí jak je popsáno v následující sekci
  [Volba prostředí](#volba-prostředí).
- Pokud to prostředí dovolí, nerozdělujte kód do více souborů a používejte pouze standardní
  knihovny. Úloha je natolik jednoduchá, aby nevyžadovala složitější členění, či použití knihoven
  třetích stran.
- Chcete-li své řešení předložit ke kontrole, zašlete URL vašeho repozitáře na adresu
  [kariera@edhouse.cz](mailto:kariera@edhouse.cz).

Upřesnění: Sestavení a spuštění vašich úloh budeme automatizovat. Chceme, aby bylo možné vaše řešení
snadno sestavit a spustit z příkazové řádky:

```text
%> dotnet build
(...)

%> dotnet run < priklad.txt
4906

%>
```

Obdobná bude situace v Rust s Cargo, C++ s CMake a v Javě s Maven.

V Pythonu a JS (s Node.js) bude naopak situace jednoduší, neboť nebude třeba nic sestavovat

```text
> python reseni.py < priklad.txt
4906

%>
```

## Volba prostředí

Pro vývoj řešení doporučujeme Visual Studio Code, jelikož v následujících sekcích odkazujeme
na postupy z oficiální dokumentace tohoto nástroje. Na vývojovém prostředí ale nakonec nezáleží,
podstatné je dodržet požadovaný tooling a strukturu repozitáře.

__Pro spouštění příkazů ve Windows používejte výhradně CMD__.

### C++

Potřebujeme, aby váš repozitář definoval zcela triviální CMake project stejně jak je tomu
v příkladě [zde](https://cmake.org/cmake/help/latest/guide/tutorial/A%20Basic%20Starting%20Point.html#exercise-1-building-a-basic-project). Použijete-li VS Code, je možné postupovat například podle návodu [zde](https://code.visualstudio.com/docs/cpp/cmake-quickstart).

Odevzdávejte prosím pouze zdrojový kód a CMakeLists.txt. Očekáváná struktura vašeho repozitáře je:

```text
intern-2025-%GITHUB_USERNAME%
|- README.md
|- vypocty.txt
|- priklad.txt
|- reseni.cpp
|- CMakeLists.txt
```

Vše ostatní je vygenerováno a patří do `.gitignore`.
Pro generování souborů potřebných pro sestavení vašeho řešení použijeme příkaz:

```text
intern-2025-%GITHUB_USERNAME%> cmake -B build .
```

Pro sestavení příkaz:

```text
intern-2025-%GITHUB_USERNAME%> cmake --build build -–config Release
```

Pro spuštění potom příkaz

```text
intern-2025-%GITHUB_USERNAME%> .\build\Release\reseni.exe < vypocty.txt
```

Využití CMake vám dává teoretickou možnost použít libovolný překladač a build systém. My budeme řešení kontrolovat překladačem `gcc`. Buďto použijte ten stejný, nebo se vyvarujte použití jakýchkoliv nestandardních jazykových prostředků.

### C\#

Použijte .NET 8

Potřebujeme, aby váš repozitář definoval triviální .NET Console App projekt. Vytvořit projektový
adresář můžete podle [návodu zde](https://code.visualstudio.com/docs/csharp/get-started),
nebo manuálně příkazem

```text
intern-2025-%GITHUB_USERNAME%> dotnet new console -o reseni
```

Očekávaná struktura vašeho repozitáře je:

```text
intern-2025-%GITHUB_USERNAME%
|- README.md
|- vypocty.txt
|- priklad.txt
|- reseni
  |- Program.cs
  |- reseni.csproj
```

Pro sestavení vašeho řešení použijeme příkaz:

```text
intern-2025-%GITHUB_USERNAME%\reseni> dotnet build
```

Pro spuštění pak příkaz:

```text
intern-2025-%GITHUB_USERNAME%\reseni> dotnet run < ..\vypocty.txt
```

### Java

Použijte OpenJDK a Java 21.

Potřebujeme, aby váš repozitář definoval triviální Maven projekt
[quickstart archetypu](https://maven.apache.org/archetypes/maven-archetype-quickstart/).
Použijete-li VS Code, může vám pomoci také [návod zde](https://code.visualstudio.com/docs/java/java-build#_generate-project-from-maven-archetype).

Název package musí být __reseni__.

Očekávaná struktura vašeho repozitáře je:

```text
intern-2025-%GITHUB_USERNAME%
|- README.md
|- vypocty.txt
|- priklad.txt
|- reseni
  |- .mvn
    |- ...
  |- src
    |- main\java\reseni\App.java
    |- test
      |- ...
  |- pom.xml
```

Pro sestavení použijeme příkaz

```text
intern-2025-%GITHUB_USERNAME%\reseni> mvn package
```

Pro spuštění použijeme plugin exec:java:

```text
intern-2025-%GITHUB_USERNAME%\reseni> mvn exec:java -Dexec.mainClass="reseni.App" < ..\vypocty.txt
```

### Python

Použijte Python ve verzi 3.13

Očekávaná struktura vašeho repozitáře je:

```text
intern-2025-%GITHUB_USERNAME%
|- README.md
|- vypocty.txt
|- priklad.txt
|- reseni
```

Pro spuštění budeme používat příkaz:

```text
intern-2025-%GITHUB_USERNAME%> python reseni.py < vypocty.txt
```

### Rust

Použijte Rust 1.84, edice 2021

Potřebujeme, aby váš repozitář definoval triviální binární crate. S tvorbou crate vám může pomoci
návod [zde](https://code.visualstudio.com/docs/languages/rust#_hello-world), nebo příkaz:

```text
intern-2025-%GITHUB_USERNAME%\> cargo new reseni --vcs none
```

Všimněte si přepínače `--vcs none`.

Očekávaná struktura vašeho repozitáře je:

```text
intern-2025-%GITHUB_USERNAME%
|- README.md
|- vypocty.txt
|- priklad.txt
|- reseni
  |- src
    |- main.rs
  |- Cargo.toml
```

Pro sestavení vašeho řešení použijeme příkaz:

```text
intern-2025-%GITHUB_USERNAME%\reseni> cargo build
```

Pro spuštění pak příkaz:

```text
intern-2025-%GITHUB_USERNAME%\reseni> cargo run < ..\vypocty.txt
```

### JavaScript

Pro rozběhnutí kódu v JS použijte Node.js v22. Postupovat můžete podle návodu
[zde](https://code.visualstudio.com/docs/nodejs/nodejs-tutorial).

Očekávaná struktura vašeho repozitáře je:

```text
intern-2025-%GITHUB_USERNAME%
|- README.md
|- vypocty.txt
|- priklad.txt
|- reseni.js
```

Pro spuštění kódu použijeme příkaz:

```text
intern-2025-%GITHUB_USERNAME%> node reseni.js < vypocty.txt
```
