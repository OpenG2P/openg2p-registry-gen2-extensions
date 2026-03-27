from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PGeo, G2PPerson,
    G2PPersonHistory, G2PGeoHistory
)
from ..services import G2PRegisterDomainServiceFarmer
from .enums import DisabilityTypeEnum, DisabilitySeverityEnum, SourceOfIncomeEnum, EducationalLevelEnum


# All Register classes should have the prefix G2PRegister
class G2PRegisterFarmer(G2PRegister, G2PPerson, G2PGeo):
    __tablename__ = "g2p_register_farmers"

    # Farmer Details - additional fields beyond G2PPerson base
    estimated_age: Mapped[int] = mapped_column(Integer, nullable=True)
    has_personal_phone: Mapped[bool] = mapped_column(Boolean, nullable=True)
    disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
    disability_type: Mapped[DisabilityTypeEnum] = mapped_column(String, nullable=True)       # DisabilityTypeEnum
    disability_severity: Mapped[DisabilitySeverityEnum] = mapped_column(String, nullable=True)   # DisabilitySeverityEnum
    source_of_income: Mapped[SourceOfIncomeEnum] = mapped_column(String, nullable=True)      # SourceOfIncomeEnum; use source_of_income_other when OTHERS (Excel)
    source_of_income_other: Mapped[str] = mapped_column(String, nullable=True)
    language_spoken: Mapped[str] = mapped_column(String, nullable=True)       # Attribute lookup (Excel: ISO-639-2 searchable dropdown)
    education_level: Mapped[EducationalLevelEnum] = mapped_column(String, nullable=True)       # EducationalLevelEnum
    # IDs - foundational_id (National ID) comes from G2PPerson
    # functional_record_id (Farmer ID) comes from G2PRegister
    national_id_masked: Mapped[str] = mapped_column(String, nullable=True)

    def get_record_name_fields(self) -> str:
        """Return farmer fields used to build record_name."""
        return G2PRegisterDomainServiceFarmer().construct_record_name(self.to_dict())

    def get_search_text_fields(self) -> str:
        """Return farmer fields used to build search_text."""
        return G2PRegisterDomainServiceFarmer().construct_search_text(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryFarmer(G2PRegisterHistory, G2PPersonHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_farmers"

    estimated_age: Mapped[int] = mapped_column(Integer, nullable=True)
    has_personal_phone: Mapped[bool] = mapped_column(Boolean, nullable=True)
    disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
    disability_type: Mapped[str] = mapped_column(String, nullable=True)
    disability_severity: Mapped[str] = mapped_column(String, nullable=True)
    source_of_income: Mapped[str] = mapped_column(String, nullable=True)
    source_of_income_other: Mapped[str] = mapped_column(String, nullable=True)
    language_spoken: Mapped[str] = mapped_column(String, nullable=True)
    national_id_masked: Mapped[str] = mapped_column(String, nullable=True)
