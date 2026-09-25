# Maliklang V2.0.0 - Core DNA Lexer Layer
# Author: Shailendra Kumar Singh

class DNALexer:
    def __init__(self, sequence: str):
        # इंसानी DNA के 4 वैध बेस टोकन्स (Valid Base Tokens)
        self.valid_bases = {'A', 'T', 'C', 'G'}
        # इनपुट सीक्वेंस को क्लीन करना (spaces या नई लाइन हटाना)
        self.sequence = sequence.upper().replace(" ", "").replace("\n", "")

    def tokenize(self, block_size: int = 4):
        """
        DNA श्रृंखला को निर्धारित साइज (Default: 4) के ब्लॉक्स में तोड़ना
        और अमान्य (Invalid) टोकन्स को फ़िल्टर करना।
        """
        tokens = []
        for i in range(0, len(self.sequence), block_size):
            block = self.sequence[i:i+block_size]
           
            # यदि ब्लॉक पूरा है (जैसे 4 अक्षर का) और सारे अक्षर वैध हैं
            if len(block) == block_size and all(base in self.valid_bases for base in block):
                tokens.append(block)
            else:
                # यदि कोई अमान्य अक्षर (जैसे X या Z) आ जाए, तो उसे स्किप या फ्लैग करें
                continue
               
        return tokens

# टेस्ट रन (टैबलेट पर चेक करने के लिए)
if __name__ == "__main__":
    test_dna = "ATCGATTGCTAGCTAGCTAG"
    lexer = DNALexer(test_dna)
    print("🔬 Maliklang V2.0.0 Generated DNA Tokens:", lexer.tokenize())
 
