from sqlalchemy import String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory, G2PGeo
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterFarmer(G2PRegister, G2PGeo):
    __tablename__ = "g2p_register_farmers"

    # internal_record_id
    # functional_record_id -> farmer_id
    # foundational_id -> national_id
    # link_foundational_id -> NONE
    # link_internal_record_id -> household's internal_record_id
    # master_register_id -> household register_id
    
    # DCI fields
    # identifier_type: Mapped[str] = mapped_column(String, nullable=True)
    # identifier_value: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    date_of_birth: Mapped[str] = mapped_column(Date, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    marital_status: Mapped[str] = mapped_column(String, nullable=True)
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)

    address: Mapped[str] = mapped_column(String, nullable=False)
    district: Mapped[str] = mapped_column(String, nullable=False)
    region: Mapped[str] = mapped_column(String, nullable=False)
    mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return farmer-specific fields for search text aggregation.
        G2PRegister and G2PGeo fields are automatically included via event listeners.
        """
        return [
            self.first_name or "",
            self.last_name or "",
            str(self.date_of_birth) if self.date_of_birth else "",
            self.gender or "",
            self.marital_status or "",
            str(self.is_disabled) if self.is_disabled is not None else "",
            self.address or "",
            self.district or "",
            self.region or "",
            self.mobile_number or "",
            self.email or "",
        ]

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryFarmer(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_farmers"

    # Override all columns from G2PRegisterFarmerBase to make them nullable for history
    # identifier_type: Mapped[str] = mapped_column(String, nullable=True)
    # identifier_value: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)

    date_of_birth: Mapped[str] = mapped_column(Date, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    district: Mapped[str] = mapped_column(String, nullable=True)
    region: Mapped[str] = mapped_column(String, nullable=True)
    mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    marital_status: Mapped[str] = mapped_column(String, nullable=True)
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
