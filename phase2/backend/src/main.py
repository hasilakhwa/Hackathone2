from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import tasks
from .core.config import settings
from .core.database import init_db


def create_app():
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        description="Todo Backend API for the Todo Full-Stack Web Application"
    )

    # Initialize database
    init_db()

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        # Expose headers for JWT
        expose_headers=["Access-Control-Allow-Origin"]
    )

    # Include API routes
    app.include_router(tasks.router, prefix="/api/{user_id}", tags=["tasks"])

    @app.get("/")
    def read_root():
        return {
            "message": "Todo Backend API",
            "version": settings.version,
            "description": "Secure task management API with JWT authentication"
        }

    @app.get("/health")
    def health_check():
        return {"status": "healthy", "version": settings.version}

    @app.get("/api/health")
    def api_health_check():
        return {
            "status": "healthy",
            "version": settings.version,
            "endpoints": [
                "/api/{user_id}/tasks",
                "/api/{user_id}/tasks/{id}",
                "/api/{user_id}/tasks/{id}/complete"
            ]
        }

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)