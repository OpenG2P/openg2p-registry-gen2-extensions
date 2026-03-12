from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PGeo, G2PPerson,
    G2PPersonHistory, G2PGeoHistory
)


# All Register classes should have the prefix G2PRegister
class G2PRegisterFarmer(G2PRegister, G2PPerson, G2PGeo):
    __tablename__ = "g2p_register_farmers"

    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return farmer-specific fields for search text aggregation.
        G2PRegister, G2PPerson, and G2PGeo fields are automatically included via event listeners.
        """
        return [
            str(self.is_disabled) if self.is_disabled is not None else "",
        ]

    def get_record_name_fields(self) -> list[str]:
        """Return farmer fields used to build record_name."""
        return [
            self.first_name or "",
            self.last_name or ""
        ]


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryFarmer(G2PRegisterHistory, G2PPersonHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_farmers"

    # Farmer-specific fields for history
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
