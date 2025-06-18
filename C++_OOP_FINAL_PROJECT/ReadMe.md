TOPIC: Contact Management with Groups
#include <iostream> - Allows printing and taking input in the console.
#include <cstring>- Provides functions to handle C-style strings.
#include <stdexcept> - Gives access to standard error-handling mechanisms (not used in this code).
Struct: Contact**
struct Contact { - Defines a simple structure to hold a name and phone number.
char name[30]; - An array of characters to store the name (max 29 characters + 1 for null terminator).
char phone[15]; - An array of characters to store the phone number (max 14 characters + 1 for null terminator).
};`- Ends the Contact structure definition.
BaseContact Class (Abstract)**
class BaseContact {- Defines a base class with common properties for contacts.
public:- Makes following methods accessible anywhere.
virtual ~BaseContact() {} - Defines a virtual destructor to ensure proper cleanup.
virtual void showInfo() const = 0; - A pure virtual function that must be implemented by subclasses.
virtual const char* getName() const = 0; - Requires subclasses to define how names are retrieved.
virtual const char* getPhone() const = 0; - Requires subclasses to define how phone numbers are retrieved.
}; - Ends BaseContact class definition.
PersonalContact Class**
class PersonalContact : public BaseContact {` - Defines a subclass inheriting from `BaseContact`.
private: - Marks these attributes as only accessible inside the class.
Contact* contact; - Pointer to a `Contact` structure.
char birthday[11];` - Array to store birthday as a string (format: YYYY-MM-DD).
public:` - Marks following methods as accessible from outside the class.
PersonalContact(const char* name, const char* phone, const char* bday) {` - Constructor for initializing a personal contact.
contact = new Contact();` - Dynamically allocates memory for a new `Contact` instance.
strncpy(contact->name, name, 29);` - Safely copies the name to `contact->name`.
contact->name[29] = '\0';` - Ensures the name string is properly null-terminated.
strncpy(contact->phone, phone, 14);` - Copies the phone number to `contact->phone`.
contact->phone[14] = '\0';` - Ensures proper null termination for the phone number.
strncpy(birthday, bday, 10);` - Copies the birthday to `birthday`.
birthday[10] = '\0';` - Ensures the birthday string is properly null-terminated.
}` - Ends constructor function.
~PersonalContact() {` - Destructor to clean up allocated memory.
delete contact;` - Deletes the allocated `Contact` instance to avoid memory leaks.
 `}` - Ends destructor function.
void showInfo() const {` - Prints out personal contact information.
std::cout << "Personal Contact: " << contact->name ...;` - Prints the contact details.
}` - Ends `showInfo` function.
const char* getName() const { return contact->name; }` - Returns the name.
const char* getPhone() const { return contact->phone; }` - Returns the phone number.
const char* getBirthday() const { return birthday; }` - Returns the birthday.
};` - Ends `PersonalContact` class definition.
BusinessContact Class
class BusinessContact : public BaseContact {` - Defines a subclass for business contacts.
private:` - Marks attributes as inaccessible outside the class.
Contact* contact;` - Pointer to a `Contact` structure.
char company[20];` - Array to store company name.
public:` - Marks methods as accessible.
BusinessContact(const char* name, const char* phone, const char* comp) {` - Constructor for a business contact.
contact = new Contact();` - Dynamically allocates memory.
strncpy(contact->name, name, 29);` - Copies the name safely.
contact->name[29] = '\0';` - Ensures proper null termination.
strncpy(contact->phone, phone, 14);` - Copies the phone number safely.
contact->phone[14] = '\0';` - Null terminates the phone number.
strncpy(company, comp, 19);` - Copies the company name safely.
company[19] = '\0';` - Ensures proper null termination.
}` - Ends constructor.
~BusinessContact() { delete contact; }` - Destructor that deletes allocated memory.
 `void showInfo() const {` - Prints business contact details.
 `std::cout << "Business Contact: " << contact->name ...;` - Prints details.
 `}` - Ends `showInfo` function.
 `const char* getName() const { return contact->name; }` - Returns name.
 `const char* getPhone() const { return contact->phone; }` - Returns phone number.
 `const char* getCompany() const { return company; }` - Returns company name.
`};` - Ends `BusinessContact` class.
Group Struct**
 `struct Group {` - Defines a structure to store contact groups.
 `char groupName[20];` - Stores group name.
 `BaseContact** members;` - Stores pointers to group members.
 `int memberCount, capacity;` - Tracks number of members and array size.
 `Group(const char* name) : memberCount(0), capacity(5) {` - Constructor for initializing a group.
 `}` - Ends `Group` constructor.
 `~Group() { delete[] members; }` - Destructor releases allocated memory.
 `void addMember(BaseContact* contact) {` - Adds a member dynamically.
 `if (memberCount == capacity) {` - Expands memory if needed.
 `}` - Ends memory expansion logic.
 `members[memberCount++] = contact;` - Adds a contact.
 `}` - Ends function.
 `bool removeMember(...) {` - Removes a member from the group.
 `}` - Ends `removeMember` function.
 `void showMembers() const {` - Prints group members.
}- Ends `showMembers` function.
`};` - Ends `Group` struct.
Main Function
int main() {` - Entry point of the program.
ContactManager manager;` - Creates a contact manager.
manager.addContact(...);` - Adds contacts to the system.
manager.showAllContacts();` - Displays all contacts.
 manager.addGroup("Family");` - Creates a group.
 BaseContact* contact = manager.getContact("Jean");` - Retrieves a contact.
 if (contact) family->addMember(contact);` - Adds a member to a group.
 manager.showAllGroups();` - Displays groups.
 manager.removeContact("Jean");` - Removes a contact.
 manager.showAllGroups();` - Displays groups after removal.
 manager.removeGroup("Work");` - Removes a group.
 manager.showAllContacts();` - Displays remaining contacts.
 return 0;` - Ends program.
