import pandas as pd

# Step 1: Sample Data (simulating lexical analysis logs)
data = {
    'Filename': ['main.py', 'parser.py', 'lexer.py', 'utils.py', 'scanner.py'],
    'Token_Count': [120, 200, 80, 150, 60],
    'Line_Count':  [30,  25,  40, 20,  50]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Feature Computation — Token Density
df['Token_Density'] = df['Token_Count'] / df['Line_Count']

# Step 4: Flag Generation — Is_Token_Heavy
THRESHOLD = 5.0
df['Is_Token_Heavy'] = df['Token_Density'].apply(lambda x: 'YES' if x > THRESHOLD else 'NO')

# Step 5: Display Output
print("=" * 65)
print("       LEXICAL ANALYSIS — TOKEN DENSITY INDICATOR")
print("=" * 65)
print(df.to_string(index=False))
print("=" * 65)
print(f"\nThreshold Used : {THRESHOLD} tokens/line")
print(f"Heavy Files    : {df[df['Is_Token_Heavy'] == 'YES']['Filename'].tolist()}")
print(f"Safe Files     : {df[df['Is_Token_Heavy'] == 'NO']['Filename'].tolist()}")