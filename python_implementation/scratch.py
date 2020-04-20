import json
from graphqlclient import GraphQLClient



def make_client() -> GraphQLClient:
    client = GraphQLClient('https://admin-next.airbnb.com/api/v3')
    # Add api token if needed
    # client.inject_token()
    return client

def test_airbnb():
    client = make_client()
    QUERY = """
        query {
            causes {
                presentDisasterResponseLandingPage {
                    disasters {
                        name,
                        id,
                        canonicalName
                    }
                }
            }
        }
    """
    data = client.execute(query=QUERY)
    data = json.loads(data)
    print(json.dumps(data, indent=4, sort_keys=True))


test_airbnb()
