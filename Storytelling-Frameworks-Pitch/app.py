from prompts.classification import classify_strytell
from prompts.idea import generate_idea_input

storytelling_frameworks_expl_filepath = "strytell-theory\strytell-frameworks-explained.txt"
storytelling_classification_expl_filepath = "strytell-theory\strytell-classification-variables.txt"

def load_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def get_float_input(prompt, default):
    while True:
        try:
            return float(input(prompt) or default)
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    # Advanced settings prompt
    advanced_settings = input("Do you want to access advanced settings and other options? (y/n): ").lower()
    if advanced_settings == "y":
        model = input("Enter your 'model' (leave empty to use gpt-3.5-turbo): ") or 'gpt-3.5-turbo'
        temperature_classification = get_float_input("Enter your temperature for classification (leave empty to use 0.2): ", 0.2)
        temperature_idea = get_float_input("Enter your temperature for idea generation (leave empty to use 0.3): ", 0.3)
        frameworks_description = input("Do you want a description of the frameworks before prompting? (y/n): ").lower()
    else:
        model = 'gpt-3.5-turbo'
        temperature_classification = 0.2
        temperature_idea = 0.3
        frameworks_description = 'n'

    if frameworks_description == "y":
        storytelling_frameworks = load_text(storytelling_frameworks_expl_filepath)
        print("\n", storytelling_frameworks)
        input("\nPress Enter to continue...")
    
    while True:  # Outer loop for repeating the entire process
        storytelling_classification = load_text(storytelling_classification_expl_filepath)
        storytelling_classification_user = ''
        for line in storytelling_classification.splitlines():
            print("\n" + line)
            user_input = input("Enter a value for the variable: ")
            if user_input == "":
                pass
            variable = line.split(":")[0]
            storytelling_classification_user += f"{variable}: {user_input}\n"

        print("\n--- Dividing Line ---\n")
        print("You have given the following values for the variables:\n")
        print(storytelling_classification_user)
        print("\nFetching results...")

        while True:  # Inner loop for reclassification
            storytelling_classification_assistant = classify_strytell(storytelling_classification_user, model, temperature_classification)
            print("\n--- Dividing Line ---\n")
            print(storytelling_classification_assistant)

            # Ask the user if they want to redo classification
            repeat_classify = input("\nDo you want to redo classification? (y/n): ").lower()
            if repeat_classify != 'y':
                break

        while True:
            framework_selection_user = input("\nSelect framework that you want to use and press Enter to continue... (1/2/3): ") or '1'
            print("\nFetching results...")

            idea = generate_idea_input(storytelling_classification_user, storytelling_classification_assistant, framework_selection_user, model, temperature_idea)
            print("\n--- Dividing Line ---\n")
            print(idea)

            # Ask the user if they want to select a different framework
            repeat = input("\nDo you want to redo or select a different framework? (y/n): ").lower()
            if repeat != 'y':
                break
        
        # Ask the user if they want to restart the entire process
        restart = input("\nDo you want to restart the entire process with the same settings? (y/n): ").lower()
        if restart != 'y':
            break

    input("\nThanks! Press Enter to exit...")

if __name__ == "__main__":
    main()
