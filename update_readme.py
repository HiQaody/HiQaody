import requests
from datetime import datetime

def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"📜 _\"{data['content']}\"_ — **{data['author']}**"
    except Exception as e:
        return "📝 Quote service unavailable."
    return "📝 No quote today."

def generate_readme_content():
    today = datetime.now().strftime("%A %d %B %Y")
    quote = get_random_quote()

    return f"""\
# 👋 Bienvenue sur HiQaody 👨‍💻

Salut ! Je suis **Jacquinot Randrianomenjanahary**, un **développeur full-stack et expert DevOps** passionné par la création de solutions modernes et performantes. Avec une solide expérience en développement web, mobile et DevOps, je transforme vos idées en applications robustes et scalables.

---

**🗓️ Mise à jour automatique :** _{today}_  
{quote}

---

## 🚀 À propos de moi

- 💻 **Compétences principales :**
  - **Backend :** Java (Spring Boot), PHP (Laravel, CodeIgniter), Node.js
  - **Frontend :** ReactJS, NextJS, VueJS
  - **DevOps :** Docker, Kubernetes, Jenkins, CI/CD, GitHub Actions
  - **Bases de données :** PostgreSQL, MySQL, SQLite, SQL Server
  - **Mobile :** Flutter (Android & iOS)
  - **Langages :** Java, PHP, JavaScript, TypeScript, Python, Dart, C#

- 🌱 Actuellement, je m'intéresse à :  
  - L'intégration de **GraphQL** dans mes projets.  
  - L'amélioration des pipelines **CI/CD** pour le déploiement automatisé.

- 🌍 Disponible pour :
  - **Freelance** ou collaborations sur des projets innovants.  
  - Opportunités dans des entreprises technologiques ambitieuses.

---

## 📌 Projets Réalisés

### 📚 **Bibliothèque Numérique - EMIT**
- **Description :** Une application en architecture microservices pour la gestion de livres.
- **Technologies :** Spring Boot, NextJS, Docker, Jenkins, PostgreSQL.
- **Résultat :** Une solution robuste capable de gérer des milliers d'utilisateurs simultanément.

### 🖨️ **Génération de QR Codes**
- **Description :** Automatisation de la génération de QR Codes pour des attestations administratives.
- **Technologies :** Python.
- **Impact :** Réduction de 70% du temps de traitement des documents.

### 📱 **Application Mobile "Torohay"**
- **Description :** Application éducative pour apprendre une langue locale.
- **Technologies :** Flutter, SQLite.
- **Résultat :** Une adoption réussie dans plusieurs régions.

*Découvrez plus de projets dans [mon portfolio](https://jacquinot-randria.vercel.app).*

---

## ✨ Pourquoi travailler avec moi ?

1. **Expertise technique avérée :** Maîtrise des frameworks modernes pour le web et le mobile.
2. **Approche orientée résultats :** Focus sur des solutions performantes et maintenables.
3. **Adaptabilité :** Capacité à collaborer en équipe ou en freelance selon vos besoins.

---

## 📫 Contactez-moi

- **E-mail :** [hiqaody@gmail.com](mailto:hiqaody@gmail.com)  
- **LinkedIn :** [Jacquinot Randrianomenjanahary](https://www.linkedin.com/in/jacquinotrandrianomenjanahary)  
- **GitHub :** [@HiQaody](https://github.com/HiQaody)  
- **Portfolio :** [hiqaody.vercel.com](https://jacquinot-randria.vercel.app)  

---

_Automatically updated with Python 🐍 & GitHub Actions._

"""

def write_readme(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    readme = generate_readme_content()
    write_readme(readme)
