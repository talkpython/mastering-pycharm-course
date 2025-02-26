from typing import List

# noinspection PyPackageRequirements
from pydantic import BaseModel

from models.video_model import Video


class Category(BaseModel):
    category: str
    image: str
    videos: List[Video]
