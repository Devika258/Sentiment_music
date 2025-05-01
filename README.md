# Sentiment-Based Music Recommender

An AI-powered, cloud-native application that recommends curated playlists based on user mood.  
Built for **CMP9785M Cloud Development** coursework submission.

---

## Overview

Users input one word text describing their mood (e.g., "Sad","happy","calm").  
The system uses **OpenAI** for sentiment analysis, then fetches matching playlists via the **Spotify API**.

**Technologies Used**:
- **FastAPI** (Backend)
- **ReactJS** (Frontend)
- **PostgreSQL** (Database)
- **AWS ECS/Lambda**, **Netlify/Vercel** (Deployment)

---

## Features

- User Authentication (JWT-based)
- Mood-Based Playlist Recommendations
- Sentiment Analysis via OpenAI API
- Playlist Fetching via Spotify API
- Credit Management System
- Contact Form for Feedback Submission
- Cloud-Native Modular Architecture
- Dockerized Backend
- GitHub Actions CI/CD Pipeline

---

## System Architecture

> *(Architecture Diagram Placeholder – Upload as `architecture.png` if available)*

**Main Components**:
- **Frontend** (ReactJS)
- **Backend** (FastAPI)
- **External APIs** (OpenAI & Spotify)
- **PostgreSQL** (AWS RDS)

**System Flow**:
User Input → FastAPI Backend → OpenAI & Spotify APIs → PostgreSQL → Frontend Display


---

## API Endpoints

| Endpoint            | Method | Description                            |
|---------------------|--------|----------------------------------------|
| `/signup`           | POST   | Register a new user                    |
| `/login`            | POST   | Authenticate and receive JWT token     |
| `/submit-mood`      | POST   | Submit mood text for analysis          |
| `/credits`          | GET    | Check available user credits           |
| `/playlists`        | GET    | Fetch playlists based on analyzed mood |
| `/submit-feedback`  | POST   | Submit user feedback via contact form  |

---

## Deployment Strategy

- Backend deployed via **AWS Lambda** (serverless) or **AWS ECS** (Dockerized).
- Frontend hosted on **Netlify** or **Vercel**.
- HTTPS secured APIs (optional Cloudflare DNS setup).
- Environment Variables securely managed using AWS Secrets Manager.

**Estimated Running Costs**:
- AWS Lambda/ECS ➔ ~$5/month
- AWS RDS PostgreSQL ➔ ~$10/month
- OpenAI API ➔ ~$0.002/request
- Netlify/Vercel Hosting ➔ Free-Tier (students)

---

## Security Practices

- Passwords stored with **bcrypt** hashing.
- User authentication handled with **JWT tokens**.
- **CORS** enabled carefully for API security.
- Usage of secure API keys and access tokens.

---
---

## References

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

## Contact
Built by: Devika Sivanjali Rajesh
Student ID: 29718997
Submission Date: 8th May 2025

---

## Project Structure

```bash
sentiments/
├── backend/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── mood.py
│   │   ├── feedback.py
│   ├── models/
│   ├── database.py
├── frontend/
│   ├── public/
│   │   ├── architecture.html
│   │   ├── contact.html
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
├── README.md
├── Dockerfile
├── .gitignore
└── requirements.txt
