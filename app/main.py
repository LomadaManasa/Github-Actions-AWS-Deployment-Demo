from fastapi import FastAPI, Request
from mangum import Mangum
import logging

# Set up logger to capture incoming request paths
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from api.v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')

# Attach versioned routes
app.include_router(api_router, prefix="/api/v1")

# Base test endpoint
@app.get("/", tags=["Endpoint Test"])
def main_endpoint_test():
    logger.info("Welcome CI/CD Pipeline with GitHub Actions!")
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}





# Log every incoming HTTP request (method and path)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"🔥 Request received: {request.method} {request.url.path}")
    response = await call_next(request)
    return response

# Lambda entrypoint for API Gateway

handler = Mangum(app, api_gateway_base_path="/default")

