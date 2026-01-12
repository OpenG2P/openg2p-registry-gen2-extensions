import logging

from openg2p_registry_core.services import G2PRegisterDomainService
from openg2p_registry_core.schemas.payload import ChangeRequestRequestPayload

_logger = logging.getLogger('g2p-register-family-member-service')

class G2PRegisterFamilyMemberDomainService(G2PRegisterDomainService):
    pass

    async def validate_domain_attributes(self, change_request_request_payload: ChangeRequestRequestPayload):
        _logger.info("Validating family member domain attributes")
        pass
