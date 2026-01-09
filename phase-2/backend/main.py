from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes.tasks


app = FastAPI(title="Todo API", version="1.0.0")


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(routes.tasks.router, prefix="/api/tasks", tags=["tasks"])


@app.get("/")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok", "message": "Todo API is running successfully"}


@app.get("/api/health")
async def detailed_health_check():
    """
    Detailed health check endpoint.
    """
    return {
        "status": "healthy",
        "service": "Todo API",
        "version": "1.0.0"
    }