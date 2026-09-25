# Maliklang V2.0.0 - Real-Time Genomic WebSockets Layer
# Author: Shailendra Kumar Singh

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json

app = FastAPI(title="Maliklang V2 Genomic Bio-Connect")

class BioMeshManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_alert(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = BioMeshManager()

@app.websocket("/ws/bio-sensor")
async def bio_sensor_endpoint(websocket: WebSocket):
    """
    FastAPI WebSocket Layer: लाइव नैनो-सेंसर्स से DNA डेटा स्ट्रीम रिसीव करना
    और रियल-टाइम में उसे रिपॉन्ड करना।
    """
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            genomic_payload = json.loads(data)
           
            dna_sequence = genomic_payload.get("sequence", "")
            sensor_id = genomic_payload.get("sensor_id", "UNKNOWN_NODE")
           
            print(f"📡 [MESH NODE {sensor_id}]: Stream Received. Parsing payload...")
           
            await websocket.send_json({
                "status": "PROCESSED",
                "message": f"Data node {sensor_id} integrated with Maliklang Engine."
            })
           
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print(f"🛑 [MESH NODE]: Sensor disconnected safely.")
 
