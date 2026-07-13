import joblib
import argparse
import glob
import pandas as pd

FEATURE = ['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']

scaler = joblib.load(r"models\scaler.pkl")
imputer = joblib.load(r"models\imputer.pkl")
model = joblib.load(r"models\RF.pkl")

parser = argparse.ArgumentParser(
    prog= "app.py",
    description= "ONCFM - Détecteur de faux billets"
)
parser.add_argument(
        '--values', 
        type=float, 
        nargs=6,
        metavar=('diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length'),
        help='6 valeurs géométriques du billet'
)

args = parser.parse_args()

if args.values:
    df = pd.DataFrame(
        [args.values], 
        columns=['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']
    )
else:
    # chercher dans data/fresh/
    fichiers = glob.glob(r"data\fresh\*.csv")
    if len(fichiers) == 1:
        df = pd.read_csv(fichiers[0], sep=None, engine='python')
    elif len(fichiers) == 0:
        raise FileNotFoundError("Aucun fichier CSV trouvé dans data/fresh/")
    else:
        raise ValueError(f"{len(fichiers)} fichiers trouvés dans data/fresh/, laissez-en un seul.")

df = df[FEATURE]

X = scaler.transform(df)
X = imputer.transform(X)
X = pd.DataFrame(X, columns=FEATURE)
predictions = model.predict(X)

print("\n" + "="*50)
print("   ONCFM - Résultats de l'analyse")
print("="*50)

for i, pred in enumerate(predictions):
    statut = "FAUX BILLET ⚠️" if pred else "Vrai billet ✅"
    print(f"  Billet {i+1:>3} | {statut}")

print("="*50)
print(f"  Total analysés : {len(predictions)}")
print(f"  Faux détectés  : {sum(predictions)}")
print(f"  Vrais          : {sum(~predictions)}")
print("="*50 + "\n")