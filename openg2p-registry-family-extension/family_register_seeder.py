"""
Family Register Seeder Script

This script creates 25 family records with complete data including:
- Family information
- 1-5 family members per family

Usage:
    python family_register_seeder.py

Features:
    - Runs all database migrations for family extension models (excluding history)
    - Seeds register definitions with schema configurations
    - Creates 25 complete family records with all related data
"""

# IMPORTANT: Set environment variables and paths BEFORE any other imports
import os
import sys
from pathlib import Path

# Add local src directories to Python path for local development
SCRIPT_DIR = Path(__file__).resolve().parent
SRC_DIR = SCRIPT_DIR / "src"
CORE_SRC_DIR = SCRIPT_DIR.parent.parent / "openg2p-registry-gen2" / "openg2p-registry-core" / "src"

if CORE_SRC_DIR.exists():
    sys.path.insert(0, str(CORE_SRC_DIR))
if SRC_DIR.exists():
    sys.path.insert(0, str(SRC_DIR))

# Database configuration - Update these values for your environment
DB_DRIVER = "postgresql+asyncpg"
DB_USERNAME = "postgres"
DB_PASSWORD = "password"
DB_HOSTNAME = "localhost"
DB_PORT = "5436"
DB_DBNAME = "registry-gen2-family_db"

# Set environment variables for ALL possible prefixes used by different modules
# openg2p_fastapi_common uses env_prefix="common_"
# registry_core uses env_prefix="registry_core_"
# registry_extensions uses env_prefix="registry_extensions_"
for prefix in [
    "COMMON_",
    "REGISTRY_STAFF_PORTAL_API_",
    "REGISTRY_CORE_",
    "REGISTRY_EXTENSIONS_",
    ""
]:
    os.environ[f"{prefix}DB_DRIVER"] = DB_DRIVER
    os.environ[f"{prefix}DB_USERNAME"] = DB_USERNAME
    os.environ[f"{prefix}DB_PASSWORD"] = DB_PASSWORD
    os.environ[f"{prefix}DB_HOSTNAME"] = DB_HOSTNAME
    os.environ[f"{prefix}DB_PORT"] = DB_PORT
    os.environ[f"{prefix}DB_DBNAME"] = DB_DBNAME

import asyncio
import uuid
import random
import csv
from datetime import datetime, date, timedelta

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import select

DATABASE_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_DBNAME}"

# Initialize the application context
from openg2p_registry_core.app import Initializer as CoreInitializer

# Initialize core
CoreInitializer().initialize()

from openg2p_registry_family_extension.register_domain.models import (
    G2PRegisterFamily,
    G2PRegisterFamilyMember,
)
from openg2p_registry_core.models import (
    G2PRegisterDefinition,
    G2PRegisterSchema,
    G2PRegistryConfiguration,
    RegisterPurposeEnum
)


