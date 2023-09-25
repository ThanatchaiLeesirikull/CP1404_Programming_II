import wikipedia

# Set language to English (or any other preferred language)
wikipedia.set_lang("en")

exit_flag = False  # Initialize a flag variable

while not exit_flag:
    # Prompt the user for input
    user_input = input("Enter a page title or search phrase (or leave blank to exit): ")

    # Check if the user wants to exit
    if not user_input:
        exit_flag = True  # Set the flag to True to exit the loop
    else:
        try:
            # Use autosuggest=False to prevent unexpected suggestions
            page = wikipedia.page(user_input, auto_suggest=False)

            # Print page title, summary, and URL
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation Error: Multiple matching pages found. Please choose one:")
            for i, option in enumerate(e.options):
                print(f"{i + 1}. {option}")

        except wikipedia.exceptions.PageError:
            print("Page not found. Please try another search term.")
