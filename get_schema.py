import requests
import json

# The full introspection query
introspection_query = """
query IntrospectionQuery {
    __schema {
        queryType { name }
        mutationType { name }
        subscriptionType { name }
        types {
            ...FullType
        }
        directives {
            name
            description
            locations
            args {
                ...InputValue
            }
        }
    }
}

fragment FullType on __Type {
    kind
    name
    description
    fields(includeDeprecated: true) {
        name
        description
        args {
            ...InputValue
        }
        type {
            ...TypeRef
        }
        isDeprecated
        deprecationReason
    }
    inputFields {
        ...InputValue
    }
    interfaces {
        ...TypeRef
    }
    enumValues(includeDeprecated: true) {
        name
        description
        isDeprecated
        deprecationReason
    }
    possibleTypes {
        ...TypeRef
    }
}

fragment InputValue on __InputValue {
    name
    description
    type { ...TypeRef }
    defaultValue
}

fragment TypeRef on __Type {
    kind
    name
    ofType {
        kind
        name
        ofType {
            kind
            name
            ofType {
                kind
                name
                ofType {
                    kind
                    name
                    ofType {
                        kind
                        name
                        ofType {
                            kind
                            name
                            ofType {
                                kind
                                name
                            }
                        }
                    }
                }
            }
        }
    }
}
"""

def get_schema():
    # Get token from Redis (you'll need to implement this part)
    # For now, we'll use a placeholder token
    token = "YOUR_LINEAR_TOKEN"  # Replace with actual token
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    response = requests.post(
        "https://api.linear.app/graphql",
        json={"query": introspection_query},
        headers=headers
    )
    
    if response.status_code == 200:
        with open("linear_schema.json", "w") as f:
            json.dump(response.json(), f, indent=2)
        print("Schema saved to linear_schema.json")
    else:
        print(f"Error fetching schema: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    get_schema() 