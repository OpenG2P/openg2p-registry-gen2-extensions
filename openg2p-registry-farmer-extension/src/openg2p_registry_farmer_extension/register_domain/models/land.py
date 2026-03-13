from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoShape,
    G2PGeoHistory, G2PGeoShapeHistory
)
from ..services import G2PRegisterDomainServiceLand


# All Register classes should have the prefix G2PRegister
class G2PRegisterLand(G2PRegister, G2PGeo, G2PGeoShape):
    __tablename__ = "g2p_register_lands"
    
    land_tenure: Mapped[str] = mapped_column(String, nullable=True)
    land_size: Mapped[str] = mapped_column(String, nullable=True)
    measurement: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> str:
        """Return land fields used to build search_text."""
        return G2PRegisterDomainServiceLand().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return land record_name from domain service implementation."""
        return G2PRegisterDomainServiceLand().construct_record_name(self.to_dict())

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryLand(G2PRegisterHistory, G2PGeoHistory, G2PGeoShapeHistory):
    __tablename__ = "g2p_register_history_lands"

    # Land-specific fields for history
    land_tenure: Mapped[str] = mapped_column(String, nullable=True)
    land_size: Mapped[str] = mapped_column(String, nullable=True)
    measurement: Mapped[str] = mapped_column(String, nullable=True)
