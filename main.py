# Maliklang V2.0.0 - Main System Entry Point
# Author: Shailendra Kumar Singh

import asyncio
from multi_agent_mesh import GenomicAgentMesh

class MaliklangV2Engine:
    def __init__(self):
        print("🔬 [SYSTEM INITIALIZATION]: Maliklang V2.0.0 Bio-Computing Engine Online.")
        print("🛡️ [SECURITY CONFIGURATION]: AST Genetic Shield Integrated.")

    async def execute_health_scan(self, raw_sequence: str, patient_id: str):
        """
        Master Execution: डेटा स्ट्रीम को कैप्चर करना और
        मल्टी-एजेंट मेश के ज़रिए रीयल-टाइम डायग्नोसिस रिपोर्ट तैयार करना।
        """
        print(f"\n──────────────────────────────────────────────────")
        print(f"🏥 [PATIENT RUNTIME]: Initiating Scan for ID: {patient_id}")
        print(f"──────────────────────────────────────────────────")
       
        mesh_node = GenomicAgentMesh(raw_sequence, node_id=patient_id)
        scan_report = await mesh_node.agent_orchestrator()
       
        print(f"──────────────────────────────────────────────────")
        print(f"📋 [SYSTEM DIAGNOSIS REPORT]:\n{scan_report}")
        print(f"──────────────────────────────────────────────────")
        return scan_report

if __name__ == "__main__":
    engine = MaliklangV2Engine()
   
    # टेस्ट केस 1: पूरी तरह स्वस्थ DNA सैंपल
    healthy_sample = "ATCGATCGATCGATCGATCG"
   
    # टेस्ट केस 2: म्यूटेशन वाला सैंपल (BRCA1 और TP53 म्यूटेशन टोकन्स)
    high_risk_sample = "ATCGATTGCTAGCTAGCTAG"
   
    async def run_tests():
        await engine.execute_health_scan(healthy_sample, "PATIENT_NODE_01_HEALTHY")
        await engine.execute_health_scan(high_risk_sample, "PATIENT_NODE_02_HIGH_RISK")

    asyncio.run(run_tests())
 
