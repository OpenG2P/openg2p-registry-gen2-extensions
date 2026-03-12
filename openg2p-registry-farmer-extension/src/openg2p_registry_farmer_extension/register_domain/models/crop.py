from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
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

    def get_search_text_fields(self) -> list[str]:
        """
        Return crop-specific fields for search text aggregation.
        G2PRegister fields are automatically included via event listeners.
        """
        return [
            self.activity_group or "",
            self.crop_type or "",
            self.variety or "",
            self.season or "",
            self.end_use or "",
            self.irrigation or "",
            self.irrigation_water or "",
            self.fertilizer_type or "",
        ]

    def get_record_name_fields(self) -> list[str]:
        """Return crop fields used to build record_name."""
        return [
            self.crop_type or "",
            self.functional_record_id or "",
        ]

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
