---
title: Zeus Banking Trojan
categories: [guid]
tags: [malawar,Trojan,Zeus Banking Trojan,]
image: images/malawar/zeuss.jpg
---


# Malware Analysis Report: zeus.pdf.exe

# Zeus Trojan Overview

## Background Information
- **Purpose:** Primarily created to be a financial banking trojan.
- **First Spotted:** 2007, when Zeus Trojan was caught stealing sensitive information from systems owned by the **U.S. Department of Transportation**.
- **Variants:** Over **573 known versions** and **36 known families**, according to [Zeus Museum](https://zeusmuseum.com/).
- **Code Leak:** Malicious code became public in **2011** after a leak.
- **Suspected Author:** *Evgeniy Mikhailovich Bogachev*  
  - Source: [Krebs on Security](https://krebsonsecurity.com/2015/02/fbi-3m-bounty-for-zeus-trojan-author/)

## Delivery Methods
- **Drive-by Downloads**  
  - Users visit a compromised website hosting the backdoor trojan.  
  - Now largely **obsolete** due to modern browser protections.
  
- **Phishing & Spam Campaigns**  
  - **Primary infection method** in modern attacks.  
  - Victims are tricked into downloading and executing malicious attachments or links.

## Primary Goals
- **Steal financial information** from infected systems.
- **Exfiltrate** sensitive banking data.
- **Add infected machines to a botnet**, often P2P-based (depends on Zeus family).

## Crackdown History
- **Gameover Zeus** (a major variant) was taken down by the **FBI in 2014**.
- **Impact in the U.S.:** Estimated **25% of computers** were infected.
- **Financial Damages:** Over **$100 million**.
- **Evgeniy Bogachev:** $3 million bounty by the FBI, still **one of the most wanted hackers**.

## Impact
- Inspired **hundreds of additional malware variants** using parts of Zeus's source code.
- Resulted in **millions of infected machines**.
- **Global damages in the hundreds of millions of dollars**.


## Overview
- **File Name**: `zeus.pdf.exe`
- **File Type**: Windows Executable
- **Target OS**: Windows
- **Time Date Stamp**: Mon Nov 25 10:32:03 2013 UTC
- **Hashes**:
  - MD5: `ea039a854d20d7734c5add48f1a51c34`
  - SHA1: `9615dca4c0e46b8a39de5428af7db060399230b2`
  - SHA256: `69e966e730557fde8fd84317cdef1ece00a8bb3470c0b58f3231e170168af169`
- **IMPHASH**: `308fe2649c586660c71bc787d65e54fd`

## VirusTotal Scan Overview
- **Detection Rate**: 53/76 antivirus engines flagged the file as malicious.
- **Primary Threat Label**: `trojan.zaccess/sirefef`
- **Threat Categories**:
  - Trojan: 33 detections
  - Dropper: 5 detections
- **Common Threat Names**:
  - `zaccess`: 13 occurrences
  - `sirefef`: 7 occurrences
  - `wldcr`: 5 occurrences
- **Notable Detections**:
  - ALYac: `Trojan.ZeroAccess.RN`
  - Kaspersky: `Backdoor.Win32.ZAccess.evyo`
  - Microsoft: `Backdoor:Win32/ZAccess!MTB`
  - Malwarebytes: `Sirefef.Trojan.Bot.DDS`
  - Symantec: `Trojan.Zeroaccess.C`
  
## basic capa output
![VirusTotal Scan Results](images/malawar/capa.PNG)

### Visual Representation

![VirusTotal Scan Results](images/malawar/Virus_Total.PNG)
*Caption: Screenshot of VirusTotal scan results for zeus.pdf.exe.*

## CrowdSourced IDS Alerts
- **Alerts**: 3 high-severity alerts detected
  - **Target**: IP `85.114.12…`, Port `53` (DNS traffic)
  - **Category**: Network Trojan activity
  - **Source**: Proofpoint Emerging Threats Open ruleset
- **Alert Summary**:
  - High: 3 alerts
  - Medium: 0 alerts
  - Low: 0 alerts
  - Info: 0 alerts
## Language Detection

![lang.PNG](images/malawar/lang.PNG)
- **Probable Languages**:
  - C#: 60% probability, 3 pattern occurrences
  - C: 40% probability, 2 pattern occurrences
## Additional Findings
- **Embedded PE Files**: None detected.
- **Registry Keys**: No patterns found.
- **Special Artifacts**: None identified.
- **Function Count**: 81 functions analyzed, with sizes ranging from 1 to 1060 bytes; notable large functions (`sub_0040142f`, `sub_00408469`) may indicate complex logic.

## Windows API Analysis
- **Total Imports/Exports Analyzed**: 150
- **Categorized Behaviors**:
  - **File and Directory Discovery** (34 functions):
    - Functions like `CreateFile`, `WriteFile`, `DeleteFileA`, `FindFirstFile`, and `Path*` variants indicate extensive file manipulation and directory traversal capabilities.
  - **Persistence**:
    - Uses `WinExec` and `SetCurrentDirectory` for execution and persistence mechanisms.
  - **Credential Access and Keylogging** (5 functions):
    - `GetAsyncKeyState`, `VkKeyScanA`, and `GetKeynameTextA` suggest keylogging to capture user input.
  - **Networking/Web** (2 functions):
    - Limited to `Ping`, indicatng basic network activity.
  - **Memory Management** (17 functions):
    - `LocalAlloc`, `VirtualQueryEx`, and `HeapFree` show memory manipulation.
  - **Evasion/Bypassing** (6 functions):
    - `CreateFileMappingA`, `GetTickCount`, and `DeleteFileA` hint at anti-analysis techniques.
  - **Information Gathering** (32 functions):
    - `GetClipboardData`, `GetDriveTypeA`, and `GetWindowsDirectory` suggest data harvesting.
  - **Process Management** (9 functions):
    - `WinExec` and `GetCurrentThread` for process control.
  - **DLL/Resource Handling** (7 functions):
    - `GetModuleHandleW` and `FreeLibrary` for resource access.
- **Linked DLLs**: `SHLWAPI.dll`, `KERNEL32.dll`, `USER32.dll`
- ![libraries Scan Results](images/malawar/libraries.PNG)


## Section Analysis

![VirusTotal Scan Results](images/malawar/section.PNG)
- **Sections**:
  - `.text`: 0xb571 bytes, Entropy: 6.71 (code section)
  - `.data`: 0x128b1 bytes, Entropy: 6.13 (data storage)
  - `.itext`: 0x84d bytes, Entropy: 4.82 (possibly initialization code)
  - `.pdata`: 0x17cbe bytes, Entropy: 6.77 (exception handling)
  - `.rsrc`: 0x58f2 bytes, Entropy: 6.14 (resources)
  - `.reloc`: 0x15ec bytes, Entropy: 6.44 (relocation table)
- **Observation**: High entropy in `.text` and `.pdata` suggests packed or obfuscated code.

## String Analysis

![PestudioScan Results](images/malawar/strings.PNG)
- **Stack Strings**: `c0lV`, `O9lp`, `6zQy`, `P3RRw`, `qpju` (random, possibly encrypted)
- **Decoded Strings**: Numerous short strings (e.g., `0BKn`, `pjAb:$a$`, `O8Xu`), likely obfuscated data or keys.
- **Interesting Patterns**: References to `SHLWAPI.dll`, `KERNEL32.dll`, `USER32.dll`.


## File Header



## API calls
- AllowSetForegroundWindow: <span style="background-color: yellow">Allows a specified process to set the foreground window even if the process does not currently own the foreground windows focus.
</span>

- GetCapture

- GetWindowTextLength

- GetEnvironmentVariable

- GetEnvironmentVariable

- VkKeyScan: <span style="background-color: yellow"> Translates a character to the corresponding virtual-key code</span>

- GetAsyncKeyState:  <span style="background-color: yellow">Allows you to determine whether a particular key is currently pressed or released</span>

- PathRenameExtension

- WriteFile

- FindNextFile

- GetCurrentThread

- WinExec: 	<span style="background-color: yellow">Legacy function used to launch an application or execute a command line. Available in
	earlier versions of Windows</span>

- GlobalAddAtom: <span style="background-color: yellow">Adds a string to the atom table. Atom table are used for storing small pieces of string-based data. Legacy mechanism</span>


- GetClipboardOwner

- GetClipboardData

- EnumClipboardFormats

- DdeQueryNextServer

- GetConsoleAliasExesLength:<span style="background-color: yellow"> Retrieves executable files.
</span>

- SetCurrentDirectory

## Defense Evasion

![cutter Scan Results](images/malawar/cutter.PNG)
---

Tests to see how long the Windows machine has been running with the GetTickCount() function. (MITRE ATT&CK sub-technique 3 T1497.003).
**String Address Location**
Looking into a set of extracted strings (random gibberish followed by a DLL function): 

<span style="background-color: red">CellrotoCrudUntohighCols </span>
KERNEL32.CreateFileA

I suspect each of these random blobs of strings is the programs function name for the specific function called within the DLLs function

![adress Scan Result](images/malawar/Address.PNG)


![ighC Scan Result](images/malawar/ighC.PNG)

**The string `icgH`  has an offset of 19 address space away from the `KERNEL32.MulDiv` function, meaning they are relatively close**

![kernel32.PNG](images/malawar/creatFileA.PNG)

![kernel32.PNG](images/malawar/kernel32.PNG)

# Basic Dynamic Analysis
 ## Host-based Indicators
 ## Tools Used: Procmon, INetSim, & Wireshark
 
![autoPNG](images/malawar/autoinsatll.PNG)

Under invoice parent process has two child processes, including a suspended ``cmd.exe`` with a child  
``conhost.exe``

![again.PNG](images/malawar/agaiiiin.PNG)

Under ```wininit.exe``` -> ```svchost.exe``` -> ```GoogleUpdate.exe``` is dropped.

![dll.PNG](images/malawar/dll.PNG)

**Drops ```msimg32.dll``` and ```InstallFlashPlayer.exe``` into ```C:\Users\glitch\AppData\Local\Temp\InstallFlashPlayer.exe ```.**

![msimg32.dllPNG](images/malawar/dll2.PNG)

![inetsim.PNG](images/malawar/remnux.PNG)

Started  ```inetsim``` to simulate DNS server and Wireshark for packet capture.

![http.PNG](images/malawar/shark.PNG)

## YARA Rule Matches
- **Keylogger**:
  - Matches: `USER32.dll` (0x1ec42), `GetAsyncKeyState` (0x1eb4c)
- **Windows File Operations**:
  - Matches: `KERNEL32.dll` (0x1ea54), `WriteFile` (0x1e91c), `DeleteFileA` (0x32048), `CreateFileA` (0x3178e), `FindFirstFileA` (0x3190e)
# Detection Rues (YARA)

YARA rule used to detect the Zeus Banking Trojan Version 26-Nov-2013.

```console

// import pe

rule Zeus {

 meta:

 author="Grant C."

 description="A detection rule against ZuesBankingVersion_26Nov2013"

 strings:

 $file_name="invoice_2318362983713_823931342io.pdf.exe" ascii

 // Suspected name of functions and DLL functionalities.


$function_name_KERNEL32="AsksmaceaglyBubuPulsKaifTeasMistPeelGhisPrimChaoLyr

eroeno" ascii

 $function_name_KERNERL32_CreateFileA="CellrotoCrudUntohighCols"

ascii

 $function_name_KERNEL32_FINDFIRSTFILEA="GeneAilshe" ascii

 // PE Magic Byte.

 $PE_magic_byte="MZ"

 // Hex String Function Name + DLL.

 $hex_string_SHLWAPI_PATHREMOVEFILESPECA= {44 65 6E 79 4C 75 62 65 44

75 6E 73 73 61 77 73 4F 72 65 73 76 61 72 75 74 00 53 48 4C 57 41 50 49}

 condition:

 // Use the pe library to create fine-grained rules for PE files.

 // pe.ispie

 $PE_magic_byte at 0 and $filename

 and $function_name_KERNEL32

 or $function_name_KERNERL32_CreateFileA

 or $function_name_KERNEL32_FINDFIRSTFILEA

 and $hex_string_SHLWAPI_PATHREMOVEFILESPECA
```


Run the ``` yara64 zeus_rule.yara invoice_2318362983713_823931342io.pdf.exe -s -w -p 32 ```to detect this malware variant based on unique strings.

```s```: Print matched strings to stdout.            
```w```: Ignore warnings.                  
```p 32```: Allocate 32 threads.

# Résumé of Key Findings
The file `zeus.pdf.exe` is a sophisticated **Trojan** (`ZAccess/Sirefef`), detected by 53/76 antivirus engines, acting as a backdoor and dropper with aliases `zaccess`, `sirefef`, and `wldcr`. Compiled on November 25, 2013, it targets Windows systems, leveraging 150 imported functions across `SHLWAPI.dll`, `KERNEL32.dll`, and `USER32.dll`. It exhibits extensive file manipulation (34 functions), keylogging (5 functions), and information gathering (32 functions), with minimal networking (`Ping`). Three high-severity IDS alerts (IP `85.114.12…`, port 53) confirm network Trojan activity. YARA rules flag keylogging and file operations, while high-entropy sections (e.g., `.text`: 6.71) suggest obfuscation. Likely coded in **C# (60%)** or **C (40%)**, this malware poses a severe threat through persistence, credential theft, and system compromise.