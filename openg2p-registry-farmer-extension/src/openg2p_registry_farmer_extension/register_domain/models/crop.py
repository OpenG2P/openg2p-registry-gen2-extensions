from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, validates
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel
import uuid


# All Register classes should have the prefix G2PRegister
class G2PRegisterCrop(G2PRegister):
    __tablename__ = "g2p_register_crops"

    # internal_record_id
    # functional_record_id -> NONE
    # foundational_id -> NONE
    # link_foundational_id -> NONE
    # link_internal_record_id -> land's internal_record_id
    # master_register_id -> land register_id

    activity_group: Mapped[str] = mapped_column(String, nullable=True)
    crop_type: Mapped[str] = mapped_column(String, nullable=True)
    variety: Mapped[str] = mapped_column(String, nullable=True)
    season: Mapped[str] = mapped_column(String, nullable=True)
    end_use: Mapped[str] = mapped_column(String, nullable=True)
    irrigation: Mapped[str] = mapped_column(String, nullable=True)
    irrigation_water: Mapped[str] = mapped_column(String, nullable=True)
    fertilizer_type: Mapped[str] = mapped_column(String, nullable=True)

    @validates('activity_group', 'crop_type', 'variety', 'season', 'end_use', 'irrigation', 'irrigation_water', 'fertilizer_type')
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
            self.activity_group or "",
            self.crop_type or "",
            self.variety or "",
            self.season or "",
            self.end_use or "",
            self.irrigation or "",
            self.irrigation_water or "",
            self.fertilizer_type or ""
        ]
        self.search_text = " ".join(searchable_fields).strip()

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryCrop(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_crops"

    # Override all columns from G2PRegisterCropBase to make them nullable for history
    activity_group: Mapped[str] = mapped_column(String, nullable=True)
    crop_type: Mapped[str] = mapped_column(String, nullable=True)
    variety: Mapped[str] = mapped_column(String, nullable=True)
    season: Mapped[str] = mapped_column(String, nullable=True)
    end_use: Mapped[str] = mapped_column(String, nullable=True)
    irrigation: Mapped[str] = mapped_column(String, nullable=True)
    irrigation_water: Mapped[str] = mapped_column(String, nullable=True)
    fertilizer_type: Mapped[str] = mapped_column(String, nullable=True)