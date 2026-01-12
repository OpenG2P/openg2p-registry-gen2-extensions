from sqlalchemy import String, Float, Date
from sqlalchemy.orm import Mapped, mapped_column, validates
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterLand(G2PRegister):
    __tablename__ = "g2p_register_lands"

    # internal_record_id
    # functional_record_id -> NONE
    # foundational_id -> NONE
    # link_foundational_id -> farmer's foundational_id
    # link_internal_record_id -> farmer's internal_record_id
    # master_register_id -> farmer register_id
    location: Mapped[str] = mapped_column(String, nullable=True)
    land_tenure: Mapped[str] = mapped_column(String, nullable=True)
    land_size: Mapped[float] = mapped_column(Float, nullable=True)
    mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    registration_date: Mapped[str] = mapped_column(Date, nullable=True)
    relationship_with_household_head: Mapped[str] = mapped_column(String, nullable=True)

    @validates('location', 'land_tenure', 'land_size', 'mobile_number', 'registration_date', 'relationship_with_household_head')
    def update_search_text(self, _key: str, value: str) -> str:
        """
        Automatically update search_text whenever any searchable field is modified.
        Combines all searchable fields into a single text for trigram search.
        """
        self._populate_search_text()
        return value

    def _populate_search_text(self) -> None:
        """
        Populate search_text by combining all searchable fields.
        """
        searchable_fields: list[str] = [
            self.location or "",
            self.land_tenure or "",
            self.land_size or "",
            self.mobile_number or "",
            self.registration_date or "",
            self.relationship_with_household_head or ""
        ]
        self.search_text = " ".join(searchable_fields).strip()


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryLand(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_lands"

    # Override all columns from base to make them nullable for history
    location: Mapped[str] = mapped_column(String, nullable=True)
    land_tenure: Mapped[str] = mapped_column(String, nullable=True)
    land_size: Mapped[float] = mapped_column(Float, nullable=True)
    mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    registration_date: Mapped[str] = mapped_column(Date, nullable=True)
    relationship_with_household_head: Mapped[str] = mapped_column(String, nullable=True)
