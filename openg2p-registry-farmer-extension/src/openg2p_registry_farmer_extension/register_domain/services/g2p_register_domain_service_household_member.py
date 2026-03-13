import logging

from openg2p_registry_core.services import G2PRegisterDomainService
from openg2p_registry_core.schemas import ChangeRequestRequestPayload

_logger = logging.getLogger('g2p-register-domain-service')

class G2PRegisterDomainServiceHouseholdMember(G2PRegisterDomainService):

    async def validate_domain_attributes(self, change_request_request_payload: ChangeRequestRequestPayload):
        _logger.info("Validating farmer domain attributes")
        return

    def construct_record_name(self, payload: dict) -> str:
        _logger.info("Constructing record name for household member")

        first_name = (payload.get("first_name") or "").strip()
        last_name = (payload.get("last_name") or "").strip()
        return " ".join(filter(None, [first_name, last_name])).strip()
