from neo4j import GraphDatabase

uri = "bolt://3.239.40.139:7687"
username = "neo4j"
password = "mixes-results-labels"

class Neo4jApp:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_person(self, name):
        with self.driver.session() as session:
            result = session.run("CREATE (a:Person {name: $name}) RETURN a.name", name=name)
            for record in result:
                print("Created person:", record["a.name"])

    def get_all_persons(self):
        with self.driver.session() as session:
            result = session.run("MATCH (a:Person) RETURN a.name AS name")
            print("All Persons in DB:")
            for record in result:
                print("-", record["name"])

    def update_person(self, old_name, new_name):
        with self.driver.session() as session:
            session.run(
                "MATCH (a:Person {name: $old}) SET a.name = $new",
                old=old_name, new=new_name
            )
            print(f"Updated {old_name} to {new_name}")

    def delete_person(self, name):
        with self.driver.session() as session:
            session.run("MATCH (a:Person {name: $name}) DELETE a", name=name)
            print(f"Deleted person: {name}")

    def create_friendship(self, name1, name2):
        with self.driver.session() as session:
            session.run("""
                MATCH (a:Person {name: $name1}), (b:Person {name: $name2})
                CREATE (a)-[:FRIENDS_WITH]->(b)
            """, name1=name1, name2=name2)
            print(f"{name1} is now friends with {name2}")



if __name__ == "__main__":
    app = Neo4jApp(uri, username, password)

    
    app.create_person("Harsh")
    app.create_person("Disha")
    app.create_person("Aryan")

    
    app.create_friendship("Harsh", "Disha")
    app.create_friendship("Harsh", "Aryan")

    
    app.get_all_persons()

    
    app.update_person("Aryan", "Aryan Raj")

   
    app.delete_person("Disha")

    
    app.get_all_persons()

    app.close()