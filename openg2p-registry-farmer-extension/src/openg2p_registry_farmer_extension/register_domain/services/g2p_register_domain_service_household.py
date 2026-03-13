import logging

from openg2p_registry_core.services import G2PRegisterDomainService
from openg2p_registry_core.schemas import ChangeRequestRequestPayload

_logger = logging.getLogger('g2p-register-domain-service')

class G2PRegisterDomainServiceHousehold(G2PRegisterDomainService):

    async def validate_domain_attributes(self, change_request_request_payload: ChangeRequestRequestPayload):
        _logger.info("Validating farmer domain attributes")
        return

    def construct_record_name(self, payload: dict) -> str:
        _logger.info("Constructing record name for household")

        head_or_id = (
            (payload.get("household_head") or "").strip()
            or (payload.get("functional_record_id") or "").strip()
        )

        return f"{head_or_id} Household".strip()
