import logging

from openg2p_registry_core.services import G2PRegisterDomainService
from openg2p_registry_core.schemas import ChangeRequestRequestPayload

_logger = logging.getLogger('g2p-register-domain-service')

class G2PRegisterDomainServiceFarmer(G2PRegisterDomainService):

    async def validate_domain_attributes(self, change_request_request_payload: ChangeRequestRequestPayload):
        _logger.info("Validating farmer domain attributes")
        return


    def construct_record_name(self, payload: dict) -> str:
        _logger.info("Constructing record name for farmer")

        first_name = (payload.get("first_name") or "").strip()
        last_name = (payload.get("last_name") or "").strip()
        record_name = (payload.get("record_name") or "").strip()
        if first_name and last_name:
            record_name = f"{first_name} {last_name}"

        _logger.debug(f"Constructed record name for farmer: {record_name}")
        return record_name
