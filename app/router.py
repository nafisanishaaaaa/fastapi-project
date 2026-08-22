from fastapi import APIRouter
from app.routers import (
    path_parameter,
    query_parameter,
    request_body,
    form_data,
    file_upload,
    error_handling,
    path_configuration,
    body_updates,
    dependency,
    security,
    json_encoder,
    hero, background_task
)
router = APIRouter()
router.include_router(path_parameter.router)
router.include_router(query_parameter.router)
router.include_router(request_body.router)
router.include_router(form_data.router)
router.include_router(file_upload.router)
router.include_router(error_handling.router)
router.include_router(path_configuration.router)
router.include_router(json_encoder.router)
router.include_router(body_updates.router)
router.include_router(dependency.router)
router.include_router(security.router)
router.include_router(hero.router)
router.include_router( background_task.router)