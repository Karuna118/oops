class Instagram:
    def __init__(self,title, description,Creator_name,Location):  
        self.title = title
        self.description = description
        self.likes = 0
        self.comments = []
        self.Creator_name = Creator_name
        self.Location = Location
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    def display_comments(self):
        print("the commment is")
        for comment in self.comments:
            print(comment)
    def display_Creator_name(self):
        print("the  Creator_name is",self.Creator_name)
    def display_Location(self):
        print("the  Location is",self.Location)

    def display_comments(self,comments):
        if len(self.comments)==0:
            print("no comments yet")
        else:
            print("comments are:")
            for comment in self.comments:
                print(comment)

    def add_comment(self,comments):
        self.comments.append(comment)

    def del_comment(self,comments):
        self.comments.pop(comment)
        
        

reel1=Instagram("dancing","dancing with friends","karu ","BGNagar")
reel1.disliked() 
reel1.liked() 


reel2=Instagram("finance minister conference","finance minister conference with friends","shalini","arkalgud")
reel1.liked() 
reel2.liked() 
reel1.disliked() 
reel1.display_likes()
reel2.display_likes()
reel1.display_comments("wonderful")
reel2.display_Location()
reel1.display_Creator_name()
print(id(reel1))
print(id(reel2))