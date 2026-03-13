from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PPerson, G2PGeo,
    G2PPersonHistory, G2PGeoHistory
)
from ..services import G2PRegisterDomainServiceHouseholdMember


# All Register classes should have the prefix G2PRegister
class G2PRegisterHouseholdMember(G2PRegister, G2PPerson, G2PGeo):
    __tablename__ = "g2p_register_household_members"

    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return household member-specific fields for search text aggregation.
        G2PRegister, G2PPerson, and G2PGeo fields are automatically included via event listeners.
        """
        return [
            str(self.is_disabled) if self.is_disabled is not None else "",
        ]

    def get_record_name_fields(self) -> str:
        """Return household member record_name from domain service implementation."""
        return G2PRegisterDomainServiceHouseholdMember().construct_record_name(self.to_dict())

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHouseholdMember(G2PRegisterHistory, G2PPersonHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_household_members"

    # HouseholdMember-specific fields for history
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
