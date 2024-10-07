from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # HTML content with clock and a fun message
    html_content = """
    <!doctype html>
    <html>
        <head>
            <title>Hello Page</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }
                .clock { font-size: 24px; margin-top: 20px; }
                .fun { font-size: 18px; margin-top: 20px; }
            </style>
            <script>
                function startClock() {
                    setInterval(updateClock, 1000);
                }

                function updateClock() {
                    var now = new Date();
                    var timeString = now.toLocaleTimeString();
                    document.getElementById('clock').innerText = timeString;
                }
            </script>
        </head>
        <body onload="startClock()">
            <h1>Hello, Welcome to the Fun Page!</h1>
            <div class="clock" id="clock">Clock Loading...</div>
            <div class="fun">Keep Smiling :)</div>
        </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
