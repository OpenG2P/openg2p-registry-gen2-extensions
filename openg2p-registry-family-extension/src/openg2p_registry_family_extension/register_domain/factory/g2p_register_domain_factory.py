from typing import Optional
from openg2p_fastapi_common.service import BaseService
from openg2p_registry_core.services import G2PRegisterDomainService

from ..services import G2PRegisterFamilyDomainService, G2PRegisterFamilyMemberDomainService

class G2PRegisterDomainFactory(BaseService):

    g2p_register_domain_service: G2PRegisterDomainService = None
    
    def get_domain_service(self, register_mnemonic: str) -> Optional[G2PRegisterDomainService]:
        if register_mnemonic.upper() == "FAMILY":
            g2p_register_domain_service = G2PRegisterFamilyDomainService.get_component()
            return g2p_register_domain_service
        if register_mnemonic.upper() == "FAMILYMEMBER":
            g2p_register_domain_service = G2PRegisterFamilyMemberDomainService.get_component()
            return g2p_register_domain_service
        return None