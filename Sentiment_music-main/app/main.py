from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.routes import mood   # ✅ Already included
from app.routes import auth   # ✅ Add this line to include auth

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment-Based Music Recommendation API",
    description="API for recommending music based on sentiment analysis",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static & Templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
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

# ✅ Include routers
app.include_router(mood.router, prefix="/api/mood", tags=["Mood Analysis"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])  # ✅ Add this line

# -------------------------
#      Run Server
# -------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
