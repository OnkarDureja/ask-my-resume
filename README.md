# AskCV

**Live demo:** https://onkar-ask-my-resume.streamlit.app

A conversational assistant that lets recruiters ask questions about Onkar Dureja's background, skills, and projects, and get answers grounded only in verified portfolio data. It can also score Onkar's resume against a pasted job description, highlighting matched skills, missing skills, and a fit verdict.

## Why this exists

Most portfolios are static. A recruiter skims a resume once and moves on. AskCV turns that resume into something a recruiter can actually interrogate, ask about a specific project, a specific skill, or how a background fits a role they're hiring for.

The one rule that shaped every design decision here: the assistant must never guess. If something isn't in the portfolio data, it says so directly instead of inventing an answer. A chatbot that hallucinates a skill a recruiter later disproves in an interview is worse than no chatbot at all.

## How it works

- The entire portfolio (education, work experience, projects, skills) lives in `portfolio_data.md`, a plain markdown file.
- On each request, that file is read and injected directly into the system prompt sent to the LLM.
- No retrieval, no vector database. The portfolio is small enough to fit entirely in context, so a RAG pipeline would add complexity without adding value.
- Responses stream token by token, the same experience as a standard chat interface.
- The system prompt includes a hard constraint: answer only from the provided data, and say plainly when something isn't covered rather than estimating or inferring.

## Stack

- Python, Streamlit
- Groq API (`openai/gpt-oss-120b`) for inference
- Pydantic for structured data validation
- python-dotenv for local secrets

## Running locally

```
git clone https://github.com/OnkarDureja/ask-my-resume.git
cd ask-my-resume
uv sync
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_key_here
GROQ_MODEL=openai/gpt-oss-120b
```

Then run:

```
uv run streamlit run app.py
```

## Project status

This is an active learning project built as part of an AI Engineer course, focused on prompt engineering, structured output, and streaming responses. JD-matching and further polish are in progress.