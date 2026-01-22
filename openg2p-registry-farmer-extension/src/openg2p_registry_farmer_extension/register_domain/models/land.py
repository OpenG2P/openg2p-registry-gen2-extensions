from sqlalchemy import String, Float, Date
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoShape
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterLand(G2PRegister, G2PGeo, G2PGeoShape):
    __tablename__ = "g2p_register_lands"

    # internal_record_id
    # functional_record_id -> NONE
    # foundational_id -> NONE
    # link_foundational_id -> farmer's foundational_id
    # link_internal_record_id -> farmer's internal_record_id
    # master_register_id -> farmer register_id
    
    location: Mapped[str] = mapped_column(String, nullable=True)
    land_tenure: Mapped[str] = mapped_column(String, nullable=True)
    land_size: Mapped[float] = mapped_column(Float, nullable=True)
    measurement: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return land-specific fields for search text aggregation.
        G2PRegister, G2PGeo, and G2PGeoShape fields are automatically included via event listeners.
        """
        return [
            self.location or "",
            self.land_tenure or "",
            str(self.land_size) if self.land_size is not None else "",
            self.measurement or "",
        ]


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryLand(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_lands"

    # Override all columns from base to make them nullable for history
    location: Mapped[str] = mapped_column(String, nullable=True)
    land_tenure: Mapped[str] = mapped_column(String, nullable=True)
    land_size: Mapped[float] = mapped_column(Float, nullable=True)
    measurement: Mapped[str] = mapped_column(String, nullable=True)
