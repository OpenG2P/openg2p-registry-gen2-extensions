from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceFarmInputs


# All Register classes should have the prefix G2PRegister
class G2PRegisterFarmInputs(G2PRegister):
    __tablename__ = "g2p_register_farm_inputs"

    # link_internal_record_id -> Farmer's internal_record_id
    fertilizer_use: Mapped[bool] = mapped_column(Boolean, nullable=True)
    pesticide_use: Mapped[bool] = mapped_column(Boolean, nullable=True)
    insecticide_use: Mapped[bool] = mapped_column(Boolean, nullable=True)
    improved_seed_use: Mapped[bool] = mapped_column(Boolean, nullable=True)
    water_source: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (Excel: Rainfed; Irrigation GW/Surface; Well; Water Harvesting; Surface Water)
    access_to_machinery: Mapped[bool] = mapped_column(Boolean, nullable=True)
    access_to_finance: Mapped[bool] = mapped_column(Boolean, nullable=True)

    def get_search_text_fields(self) -> str:
        """Return farm inputs fields used to build search_text."""
        return G2PRegisterDomainServiceFarmInputs().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return farm inputs record_name from domain service implementation."""
        return G2PRegisterDomainServiceFarmInputs().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryFarmInputs(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_farm_inputs"

    fertilizer_use: Mapped[bool] = mapped_column(Boolean, nullable=True)
    pesticide_use: Mapped[bool] = mapped_column(Boolean, nullable=True)
    insecticide_use: Mapped[bool] = mapped_column(Boolean, nullable=True)
    improved_seed_use: Mapped[bool] = mapped_column(Boolean, nullable=True)
    water_source: Mapped[str] = mapped_column(String, nullable=True)
    access_to_machinery: Mapped[bool] = mapped_column(Boolean, nullable=True)
    access_to_finance: Mapped[bool] = mapped_column(Boolean, nullable=True)
