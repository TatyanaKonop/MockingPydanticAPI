from __future__ import annotations

from pydantic import BaseModel


class PostResponseSchema(BaseModel):
    message: str
    run_id: int
