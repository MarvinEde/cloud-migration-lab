import os 
import sys


#je fais une liste des extensions ou fichiers sensibles (cle,mdp, ect)
FORBIDDEN_EXTENSIONS = ['.key', '.pem', '.p12', '.pfx', '.crt', '.csr', '.ovpn', '.conf', '.cfg', '.ini', '.log', '.bak', '.backup']
FORBIDDEN_KEYWORDS = ['PASSWORD=', 'SECRET_KEY=', 'PRIVATE_KEY=']

def scan_repository():
    print("--- Audit de sécurité en cours ---")
    issues_found = 0

    # Parcours de tous les fichiers du projet
    for root, dirs, files in os.walk('.'):
        if ".git" in root:
            continue  # Ignorer le dossier .git

        for file in files:
            file_path = os.path.join(root, file)

            if file == "scanner.py":
                continue  # Ignorer le script de scan lui-même

            _, ext = os.path.splitext(file)

            # Vérification des extensions interdites
            if ext in FORBIDDEN_EXTENSIONS:
                print(f"[ALERTE] Fichier sensible trouvé : {file_path}")
                issues_found += 1

            # Vérification des mots-clés interdits
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()
                for keyword in FORBIDDEN_KEYWORDS:
                    if keyword in content:
                        print(f"[ALERTE] Mot-clé sensible trouvé dans {file_path} : {keyword}")
                        issues_found += 1

    if issues_found == 0:
        print("--- Audit terminé. Aucun problème de sécurité trouvé. ---")
        return True
    else:
        print(f"--- Audit terminé. {issues_found} problème(s) trouvé(s). ---")
        return False
    
if __name__ == "__main__":
    is_safe = scan_repository()
    
    if not is_safe:
        print("BUILD REJETEE : Des problèmes de sécurité ont été détectés.")
        sys.exit(1)  # Sortie avec code d'erreur pour indiquer l'échec du build
    else:
        print("BUILD ACCEPTÉE : Aucun problème de sécurité détecté.")
        sys.exit(0)  # Sortie avec code de succès pour indiquer que le build peut continuer