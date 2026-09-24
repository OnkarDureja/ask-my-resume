# Onkar Dureja — Portfolio Data

This file is the only source of truth for the assistant. Never answer from outside this file. If something is not covered here, say so directly instead of guessing.

## Basic Info

- Name: Onkar Dureja
- Location: Dadri, Uttar Pradesh, India
- Email: onkardureja02@gmail.com
- Phone: +91 7678651460
- LinkedIn and GitHub: linked from the portfolio site (see links in the app)

## Education

- Galgotias University, Greater Noida, Uttar Pradesh — Aug 2023 to Jul 2027
- B.Tech in Computer Science and Engineering, Specialization: Artificial Intelligence & Machine Learning
- CGPA: 8.6 / 10.0

## Technical Skills

- Languages: Java, Swift, Python, SQL
- CS Fundamentals: Data Structures & Algorithms, Object-Oriented Programming, DBMS, Operating Systems
- AI & LLM Engineering: LLM APIs (Groq, Gemini, OpenAI-compatible), Prompt Engineering, Structured JSON Output Design, Schema Validation with Pydantic, Document Parsing (PDF/DOCX), Streamlit, AI-Assisted Development using Claude
- iOS Development: SwiftUI, MVVM, Swift Concurrency (async/await), MapKit
- Backend & Databases: Supabase (PostgreSQL, Auth, Storage, Edge Functions), Relational Database Design, REST APIs
- Tools & Practices: Git, GitHub, Xcode, VS Code, uv, Jira, Figma, Agile/Scrum, Requirement Analysis (SRS), Sprint Planning, Technical Documentation, Team Leadership

## Work Experience

### Aarogya Virohan Pvt. Ltd. — Technical Team Lead (Remote Internship)
Jun 2026 – Present

- Owns technical execution for a multi-tenant SaaS platform serving physiotherapy clinics, working with the founding team to translate clinical workflows into product requirements
- Authors module-level requirement specifications covering scope, data model, and acceptance criteria; acts as the single point of clarification for the development team
- Manages backend and frontend developers on weekly sprint cycles and owns release readiness
- Shipped: clinical assessment tools, a patient-facing prescription module, and a spreadsheet-to-database CRM migration

### Infosys — iOS Developer Intern
May 2026 – Jun 2026, Mysuru, Karnataka

- Built a Fleet Management System iOS application for a multi-country retail chain using SwiftUI and an MVVM architecture with Swift Concurrency
- Elected Scrum Master; team finished top 3 of 10
- Engineered a real-time crash detection module with haptic feedback alerts and integrated voice-based logging in the driver section, enabling hands-free incident reporting and instant driver status capture
- Developed a contextual recommendation engine across the vehicle and driver management modules, surfacing prioritized operational insights to streamline fleet coordinator decision-making

## Projects

### HireLens — AI Resume Screening Tool
Stack: Python, Streamlit, Groq LLM API, Pydantic

- A resume screening application where a recruiter pastes a job description, uploads multiple PDF or DOCX resumes, and receives ranked candidates with matched skills, missing skills, and a fit verdict
- Designed the LLM layer around strict Pydantic schemas so every response returns typed, validated fields instead of free-form text
- Tuned the scoring prompt to evaluate candidates on evidence from the resume rather than counting job-description keywords
- Separated the evaluation logic from the Streamlit interface so scoring can be imported and tested independently of the UI
- Handled unreadable files gracefully so a single bad upload never fails the batch
- Deployed publicly on Streamlit Community Cloud; dependencies managed with uv; maintained as a public repository

### Vyom — Astronomy & Sky-Events iOS App
Stack: SwiftUI, Supabase, SwiftAA, MVVM
Status: TestFlight Beta, built with a 4-person team

- Helps stargazers plan and track sky events (eclipses, meteor showers, planetary conjunctions, moon phases) with per-location visibility scoring
- Implemented interactive SwiftUI event visualizers with real-time sky simulation
- Integrated Sign in with Apple using Supabase Auth (nonce/SHA-256), plus photo upload and account management via Storage and Edge Functions
- Backend: Supabase (PostgreSQL) with SwiftAA astronomical calculations
- Managed a shared multi-developer codebase on GitHub

### Attune — Emotional Presence & Support App
Stack: SwiftUI, iOS

- A SwiftUI iOS app designed to support emotional regulation during anxiety episodes
- Features a scenario-driven Practice Mode that walks the user through grounding scenarios
- Uses state-driven breathing animations to guide the user through breathing exercises
- Built with accessibility-first design: VoiceOver support, Dynamic Type, and reduced-motion compliance
- This is a personal/solo project exploring SwiftUI animation and accessibility patterns rather than a team production build

### AskCV — Conversational Resume Assistant (this application)
Stack: Python, Streamlit, Groq LLM API, Pydantic

- A chat interface that lets recruiters ask questions about Onkar's background and get answers grounded only in verified portfolio data
- Includes a JD-matching feature: a recruiter pastes a job description and the assistant scores Onkar's resume against it, highlighting matched skills, missing skills, and a fit verdict
- Built as the second project in an AI Engineer course, focused on prompt engineering and structured/streaming LLM output without RAG or a vector database, since the portfolio data is small enough to fit directly in the system prompt

## Programs & Recognition

- Selected for the iOS Student Developer Program (top 100 in the university); led a 4-person team building an iOS application

## Answering Rules for the Assistant

- Only answer using the information in this file
- If asked about something not covered here (a technology, a project, an experience), say plainly that this isn't something in Onkar's current portfolio data, rather than guessing or inferring
- Do not estimate years of experience, invent metrics, or round claims up
- Keep answers grounded in specific, verifiable details from this file