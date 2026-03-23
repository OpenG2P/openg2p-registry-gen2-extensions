from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaFarmInputs(G2PRegisterBaseSchema):
    """
    Schema for Farm Inputs / Inputs and Access to Resources register.
    Inherits fields from G2PRegisterBaseSchema.
    link_internal_record_id -> Land's internal_record_id
    """
    fertilizer_use: Optional[bool] = None
    pesticide_use: Optional[bool] = None
    insecticide_use: Optional[bool] = None
    improved_seed_use: Optional[bool] = None
    water_source: Optional[str] = None
    access_to_machinery: Optional[bool] = None
    access_to_finance: Optional[bool] = None


class G2PRegisterHistorySchemaFarmInputs(G2PRegisterHistorySchema):
    """
    Schema for Farm Inputs history.
    Inherits fields from G2PRegisterHistorySchema.
    """
    fertilizer_use: Optional[bool] = None
    pesticide_use: Optional[bool] = None
    insecticide_use: Optional[bool] = None
    improved_seed_use: Optional[bool] = None
    water_source: Optional[str] = None
    access_to_machinery: Optional[bool] = None
    access_to_finance: Optional[bool] = None
