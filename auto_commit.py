#!/usr/bin/env python3
import os
from datetime import datetime
import random
import string

def get_today_date():
    return datetime.now().strftime("%a %b %d %Y")

def get_days_before_new_year():
    today = datetime.now()
    next_year = today.year + 1
    new_year = datetime(next_year, 1, 1)
    days_left = (new_year - today).days
    return f"**{days_left} days before {next_year} ⏱**"

def get_bot_signing():
    moods = {
        0: "passion",
        1: "determination",
        2: "creativity",
        3: "innovation",
        4: "excellence",
        5: "expertise",
        6: "excellence"
    }
    mood = moods[datetime.now().weekday()]
    return f"🤖 This README is updated with {mood}, by Oumllack ❤️"

def update_readme():
    readme_content = f"""<h1 align="center">Hello <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="40"></h1>

### About Me 👋

I am an Implementation Engineer passionate about Deep Learning, MLOps, and DevOps. I specialize in building and deploying machine learning models at scale, with a focus on automation and best practices in production environments.

### 🛠 &nbsp;Languages and Tools :

<p>
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/tensorflow/tensorflow-original.svg" title="TensorFlow" alt="TensorFlow" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/pytorch/pytorch-original.svg" title="PyTorch" alt="PyTorch" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/kubernetes/kubernetes-plain.svg" title="Kubernetes" alt="Kubernetes" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/amazonwebservices/amazonwebservices-original.svg" title="AWS" alt="AWS" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original.svg" title="Git" alt="Git" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/terraform/terraform-original.svg" title="Terraform" alt="Terraform" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/jupyter/jupyter-original.svg" title="Jupyter" alt="Jupyter" width="40" height="40"/>&nbsp;
</p>

---

### 🔥 &nbsp; My Stats :

[![GitHub Streak](https://streak-stats.demolab.com?user=Oumllack&theme=dark&hide_border=true&card_width=500)](https://git.io/streak-stats)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Oumllack&hide=html&layout=compact&theme=vision-friendly-dark)](https://github.com/anuraghazra/github-readme-stats)

---

### Visitor Count

<img src="https://profile-counter.glitch.me/Oumllack/count.svg" />

Last updated: {get_today_date()}

{get_days_before_new_year()}

{get_bot_signing()}
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)

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