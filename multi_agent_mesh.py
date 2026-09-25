# Maliklang V2.0.0 - Distributed Genomic Multi-Agent Mesh
# Author: Shailendra Kumar Singh

import asyncio
from dna_lexer import DNALexer
from genetic_shield import GeneticShield

class GenomicAgentMesh:
    def __init__(self, raw_dna_stream: str, node_id: str = "SENSOR_01"):
        self.raw_data = raw_dna_stream
        self.node_id = node_id
        self.shield = GeneticShield()

    async def agent_lexer_task(self):
        """एजेंट 1: लाइव डेटा को तुरंत टोकनाइज़ और पार्स करना"""
        print(f"🧬 [AGENT 1 - LEXER]: Parsing genomic stream from Node {self.node_id}...")
        await asyncio.sleep(0.5)
        lexer = DNALexer(self.raw_data)
        tokens = lexer.tokenize()
        print(f"✅ [AGENT 1]: Tokenization Complete. Generated {len(tokens)} tokens.")
        return tokens

    async def agent_shield_task(self, tokens: list):
        """एजेंट 2: बायो-सिक्योरिटी और कैंसर म्यूटेशन को लाइव स्कैन करना"""
        print(f"🛡️ [AGENT 2 - SHIELD]: Running AST Genetic Scanning against DB...")
        await asyncio.sleep(0.5)
        scan_result = self.shield.scan_tokens(tokens)
        return scan_result

    async def agent_orchestrator(self):
        """एजेंट 3: सभी एजेंट्स को समानांतर (Parallel) चलाना और निर्णय लेना"""
        print(f"🚀 [AGENT 3 - MESH MAIN]: Orchestrating Bio-Computing Nodes...")
        tokens = await self.agent_lexer_task()
        if not tokens:
            return "❌ [MESH ERROR]: No valid DNA tokens to process."
        final_report = await self.agent_shield_task(tokens)
        print(f"📊 [MESH REPORT FOR {self.node_id}]: Integration Success.")
        return final_report

if __name__ == "__main__":
    sample_dna_stream = "ATCGATTGCTAGCTAGCTAG"
    mesh = GenomicAgentMesh(sample_dna_stream)
    report = asyncio.run(mesh.agent_orchestrator())
    print("\n--- FINAL SYSTEM OUTPUT ---")
    print(report)
 
