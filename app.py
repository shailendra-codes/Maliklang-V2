import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import multi_agent_mesh

app = FastAPI(title="Maliklang-V2 AI Platform")

@app.get("/", response_class=HTMLResponse)
def home():
    # ग्रामीण डॉक्टरों के लिए एक सुंदर और सीधा HTML विज़ुअल इंटरफ़ेस
    html_content = """
    <html>
        <head>
            <title>Maliklang-V2 AI Portal</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #121212; color: #ffffff; text-align: center; padding: 50px; }
                .container { border: 2px solid #00ffcc; padding: 30px; display: inline-block; border-radius: 10px; background-color: #1e1e1e; }
                h1 { color: #00ffcc; }
                .status { color: #ffcc00; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Maliklang-V2 Genomic AI Engine</h1>
                <p class="status">⚡ LIVE ON RENDER CLIENT SERVER ⚡</p>
                <hr style="border-color: #00ffcc;">
                <p>बहराइच फाउंडर विज़न: बिना इंटरनेट ग्रामीण स्वास्थ्य क्रांति हेतु तैयार।</p>
                <p><strong>सिस्टम स्टेटस:</strong> 100% सुरक्षित एवं एक्टिवेटिड।</p>
            </div>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
 
