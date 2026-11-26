# Hi, I'm Ahmad Jarad 👋

**Freelance Full-Stack Developer** — .NET · Angular · Secure Systems
📍 Damascus, Syria · 🗣 Arabic · English · German

Freelance developer since 2022. I deliver production web platforms end to end: requirements, architecture, backend APIs, Angular interfaces, real-time features, security, CI/CD and VPS deployment.

📄 [**Download my CV**](docs/Ahmad_Jarad_CV.pdf) · 💼 [**Software Portfolio**](docs/Ahmad_Jarad_Portfolio.pdf) · ▶️ [YouTube: Algorithm Bytes](https://youtube.com/@algorithmbytes) · ✉️ [ahmad222jarad@gmail.com](mailto:ahmad222jarad@gmail.com)

## 🛠 Tech Stack

![C#](https://img.shields.io/badge/C%23-239120?style=flat&logo=csharp&logoColor=white)
![.NET](https://img.shields.io/badge/ASP.NET_Core-512BD4?style=flat&logo=dotnet&logoColor=white)
![Angular](https://img.shields.io/badge/Angular-DD0031?style=flat&logo=angular&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=flat&logo=microsoftsqlserver&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=flat&logo=rabbitmq&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white)
![Linux](https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-2088FF?style=flat&logo=githubactions&logoColor=white)

**Architecture:** Clean Architecture · DDD · CQRS · Modular Monolith · Microservices
**Real-time & messaging:** SignalR · gRPC · RabbitMQ
**Security:** JWT · RBAC · OWASP Top 10 · rate limiting · audit logging · encryption · WireGuard · ClamAV

## 🏢 Client Projects

| Project | Role | Highlights |
|---|---|---|
| [Syrian Medical CRM](https://syrian-medical.tech) · [code](https://github.com/Ahmadjarad47/CRM.Medical) | Backend Developer | Production medical lab platform: API/Application/Domain/Infrastructure/RealTime layers, auth, caching, chat, notifications, CI/CD to VPS |
| [Aljawhara Plus](https://aljawharaplus.com) | Full-Stack & UI Designer | Kuwaiti e-commerce platform: modular monolith, Redis caching, real-time chat, Hostinger VPS |
| [Mazad Syria](https://syriamazad.com) | Full-Stack Developer | Auction platform: real-time updates, concurrency-aware bidding rules, rate limiting |
| [AOM Engineering](https://aom-engineering.de) | Full-Stack Developer | DDD-based corporate platform with Redis performance work and hardened deployment |

## 💼 Recent Work (2026)

### IPM: Internal Project Management System · Full-Stack Developer · [backend](https://github.com/Ahmadjarad47/ipm-backend) · [frontend](https://github.com/Ahmadjarad47/ipm-web)
Open-source project-management platform built module by module from a formal SRS.
- **Backend (.NET 10):** Clean Architecture + CQRS (Mediator), EF Core/PostgreSQL 17, Redis, SignalR, Serilog + Seq, OpenAPI (Scalar).
- **Features:** JWT + refresh tokens with default-deny permissions at system and project scope · hierarchical work items with cycle-safe relations, custom fields and configurable workflows · sequential approvals engine (delegation, self-approval ban, transition gating) · Git integration with HMAC-signed webhooks for GitHub/GitLab/Gitea · tamper-evident hash-chained audit log · real-time and Telegram notifications through an outbox worker · dashboard, global search and Excel reports.
- **Frontend (Angular 22):** Arabic RTL, standalone components, signals, zoneless, generic REST/list/lookup stores, optimistic concurrency (ETag), accessibility checks.
- **Quality:** domain unit tests, architecture tests, integration tests on real PostgreSQL/Redis (Testcontainers), requirements-to-tests traceability. Shipped with Docker + nginx.

### ERP101: Industrial Manufacturing ERP · Full-Stack Developer *(in development)*
ERP for industrial manufacturing, from engineering through production.
- **Features:** visual bill-of-materials tree with cost roll-up · make-or-buy decisions (MCDM) · 10-stage purchasing workflow with RFQs and suppliers · warehouses and stock movements (FIFO) · production routing with Gantt scheduling · task tracking · roles and permissions.
- **Backend:** .NET 10 Clean Architecture, CQRS (source-generated Mediator), PostgreSQL, Redis, JWT, Arabic problem+json errors, ETag concurrency, audit log, architecture tests, Docker Compose + Caddy deployment.
- **Frontend:** Angular 22 with Clean Architecture (domain / application / infrastructure), signal stores, light/dark design tokens, RTL.

## 🔐 Secure Distributed System (graduation project)

Designed and deployed a working prototype across **two VPS servers** with regional data isolation: WireGuard tunnels, authenticated relay services, AES-256 / ChaCha20-Poly1305 encryption, digital signatures, replay protection, and a secure file pipeline with ClamAV scanning.

## 🚀 Open-Source Repositories

| Repository | Description |
|---|---|
| [algobytes-architecture](https://github.com/Ahmadjarad47/algobytes-architecture) | .NET + Angular starter: auth/OTP, RBAC + ABAC policies, dynamic custom fields, audit logs, health probes |
| [ipm-backend](https://github.com/Ahmadjarad47/ipm-backend) | Project-management API on .NET 10: Clean Architecture, CQRS, PostgreSQL, Redis, SignalR, approvals engine, Git webhooks, hash-chained audit log, Testcontainers integration tests |
| [ipm-web](https://github.com/Ahmadjarad47/ipm-web) | Angular 22 Arabic-first RTL client for IPM: signals, zoneless, server-driven workflows, real-time notifications, SRS-traced tests |

## 🎓 Education & Content

- B.Sc. Computer Science — University of Al-Ettihad, Syria (2021–2025)
- Creator of **[Algorithm Bytes](https://youtube.com/@algorithmbytes)**: Arabic tutorials on .NET, Angular, algorithms, secure coding and cybersecurity fundamentals.
