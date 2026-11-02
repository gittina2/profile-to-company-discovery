# Profile-to-Company discovery

**An AI-powered tool for discovering companies aligned with a professional profile.**

## Overview

Profile-to-Company discovery is a project in development that explores how AI and automated web search can support professional career exploration.

The tool aims to transform a CV or free-text professional profile into structured information, identify relevant areas of expertise and interests, and use this information to discover and evaluate companies that may be a good match.

Rather than focusing exclusively on job postings, the goal is to identify companies whose activities, technologies, and business domains align with a person's professional background.

## How it works

The current prototype is built around three main steps:

1. **Profile extraction** – An LLM analyses the input text and extracts structured information about skills, expertise, work activities, interests, and preferences.
2. **Search query generation** – The structured profile is used to generate targeted web search queries.
3. **Company evaluation** – Search results are analysed to identify companies and assess their relevance to the profile.

## Tech stack

- **Python** – Core application logic
- **FastAPI** – API endpoints
- **Ollama** – Local LLM inference
- **n8n** – Workflow orchestration
- **Tavily** – Web search API

## Project status

<code>Work in progress</code>

The core profile extraction, search query generation, and company evaluation components have been implemented and tested individually.

The end-to-end workflow integration and further improvements to search quality, company identification, and evaluation are still in progress.

## Future developments

- Complete and refine the end-to-end n8n workflow.
- Improve company deduplication and relevance ranking.
- Add a user-friendly interface for profile submission and results exploration.
- Improve evaluation reliability and source traceability.
