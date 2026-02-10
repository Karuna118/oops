#Encapsulation

class InstagramAccount:
    # Public variable
    account_name = ""

    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []          # Protected variable
        self.__archived_reels = []        # Private variable
        self.__password = password        # Private password

    # 1. Add private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    # 2. Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    # 3. Add archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    # 4. Display archived reels
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    # 5. Getter method for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied! Incorrect password"

    # 6. Setter method to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully!")
        else:
            print("Password update failed! Incorrect old password")




# Create object
account = InstagramAccount("krutik_vlogs", "1234")

# Add private reels
account.add_private_reel("Gym Transformation Reel")
account.add_private_reel("Travel Vlog Reel")

# Add archived reels
account.add_archived_reel("Old Dance Reel")
account.add_archived_reel("College Memories Reel")

# Display private reels
print("\nFollower View:")
account.display_private_reels(True)

print("\nNon-Follower View:")
account.display_private_reels(False)

# Display archived reels
print("\nArchived Reels (Correct Password):")
account.display_archived_reels("1234")

print("\nArchived Reels (Wrong Password):")
account.display_archived_reels("0000")

# Update password
print("\nUpdating Password:")
account.set_password("1234", "5678")

# Check archived reels again
print("\nArchived Reels After Password Update:")
account.display_archived_reels("5678")