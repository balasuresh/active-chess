from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, JSON
from sqlalchemy.sql import func
from app.database import Base

class UserProgress(Base):
    __tablename__ = "user_progress"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    enrollment_id = Column(Integer, ForeignKey("enrollments.id"))
    tutorial_id = Column(Integer, ForeignKey("tutorials.id"), nullable=True)
    puzzle_id = Column(Integer, ForeignKey("puzzles.id"), nullable=True)
    is_completed = Column(Boolean, default=False)
    attempts = Column(Integer, default=0)
    score = Column(Integer, default=0)
    last_accessed = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    activity_log = Column(JSON)
    completed_at = Column(DateTime(timezone=True), nullable=True)
