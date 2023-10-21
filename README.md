# Account-Manager




It's a simple command-line tool that allows users to manage and store profiles with usernames and passwords. The primary functions of your program include:

Adding Profiles: Users can add profiles by providing a username and password. The program records the date and time the profile was created.

Showing Profiles: Users can list and view all existing profiles. The program hides usernames and passwords with asterisks for added security, ensuring sensitive information is not easily visible.

Deleting Profiles: Users can delete specific profiles by entering the profile number or delete all profiles at once.

Clearing the Terminal: Users can clear the terminal screen, providing a clean and organized workspace.

Exiting the Program: Users can gracefully exit the program, saving the profiles to a JSON file.

JSON File Handling: The program loads existing profiles from a JSON file at startup and saves the profiles to the same JSON file upon exit.

Data Masking: Profiles displayed in the terminal are masked, showing asterisks instead of the actual username and password for added privacy.

Overall, this program serves as a basic password manager. It allows users to store, manage, and view profiles securely while maintaining a record of when each profile was created. The combination of features makes it a useful utility for individuals who want a straightforward way to organize and protect their login credentials.

