# project/app/api/crud.py


from typing import List, Optional

from app.models.tortoise import TextSummary

from app.models.pydantic import (  # isort:skip
    SummaryPayloadSchema,
    SummaryUpdatePayloadSchema,
)


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="")
    await summary.save()
    return summary.id


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    else:
        return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryUpdatePayloadSchema) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).update(
        url=payload.url, summary=payload.summary
    )
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary[0]
    return None
