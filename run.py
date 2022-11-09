from src import main

if __name__ == "__main__":
    schema = input(
        """
        Press Just the number of the schema to use:\n
        Which Schema will be used?\n
1. Assitence \n
2. Workshop\n
3. Committe\n
[1,2,3] -> 1 by default : """
    )
    schemas = {1: "assistance", 2: "workshop", 3: "committe"}
    if not schema in schemas:
        schema = 1
    main(schemas[schema])
