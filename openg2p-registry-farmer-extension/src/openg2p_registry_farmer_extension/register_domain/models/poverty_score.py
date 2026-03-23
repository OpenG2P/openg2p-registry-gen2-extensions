from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServicePovertyScore


# All Register classes should have the prefix G2PRegister
class G2PRegisterPovertyScore(G2PRegister):
    __tablename__ = "g2p_register_poverty_scores"

    # link_internal_record_id -> Household's internal_record_id
    poverty_score: Mapped[str] = mapped_column(String, nullable=True)
    poverty_score_type: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> str:
        """Return poverty score fields used to build search_text."""
        return G2PRegisterDomainServicePovertyScore().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return poverty score record_name from domain service implementation."""
        return G2PRegisterDomainServicePovertyScore().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryPovertyScore(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_poverty_scores"

    poverty_score: Mapped[str] = mapped_column(String, nullable=True)
    poverty_score_type: Mapped[str] = mapped_column(String, nullable=True)
