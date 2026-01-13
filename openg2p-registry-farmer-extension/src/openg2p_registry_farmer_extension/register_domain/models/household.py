from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, validates
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterHousehold(G2PRegister):
    __tablename__ = "g2p_register_households"

    # internal_record_id
    # functional_record_id -> household_id
    # foundational_id -> NONE
    # link_foundational_id -> NONE
    # link_internal_record_id -> NONE
    # master_register_id -> NONE

    # DCI fields
    identifier_type: Mapped[str] = mapped_column(String, nullable=True)
    identifier_value: Mapped[str] = mapped_column(String, nullable=True)

    address: Mapped[str] = mapped_column(String, nullable=True)
    district: Mapped[str] = mapped_column(String, nullable=True)
    region: Mapped[str] = mapped_column(String, nullable=True)
    poverty_score: Mapped[float] = mapped_column(Float, nullable=True)
    poverty_score_type: Mapped[str] = mapped_column(String, nullable=True)
    household_head: Mapped[str] = mapped_column(String, nullable=True)

    @validates('address', 'district', 'region', 'poverty_score', 'poverty_score_type', 'household_head')
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
            self.address or "",
            self.district or "",
            self.region or "",
            str(self.poverty_score) if self.poverty_score is not None else "",
            self.poverty_score_type or "",
            self.household_head or ""
        ]
        self.search_text = " ".join(searchable_fields).strip()


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHousehold(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_households"

    # Override all columns from base to make them nullable for history
    identifier_type: Mapped[str] = mapped_column(String, nullable=True)
    identifier_value: Mapped[str] = mapped_column(String, nullable=True)

    address: Mapped[str] = mapped_column(String, nullable=True)
    district: Mapped[str] = mapped_column(String, nullable=True)
    region: Mapped[str] = mapped_column(String, nullable=True)
    poverty_score: Mapped[float] = mapped_column(Float, nullable=True)
    poverty_score_type: Mapped[str] = mapped_column(String, nullable=True)
    household_head: Mapped[str] = mapped_column(String, nullable=True)

