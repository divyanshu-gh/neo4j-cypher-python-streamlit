
from neo4j import GraphDatabase

class GraphApp:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def create_startup(self, name, year, location):
        query = """
        MERGE (s:Startup {name: $name})
        ON CREATE SET s.year = $year, s.location = $location
        """
        with self.driver.session() as session:
            session.run(query, name=name, year=year, location=location)

    def create_founder(self, name, age, experience):
        query = """
        MERGE (f:Founder {name: $name})
        ON CREATE SET f.age = $age, f.experience = $experience
        """
        with self.driver.session() as session:
            session.run(query, name=name, age=age, experience=experience)

    def create_investor(self, name, firm, investor_type):
        query = """
        MERGE (i:Investor {name: $name})
        ON CREATE SET i.firm = $firm, i.investor_type = $investor_type
        """
        with self.driver.session() as session:
            session.run(query, name=name, firm=firm, investor_type=investor_type)

    def create_sector(self, name):
        query = """
        MERGE (sec:Sector {name: $name})
        """
        with self.driver.session() as session:
            session.run(query, name=name)

    def link_startup_to_founder(self, startup_name, founder_name):
        query = """
        MATCH (s:Startup {name: $startup_name})
        MATCH (f:Founder {name: $founder_name})
        MERGE (s)-[:FOUNDED_BY]->(f)
        """
        with self.driver.session() as session:
            session.run(query, startup_name=startup_name, founder_name=founder_name)

    def link_startup_to_investor(self, startup_name, investor_name):
        query = """
        MATCH (s:Startup {name: $startup_name})
        MATCH (i:Investor {name: $investor_name})
        MERGE (s)-[:FUNDED_BY]->(i)
        """
        with self.driver.session() as session:
            session.run(query, startup_name=startup_name, investor_name=investor_name)

    def link_startup_to_sector(self, startup_name, sector_name):
        query = """
        MATCH (s:Startup {name: $startup_name})
        MATCH (sec:Sector {name: $sector_name})
        MERGE (s)-[:OPERATES_IN]->(sec)
        """
        with self.driver.session() as session:
            session.run(query, startup_name=startup_name, sector_name=sector_name)

    def get_all_startups(self):
        query = """
        MATCH (s:Startup)
        OPTIONAL MATCH (s)-[:FOUNDED_BY]->(f:Founder)
        OPTIONAL MATCH (s)-[:FUNDED_BY]->(i:Investor)
        OPTIONAL MATCH (s)-[:OPERATES_IN]->(sec:Sector)
        RETURN DISTINCT s.name AS startup, s.year AS year, s.location AS location,
                        f.name AS founder, i.name AS investor, sec.name AS sector
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]
