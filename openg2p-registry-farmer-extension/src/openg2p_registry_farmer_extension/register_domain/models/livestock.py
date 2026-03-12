from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterLivestock(G2PRegister):
    __tablename__ = "g2p_register_livestocks"

    livestock_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    livestock_system: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return livestock-specific fields for search text aggregation.
        G2PRegister fields are automatically included via event listeners.
        """
        return [
            self.livestock_type or "",
            str(self.count) if self.count is not None else "",
            self.livestock_system or "",
        ]

    def get_record_name_fields(self) -> list[str]:
        """Return livestock fields used to build record_name."""
        return [
            str(self.count) if self.count is not None else "",
            self.livestock_type or "",
            self.functional_record_id or "",
        ]


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryLivestock(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_livestocks"

    # Override all columns from base to make them nullable for history
    livestock_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    livestock_system: Mapped[str] = mapped_column(String, nullable=True)
