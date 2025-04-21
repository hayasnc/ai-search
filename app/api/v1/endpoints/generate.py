import json
from enum import Enum
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.content_generator.llama_gen import LlamaContentGenerator

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
    status: bool
    messages: list[str]


@router.post("/generate-message", response_model=MessageResponse)
def generate_gift_message(payload: MessageRequest):
    """
    Generate a custom AI message based on relationship, tone, and occasion.
    """

    occasion = payload.occasion.value
    tone = payload.tone.value
    relationship = payload.relationship.value
    note = payload.note

    prompt = (
        f"Generate 5 different {tone} messages for the occasion: {occasion}. "
        f"The messages should be suitable for: {relationship}."
    )
    if note:
        prompt += f" Additional note: {note}"

    prompt += (
        "Respond in JSON format:\n"
        "{\n"
        '  "messages": [\n'
        '    "msg 1",\n'
        '    "msg 2",\n'
        '    "msg 3",\n'
        '    "msg 4",\n'
        '    "msg 5"\n'
        "  ]\n"
        "}\n"
        "\n"
        "Only return the JSON. Do not include any explanations or extra text."
    )
    content_generator = LlamaContentGenerator()
    content = content_generator.generate_content(prompt)
    parsed = json.loads(content)
    response = parsed["messages"]
    return {"status": True, "messages": response}
