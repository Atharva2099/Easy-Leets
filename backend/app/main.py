from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.analyze import router as analyze_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes with the correct prefix
app.include_router(analyze_router, prefix="/api")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "MAAI Backend API"}

# Global health check
@app.get("/health")
async def health():
    return {"status": "server running"}