from fastapi import APIRouter

from .endpoints import (
    users,
    utils
)


router = APIRouter()


router.include_router(users.router, prefix='/users', tags=['User'])
router.include_router(utils.router)

