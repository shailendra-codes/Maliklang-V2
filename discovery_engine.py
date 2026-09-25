# Maliklang V2.0.0 - Dynamic Self-Learning Discovery Engine
# Author: Shailendra Kumar Singh
# License: MIT License

class MutationDiscoveryEngine:
    def __init__(self):
        # पहले से ज्ञात म्यूटेशन्स
        self.known_mutations = {"ATTG", "CTAG"}
        # स्वस्थ DNA के आम पैटर्न्स
        self.healthy_patterns = {"AAAA", "TTTT", "GGGG", "CCCC", "ATCG"}
        # 🧠 Dynamic Research Registry: लाइव खोजे गए नए म्यूटेशन्स यहाँ जमा होंगे
        self.discovered_registry = {}

    def analyze_and_learn(self, dna_tokens: list, patient_id: str):
        """
        एडवांस तरीका: जांच के दौरान अज्ञात पैटर्न को ढूंढना, रजिस्टर करना
        और रन-टाइम पर अपने डेटाबेस को खुद अपग्रेड (Self-Learn) करना।
        """
        new_flags = []

        for index, token in enumerate(dna_tokens):
            # यदि टोकन बिल्कुल नया है (न स्वस्थ लिस्ट में है, न ज्ञात म्यूटेशन में)
            if token not in self.known_mutations and token not in self.healthy_patterns:
               
                # यदि यह नया पैटर्न पहले ही किसी मरीज में खोजा जा चुका है
                if token in self.discovered_registry:
                    self.discovered_registry[token]["occurrence_count"] += 1
                    status = f"🔁 [KNOWN UNKNOWN]: Already flagged in prior research."
                else:
                    # पहली बार खोजे जाने पर रजिस्ट्री में दर्ज करना (Self-Learning)
                    self.discovered_registry[token] = {
                        "first_patient": patient_id,
                        "occurrence_count": 1,
                        "status": "UNDER_ACTIVE_RESEARCH"
                    }
                    status = f"🌟 [NEW DISCOVERY]: Registered code for global research."
               
                new_flags.append(f"Pos {index} ('{token}'): {status}")

        if new_flags:
            return f"🔬 [MALIKLANG LIVE RESEARCH REPORT]:\n--> " + "\n--> ".join(new_flags)
        return "✅ [DISCOVERY SYSTEM]: Base genome matches stable templates."

# लोकल रिसर्च टेस्ट रन
if __name__ == "__main__":
    engine = MutationDiscoveryEngine()
   
    # टेस्ट 1: मरीज 1 के शरीर में 'GGCT' नाम का नया पैटर्न मिला (पहली बार खोज)
    print("🏥 [PATIENT 01 SCAN]")
    print(engine.analyze_and_learn(['ATCG', 'GGCT', 'AAAA'], "PATIENT_01"))
   
    # टेस्ट 2: मरीज 2 के शरीर में दोबारा वही 'GGCT' पैटर्न मिला (सिस्टम को पहले से याद है)
    print("\n🏥 [PATIENT 02 SCAN]")
    print(engine.analyze_and_learn(['TTTT', 'GGCT', 'CCCC'], "PATIENT_02"))
 
