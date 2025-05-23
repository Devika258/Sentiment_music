from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

# ✅ Import route modules
from app.routes import mood
from app.routes import auth

# 🚀 Initialize FastAPI application
app = FastAPI(
    title="Sentiment-Based Music Recommendation API",
    description="A system that recommends playlists based on mood using OpenAI and JWT authentication.",
    version="1.0.0"
)

# 🌍 Enable CORS (configure securely for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔐 TODO: Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📁 Serve static assets & templates if needed
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# 🏠 Root endpoints
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Sentiment-Based Music Recommendation API"}

@app.get("/health", tags=["Root"])
async def health_check():
    return {"status": "healthy"}

# 🔌 Register application routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(mood.router, prefix="/api/mood", tags=["Mood Analysis"])

# 🔍 Print registered routes (for debugging)
for route in app.routes:
    print("✅ ROUTE:", route.path)

# ⚙️ Run the server (only for local execution)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
