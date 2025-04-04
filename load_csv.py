import csv
from app.graph_logic import GraphApp
from app.config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

# Connect to Neo4j
app = GraphApp(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)

# Path to CSV
csv_file = 'data/sample_data.csv'

with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            # Create nodes
            app.create_startup(row['startup'], int(row['year']), row['location'])
            app.create_founder(row['founder_name'], int(row['founder_age']), int(row['founder_experience']))
            app.create_investor(row['investor_name'], row['investor_firm'], row['investor_type'])
            app.create_sector(row['sector'])

            # Create relationships
            app.link_startup_to_founder(row['startup'], row['founder_name'])
            app.link_startup_to_investor(row['startup'], row['investor_name'])
            app.link_startup_to_sector(row['startup'], row['sector'])

            print(f"Loaded startup: {row['startup']}")
        except Exception as e:
            print(f"Error processing row: {row}")
            print(str(e))

# Close connection
app.close()
