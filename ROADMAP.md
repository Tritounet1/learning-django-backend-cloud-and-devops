# 🚀 Roadmap Développeur Backend / Cloud

> Bac +3 Informatique — Objectif : CDI Développeur Backend / Cloud

---

## ☁️ Quel Cloud choisir ?

**AWS est le leader en France** (et globalement), suivi de Microsoft Azure puis Google Cloud Platform (GCP).

| Cloud     | Popularité                   | Contexte typique                             |
| --------- | ---------------------------- | -------------------------------------------- |
| **AWS**   | ⭐ Le plus demandé           | Startups, scale-ups, grands groupes          |
| **Azure** | ⭐⭐ Très fort en entreprise | Grandes entreprises, banques, secteur public |
| **GCP**   | Moins présent                | Boîtes tech orientées data/ML                |

> 💡 **Conseil : continue sur AWS.** Les fondamentaux cloud (VPC, IAM, serverless, containers) se transfèrent facilement d'un provider à l'autre.

---

## 🗺️ La Roadmap

Organisée en **4 niveaux de priorité**, du plus urgent au plus différenciant.

---

## 🔴 Niveau 1 — Les fondamentaux incontournables

### Langage backend principal

- [ ] Maîtriser un langage sérieusement : **Python** (le plus polyvalent) ou **Java/Kotlin** ou **Go** (très demandé en cloud-native)
- [ ] POO avancée, design patterns (Factory, Singleton, Repository, Strategy)
- [ ] Gestion des erreurs, logging, tests unitaires

### APIs REST

- [ ] Concevoir et implémenter une API REST propre (verbes HTTP, codes de statut, pagination, versionning)
- [ ] Framework associé : FastAPI / Django (Python), Spring Boot (Java), Gin/Echo (Go)
- [ ] Authentification : JWT, OAuth2, sessions
- [ ] Documentation : OpenAPI / Swagger

### Bases de données

- [ ] SQL avancé : jointures, index, transactions, EXPLAIN/ANALYZE
- [ ] PostgreSQL en particulier (le plus utilisé en prod)
- [ ] Notions de NoSQL : MongoDB ou DynamoDB (AWS)
- [ ] ORM : SQLAlchemy (Python), Hibernate (Java)
- [ ] Migrations de schéma (Alembic, Flyway, Liquibase)

### Git & bonnes pratiques

- [ ] Git flow, branches, rebase vs merge, gestion des conflits
- [ ] Écrire de bons commits (conventional commits)
- [ ] Pull requests, code review

---

## 🟠 Niveau 2 — Le cœur du métier cloud/backend

> ⏱️ Durée estimée : 4-6 mois | Ce qui te différencie d'un dev web classique

### Docker & Containers

- [ ] Dockerfile, build d'images, multi-stage builds
- [ ] Docker Compose pour le dev local
- [ ] Notions de registry (ECR sur AWS, Docker Hub)

### Kubernetes (K8s) — notions solides

- [ ] Pods, Deployments, Services, Ingress, ConfigMaps, Secrets
- [ ] Helm (gestionnaire de packages K8s)
- [ ] ℹ️ Tu n'as pas besoin d'être expert K8s dès le départ, mais les bases sont très attendues

### AWS — aller au-delà du basique

- [ ] **Compute** : EC2, Lambda (serverless), ECS/EKS (containers)
- [ ] **Storage** : S3 (en profondeur), EBS, EFS
- [ ] **Réseau** : VPC, subnets, security groups, Route 53, CloudFront
- [ ] **IAM** : rôles, policies, principe du moindre privilège — _c'est crucial_
- [ ] **Messaging** : SQS, SNS, EventBridge
- [ ] **BDD managées** : RDS (PostgreSQL), DynamoDB
- [ ] **Monitoring** : CloudWatch, alertes, dashboards

### Infrastructure as Code (IaC)

- [ ] **Terraform** → standard de l'industrie, **priorité absolue**
- [ ] Notions de AWS CDK ou CloudFormation _(bonus)_

### CI/CD

- [ ] GitHub Actions (le plus accessible pour commencer)
- [ ] Concepts : pipeline, stages, artefacts, déploiement automatisé
- [ ] GitLab CI _(bonus — très utilisé en France en entreprise)_

---

## 🟡 Niveau 3 — Ce qui fait un bon candidat "senior junior"

> ⏱️ À travailler en parallèle des niveaux précédents

### Architecture & conception

- [ ] Architecture microservices vs monolithe (et leurs trade-offs)
- [ ] Event-driven architecture, queues de messages (RabbitMQ, Kafka en notions)
- [ ] API Gateway pattern, BFF (Backend For Frontend)
- [ ] 12-factor app methodology

### Sécurité applicative

- [ ] OWASP Top 10 (injection SQL, XSS, CSRF…)
- [ ] Secrets management : AWS Secrets Manager, HashiCorp Vault _(notions)_
- [ ] HTTPS, TLS, certificats
- [ ] Principe du moindre privilège partout

### Observabilité

- [ ] Les 3 piliers : **logs**, **métriques**, **traces**
- [ ] Stack type : Prometheus + Grafana, ou Datadog, ou ELK
- [ ] Structurer ses logs (JSON, correlation IDs)

### Tests

- [ ] Tests unitaires, tests d'intégration, tests de contrat
- [ ] TDD _(notions)_

---

## 🟢 Niveau 4 — Les plus qui font la différence

> ⏱️ À construire dans le temps, tout au long de ta progression

- [ ] **Certification AWS** : commence par **AWS Cloud Practitioner** (~60€), puis vise **AWS Solutions Architect Associate** (très reconnu)
- [ ] Linux / Bash : commandes de base, scripting, cron, systemd
- [ ] Kafka : messagerie event-driven à grande échelle
- [ ] GraphQL : alternative aux REST APIs
- [ ] Notions de FinOps : comprendre et optimiser les coûts cloud
- [ ] Contribuer à un projet open-source _(même petit)_

---

## 📅 Planning suggéré sur 6-9 mois

| Période    | Focus                                                   |
| ---------- | ------------------------------------------------------- |
| Mois 1-2   | Consolider le langage principal + API REST + PostgreSQL |
| Mois 2-3   | Docker + Git avancé + déployer un vrai projet sur AWS   |
| Mois 4-5   | Terraform + CI/CD + Kubernetes basics                   |
| Mois 5-6   | Architecture, sécurité, observabilité                   |
| En continu | Projets perso, préparer la certif AWS                   |

---

## 💡 Conseil clé : le projet perso est roi

> Construis **1 projet de bout en bout** que tu peux montrer en entretien.

Un bon projet à viser :

- Une **API REST** déployée sur AWS
- Avec une **pipeline CI/CD** automatisée
- De l'**IaC Terraform** pour provisionner l'infra
- Du **monitoring** (logs + métriques)
- Un **README** propre qui explique les choix techniques

Ça vaut bien plus qu'une liste de technos sur un CV. 🎯

---

_Roadmap générée pour un profil Bac +3 Informatique visant un CDI Backend / Cloud — Focus AWS_ (généré par CLAUDE)
