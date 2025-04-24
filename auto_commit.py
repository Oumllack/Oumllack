#!/usr/bin/env python3
import os
from datetime import datetime
import random
import string

def update_readme():
    # Chemin vers le README.md
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    
    # Lire le contenu actuel
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Générer un caractère aléatoire
    random_char = random.choice(string.ascii_letters + string.digits)
    
    # Ajouter une ligne invisible avec la date et un caractère aléatoire
    current_date = datetime.now().strftime("%Y-%m-%d")
    invisible_line = f"<!-- Last updated: {current_date} - {random_char} -->\n"
    
    # Si une ligne similaire existe déjà, la remplacer
    if "<!-- Last updated:" in content:
        lines = content.split('\n')
        new_lines = [line for line in lines if not line.startswith("<!-- Last updated:")]
        content = '\n'.join(new_lines)
    
    # Ajouter la nouvelle ligne au début du fichier
    new_content = invisible_line + content
    
    # Sauvegarder les modifications
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def git_commit():
    # Se déplacer dans le répertoire du script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Configurer les commandes git
    os.system('git add README.md')
    commit_date = datetime.now().strftime("%Y-%m-%d")
    os.system(f'git commit -m "Mise à jour automatique du README - {commit_date}"')
    os.system('git push')

if __name__ == "__main__":
    update_readme()
    git_commit() 