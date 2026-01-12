from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, validates
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterMachinery(G2PRegister):
    __tablename__ = "g2p_register_machineries"

    # internal_record_id
    # functional_record_id -> NONE
    # foundational_id -> NONE
    # link_foundational_id -> farmer's foundational_id
    # link_internal_record_id -> farmer's internal_record_id
    # master_register_id -> farmer register_id
    machinery_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    equipment_source: Mapped[str] = mapped_column(String, nullable=True)

    @validates('machinery_type', 'count', 'equipment_source')
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
            self.machinery_type or "",
            self.count or "",
            self.equipment_source or ""
        ]
        self.search_text = " ".join(searchable_fields).strip()


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryMachinery(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_machineries"

    # Override all columns from base to make them nullable for history
    machinery_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    equipment_source: Mapped[str] = mapped_column(String, nullable=True)

