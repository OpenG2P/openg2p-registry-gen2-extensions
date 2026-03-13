from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceLivestock


# All Register classes should have the prefix G2PRegister
class G2PRegisterLivestock(G2PRegister):
    __tablename__ = "g2p_register_livestocks"

    livestock_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    livestock_system: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> str:
        """Return livestock fields used to build search_text."""
        return G2PRegisterDomainServiceLivestock().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return livestock record_name from domain service implementation."""
        return G2PRegisterDomainServiceLivestock().construct_record_name(self.to_dict())

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryLivestock(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_livestocks"

    # Override all columns from base to make them nullable for history
    livestock_type: Mapped[str] = mapped_column(String, nullable=True)
    count: Mapped[int] = mapped_column(Integer, nullable=True)
    livestock_system: Mapped[str] = mapped_column(String, nullable=True)
