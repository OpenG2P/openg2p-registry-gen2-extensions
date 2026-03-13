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

    def get_search_text_fields(self) -> list[str]:
        """
        Return land-specific fields for search text aggregation.
        G2PRegister, G2PGeo, and G2PGeoShape fields are automatically included via event listeners.
        """
        return [
            self.land_tenure or "",
            str(self.land_size) if self.land_size is not None else "",
            self.measurement or "",
        ]

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
