from enum import Enum
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.content_generator.openai_gen import OpenAIContentGenerator

router = APIRouter()


class RelationshipEnum(str, Enum):
    spouse = "spouse"
    boyfriend = "boyfriend"
    girlfriend = "girlfriend"
    friend = "friend"
    parent = "parent"
    sibling = "sibling"


class ToneEnum(str, Enum):
    friendly = "friendly"
    formal = "formal"
    funny = "funny"
    romantic = "romantic"


class OccasionEnum(str, Enum):
    birthday = "birthday"
    anniversary = "anniversary"
    graduation = "graduation"
    promotion = "promotion"
    holiday = "holiday"
    wedding = "wedding"


class MessageRequest(BaseModel):
    relationship: RelationshipEnum = Field(..., example="spouse")
    tone: ToneEnum = Field(..., example="funny")
    occasion: OccasionEnum = Field(..., example="birthday")
    note: Optional[str] = Field(
        None, example="Hope your day is as awesome as you!"
    )  # noqa


class MessageResponse(BaseModel):
    message: str


@router.post("/generate-message", response_model=MessageResponse)
def generate_ai_message(payload: MessageRequest):
    """
    Generate a custom AI message based on relationship, tone, and occasion.
    """

    base = (
        f"This is a {payload.tone} message for your {payload.relationship} "
        f"on their {payload.occasion}."
    )

    if payload.note:
        base += f" Here's a special note: {payload.note}"

    # This is where you'd plug in your real AI generation logic (OpenAI, etc.)
    ai_message = OpenAIContentGenerator().generate_gift_message(
        purpose=payload.occasion.value,
        tone=payload.tone.value,
        audience=payload.relationship.value,
        note=payload.note if payload.note else "",
    )
    return MessageResponse(message=ai_message)
