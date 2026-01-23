from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterMachinery(G2PRegister):
    __tablename__ = "g2p_register_machineries"

    machinery_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    equipment_source: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return machinery-specific fields for search text aggregation.
        G2PRegister fields are automatically included via event listeners.
        """
        return [
            self.machinery_type or "",
            str(self.count) if self.count is not None else "",
            self.equipment_source or "",
        ]


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryMachinery(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_machineries"

    # Override all columns from base to make them nullable for history
    machinery_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    equipment_source: Mapped[str] = mapped_column(String, nullable=True)