class FamilyRegisterSeeder:
    """Seeder for family register with complete family member data"""

    # Sample data for realistic generation
    FIRST_NAMES = [
        "Rajesh", "Priya", "Amit", "Deepa", "Suresh", "Anita", "Vikram", "Neha",
        "Arjun", "Pooja", "Ramesh", "Divya", "Sanjay", "Kavya", "Arun", "Sneha",
        "Kiran", "Meera", "Ravi", "Sunita", "Mohan", "Lakshmi", "Naveen", "Radha"
    ]

    LAST_NAMES = [
        "Kumar", "Singh", "Patel", "Sharma", "Gupta", "Verma", "Rao", "Nair",
        "Desai", "Iyer", "Reddy", "Bhat", "Joshi", "Mishra", "Pandey", "Sinha",
        "Mehta", "Chopra", "Malhotra", "Kapoor", "Agarwal", "Jain", "Shah", "Bansal"
    ]

    FAMILY_NAMES = [
        "The Kumar Family", "The Singh Family", "The Patel Family", "The Sharma Family",
        "The Gupta Family", "The Verma Family", "The Rao Family", "The Nair Family"
    ]

    HOUSING_TYPES = ["Apartment", "House", "Cottage", "Villa", "Townhouse", "Duplex"]
    HOUSE_CONDITIONS = ["Excellent", "Good", "Fair", "Poor", "Very Poor"]
    SANITATION_CONDITIONS = ["Flush Toilet", "Pit Latrine", "Bucket", "Open Defecation", "None"]
    WATER_ACCESS = ["Piped Water", "Well", "Hand Pump", "Borewell", "Tanker", "River/Pond"]
    ELECTRICITY_ACCESS = ["Grid Connected", "Solar", "Generator", "None"]
    ETHNIC_GROUPS = ["Group A", "Group B", "Group C", "Group D", "Group E"]

    GENDERS = ["MALE", "FEMALE"]
    MARITAL_STATUSES = ["SINGLE", "MARRIED", "WIDOWED", "DIVORCED", "SEPARATED"]
    EDUCATION_LEVELS = ["No Education", "Primary", "Secondary", "Higher Secondary", "Graduate", "Post Graduate"]
    EMPLOYMENT_STATUSES = ["Employed", "Unemployed", "Self-Employed", "Student", "Homemaker", "Retired"]
    RELATIONSHIPS = ["Head", "Spouse", "Child", "Parent", "Sibling", "Other Relative", "Non-Relative"]
    ROLES = ["Head", "Member", "Dependent"]
    INCOME_SOURCES = ["Salary", "Business", "Agriculture", "Pension", "Remittance", "Other"]
    INCOME_LEVELS = ["Low", "Medium", "High"]
    LAND_TYPES = ["Agricultural", "Residential", "Commercial", "Mixed"]
    OCCUPATIONS = ["Farmer", "Laborer", "Trader", "Student", "Homemaker", "Teacher", "Carpenter"]
    LANGUAGE_CODES = ["en", "hi", "ta", "te", "kn", "ml", "mr", "gu", "bn"]
    COUNTRY_CODES = ["IN"]

    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL, echo=False)
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False)
        self.system_user = "seeder"
        self.now = datetime.now()
        self.locations = self._load_locations()

    def _load_locations(self) -> list[dict]:
        """Load locations from CSV file"""
        locations_file = SCRIPT_DIR / "locations.csv"
        locations = []
        if locations_file.exists():
            with open(locations_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    locations.append({
                        'admin2Pcode': row['admin2Pcode'],  # small area
                        'admin1Pcode': row['admin1Pcode'],  # large area
                        'admin2Name': row['admin2Name_en'],
                        'admin1Name': row['admin1Name_en'],
                    })
        if not locations:
            # Fallback if file not found
            locations = [{'admin2Pcode': 'DEFAULT_SMALL', 'admin1Pcode': 'DEFAULT_LARGE', 'admin2Name': 'Default', 'admin1Name': 'Default'}]
        return locations

    def get_random_location(self) -> dict:
        """Get a random location from loaded locations"""
        return random.choice(self.locations)

    def generate_family_id(self) -> str:
        """Generate unique family ID"""
        return f"FAMILY-{uuid.uuid4().hex[:8].upper()}"

    def generate_random_birth_date(self, min_age: int = 0, max_age: int = 80) -> date:
        """Generate random birth date"""
        days_back = random.randint(min_age * 365, max_age * 365)
        return date.today() - timedelta(days=days_back)

    def generate_geo_coordinates(self) -> tuple[str, str, str]:
        """Generate random geo coordinates for India region (as strings for DB)"""
        latitude = str(round(random.uniform(8.0, 35.0), 6))
        longitude = str(round(random.uniform(68.0, 97.0), 6))
        altitude = str(round(random.uniform(0, 2000), 2))
        return latitude, longitude, altitude

    def generate_plus_code(self, lat: str, lng: str) -> str:
        """Generate a simple plus code approximation"""
        return f"{int(float(lat)*100):04d}+{int(float(lng)*100):04d}"

    def create_family(self) -> G2PRegisterFamily:
        """Create a single family record"""
        family_name = random.choice(self.FAMILY_NAMES)

        family = G2PRegisterFamily(
            internal_record_id=str(uuid.uuid4()),
            functional_record_id=self.generate_family_id(),
            record_name=family_name,
            family_name=family_name,
            type_of_housing=random.choice(self.HOUSING_TYPES),
            house_condition=random.choice(self.HOUSE_CONDITIONS),
            sanitation_condition=random.choice(self.SANITATION_CONDITIONS),
            water_access=random.choice(self.WATER_ACCESS),
            electricity_access=random.choice(self.ELECTRICITY_ACCESS),
            ethnic_group=random.choice(self.ETHNIC_GROUPS),
            belong_to_protected_groups=random.choice([True, False]),
            under_other_vulnerable_status=random.choice([True, False]),
            created_by=self.system_user,
            created_at=self.now,
            last_approved_at=self.now,
            last_approved_by=self.system_user,
        )
        return family

    def create_family_members(self, family: G2PRegisterFamily, count: int) -> list:
        """Create family members with G2PPerson and G2PGeo fields"""
        members = []
        head_created = False
        
        for i in range(count):
            first_name = random.choice(self.FIRST_NAMES)
            last_name = random.choice(self.LAST_NAMES)
            gender = random.choice(self.GENDERS)
            
            is_head = not head_created and i == 0
            if is_head:
                head_created = True
                relationship = "Head"
                role = "Head"
            else:
                relationship = random.choice(["Spouse", "Child", "Parent", "Sibling", "Other Relative"])
                role = random.choice(["Member", "Dependent"])

            # Generate geo coordinates
            lat, lng, alt = self.generate_geo_coordinates()
            location = self.get_random_location()
            
            member = G2PRegisterFamilyMember(
                internal_record_id=str(uuid.uuid4()),
                functional_record_id=f"FAM-MEM-{uuid.uuid4().hex[:8].upper()}",
                record_name=f"{first_name} {last_name}",
                link_internal_record_id=family.internal_record_id,
                
                # G2PPerson fields
                foundational_id=f"UIN-{random.randint(100000000, 999999999)}",
                first_name=first_name,
                middle_name=random.choice(self.FIRST_NAMES) if random.random() > 0.7 else None,
                last_name=last_name,
                given_name=first_name,
                prefix="Mr." if gender == "MALE" else "Ms.",
                suffix="",
                gender=gender,
                birth_date=self.generate_random_birth_date(min_age=0, max_age=80),
                phone_numbers=[{
                    "type": "mobile",
                    "number": f"+91{random.randint(6000000000, 9999999999)}",
                    "is_primary": True
                }],
                emails=[{
                    "type": "personal",
                    "address": f"{first_name.lower()}.{last_name.lower()}@family.local",
                    "is_primary": True
                }],
                marital_status=random.choice(self.MARITAL_STATUSES),
                occupation=random.choice(self.OCCUPATIONS),
                income_level=random.choice(self.INCOME_LEVELS),
                language_code=random.choice(self.LANGUAGE_CODES),
                education_level=random.choice(self.EDUCATION_LEVELS),
                registration_date=date.today(),
                
                # G2PGeo fields
                latitude=lat,
                longitude=lng,
                altitude=alt,
                plus_code=self.generate_plus_code(lat, lng),
                address_line_1=f"{random.randint(1, 999)} {random.choice(['Main', 'Village', 'Street'])} Road",
                address_line_2=location['admin2Name'],
                postal_code=f"{random.randint(100000, 999999)}",
                country_code=random.choice(self.COUNTRY_CODES),
                # Note: Not setting geo_lowest_level_value_id to avoid triggering service call
                geo_code_hierarchy_json={
                    "lowest_level_value_id": location['admin2Pcode'],
                    "hierarchy": [
                        {"level": "admin1", "level_value_mnemonic": location['admin1Name'], "level_value_id": location['admin1Pcode']},
                        {"level": "admin2", "level_value_mnemonic": location['admin2Name'], "level_value_id": location['admin2Pcode']}
                    ]
                },
                
                # FamilyMember-specific fields
                marriage_date=self.generate_random_birth_date(min_age=18, max_age=50).isoformat() if random.random() > 0.5 else None,
                divorce_date=None,
                employment_status=random.choice(self.EMPLOYMENT_STATUSES),
                role_in_household=role,
                relationship_with_household_head=relationship,
                sources_of_income=random.choice(self.INCOME_SOURCES),
                annual_income=random.choice(self.INCOME_LEVELS),
                owns_a_two_wheeler=random.choice([True, False]),
                owns_a_three_wheeler=random.choice([True, False]),
                owns_a_four_wheeler=random.choice([True, False]),
                owns_a_cart=random.choice([True, False]),
                land_ownership=random.choice([True, False]),
                type_of_land_owned=random.choice(self.LAND_TYPES) if random.random() > 0.5 else None,
                land_size=f"{random.randint(1, 50)}" if random.random() > 0.5 else None,
                owns_house=random.choice([True, False]),
                owns_livestock=random.choice([True, False]),
                is_head=is_head,
                is_disabled=random.choice([True, False, False, False]),  # 25% chance
                is_pregnant_and_lactating=random.choice([True, False, False]) if gender == "FEMALE" else False,
                is_malnourished_child=random.choice([True, False, False, False, False]),  # 20% chance
                
                # Audit fields
                created_by=self.system_user,
                created_at=self.now,
                last_approved_at=self.now,
                last_approved_by=self.system_user,
            )
            members.append(member)
        return members

    def get_family_schema_config(self):
        """Get schema configuration for Family register"""
        return {
            'search_result_schema': [
                {"field_name": "family_name", "display_label": "Family Name", "order": 1},
                {"field_name": "type_of_housing", "display_label": "Type of Housing", "order": 2},
                {"field_name": "house_condition", "display_label": "House Condition", "order": 3},
                {"field_name": "ethnic_group", "display_label": "Ethnic Group", "order": 4}
            ],
            'filter_schema': [
                {"field_name": "family_name", "display_label": "Family Name", "filter_type": "text", "order": 1, "allowed_operators": ["eq", "contains"]},
                {"field_name": "type_of_housing", "display_label": "Type of Housing", "filter_type": "dropdown", "order": 2, "allowed_operators": ["eq", "in"], "options_source": "distinct"},
                {"field_name": "house_condition", "display_label": "House Condition", "filter_type": "dropdown", "order": 3, "allowed_operators": ["eq", "in"], "options_source": "distinct"},
                {"field_name": "ethnic_group", "display_label": "Ethnic Group", "filter_type": "dropdown", "order": 4, "allowed_operators": ["eq", "in"], "options_source": "distinct"}
            ],
            'deduplicate_schema': [
                {"field_name": "family_name", "match_type": "fuzzy", "weight": 0.5},
                {"field_name": "type_of_housing", "match_type": "exact", "weight": 0.3},
                {"field_name": "house_condition", "match_type": "exact", "weight": 0.2}
            ]
        }

    def get_family_member_schema_config(self):
        """Get schema configuration for Family Member register"""
        return {
            'search_result_schema': [
                {"field_name": "first_name", "display_label": "First Name", "order": 1},
                {"field_name": "last_name", "display_label": "Last Name", "order": 2},
                {"field_name": "gender", "display_label": "Gender", "order": 3},
                {"field_name": "birth_date", "display_label": "Birth Date", "order": 4},
                {"field_name": "relationship_with_household_head", "display_label": "Relationship", "order": 5}
            ],
            'filter_schema': [
                {"field_name": "first_name", "display_label": "First Name", "filter_type": "text", "order": 1, "allowed_operators": ["eq", "contains"]},
                {"field_name": "last_name", "display_label": "Last Name", "filter_type": "text", "order": 2, "allowed_operators": ["eq", "contains"]},
                {"field_name": "gender", "display_label": "Gender", "filter_type": "dropdown", "order": 3, "allowed_operators": ["eq", "in"], "options_source": "distinct"},
                {"field_name": "relationship_with_household_head", "display_label": "Relationship", "filter_type": "dropdown", "order": 4, "allowed_operators": ["eq", "in"], "options_source": "distinct"},
                {"field_name": "education_level", "display_label": "Education Level", "filter_type": "dropdown", "order": 5, "allowed_operators": ["eq", "in"], "options_source": "distinct"}
            ],
            'deduplicate_schema': [
                {"field_name": "first_name", "match_type": "fuzzy", "weight": 0.3},
                {"field_name": "last_name", "match_type": "fuzzy", "weight": 0.3},
                {"field_name": "birth_date", "match_type": "exact", "weight": 0.4}
            ]
        }

    async def seed_registry_configuration(self, session):
        """Seed global registry configuration"""
        print("Seeding Registry Configuration...")
        result = await session.execute(select(G2PRegistryConfiguration))
        if not result.scalar():
            config = G2PRegistryConfiguration(
                registry_name="G2P Family Registry",
                registry_logo=None
            )
            session.add(config)
            print("  ✓ Added registry configuration")
        else:
            print("  ✓ Registry configuration already exists")

    async def verify_register_definitions(self, session):
        """Verify that required register definitions exist, create if missing"""
        register_definitions = [
            {'register_mnemonic': 'Family', 'register_subject': 'Families', 'register_description': 'Family Register', 'schema_config': self.get_family_schema_config()},
            {'register_mnemonic': 'FamilyMember', 'register_subject': 'Family Members', 'register_description': 'Family Member Register', 'schema_config': self.get_family_member_schema_config()},
        ]

        for register_def in register_definitions:
            result = await session.execute(
                select(G2PRegisterDefinition).where(G2PRegisterDefinition.register_mnemonic == register_def['register_mnemonic'])
            )
            if not result.scalar():
                print(f"Creating register definition: {register_def['register_mnemonic']}")
                register_id = str(uuid.uuid4())
                register_definition = G2PRegisterDefinition(
                    register_id=register_id,
                    register_mnemonic=register_def['register_mnemonic'],
                    register_subject=register_def['register_subject'],
                    register_description=register_def['register_description'],
                    register_purpose=RegisterPurposeEnum.REGISTER.value,
                    dedup_is_enabled=False,
                    dedup_threshold_score=0.0
                )
                session.add(register_definition)

                schema_config = register_def['schema_config']
                register_schema = G2PRegisterSchema(
                    register_id=register_id,
                    deduplicate_schema=schema_config['deduplicate_schema'],
                    search_result_schema=schema_config['search_result_schema'],
                    filter_schema=schema_config['filter_schema']
                )
                session.add(register_schema)

        await session.commit()
        return True

    async def seed_families(self, session):
        """Seed 25 families with complete data"""
        print("Seeding Family records...")

        family_count = 0
        member_count = 0

        for i in range(25):
            print(f"  Creating family {i+1}/25...")

            # Create family
            family = self.create_family()
            session.add(family)
            await session.flush()
            family_count += 1

            # Create family members (1-5 per family)
            num_members = random.randint(1, 5)
            members = self.create_family_members(family, num_members)
            for member in members:
                session.add(member)
            await session.flush()
            member_count += num_members

        return family_count, member_count

    async def run(self):
        """Execute the seeding process"""
        async with self.async_session() as session:
            try:
                # Seed registry configuration first
                await self.seed_registry_configuration(session)

                # Verify register definitions
                if not await self.verify_register_definitions(session):
                    return False

                # Seed data
                counts = await self.seed_families(session)

                # Commit all changes
                await session.commit()

                print("\n✓ Family register seeding completed successfully!")
                print(f"  - {counts[0]} Family records created")
                print(f"  - {counts[1]} Family Member records created")
                return True

            except Exception as e:
                await session.rollback()
                print(f"\n✗ Error during seeding: {str(e)}")
                import traceback
                traceback.print_exc()
                return False


async def create_search_text_indexes(engine):
    """Create trigram indexes on search_text columns for full-text search"""
    from sqlalchemy import text
    
    tables = [
        G2PRegisterFamily.__tablename__,
        G2PRegisterFamilyMember.__tablename__,
    ]
    
    async with engine.begin() as conn:
        # Ensure pg_trgm extension exists
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS pg_trgm"))
        
        for table in tables:
            index_name = f"idx_{table}_search_text_trigram"
            # Use IF NOT EXISTS to avoid errors if index already exists
            await conn.execute(text(
                f'CREATE INDEX IF NOT EXISTS {index_name} ON {table} USING gin (search_text gin_trgm_ops)'
            ))
            print(f"  ✓ Created index {index_name}")


async def main():
    """Main entry point"""
    # First, ensure migrations are run
    print("Running database migrations for family extension models...")
    try:
        # Run family extension migrations (excluding history models)
        await G2PRegisterFamily.create_migrate()
        await G2PRegisterFamilyMember.create_migrate()

        print("✓ Database migrations completed\n")
    except Exception as e:
        print(f"✗ Migration error: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)

    # Create search_text indexes
    print("Creating search_text trigram indexes...")
    try:
        from sqlalchemy.ext.asyncio import create_async_engine
        engine = create_async_engine(DB_URL)
        await create_search_text_indexes(engine)
        await engine.dispose()
        print("✓ Indexes created\n")
    except Exception as e:
        print(f"✗ Index creation error: {str(e)}")
        import traceback
        traceback.print_exc()

    # Now run the seeder
    seeder = FamilyRegisterSeeder()
    success = await seeder.run()
    exit(0 if success else 1)


if __name__ == "__main__":
    asyncio.run(main())
