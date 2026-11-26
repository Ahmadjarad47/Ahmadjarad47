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

### ⭐ IPM: Internal Project Management Platform · Full-Stack Developer
**Open source** · [ipm-backend](https://github.com/Ahmadjarad47/ipm-backend) (.NET 10) · [ipm-web](https://github.com/Ahmadjarad47/ipm-web) (Angular 22) · MIT

**The idea.** Organisations run projects across chat threads, spreadsheets and tools that each force a fixed process. IPM is one **single source of truth** for projects, tasks, owners and **approval decisions**. Every change records who made it, when, and who approved it, and the system never hard-codes a workflow or status name. Admins define their own work-item types, fields, statuses, transitions, approval chains and roles from the UI. It is an Arabic-first, self-hosted alternative in the spirit of OpenProject and Jira, built around governance and auditability.

**What it does**
| Area | What I built |
|---|---|
| 🧩 **Flexible work model** | Admin-defined work-item types (Feature, Task, Bug…) with custom fields, parent/child hierarchy and cross-type dependencies; cycle detection; board, list and tree views; bulk edit; project templates. |
| 🔄 **Configurable workflows** | Statuses and transitions per type and per project, guarded by permissions, open dependencies and pending approvals. |
| ✅ **Hierarchical approvals engine** | Sequential multi-stage approvals chosen by rules (project, type, stage); self-approval ban; delegation; admin override with a reason; requests become invalid when a protected field changes; sensitive edits go through approval and are applied atomically. |
| 🔐 **Dynamic permissions** | Around 45 permission keys at system and project scope, default-deny with explicit denies, privilege-escalation guards, JWT + refresh-token rotation, lockout and rate limiting. |
| 🔗 **Git integration** | Connect GitHub, GitLab or Gitea repositories; HMAC-signed webhooks with replay protection and de-duplication; commits and PRs mentioning `PROJ-123` link to the work item automatically. |
| 🧾 **Tamper-evident audit** | Hash-chained audit log that can be verified and exported, plus human-readable activity feeds on every entity. |
| 🔔 **Real-time notifications** | SignalR push in the browser, plus Telegram notifications delivered by a transactional outbox worker with retries and rate limits. |
| 📊 **Insight** | KPI dashboard, project timeline, global search and Excel work reports. |

**Engineering**
- **Backend:** .NET 10 · Clean Architecture · CQRS (source-generated Mediator) · EF Core + PostgreSQL 17 · Redis · SignalR · FluentValidation · Serilog + Seq · Scalar/OpenAPI. **130+ REST endpoints** (76 commands, 57 queries), Arabic problem+json errors, ETag/If-Match optimistic concurrency.
- **Frontend:** Angular 22 with standalone components, signals, zoneless change detection and `OnPush` everywhere; generic typed REST client and list/lookup stores; fully RTL, keyboard-accessible with contrast checks.
- **Quality:** **400+ backend tests** (domain, architecture rules, integration tests on real PostgreSQL and Redis through Testcontainers, SignalR) and **170+ frontend tests**, including SRS acceptance rules and an API-contract guard. Every requirement is traced to its tests.
- **Process:** built from a formal SRS (`IPM-SRS-001`) in 12 modules, each delivered spec → domain → storage → application → API. Shipped with Docker, nginx and HTTPS.

### ⭐ Itqan (إتقان): Manufacturing Planning Platform · Full-Stack Developer *(in active development)*
**Open source** · [itqan-backend](https://github.com/Ahmadjarad47/itqan-backend) (.NET 10) · [itqan-web](https://github.com/Ahmadjarad47/itqan-web) (Angular 22) · MIT

**The idea.** A manufacturer building a complex product has to answer the same questions for thousands of parts: *what is it made of, what does it cost, do we make it or buy it, who supplies it, when is it produced, and is it in stock?* Usually those answers sit in separate spreadsheets that never agree. Itqan ("mastery and precision in craft") connects them all through one **product tree (BOM)**, **from product tree to finished product**.

| Stage | What I built |
|---|---|
| 🌳 **Engineer** | Unlimited-depth product tree per project with drill-down explorer and org-chart diagram; drawings, quality files and materials on every part; tree cloning between projects and versions. |
| 💰 **Cost** | Live bottom-up cost roll-up through the whole tree. |
| ⚖️ **Decide** | Mandatory **MAKE / BUY** decision per part, supported by multi-criteria scoring (MCDM). |
| 🛒 **Buy** | 10-stage purchasing workflow: requests, RFQs, quotes, supplier comparison and receipt into the warehouse. |
| 🏭 **Make** | Production routing (operations, stations, setup and run times, consumables, quality and returns) with a filterable Gantt chart. |
| 📦 **Store** | Warehouses, requisitions, stock movements, FIFO costing and warehouse reports. |
| ✅ **Track** | Manager and employee task screens with chat, roles and permissions, and admin-defined custom fields on every entity. |

- **Backend:** .NET 10 · Clean Architecture · CQRS (source-generated Mediator) · PostgreSQL · Redis · JWT with refresh-token rotation · Arabic problem+json errors · ETag concurrency · audit log · architecture tests · Docker Compose + Caddy. 140+ endpoints across 8 modules, built spec → domain → storage → application → API.
- **Frontend:** Angular 22 (signals, zoneless) with Clean Architecture (domain / application / infrastructure ports), signal stores, light/dark design tokens, fully RTL; runs on its own with seeded demo data.

## 🔐 Secure Distributed System (graduation project)

Designed and deployed a working prototype across **two VPS servers** with regional data isolation: WireGuard tunnels, authenticated relay services, AES-256 / ChaCha20-Poly1305 encryption, digital signatures, replay protection, and a secure file pipeline with ClamAV scanning.

## 🚀 Open-Source Repositories

| Repository | Description |
|---|---|
| [algobytes-architecture](https://github.com/Ahmadjarad47/algobytes-architecture) | .NET + Angular starter: auth/OTP, RBAC + ABAC policies, dynamic custom fields, audit logs, health probes |
| ⭐ [ipm-backend](https://github.com/Ahmadjarad47/ipm-backend) | **IPM API:** self-hosted project-management platform with configurable workflows, a hierarchical approvals engine, dynamic permissions, Git integration and a tamper-evident audit log. .NET 10, CQRS, PostgreSQL, Redis, SignalR, 130+ endpoints, 400+ tests |
| ⭐ [itqan-backend](https://github.com/Ahmadjarad47/itqan-backend) | **Itqan API:** manufacturing planning platform covering BOM tree, live cost roll-up, make-or-buy (MCDM), 10-stage procurement, production routing, warehouses with FIFO costing, and tasks. .NET 10, CQRS, PostgreSQL, Redis |
| ⭐ [itqan-web](https://github.com/Ahmadjarad47/itqan-web) | **Itqan web app:** Arabic-first RTL Angular 22 client with product-tree explorer, cost roll-up, procurement tracker, Gantt production plan and warehouse screens |
| ⭐ [ipm-web](https://github.com/Ahmadjarad47/ipm-web) | **IPM web app:** Arabic-first RTL client in Angular 22 (signals, zoneless): boards, work-item trees, approvals inbox, admin-configurable types/workflows/roles, real-time notifications |

## 🎓 Education & Content

- B.Sc. Computer Science — University of Al-Ettihad, Syria (2021–2025)
- Creator of **[Algorithm Bytes](https://youtube.com/@algorithmbytes)**: Arabic tutorials on .NET, Angular, algorithms, secure coding and cybersecurity fundamentals.
