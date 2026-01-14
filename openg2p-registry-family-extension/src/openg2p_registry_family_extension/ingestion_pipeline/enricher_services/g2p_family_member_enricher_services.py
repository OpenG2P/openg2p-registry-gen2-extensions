import logging
from typing import Dict
from sqlalchemy.orm import Session
from sqlalchemy import select
from openg2p_registry_core.interfaces import G2PPayloadEnricherInterface
from ...register_domain.models import G2PRegisterFamilyMember


_logger = logging.getLogger('g2p-payload-enricher-service')

# DCI Payload Enrichers
class G2PDciFamilyMemberCreateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PDciFamilyMemberCreateEnricherService")

        parent_link_internal_record_id = None

        # Extract identifier value from possible structures
        def extract_identifier_value(identifier_block: Dict) -> str | None:
            """
            Supports:
            - member_identifier
            - spdci:member_identifier
            """
            if not isinstance(identifier_block, dict):
                return None

            return (
                identifier_block.get("member_identifier")
                or identifier_block.get("spdci:member_identifier")
                or identifier_block.get("identifier_value")
            )
        
        related_persons = data.get('related_person')

        # Parent lookup (ORDER: parent1 → parent2)
        for related_person in related_persons:
            parent_identifier_data = related_person.get('related_member')

            identifier_value = extract_identifier_value(parent_identifier_data)
            if not identifier_value:
                continue

            _logger.debug(
                f"Checking for parent family member via related_member: {identifier_value}"
            )

            parent_family_member = session.execute(
                select(G2PRegisterFamilyMember).filter_by(
                    foundational_id=identifier_value
                )
            ).scalar_one_or_none()

            if parent_family_member:
                parent_link_internal_record_id = (
                    parent_family_member.link_internal_record_id
                )
                _logger.info(
                    f"Found parent family member via related_member. "
                    f"Link record ID: {parent_link_internal_record_id}"
                )
                break

        # Set link_internal_record_id
        if parent_link_internal_record_id:
            data["link_internal_record_id"] = parent_link_internal_record_id
        else:
            _logger.warning(
                "Could not find a parent family member using related_member identifier."
            )
            data["link_internal_record_id"] = None

        # Foundational ID resolution (NationalID)
        identifiers = data.get("identifiers") or []

        if isinstance(identifiers, list):
            for ident in identifiers:
                if not isinstance(ident, dict):
                    continue

                if ident.get("identifier_type") == "NationalID":
                    national_id_value = ident.get("identifier_value")
                    if national_id_value:
                        data["foundational_id"] = national_id_value
                        _logger.info(
                            f"Found NationalID. Set foundational_id: {national_id_value}"
                        )
                        break

        return data

class G2PDciFamilyMemberUpdateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PDciFamilyMemberUpdateEnricherService")
        return data

class G2PDciFamilyMemberDeleteEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PDciFamilyMemberDeleteEnricherService")
        return data

# SPDCI Payload Enrichers
class G2PSpdciFamilyMemberCreateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PSpdciFamilyMemberCreateEnricherService")
        return data

class G2PSpdciFamilyMemberUpdateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PSpdciFamilyMemberUpdateEnricherService")
        return data

class G2PSpdciFamilyMemberDeleteEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PSpdciFamilyMemberDeleteEnricherService")
        return data

# UNDP Payload Enrichers
class G2PUndpFamilyMemberCreateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PUndpFamilyMemberCreateEnricherService")
        return data

class G2PUndpFamilyMemberUpdateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PUndpFamilyMemberUpdateEnricherService")
        return data

class G2PUndpFamilyMemberDeleteEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PUndpFamilyMemberDeleteEnricherService")
        return data
