from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, validates
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel
import uuid


# All Register classes should have the prefix G2PRegister
class G2PRegisterFamily(G2PRegister):
    __tablename__ = "g2p_register_families"

    # internal_record_id
    # functional_record_id -> family_id
    # foundational_id -> NONE
    # link_foundational_id -> NONE
    # link_foundational_register_id -> NONE
    # link_internal_record_id -> NONE
    # link_internal_register_id -> NONE
    ethnic_group: Mapped[str] = mapped_column(String, nullable=True)
    belong_to_protected_groups: Mapped[bool] = mapped_column(Boolean, nullable=True)
    under_other_vulnerable_status: Mapped[bool] = mapped_column(Boolean, nullable=True)

    @validates('ethnic_group', 'belong_to_protected_groups', 'under_other_vulnerable_status')
    def update_search_text(self, _key: str, value: str) -> str:
        """
        Automatically update search_text whenever any searchable field is modified.
        Combines all searchable fields into a single text for trigram search.
        """
        self._populate_search_text()
        return value

    def _populate_search_text(self) -> None:
        """
        Populate search_text by combining all searchable family fields.
        """
        searchable_fields: list[str] = [
            self.ethnic_group or "",
            self.belong_to_protected_groups or "",
            self.under_other_vulnerable_status or ""
        ]
        self.search_text = " ".join(searchable_fields).strip()

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryFamily(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_families"

    # Override all columns from G2PRegisterFamilyBase to make them nullable for history
    ethnic_group: Mapped[str] = mapped_column(String, nullable=True)
    belong_to_protected_groups: Mapped[bool] = mapped_column(Boolean, nullable=True)
    under_other_vulnerable_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
