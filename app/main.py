from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.routes import mood  # ✅ Import your mood router

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment-Based Music Recommendation API",
    description="API for recommending music based on sentiment analysis",
    version="1.0.0"
)

# CORS Middleware (⚠️ In production, set allowed origins securely)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (like JS, CSS, images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up Jinja2 template engine (used if you serve HTML templates)
templates = Jinja2Templates(directory="app/templates")

# -------------------------
#         Routes
# -------------------------

@app.get("/")
async def root():
    return {"message": "Welcome to Sentiment-Based Music Recommendation API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# ✅ Include mood analysis route
app.include_router(mood.router, prefix="/api/mood", tags=["Mood Analysis"])

# -------------------------
#     Local Run Config
# -------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
