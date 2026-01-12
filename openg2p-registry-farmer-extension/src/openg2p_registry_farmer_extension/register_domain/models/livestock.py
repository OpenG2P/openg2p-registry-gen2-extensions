from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, validates, Integer
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterLivestock(G2PRegister):
    __tablename__ = "g2p_register_livestocks"

    # internal_record_id
    # functional_record_id -> NONE
    # foundational_id -> NONE
    # link_foundational_id -> farmer's foundational_id
    # link_internal_record_id -> farmer's internal_record_id
    # master_register_id -> farmer register_id
    livestock_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    livestock_system: Mapped[str] = mapped_column(String, nullable=True)

    @validates('livestock_type', 'count', 'livestock_system')
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
            self.livestock_type or "",
            self.count or "",
            self.livestock_system or ""
        ]
        self.search_text = " ".join(searchable_fields).strip()


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryLivestock(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_livestocks"

    # Override all columns from base to make them nullable for history
    livestock_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    livestock_system: Mapped[str] = mapped_column(String, nullable=True)

