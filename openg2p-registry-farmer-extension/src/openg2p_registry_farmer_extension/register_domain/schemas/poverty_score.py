from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaPovertyScore(G2PRegisterBaseSchema):
    """
    Schema for Poverty Score register.
    Inherits fields from G2PRegisterBaseSchema.
    link_internal_record_id -> Household's internal_record_id
    """
    poverty_score: Optional[str] = None
    poverty_score_type: Optional[str] = None


class G2PRegisterHistorySchemaPovertyScore(G2PRegisterHistorySchema):
    """
    Schema for Poverty Score history.
    Inherits fields from G2PRegisterHistorySchema.
    """
    poverty_score: Optional[str] = None
    poverty_score_type: Optional[str] = None
