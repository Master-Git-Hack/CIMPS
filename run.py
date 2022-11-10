from src import main

if __name__ == "__main__":
    schemas = {1: "assistance", 2: "workshop", 3: "committe"}
    from_file = input(
        f"Do you want to use a file? \n The file must be in schemas folder.\n The filename must be one of these{schemas} \n[y/N]: "
    )
    from_file = from_file.lower() == "y"
    schema = input(
        f"""
        Press JUST the number of the schema to use:\n
        Which Schema will be used?\n
        {schemas}
[1,2,3] -> 1 by default : """
    )

    if not schema in schemas:
        schema = 1
    main(schemas[schema], from_file)
