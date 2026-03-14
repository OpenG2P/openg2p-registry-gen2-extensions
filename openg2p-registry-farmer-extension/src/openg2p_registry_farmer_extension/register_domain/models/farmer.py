from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PGeo, G2PPerson,
    G2PPersonHistory, G2PGeoHistory
)
from ..services import G2PRegisterDomainServiceFarmer


# All Register classes should have the prefix G2PRegister
class G2PRegisterFarmer(G2PRegister, G2PPerson, G2PGeo):
    __tablename__ = "g2p_register_farmers"

    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)

    def get_record_name_fields(self) -> str:
        """Return farmer fields used to build record_name."""
        return G2PRegisterDomainServiceFarmer().construct_record_name(self.to_dict())

    def get_search_text_fields(self) -> str:
        """Return farmer fields used to build search_text."""
        return G2PRegisterDomainServiceFarmer().construct_search_text(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryFarmer(G2PRegisterHistory, G2PPersonHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_farmers"

    # Farmer-specific fields for history
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
