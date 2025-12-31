from __future__ import annotations
import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError(f"Visitor {visitor.get('name', 'Unknown')} is not vaccinated.")
        
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError(f"Visitor {visitor.get('name', 'Unknown')}'s vaccine is outdated.")
        
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"Visitor {visitor.get('name', 'Unknown')} is not wearing a mask.")
        
        return f"Welcome to {self.name}"
