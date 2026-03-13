from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoHistory
from ..services import G2PRegisterDomainServiceHousehold


# All Register classes should have the prefix G2PRegister
class G2PRegisterHousehold(G2PRegister, G2PGeo):
    __tablename__ = "g2p_register_households"

    poverty_score: Mapped[str] = mapped_column(String, nullable=True)
    poverty_score_type: Mapped[str] = mapped_column(String, nullable=True)
    household_head: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return household-specific fields for search text aggregation.
        G2PRegister and G2PGeo fields are automatically included via event listeners.
        """
        return [
            str(self.poverty_score) if self.poverty_score is not None else "",
            self.poverty_score_type or "",
            self.household_head or "",
        ]

    def get_record_name_fields(self) -> str:
        """Return household record_name from domain service implementation."""
        return G2PRegisterDomainServiceHousehold().construct_record_name(self.to_dict())

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHousehold(G2PRegisterHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_households"

    # Household-specific fields for history
    poverty_score: Mapped[str] = mapped_column(String, nullable=True)
    poverty_score_type: Mapped[str] = mapped_column(String, nullable=True)
    household_head: Mapped[str] = mapped_column(String, nullable=True)
