import os

def Check_PC(PCName):
    PATH = f"\\\\{PCName}\\c$"

    if os.path.exists(PATH):
        return True
    else:
        return False

#=========================================================================================================================================

def Selected_Browser(PCName):
    SUPPORTED_BROWSERS = ["Google Chrome", "Microsoft Edge"]
    BROWSERS_DETECTED = []
    NUMBERS = []
    VALID_CHOICES = []
    START_MENU_FOLDER = f"\\\\{PCName}\\c$\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
    FOLDER_ITEMS = os.listdir(START_MENU_FOLDER)

    for item in FOLDER_ITEMS:
        if item == "Google Chrome.lnk":
            BROWSERS_DETECTED.append("Google Chrome")
        elif item == "Microsoft Edge.lnk":
            BROWSERS_DETECTED.append("Microsoft Edge")
        else:
            pass

    for x in range(len(BROWSERS_DETECTED)):
        num = x + 1
        NUMBERS.append(str(num))
        browser = BROWSERS_DETECTED[x]
        pair = str(num), browser
        VALID_CHOICES.append(pair)

    while True:
        print("Select one of the following browsers...")
        print()
        for choice in VALID_CHOICES:
            print(f"{choice[0]} - {choice[1]}")
        print()
        CHOICE = input("Enter the number corresponding to the web browser of your choice and press ENTER: ")

        if CHOICE in NUMBERS:
            break
        else:
            print()
            print(f"'{CHOICE}' is NOT a valid input. Try again!")

    for choice in VALID_CHOICES:
        if CHOICE == choice[0]:
            return choice[1]
        else:
            pass

#=========================================================================================================================================

def Get_Profiles(PCName):
    EXCLUSIONS = [".DS_Store", "All Users", "Default", "Default User", "desktop.ini", "Public"]
    PATH = f"\\\\{PCName}\\c$\\Users"
    GET_PROFILES = os.listdir(PATH)
    PROFILE_LIST = []

    for profile in GET_PROFILES:
        if profile not in EXCLUSIONS and os.path.exists(f"\\\\{PCName}\\c$\\Users\\{profile}\\AppData\\Local"):
            PROFILE_LIST.append(profile)
        else:
            pass
    return PROFILE_LIST

#=========================================================================================================================================

def Select_Profile(ProfileList):
    VALID_CHOICES = []
    NUMBERS = []

    for num in range(len(ProfileList)):
        number = num + 1
        profile = ProfileList[num]
        pair = str(number), profile
        VALID_CHOICES.append(pair)
        NUMBERS.append(str(number))

    while True:
        print("Select one of the following profiles found..")
        print()
        for choice in VALID_CHOICES:
            print(f"{choice[0]} - {choice[1]}")
        print()
        CHOICE = input("Enter the number corresponding to the profile of your choice and press ENTER: ")

        if CHOICE in NUMBERS:
            break
        else:
            print()
            print(f"'{CHOICE}' is NOT a valid input. Try again!")

    for choice in VALID_CHOICES:
        if CHOICE == choice[0]:
            return choice[1]
        else:
            pass

#=========================================================================================================================================

def Get_Bookmarks(PCName, Profile, Browser):
    BOOKMARK_URLS = []
    BOOKMARK_NAMES = []
    GOOGLE_CHROME_PATH = f"\\\\{PCName}\\c$\\Users\\{Profile}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks"
    MS_EDGE_PATH = f"\\\\{PCName}\\c$\\Users\\{Profile}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Bookmarks"
    if Browser == "Microsoft Edge":
        GET_CONTENT = open(MS_EDGE_PATH, "r").readlines()
        for line in GET_CONTENT:
            if '"url":' in line:
                line = line.replace(' ', '')
                line = line.replace('"url":', '')
                line = line.replace('\n', '')
                BOOKMARK_URLS.append(line)
            else:
                pass
        for line in GET_CONTENT:
            if '"name":' in line:
                line = line.replace(' ', '')
                line = line.replace('"name":', '')
                line = line.replace('\n', '')
                BOOKMARK_NAMES.append(line)
        for x in range(len(BOOKMARK_URLS)):
            print(f"Name: {BOOKMARK_NAMES[x]}")
            print(f"URL: {BOOKMARK_URLS[x]}")
            print()
    elif Browser == "Google Chrome":
        GET_CONTENT = open(GOOGLE_CHROME_PATH, "r").readlines()
        for line in GET_CONTENT:
            if '"url":' in line:
                line = line.replace(' ', '')
                line = line.replace('"url":', '')
                line = line.replace('\n', '')
                BOOKMARK_URLS.append(line)
            else:
                pass
        for line in GET_CONTENT:
            if '"name":' in line:
                line = line.replace(' ', '')
                line = line.replace('"name":', '')
                line = line.replace('\n', '')
                BOOKMARK_NAMES.append(line)
        for x in range(len(BOOKMARK_URLS)):
            print(f"Name: {BOOKMARK_NAMES[x]}")
            print(f"URL: {BOOKMARK_URLS[x]}")
            print()

#=========================================================================================================================================

while True:
    PCName = input("Enter the remote computer's name and press ENTER: ")
    if PCName != "":
        break
    else:
        print()
        print("Computer name CANNOT be null. Try again!")

CheckPC = Check_PC(PCName)
if CheckPC == True:
    Browser = Selected_Browser("2003-4sr3333")
    Profiles = Get_Profiles("2003-4sr3333")
    Profile_Selected = Select_Profile(Profiles)
    Get_Bookmarks("2003-4sr3333", Profile_Selected, Browser)
else:
    pass